# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visual.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 571))
        self.tabWidget.setProperty("p3", "")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_gastronomia = QtWidgets.QWidget()
        self.tab_gastronomia.setObjectName("tab_gastronomia")
        self.label_preg1 = QtWidgets.QLabel(self.tab_gastronomia)
        self.label_preg1.setGeometry(QtCore.QRect(70, 40, 691, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_preg1.setFont(font)
        self.label_preg1.setWordWrap(True)
        self.label_preg1.setObjectName("label_preg1")
        self.txt_dondeEstoy = QtWidgets.QTextEdit(self.tab_gastronomia)
        self.txt_dondeEstoy.setGeometry(QtCore.QRect(100, 150, 181, 31))
        self.txt_dondeEstoy.setObjectName("txt_dondeEstoy")
        self.txt_presupuesto = QtWidgets.QTextEdit(self.tab_gastronomia)
        self.txt_presupuesto.setGeometry(QtCore.QRect(290, 200, 181, 31))
        self.txt_presupuesto.setObjectName("txt_presupuesto")
        self.txt_tipoEstablecimiento = QtWidgets.QTextEdit(self.tab_gastronomia)
        self.txt_tipoEstablecimiento.setGeometry(QtCore.QRect(290, 150, 181, 31))
        self.txt_tipoEstablecimiento.setObjectName("txt_tipoEstablecimiento")
        self.txt_Perimetro = QtWidgets.QTextEdit(self.tab_gastronomia)
        self.txt_Perimetro.setGeometry(QtCore.QRect(100, 200, 181, 31))
        self.txt_Perimetro.setObjectName("txt_Perimetro")
        self.txt_porciento = QtWidgets.QTextEdit(self.tab_gastronomia)
        self.txt_porciento.setGeometry(QtCore.QRect(180, 250, 181, 31))
        self.txt_porciento.setObjectName("txt_porciento")
        self.txt_criterioEconomico = QtWidgets.QTextEdit(self.tab_gastronomia)
        self.txt_criterioEconomico.setGeometry(QtCore.QRect(490, 200, 181, 31))
        self.txt_criterioEconomico.setObjectName("txt_criterioEconomico")
        self.txt_tipoComida = QtWidgets.QTextEdit(self.tab_gastronomia)
        self.txt_tipoComida.setGeometry(QtCore.QRect(490, 150, 181, 31))
        self.txt_tipoComida.setObjectName("txt_tipoComida")
        self.btn_submitQ1 = QtWidgets.QPushButton(self.tab_gastronomia)
        self.btn_submitQ1.setGeometry(QtCore.QRect(400, 250, 181, 31))
        self.btn_submitQ1.setAutoDefault(True)
        self.btn_submitQ1.setDefault(True)
        self.btn_submitQ1.setObjectName("btn_submitQ1")
        self.label_preg1_ans = QtWidgets.QLabel(self.tab_gastronomia)
        self.label_preg1_ans.setGeometry(QtCore.QRect(130, 350, 691, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_preg1_ans.setFont(font)
        self.label_preg1_ans.setWordWrap(True)
        self.label_preg1_ans.setObjectName("label_preg1_ans")
        self.tabWidget.addTab(self.tab_gastronomia, "")
        self.tab_cultura = QtWidgets.QWidget()
        self.tab_cultura.setObjectName("tab_cultura")
        self.label_preg2 = QtWidgets.QLabel(self.tab_cultura)
        self.label_preg2.setGeometry(QtCore.QRect(60, 50, 691, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_preg2.setFont(font)
        self.label_preg2.setWordWrap(True)
        self.label_preg2.setObjectName("label_preg2")
        self.txt_PresupuestoQ2 = QtWidgets.QTextEdit(self.tab_cultura)
        self.txt_PresupuestoQ2.setGeometry(QtCore.QRect(100, 160, 181, 31))
        self.txt_PresupuestoQ2.setObjectName("txt_PresupuestoQ2")
        self.txt_HoyQ2 = QtWidgets.QTextEdit(self.tab_cultura)
        self.txt_HoyQ2.setGeometry(QtCore.QRect(300, 160, 181, 31))
        self.txt_HoyQ2.setObjectName("txt_HoyQ2")
        self.btn_submitQ2 = QtWidgets.QPushButton(self.tab_cultura)
        self.btn_submitQ2.setGeometry(QtCore.QRect(500, 160, 181, 31))
        self.btn_submitQ2.setAutoDefault(True)
        self.btn_submitQ2.setDefault(True)
        self.btn_submitQ2.setObjectName("btn_submitQ2")
        self.table_Q2 = QtWidgets.QTableWidget(self.tab_cultura)
        self.table_Q2.setEnabled(True)
        self.table_Q2.setGeometry(QtCore.QRect(30, 210, 731, 321))
        self.table_Q2.setWordWrap(False)
        self.table_Q2.setObjectName("table_Q2")
        self.table_Q2.setColumnCount(13)
        self.table_Q2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_Q2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Q2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Q2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Q2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Q2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Q2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Q2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Q2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Q2.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Q2.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Q2.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Q2.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Q2.setHorizontalHeaderItem(12, item)
        self.tabWidget.addTab(self.tab_cultura, "")
        self.tab_cine = QtWidgets.QWidget()
        self.tab_cine.setObjectName("tab_cine")
        self.label_preg3 = QtWidgets.QLabel(self.tab_cine)
        self.label_preg3.setGeometry(QtCore.QRect(60, 40, 691, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_preg3.setFont(font)
        self.label_preg3.setWordWrap(True)
        self.label_preg3.setObjectName("label_preg3")
        self.txt_ProvinciaQ3 = QtWidgets.QTextEdit(self.tab_cine)
        self.txt_ProvinciaQ3.setGeometry(QtCore.QRect(100, 150, 181, 31))
        self.txt_ProvinciaQ3.setObjectName("txt_ProvinciaQ3")
        self.txt_GeneroQ3 = QtWidgets.QTextEdit(self.tab_cine)
        self.txt_GeneroQ3.setGeometry(QtCore.QRect(290, 150, 181, 31))
        self.txt_GeneroQ3.setObjectName("txt_GeneroQ3")
        self.btn_submitQ3 = QtWidgets.QPushButton(self.tab_cine)
        self.btn_submitQ3.setGeometry(QtCore.QRect(290, 200, 181, 31))
        self.btn_submitQ3.setAutoDefault(True)
        self.btn_submitQ3.setDefault(True)
        self.btn_submitQ3.setObjectName("btn_submitQ3")
        self.list_ansQ3 = QtWidgets.QListWidget(self.tab_cine)
        self.list_ansQ3.setGeometry(QtCore.QRect(120, 250, 521, 251))
        self.list_ansQ3.setObjectName("list_ansQ3")
        self.txt_ToqueQuedaQ3 = QtWidgets.QTextEdit(self.tab_cine)
        self.txt_ToqueQuedaQ3.setGeometry(QtCore.QRect(480, 150, 181, 31))
        self.txt_ToqueQuedaQ3.setObjectName("txt_ToqueQuedaQ3")
        self.tabWidget.addTab(self.tab_cine, "")
        self.tab_cumpleanos = QtWidgets.QWidget()
        self.tab_cumpleanos.setObjectName("tab_cumpleanos")
        self.label_preg4 = QtWidgets.QLabel(self.tab_cumpleanos)
        self.label_preg4.setGeometry(QtCore.QRect(40, 30, 691, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_preg4.setFont(font)
        self.label_preg4.setWordWrap(True)
        self.label_preg4.setObjectName("label_preg4")
        self.txt_PresupuestoQ4 = QtWidgets.QTextEdit(self.tab_cumpleanos)
        self.txt_PresupuestoQ4.setGeometry(QtCore.QRect(80, 140, 181, 31))
        self.txt_PresupuestoQ4.setObjectName("txt_PresupuestoQ4")
        self.txt_CiudadQ4 = QtWidgets.QTextEdit(self.tab_cumpleanos)
        self.txt_CiudadQ4.setGeometry(QtCore.QRect(80, 190, 181, 31))
        self.txt_CiudadQ4.setObjectName("txt_CiudadQ4")
        self.txt_CriterioCaroQ4 = QtWidgets.QTextEdit(self.tab_cumpleanos)
        self.txt_CriterioCaroQ4.setGeometry(QtCore.QRect(270, 190, 181, 31))
        self.txt_CriterioCaroQ4.setObjectName("txt_CriterioCaroQ4")
        self.txt_DineroNecesitoDiaQ4 = QtWidgets.QTextEdit(self.tab_cumpleanos)
        self.txt_DineroNecesitoDiaQ4.setGeometry(QtCore.QRect(460, 140, 181, 31))
        self.txt_DineroNecesitoDiaQ4.setObjectName("txt_DineroNecesitoDiaQ4")
        self.txt_PerimetroQ4 = QtWidgets.QTextEdit(self.tab_cumpleanos)
        self.txt_PerimetroQ4.setGeometry(QtCore.QRect(270, 140, 181, 31))
        self.txt_PerimetroQ4.setObjectName("txt_PerimetroQ4")
        self.btn_submitQ4 = QtWidgets.QPushButton(self.tab_cumpleanos)
        self.btn_submitQ4.setGeometry(QtCore.QRect(460, 190, 181, 31))
        self.btn_submitQ4.setAutoDefault(True)
        self.btn_submitQ4.setDefault(True)
        self.btn_submitQ4.setObjectName("btn_submitQ4")
        self.list_ansQ4 = QtWidgets.QListWidget(self.tab_cumpleanos)
        self.list_ansQ4.setGeometry(QtCore.QRect(90, 250, 521, 251))
        self.list_ansQ4.setObjectName("list_ansQ4")
        self.tabWidget.addTab(self.tab_cumpleanos, "")
        self.tab_importantes = QtWidgets.QWidget()
        self.tab_importantes.setObjectName("tab_importantes")
        self.tabWidget.addTab(self.tab_importantes, "")
        self.tab_hoy = QtWidgets.QWidget()
        self.tab_hoy.setObjectName("tab_hoy")
        self.label_preg6 = QtWidgets.QLabel(self.tab_hoy)
        self.label_preg6.setGeometry(QtCore.QRect(40, 20, 691, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_preg6.setFont(font)
        self.label_preg6.setWordWrap(True)
        self.label_preg6.setObjectName("label_preg6")
        self.txt_PresupuestoQ6 = QtWidgets.QTextEdit(self.tab_hoy)
        self.txt_PresupuestoQ6.setGeometry(QtCore.QRect(80, 110, 181, 31))
        self.txt_PresupuestoQ6.setObjectName("txt_PresupuestoQ6")
        self.txt_HoyQ6 = QtWidgets.QTextEdit(self.tab_hoy)
        self.txt_HoyQ6.setGeometry(QtCore.QRect(280, 110, 181, 31))
        self.txt_HoyQ6.setObjectName("txt_HoyQ6")
        self.btn_submitQ6 = QtWidgets.QPushButton(self.tab_hoy)
        self.btn_submitQ6.setGeometry(QtCore.QRect(280, 160, 181, 31))
        self.btn_submitQ6.setAutoDefault(True)
        self.btn_submitQ6.setDefault(True)
        self.btn_submitQ6.setObjectName("btn_submitQ6")
        self.txt_HoraActualQ6 = QtWidgets.QTextEdit(self.tab_hoy)
        self.txt_HoraActualQ6.setGeometry(QtCore.QRect(480, 110, 181, 31))
        self.txt_HoraActualQ6.setObjectName("txt_HoraActualQ6")
        self.table_Q6 = QtWidgets.QTableWidget(self.tab_hoy)
        self.table_Q6.setEnabled(True)
        self.table_Q6.setGeometry(QtCore.QRect(30, 200, 731, 321))
        self.table_Q6.setWordWrap(False)
        self.table_Q6.setObjectName("table_Q6")
        self.table_Q6.setColumnCount(13)
        self.table_Q6.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_Q6.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Q6.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Q6.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Q6.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Q6.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Q6.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Q6.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Q6.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Q6.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Q6.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Q6.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Q6.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Q6.setHorizontalHeaderItem(12, item)
        self.tabWidget.addTab(self.tab_hoy, "")
        self.tab_hoteles = QtWidgets.QWidget()
        self.tab_hoteles.setObjectName("tab_hoteles")
        self.label_preg7 = QtWidgets.QLabel(self.tab_hoteles)
        self.label_preg7.setGeometry(QtCore.QRect(50, 30, 691, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_preg7.setFont(font)
        self.label_preg7.setWordWrap(True)
        self.label_preg7.setObjectName("label_preg7")
        self.txt_ProvinciaQ7 = QtWidgets.QTextEdit(self.tab_hoteles)
        self.txt_ProvinciaQ7.setGeometry(QtCore.QRect(300, 120, 181, 31))
        self.txt_ProvinciaQ7.setObjectName("txt_ProvinciaQ7")
        self.txt_EstrellasQ7 = QtWidgets.QTextEdit(self.tab_hoteles)
        self.txt_EstrellasQ7.setGeometry(QtCore.QRect(80, 120, 181, 31))
        self.txt_EstrellasQ7.setObjectName("txt_EstrellasQ7")
        self.btn_submitQ7 = QtWidgets.QPushButton(self.tab_hoteles)
        self.btn_submitQ7.setGeometry(QtCore.QRect(500, 120, 181, 31))
        self.btn_submitQ7.setAutoDefault(True)
        self.btn_submitQ7.setDefault(True)
        self.btn_submitQ7.setObjectName("btn_submitQ7")
        self.list_ansQ7 = QtWidgets.QListWidget(self.tab_hoteles)
        self.list_ansQ7.setGeometry(QtCore.QRect(100, 190, 561, 291))
        self.list_ansQ7.setObjectName("list_ansQ7")
        self.label = QtWidgets.QLabel(self.tab_hoteles)
        self.label.setGeometry(QtCore.QRect(240, 160, 301, 20))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab_hoteles, "")
        self.tab_perimetro = QtWidgets.QWidget()
        self.tab_perimetro.setObjectName("tab_perimetro")
        self.label_preg8 = QtWidgets.QLabel(self.tab_perimetro)
        self.label_preg8.setGeometry(QtCore.QRect(140, 30, 491, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_preg8.setFont(font)
        self.label_preg8.setWordWrap(True)
        self.label_preg8.setObjectName("label_preg8")
        self.txt_DondeEstoyQ8 = QtWidgets.QTextEdit(self.tab_perimetro)
        self.txt_DondeEstoyQ8.setGeometry(QtCore.QRect(90, 130, 181, 31))
        self.txt_DondeEstoyQ8.setObjectName("txt_DondeEstoyQ8")
        self.txt_PerimetroQ8 = QtWidgets.QTextEdit(self.tab_perimetro)
        self.txt_PerimetroQ8.setGeometry(QtCore.QRect(310, 130, 181, 31))
        self.txt_PerimetroQ8.setObjectName("txt_PerimetroQ8")
        self.btn_submitQ8 = QtWidgets.QPushButton(self.tab_perimetro)
        self.btn_submitQ8.setGeometry(QtCore.QRect(530, 130, 181, 31))
        self.btn_submitQ8.setAutoDefault(True)
        self.btn_submitQ8.setDefault(True)
        self.btn_submitQ8.setObjectName("btn_submitQ8")
        self.list_ansQ8 = QtWidgets.QListWidget(self.tab_perimetro)
        self.list_ansQ8.setGeometry(QtCore.QRect(110, 190, 561, 291))
        self.list_ansQ8.setObjectName("list_ansQ8")
        self.tabWidget.addTab(self.tab_perimetro, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_preg1.setText(_translate("MainWindow", "¿Hay algún sitio donde podríamos comer aquí o cerca que sea económico y nos quede un % del presupuesto disponible para otras actividades del día?"))
        self.txt_dondeEstoy.setPlaceholderText(_translate("MainWindow", "Donde Estoy"))
        self.txt_presupuesto.setPlaceholderText(_translate("MainWindow", "Presupuesto"))
        self.txt_tipoEstablecimiento.setPlaceholderText(_translate("MainWindow", "Tipo Establecimiento"))
        self.txt_Perimetro.setPlaceholderText(_translate("MainWindow", "Perimetro"))
        self.txt_porciento.setPlaceholderText(_translate("MainWindow", "Porciento"))
        self.txt_criterioEconomico.setPlaceholderText(_translate("MainWindow", "Criterio Económico"))
        self.txt_tipoComida.setPlaceholderText(_translate("MainWindow", "Tipo Comida"))
        self.btn_submitQ1.setText(_translate("MainWindow", "OK"))
        self.label_preg1_ans.setText(_translate("MainWindow", "Respuesta"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_gastronomia), _translate("MainWindow", "Gastronomía"))
        self.label_preg2.setText(_translate("MainWindow", "Con X cantidad de dinero ¿Qué actividades culturales (obra de teatro, por ejemplo) podemos hacer esta semana (cuáles y dónde)?"))
        self.txt_PresupuestoQ2.setPlaceholderText(_translate("MainWindow", "Presupuesto"))
        self.txt_HoyQ2.setPlaceholderText(_translate("MainWindow", "Dia Hoy"))
        self.btn_submitQ2.setText(_translate("MainWindow", "OK"))
        item = self.table_Q2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.table_Q2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.table_Q2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tipo Evento"))
        item = self.table_Q2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Establecimiento"))
        item = self.table_Q2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Provincia"))
        item = self.table_Q2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Ubicacion"))
        item = self.table_Q2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Dia"))
        item = self.table_Q2.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Fecha"))
        item = self.table_Q2.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Tipo Ticket"))
        item = self.table_Q2.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Tarifa"))
        item = self.table_Q2.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Descripcion"))
        item = self.table_Q2.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Hora Inicia"))
        item = self.table_Q2.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Hora Termina"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_cultura), _translate("MainWindow", "Cultura"))
        self.label_preg3.setText(_translate("MainWindow", "Hay algún cine aquí que proyecte alguna película que podamos ver antes de que empiece el toque de queda?"))
        self.txt_ProvinciaQ3.setPlaceholderText(_translate("MainWindow", "Provincia Donde Estoy"))
        self.txt_GeneroQ3.setPlaceholderText(_translate("MainWindow", "Género Película"))
        self.btn_submitQ3.setText(_translate("MainWindow", "OK"))
        self.txt_ToqueQuedaQ3.setPlaceholderText(_translate("MainWindow", "Toque de Queda"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_cine), _translate("MainWindow", "Cine"))
        self.label_preg4.setText(_translate("MainWindow", "Massimo cumple años el día 20. ¿Qué bares o discotecas de precio elevado con una puntuación excelente están en o cerca  que podamos pagar sin quedarnos cortos de dinero para el día?"))
        self.txt_PresupuestoQ4.setPlaceholderText(_translate("MainWindow", "Presupuesto"))
        self.txt_CiudadQ4.setPlaceholderText(_translate("MainWindow", "Ciudad"))
        self.txt_CriterioCaroQ4.setPlaceholderText(_translate("MainWindow", "CriterioCaro"))
        self.txt_DineroNecesitoDiaQ4.setPlaceholderText(_translate("MainWindow", "Dinero Necesito Dia"))
        self.txt_PerimetroQ4.setPlaceholderText(_translate("MainWindow", "Perimetro"))
        self.btn_submitQ4.setText(_translate("MainWindow", "OK"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_cumpleanos), _translate("MainWindow", "Cumpleaños de Massimo"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_importantes), _translate("MainWindow", "Eventos Importantes"))
        self.label_preg6.setText(_translate("MainWindow", "A cuáles actividades podemos asistir hoy dada la hora actual?"))
        self.txt_PresupuestoQ6.setPlaceholderText(_translate("MainWindow", "Presupuesto"))
        self.txt_HoyQ6.setPlaceholderText(_translate("MainWindow", "Dia Hoy"))
        self.btn_submitQ6.setText(_translate("MainWindow", "OK"))
        self.txt_HoraActualQ6.setPlaceholderText(_translate("MainWindow", "Hora Actual"))
        item = self.table_Q6.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.table_Q6.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.table_Q6.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tipo Evento"))
        item = self.table_Q6.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Establecimiento"))
        item = self.table_Q6.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Provincia"))
        item = self.table_Q6.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Ubicacion"))
        item = self.table_Q6.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Dia"))
        item = self.table_Q6.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Fecha"))
        item = self.table_Q6.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Tipo Ticket"))
        item = self.table_Q6.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Tarifa"))
        item = self.table_Q6.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Descripcion"))
        item = self.table_Q6.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Hora Inicia"))
        item = self.table_Q6.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Hora Termina"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_hoy), _translate("MainWindow", "Hoy"))
        self.label_preg7.setText(_translate("MainWindow", "Buscar hoteles por clasificacion de estrellas y/o provincia."))
        self.txt_ProvinciaQ7.setPlaceholderText(_translate("MainWindow", "Provincia"))
        self.txt_EstrellasQ7.setPlaceholderText(_translate("MainWindow", "Estrellas"))
        self.btn_submitQ7.setText(_translate("MainWindow", "OK"))
        self.label.setText(_translate("MainWindow", "Si no quiere buscar Provincia deje un espacio en blanco (\' \')."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_hoteles), _translate("MainWindow", "Hoteles"))
        self.label_preg8.setText(_translate("MainWindow", "Buscar lugares según el perimetro que desee."))
        self.txt_DondeEstoyQ8.setPlaceholderText(_translate("MainWindow", "Donde Estoy"))
        self.txt_PerimetroQ8.setPlaceholderText(_translate("MainWindow", "Perimetro"))
        self.btn_submitQ8.setText(_translate("MainWindow", "OK"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_perimetro), _translate("MainWindow", "Perimetro"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())