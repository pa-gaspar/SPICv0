# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SPICPaginaInicial.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import SPICAdicionarAmostra
import threading
from matplotlib import pyplot as plt
import numpy as np
from scipy import stats
import csv

class Ui_SPICPaginaPrincipal(object):
    def setupUi(self, SPICPaginaPrincipal):
        SPICPaginaPrincipal.setObjectName("SPICPaginaPrincipal")
        SPICPaginaPrincipal.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(SPICPaginaPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.textoFatorMinimo = QtWidgets.QLabel(self.centralwidget)
        self.textoFatorMinimo.setObjectName("textoFatorMinimo")
        self.horizontalLayout_2.addWidget(self.textoFatorMinimo)
        self.valorFatorMinimo = QtWidgets.QLineEdit(self.centralwidget)
        self.valorFatorMinimo.setObjectName("valorFatorMinimo")
        self.horizontalLayout_2.addWidget(self.valorFatorMinimo)
        self.textoFatorMaximo = QtWidgets.QLabel(self.centralwidget)
        self.textoFatorMaximo.setObjectName("textoFatorMaximo")
        self.horizontalLayout_2.addWidget(self.textoFatorMaximo)
        self.valorFatorMaximo = QtWidgets.QLineEdit(self.centralwidget)
        self.valorFatorMaximo.setObjectName("valorFatorMaximo")
        self.horizontalLayout_2.addWidget(self.valorFatorMaximo)
        self.textoVolumeMaximo = QtWidgets.QLabel(self.centralwidget)
        self.textoVolumeMaximo.setObjectName("textoVolumeMaximo")
        self.horizontalLayout_2.addWidget(self.textoVolumeMaximo)
        self.valorVolumeMaximo = QtWidgets.QLineEdit(self.centralwidget)
        self.valorVolumeMaximo.setObjectName("valorVolumeMaximo")
        self.horizontalLayout_2.addWidget(self.valorVolumeMaximo)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textoNome = QtWidgets.QLabel(self.centralwidget)
        self.textoNome.setObjectName("textoNome")
        self.horizontalLayout.addWidget(self.textoNome)
        self.valorNome = QtWidgets.QLineEdit(self.centralwidget)
        self.valorNome.setObjectName("valorNome")
        self.horizontalLayout.addWidget(self.valorNome)
        self.textoPasta = QtWidgets.QLabel(self.centralwidget)
        self.textoPasta.setObjectName("textoPasta")
        self.horizontalLayout.addWidget(self.textoPasta)
        self.valorPasta = QtWidgets.QLineEdit(self.centralwidget)
        self.valorPasta.setObjectName("valorPasta")
        self.horizontalLayout.addWidget(self.valorPasta)
        self.botaoPasta = QtWidgets.QPushButton(self.centralwidget)
        self.botaoPasta.setObjectName("botaoPasta")
        self.horizontalLayout.addWidget(self.botaoPasta)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.botaoExcluir = QtWidgets.QPushButton(self.centralwidget)
        self.botaoExcluir.setObjectName("botaoExcluir")
        self.horizontalLayout_3.addWidget(self.botaoExcluir)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_3.addWidget(self.listWidget)
        self.botaoAdicionar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoAdicionar.setObjectName("botaoAdicionar")
        self.horizontalLayout_3.addWidget(self.botaoAdicionar)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setObjectName("label2")
        self.horizontalLayout_4.addWidget(self.label2)
        self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit2.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit2)
        self.botaoDensidade = QtWidgets.QPushButton(self.centralwidget)
        self.botaoDensidade.setObjectName("botaoDensidade")
        self.horizontalLayout_4.addWidget(self.botaoDensidade)
        self.botaoCorrelacao = QtWidgets.QPushButton(self.centralwidget)
        self.botaoCorrelacao.setObjectName("botaoCorrelacao")
        self.horizontalLayout_4.addWidget(self.botaoCorrelacao)
        self.botaoGeral = QtWidgets.QPushButton(self.centralwidget)
        self.botaoGeral.setObjectName("botaoGeral")
        self.horizontalLayout_4.addWidget(self.botaoGeral)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        SPICPaginaPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SPICPaginaPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        self.menufiat = QtWidgets.QMenu(self.menubar)
        self.menufiat.setObjectName("menufiat")
        self.menulux = QtWidgets.QMenu(self.menubar)
        self.menulux.setObjectName("menulux")
        SPICPaginaPrincipal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SPICPaginaPrincipal)
        self.statusbar.setObjectName("statusbar")
        SPICPaginaPrincipal.setStatusBar(self.statusbar)
        self.actionFechar = QtWidgets.QAction(SPICPaginaPrincipal)
        self.actionFechar.setObjectName("actionFechar")
        self.menufiat.addAction(self.actionFechar)
        self.menubar.addAction(self.menufiat.menuAction())
        self.menubar.addAction(self.menulux.menuAction())
        
        self.listaDados = []
        self.listaMassa = []
        
        self.botaoAdicionar.clicked.connect(self.abreAddAmostra)
        self.botaoPasta.clicked.connect(self.selecionaPasta)
        self.botaoExcluir.clicked.connect(self.excluiItem)
        self.botaoGeral.clicked.connect(self.geraGraficoGeral)
        self.botaoCorrelacao.clicked.connect(self.geraGraficoCorrelacao)
        self.botaoDensidade.clicked.connect(self.calculaDensidade)

        
        self.retranslateUi(SPICPaginaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(SPICPaginaPrincipal)

    def retranslateUi(self, SPICPaginaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        SPICPaginaPrincipal.setWindowTitle(_translate("SPICPaginaPrincipal", "Início - SPIC"))
        self.textoFatorMinimo.setText(_translate("SPICPaginaPrincipal", "Fator Mínimo:"))
        self.textoFatorMaximo.setText(_translate("SPICPaginaPrincipal", "Fator Máximo:"))
        self.textoVolumeMaximo.setText(_translate("SPICPaginaPrincipal", "Volume Máximo:"))
        self.textoNome.setText(_translate("SPICPaginaPrincipal", "Nome do Teste:"))
        self.textoPasta.setText(_translate("SPICPaginaPrincipal", "Pasta"))
        self.botaoPasta.setText(_translate("SPICPaginaPrincipal", "..."))
        self.botaoExcluir.setText(_translate("SPICPaginaPrincipal", "Excluir"))
        self.botaoAdicionar.setText(_translate("SPICPaginaPrincipal", "Adicionar"))
        self.label.setText(_translate("SPICPaginaPrincipal", "Unidade de Massa (eixo x): "))
        self.label2.setText(_translate("SPICPaginaPrincipal", "Unidade de Volume (eixo y): "))
        self.botaoDensidade.setText(_translate("SPICPaginaPrincipal", "Gerar Valores de Densidade"))
        self.botaoCorrelacao.setText(_translate("SPICPaginaPrincipal", "Gerar Gráfico de Correlação"))
        self.botaoGeral.setText(_translate("SPICPaginaPrincipal", "Gerar Grafico Geral"))
        self.menufiat.setTitle(_translate("SPICPaginaPrincipal", "Ar&quivo"))
        self.menulux.setTitle(_translate("SPICPaginaPrincipal", "Sobre"))
        self.actionFechar.setText(_translate("SPICPaginaPrincipal", "&Fechar"))
        
    def abreAddAmostra(self):
        
        self.addWindow = Windowamostra()
        self.addWindow.show()
        evt = threading.Event()
        self.addWindow.ajustaEvento(evt)
        t1 = threading.Thread(target=self.salvaItem,args=(evt,))
        t1.start()
        
    def selecionaPasta(self):
        #self.path =  QtWidgets.QFileDialog.getOpenFileName(self, 'Selecione uma Pasta: ', '','All Files (*.*)')
        self.path =  QtWidgets.QFileDialog.getExistingDirectory(self,"Selecione uma Pasta: ")
        if self.path != ('', ''):
            self.valorPasta.setText(self.path)
        
    def salvaItem(self,e):
        if e.wait():
            self.listWidget.addItem(str(self.listWidget.count()) + ' - Nome da Amostra: ' + self.addWindow.campoTituloAmostra.text() + ' | Quantidade un. Massa: ' + self.addWindow.campoQuantidade.text() +self.lineEdit.text() + ' | Quantidade de Medições: ' + str(self.addWindow.listaAmostras.count()))
            self.listaMassa.append(float(self.addWindow.campoQuantidade.text()))
            listaAmostra = []
            for i in range(self.addWindow.listaAmostras.count()):
                self.addWindow.listaAmostras.setCurrentRow(i)
                self.auxiliar = self.addWindow.listaAmostras.currentItem().text()
                #self.listWidget.addItem(self.addWindow.campoTituloAmostra.text() + ', ' + str(self.auxiliar))
                auxSplit = str(self.auxiliar).split(", ",3)
                for i in range(len(auxSplit)):
                    auxSplit[i] = float(auxSplit[i])
                listaAmostra.append(auxSplit)
            self.listaDados.append(listaAmostra)
            
    def excluiItem(self):
        self.listWidget.takeItem(self.listWidget.currentRow())
        del self.listaDados[self.listWidget.currentRow()]
        del self.listaMassa[self.listWidget.currentRow()]
        
    def geraListaVolumes(self):
        self.listaVolumes = []
        for i in range(len(self.listaDados)):
            aux = []
            for j in range(len(self.listaDados[i])):
                equacao = 1 - ((self.listaDados[i][j][2]-self.listaDados[i][j][1])/(self.listaDados[i][j][0]-self.listaDados[i][j][2]))
                try:
                    
                    equacao = float(self.valorVolumeMaximo.text())*((equacao - float(self.valorFatorMinimo.text()))/(float(self.valorFatorMaximo.text())-float(self.valorFatorMinimo.text())))
                    aux.append(equacao)
                except:
                    aux.append(equacao)
            self.listaVolumes.append(aux)
    
    def geraListaMedias(self):
         self.geraListaVolumes()
         self.listaMedias = []
         for i in range(len(self.listaVolumes)):
             self.listaMedias.append(np.mean(self.listaVolumes[i]))
             
             
             
            
    def geraGraficoGeral(self):
        self.geraListaVolumes()
        fig, ax = plt.subplots()
        ax.set_title("Grafico Geral - " + self.valorNome.text())
        ax.set_xlabel(self.lineEdit.text())
        ax.set_ylabel(self.lineEdit.text())
        for i in range(len(self.listaVolumes)):
            ax.plot( np.ones(len(self.listaVolumes[i]))*self.listaMassa[i], self.listaVolumes[i], 'ro' )
        fig.savefig(self.valorPasta.text() +'/'+ self.valorNome.text()+"GraficoGeral.png",dpi=500)
    
    def geraGraficoCorrelacao(self):
        self.geraListaMedias()
        fig, ax = plt.subplots()
        ax.set_title("Grafico de Correlação - " + self.valorNome.text())
        linspace = np.linspace(min(self.listaMassa),max(self.listaMassa),100)
        poly = np.polyfit(self.listaMassa,self.listaMedias,1)
        line =  np.polyval(poly,linspace)
        slope, intercept, r_value, p_value, std_err = stats.linregress(range(len(self.listaMedias)),self.listaMedias)
        ax.set_xlabel(self.lineEdit.text())
        ax.set_ylabel(self.lineEdit.text())
        ax.plot(linspace,line)
        ax.plot( self.listaMassa, self.listaMedias, 'ro' )
        plt.text(0,0.96*max(self.listaMedias),'Correlação = {:.3f} \n'.format(r_value**2) + 'Gradiente = {:.3f}'.format(slope),bbox=dict(facecolor='white', alpha=0.5))
        fig.savefig(self.valorPasta.text() +'/'+ self.valorNome.text()+"GraficoCorrelacao.png",dpi=500)
        
    def calculaDensidade(self): 
        self.geraListaMedias()
        self.listaDensidades = []
        for i in range(len(self.listaMedias)):
            if self.listaMassa[i] != 0:
                self.listaDensidades.append(self.listaMedias[i]/self.listaMassa[i])
            else:
                self.listaDensidades.append(0)
        with open(self.valorPasta.text() +'/'+ self.valorNome.text()+"Densidade.csv",mode='w') as csvFile:
            writer = csv.writer(csvFile, delimiter=',')
            for i in self.listaDensidades:
                writer.writerow([i])
            csvFile.close()
                
class Windowamostra(QtWidgets.QMainWindow, SPICAdicionarAmostra.Ui_adicionarAmostra):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        #self.connectSignalsSlots()
