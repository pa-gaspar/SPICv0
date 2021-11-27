"""
#UNIVERSIDADE TECNOLÓGICA FEDERAL DO PARANÁ

#ANO: 2021

#ALUNO: PAULO GASPAR
#ORIENTADOR: RICARDO SCHNEIDER
#COORIENTADOR: FELIPE PFRIMER

#SOFTWARE UTILIZADO PARA A ANÁLISE DE DADOS DE MEDIÇÕES DE PRESSÃO OBTIDAS NO PROCESSO DE PICNOMETRIA A GÁS

#Este software permite o usuário importar um arquivo CSV com valores de pressão...
#gerados pelo SPARKvue e realizar o cálculo de volume, selecionando manualmente...
#na interface gráfica os valores de pressão inicial, intermediária e final.

"""



import csv
import numpy as np


import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from matplotlib.widgets import Cursor
import threading


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas




class PlotGraph(FigureCanvas):
    def __init__(self,endereco,minfator=0,maxfator=1,maxvolume=1,selecao=2):
        #super().__init__()
        self.endereco = endereco
        self.minfator = minfator
        self.maxfator = maxfator
        self.maxvolume = maxvolume
        self.selecao = selecao
        self.valoresGerais()
        self.graphData = self.dadosGrafico(self.endereco)
        
        
        #self.plotar(self.graphData)
        
    def valoresGerais(self):
        #valores de pressão inicial, média e final recebem -1. 
        #Este valor representa que não há um valor valido selecionado
        self.piValue = -1
        self.pmValue = -1
        self.pfValue = -1
        
        #cria lista para argumentos das regiões selecionadas de pressão inicial, média e final
        self.argsPi = []
        self.argsPm = []
        self.argsPf = []
        
        #auxBool é um auxiliar que identifica se foi selecionado o inicio ou o fim...
        #do intervalo de medição de uma pressão
        #auxBool = False - Está no estágio de seleção do início do intervalo
        #auxBool = True - Está no estágio de seleção do fim do estágio
        self.auxBool = False
        
        #auxPress é um auxiliar referente a que pressão está sendo selecionada 
        # auxPress = 1 - Está no estágio de selecionar a pressão inicial (pi)
        # auxPress = 2 - Está no estágio de selecionar a pressão intermediária (pm)
        # auxPress = 3 - Está no estágio de selecionar a pressão final (pf)
        # auxPress = 4 - Os valores de pressão já foram selecionados e é calculado o volume
        self.auxPress = 1
        
        #posicionamento dos textos na interface gráfica
        self.axPiTexto = [0, -2]
        self.axPmTexto = [0,-3]
        self.axPfTexto = [0,-4]
        
        #posicionamento dos valores na interface gráfica
        self.axPiValue = [0, -2.5]
        self.axPmValue = [0,-3.5]
        self.axPfValue = [0,-4.5]
        self.axVolume = [0,-5]
        
        #posicionamento do botão de reset na interface gráfica
        self.axReset = [0.85, 0.8, 0.1, 0.075]
        self.axSalvar = [0.85, 0.7, 0.1, 0.075]
        
        
    def dadosGrafico(self,endereco):
        with open(endereco, newline='') as csvfile:
            #para csv gerado no SPARKvue
            #-----
            #faz a leitura do arquivo CSV gerado pelo SPARKvue
            self.auxReader = csv.reader(csvfile, delimiter=';', quotechar='|')
            #-----
            
            #converte objeto para uma lista de lista com três strings 
            self.testData = list(self.auxReader)
            #exclui o primeiro item da lista, pois é referente ao título das colunas    
        del self.testData[0]         
        #transforma testData em um vetor numpy 
        self.testData = np.asarray(self.testData)
        #mantém apenas a coluna de número 2, referente aos valores de pressão 
        self.testData = self.testData[:,2]
        
        #um for percorrendo a lista testData
        for i in range(len(self.testData)):
            #troca a vírgula, por ponto, então converte a string em um float e multiplica por mil, transformando de kPA para PA
            self.testData[i] = np.float64(self.testData[i].replace(',','.'))*1000
        
        #transforma testData de uma matriz de strings em uma matriz de floats, 
        self.testData = self.testData.astype(np.float)
        
        #-----
        
        #y recebe os valores de pressão
        y = self.testData
        #x recebe série de valores de 0 até o número total de amostras em y
        x = np.asarray(range(len(y)))
        
        return [x,y]
    
    def plotar(self,e=threading.Event):
        
        self.fig, self.ax = plt.subplots()
        plt.subplots_adjust(right=0.8)
        
        #e = threading.Event()
        
        self.bReset = Button(plt.axes(self.axReset), 'Reset')
        self.bSalvar = Button(plt.axes(self.axSalvar), 'Salvar')
        plt.ion()
        self.ax.plot(self.graphData[0],self.graphData[1],lw=2)
        self.cursor = Cursor(self.ax, horizOn=True, vertOn=True, useblit=True,
                             color = 'r', linewidth = 1)
        
        self.bReset.on_clicked(self.reset)
        self.bSalvar.on_clicked(self.salvar(e))
        self.piTexto = plt.text(self.axPiTexto[0],self.axPiTexto[1], "Pressão Inicial: ")
        self.piValueTexto = plt.text(self.axPiValue[0],self.axPiValue[1],' ')
        self.pmTexto = plt.text(self.axPmTexto[0],self.axPmTexto[1], "Pressão Intermediaria: ")
        self.pmValueTexto = plt.text(self.axPmValue[0],self.axPmValue[1],' ')
        self.pfTexto = plt.text(self.axPfTexto[0],self.axPfTexto[1], "Pressão Final: ")
        self.pfValueTexto = plt.text(self.axPfValue[0],self.axPfValue[1],' ')
        self.volumeTexto = plt.text(self.axVolume[0],self.axVolume[1],' ')
        if(self.selecao == 1):
            self.fig.canvas.mpl_connect('button_press_event', self.selecaoLivre)
        if(self.selecao == 2):
            self.fig.canvas.mpl_connect('button_press_event', self.selecaoAutomatica)
        
        #self.draw()


    def reset(self, event):
    
        self.piValue = -1
        self.pmValue = -1
        self.pfValue = -1
        self.argsPi = []
        self.argsPm = []
        self.argsPf = []
        self.auxPress = 1
        self.auxBool = False;
        
        self.piValueTexto.set_text(' ')
        self.pmValueTexto.set_text(' ')
        self.pfValueTexto.set_text(' ')
        self.volumeTexto.set_text(' ')
        
        self.ax.clear()
        self.ax.plot(self.graphData[0],self.graphData[1],lw=2)
        self.fig.canvas.draw()
        
    def salvar(self, e=threading.Event):
        def clicked(event):
            e.set()
            plt.close()
        return clicked
        
        
    def selecaoLivre(self,event):
    
        # xPoint recebe o ponto no eixo x onde ocorreu o clique na interface gráfica
        self.xPoint = event.xdata
        
        #estágio de seleção da pressão inicial (piValue)
        if self.auxPress == 1:
            #caso esteja na etapa de seleção do início do intervalo de medidas
            if self.auxBool == False:    
                #é guardado aorgumento (posição do eixo x)
                self.argsPi.append(int(event.xdata))
                #plota uma linha vertical para marcar o ponto selecionado
                self.ax.vlines(self.xPoint,min(self.graphData[1]),max(self.graphData[1]),color='blue')
                #altera auxBool para True, para ir pra etapa de seleção do fim do intervalo
                self.auxBool = True;
                
            #caso esteja na etapa de seleção do fim do intervalo de medidas    
            else:
                #é guardado aorgumento (posição do eixo x)
                self.argsPi.append(int(event.xdata))
                #plota uma linha vertical para marcar o ponto selecionado
                self.ax.vlines(self.xPoint,min(self.graphData[1]),max(self.graphData[1]),color='blue')
                #altera auxBool para False, para ir pra etapa de seleção de início de intervalo
                self.auxBool = False;
                #auxPress recebe 2, o que significa que no próximo clique... 
                #será selecionada a pressão intermediária
                self.auxPress = 2
                #piValue recebe a média dos valores de pressão selecionados
                self.piValue = np.mean(self.graphData[1][ self.argsPi[0]:self.argsPi[1]] )
                #exibe na interface gráfica o valor da pressão inicial
                self.piValueTexto.set_text('{:.2f}'.format(self.piValue) + ' Pa')
                    
        #estágio de seleção da pressão intermediária (pmValue)        
        elif self.auxPress == 2:
            #caso esteja na etapa de seleção do início do intervalo de medidas
            if self.auxBool == False:   
                #é guardado aorgumento (posição do eixo x)
                self.argsPm.append(int(event.xdata))
                #plota uma linha vertical para marcar o ponto selecionado
                self.ax.vlines(self.xPoint,min(self.graphData[1]),max(self.graphData[1]),color='green')
                #altera auxBool para True, para ir pra etapa de seleção do fim do intervalo
                self.auxBool = True;
            
            #caso esteja na etapa de seleção do fim do intervalo de medidas  
            else:
                #é guardado aorgumento (posição do eixo x)
                self.argsPm.append(int(event.xdata))
                #plota uma linha vertical para marcar o ponto selecionado
                self.ax.vlines(self.xPoint,min(self.graphData[1]),max(self.graphData[1]),color='green')
                #altera auxBool para False, para ir pra etapa de seleção de início de intervalo
                self.auxBool = False;
                #auxPress recebe 3, o que significa que no próximo clique... 
                #será selecionada a pressão final
                self.auxPress = 3
                #pmValue recebe a média dos valores de pressão selecionados
                self.pmValue = np.mean(self.graphData[1][ self.argsPm[0]:self.argsPm[1]] )
                #exibe na interface gráfica o valor da pressão intermediária
                self.pmValueTexto.set_text('{:.2f}'.format(self.pmValue) + ' Pa')
        
        #estágio de seleção da pressão final (pfValue)  
        elif self.auxPress == 3:
            #caso esteja na etapa de seleção do início do intervalo de medidas
            if self.auxBool == False:  
                #é guardado aorgumento (posição do eixo x)
                self.argsPf.append(int(event.xdata))
                #plota uma linha vertical para marcar o ponto selecionado
                self.ax.vlines(self.xPoint,min(self.graphData[1]),max(self.graphData[1]),color='red')
                #altera auxBool para True, para ir pra etapa de seleção do fim do intervalo
                self.auxBool = True;
                
            #caso esteja na etapa de seleção do fim do intervalo de medidas   
            else:
                #é guardado aorgumento (posição do eixo x)
                self.argsPf.append(int(event.xdata))
                #plota uma linha vertical para marcar o ponto selecionado
                self.ax.vlines(self.xPoint,min(self.graphData[1]),max(self.graphData[1]),color='red')
                #altera auxBool para False
                self.auxBool = False;
                #auxPress recebe 4, o que significa que o valor de volume será calculado
                self.auxPress = 4
                #pfValue recebe a média dos valores de pressão selecionados
                self.pfValue = np.mean(self.graphData[1][ self.argsPf[0]:self.argsPf[1]] )
                #exibe na interface gráfica o valor da pressão final
                self.pfValueTexto.set_text('{:.2f}'.format(self.pfValue) + ' Pa')
                
        #estágio de calculo de volume        
        if self.auxPress == 4:
            #é realizado o calculo de volume, com pressões inicial, intermediária e final
            #fatorVolume é o calculo do fator das pressoes medidas
            #volume é o valor do volume em ml após os cálculos
            self.fatorVolume = (1 - ((self.pfValue - self.pmValue)/(self.piValue - self.pfValue)))
            self.volume = (self.fatorVolume - self.minfator)/(self.maxfator - self.minfator) * self.maxvolume
            #exibe na interface gráfica o valor do volume
            self.volumeTexto.set_text("Volume = {:.2f} ml".format(self.volume))
            #auxPress recebe 0, significando para o sistema que o processo foi concluido
            self.auxPress = 0
        
        #após o clique, a interface gráfica é atualizada
        self.fig.canvas.draw() 
     
    #função que faz a seleção automática do intervalo de medidas
    def selecaoAutomatica(self,event):
        # xPoint recebe o ponto no eixo x onde ocorreu o clique na interface gráfica
        self.xPoint = event.xdata   
        #estágio de seleção da pressão inicial (piValue)
        if self.auxPress == 1:
            #é guardado os argumentos dos intervalor a serem calculados
            self.argsPi.append(int(event.xdata))
            self.argsPi.append(int(event.xdata)+20)
            #plota uma linha vertical para marcar o ponto selecionado
            self.ax.vlines(self.xPoint,min(self.graphData[1]),max(self.graphData[1]),color='blue')
            #auxPress recebe 2, o que indica para o sistema que no próximo clique...
            #será selecionado a pressão intermediária
            self.auxPress=2
            #piValue recebe a média dos valores de pressão selecionados
            self.piValue = np.mean(self.graphData[1][ self.argsPi[0]:self.argsPi[1]] )
            #exibe na interface gráfica o valor da pressão inicial
            self.piValueTexto.set_text('{:.2f}'.format(self.piValue) + ' Pa')
            
        #estágio de seleção da pressão intermediária (pmValue)        
        elif self.auxPress == 2:
            
            #é guardado aorgumento (posição do eixo x)
            self.argsPm.append(int(event.xdata)-20)
            self.argsPm.append(int(event.xdata))
            self.argsPf.append(int(event.xdata)+30)
            self.argsPf.append(int(event.xdata)+50)
            #plota uma linha vertical para marcar o ponto selecionado
            self.ax.vlines(self.xPoint,min(self.graphData[1]),max(self.graphData[1]),color='green')
            self.ax.vlines(self.xPoint+30,min(self.graphData[1]),max(self.graphData[1]),color='red')
            #será selecionada a pressão final
            self.auxPress = 3
            #pmValue recebe a média dos valores de pressão selecionados
            self.pmValue = np.mean(self.graphData[1][ self.argsPm[0]:self.argsPm[1]] )
            self.pfValue = np.mean(self.graphData[1][ self.argsPf[0]:self.argsPf[1]] )
            #exibe na interface gráfica o valor da pressão intermediária
            self.pmValueTexto.set_text('{:.2f}'.format(self.pmValue) + ' Pa')
            self.pfValueTexto.set_text('{:.2f}'.format(self.pfValue) + ' Pa')
                
        #estágio de calculo de volume        
        if self.auxPress == 3:
            #é realizado o calculo de volume, com pressões inicial, intermediária e final
    
            self.fatorVolume = (1 - ((self.pfValue - self.pmValue)/(self.piValue - self.pfValue)))
            #fatorVolume é o calculo do fator das pressoes medidas
            #volume é o valor do volume em ml após os cálculos
            self.volume = (self.fatorVolume - self.minfator)/(self.maxfator - self.minfator) * self.maxvolume
            #exibe na interface gráfica o valor do volume
            self.volumeTexto.set_text("Volume = {:.2f} ml".format(self.volume))
            #auxPress recebe 0, significando para o sistema que o processo foi concluido
            self.auxPress = 0
        
        #após o clique, a interface gráfica é atualizada
        self.fig.canvas.draw() 
        
'''
class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.title = 'PyQt5 matplotlib example - pythonspot.com'
        self.width = 640
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #m = PlotGraph('04-A.csv')
       

        self.button = QPushButton('PyQt5 button', self)
        self.button.setToolTip('This s an example button')
        self.button.move(500,0)
        self.button.resize(140,100)
        self.button.clicked.connect(self.executePlot)

        self.show()
        
    def executePlot(self):  
        self.xis = PlotGraph('04-A.csv')
        #self.xis.plotar()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
   '''     
#teste = PlotGraph('04-A.csv',0,1,1,2)
#teste.plotar()
