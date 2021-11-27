#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 22:31:18 2021

@author: paulo
"""


import sys
import SPICAdicionarAmostra
import SPICPaginaInicial


from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)



#class Window(QMainWindow, SPICAdicionarAmostra.Ui_adicionarAmostra):
class Window(QMainWindow, SPICPaginaInicial.Ui_SPICPaginaPrincipal):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        #self.connectSignalsSlots()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())