from visual import *
import turista as t
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QVBoxLayout

class visual(Ui_MainWindow):
    def __init__(self, window):
        super().__init__()
        self.setupUi(window)
        self.btn_submitQ1.clicked.connect(self.question1)
        self.btn_submitQ2.clicked.connect(self.question2)
        self.btn_submitQ3.clicked.connect(self.question3)
        self.btn_submitQ4.clicked.connect(self.question4)
        
        self.btn_submitQ6.clicked.connect(self.question6_extra)
        self.btn_submitQ7.clicked.connect(self.question7_extra)        
        self.btn_submitQ8.clicked.connect(self.question8_extra)

    def question1(self):
        _translate = QtCore.QCoreApplication.translate
        DondeEstoy = self.txt_dondeEstoy.toPlainText()
        TipoEstablecimiento = self.txt_tipoEstablecimiento.toPlainText()
        ComidaBusco = self.txt_tipoComida.toPlainText()
        Perimetro = self.txt_Perimetro.toPlainText()
        Presupuesto = self.txt_presupuesto.toPlainText()
        CriterioEconomico = self.txt_criterioEconomico.toPlainText()
        Porciento = self.txt_porciento.toPlainText()
        self.label_preg1_ans.setText(_translate("MainWindow", t.ejercicio1(DondeEstoy, TipoEstablecimiento,ComidaBusco,Perimetro,Presupuesto,CriterioEconomico,Porciento)))

    def question2(self):
        _translate = QtCore.QCoreApplication.translate
        self.table_Q2.setRowCount(0)
        Presupuesto = self.txt_PresupuestoQ2.toPlainText()
        Hoy = self.txt_HoyQ2.toPlainText()
        items = t.eventos_semana(Presupuesto,Hoy) 
        columns = len(items)
        self.table_Q2.setRowCount(columns)
        for x in range(0, columns):
            Id = items[x][0][0]
            Actividad = items[x][0][1]
            TipoEvento = items[x][0][2]
            TipoEstablecimiento = items[x][0][3]
            Provincia = items[x][0][4]
            Ubicacion = items[x][0][5]
            DiaEvento = items[x][0][6]
            Fecha = items[x][0][7]
            TipoTicket = items[x][0][8]
            Tarifa = items[x][0][9]
            Descripcion = items[x][0][10]
            HoraInicia = items[x][0][11]
            HoraTermina = items[x][0][12]
            self.table_Q2.setItem(x,0, QtWidgets.QTableWidgetItem(str(Id)))
            self.table_Q2.setItem(x,1, QtWidgets.QTableWidgetItem(Actividad))
            self.table_Q2.setItem(x,2, QtWidgets.QTableWidgetItem(TipoEvento))
            self.table_Q2.setItem(x,3, QtWidgets.QTableWidgetItem(TipoEstablecimiento))
            self.table_Q2.setItem(x,4, QtWidgets.QTableWidgetItem(Provincia))
            self.table_Q2.setItem(x,5, QtWidgets.QTableWidgetItem(Ubicacion))
            self.table_Q2.setItem(x,6, QtWidgets.QTableWidgetItem(str(DiaEvento)))
            self.table_Q2.setItem(x,7, QtWidgets.QTableWidgetItem(Fecha))
            self.table_Q2.setItem(x,8, QtWidgets.QTableWidgetItem(TipoTicket))
            self.table_Q2.setItem(x,9, QtWidgets.QTableWidgetItem(str(Tarifa)))
            self.table_Q2.setItem(x,10, QtWidgets.QTableWidgetItem(Descripcion))
            self.table_Q2.setItem(x,11, QtWidgets.QTableWidgetItem(str(HoraInicia)))
            self.table_Q2.setItem(x,12, QtWidgets.QTableWidgetItem(str(HoraTermina)))

    def question3(self):
        _translate = QtCore.QCoreApplication.translate
        Provincia = self.txt_ProvinciaQ3.toPlainText()
        Genero = self.txt_GeneroQ3.toPlainText()
        ToqueQueda = self.txt_ToqueQuedaQ3.toPlainText()
        items = t.buscar_cines(Provincia,Genero,ToqueQueda) 
        self.list_ansQ3.clear()
        for e in items:
            self.list_ansQ3.addItem(e)

    def question4(self):
        _translate = QtCore.QCoreApplication.translate
        Presupuesto = self.txt_PresupuestoQ4.toPlainText()
        Perimetro = self.txt_PerimetroQ4.toPlainText()
        DineroNecesitoDia = self.txt_DineroNecesitoDiaQ4.toPlainText()
        Ciudad = self.txt_CiudadQ4.toPlainText()
        CriterioCaro = self.txt_CriterioCaroQ4.toPlainText()
        items = t.buscar_bares_y_discotecas(Presupuesto,Perimetro,DineroNecesitoDia,Ciudad,CriterioCaro) 
        self.list_ansQ4.clear()
        for e in items:
            self.list_ansQ4.addItem(e)

    def question6_extra(self):
        _translate = QtCore.QCoreApplication.translate
        self.table_Q6.setRowCount(0)
        Presupuesto = self.txt_PresupuestoQ6.toPlainText()
        Hoy = self.txt_HoyQ6.toPlainText()
        HoraActual = self.txt_HoraActualQ6.toPlainText()
        items = t.eventos_hoy(Presupuesto,Hoy,HoraActual) 
        columns = len(items)
        self.table_Q6.setRowCount(columns)
        for x in range(0, columns):
            Id = items[x][0][0]
            Actividad = items[x][0][1]
            TipoEvento = items[x][0][2]
            TipoEstablecimiento = items[x][0][3]
            Provincia = items[x][0][4]
            Ubicacion = items[x][0][5]
            DiaEvento = items[x][0][6]
            Fecha = items[x][0][7]
            TipoTicket = items[x][0][8]
            Tarifa = items[x][0][9]
            Descripcion = items[x][0][10]
            HoraInicia = items[x][0][11]
            HoraTermina = items[x][0][12]
            self.table_Q6.setItem(x,0, QtWidgets.QTableWidgetItem(str(Id)))
            self.table_Q6.setItem(x,1, QtWidgets.QTableWidgetItem(Actividad))
            self.table_Q6.setItem(x,2, QtWidgets.QTableWidgetItem(TipoEvento))
            self.table_Q6.setItem(x,3, QtWidgets.QTableWidgetItem(TipoEstablecimiento))
            self.table_Q6.setItem(x,4, QtWidgets.QTableWidgetItem(Provincia))
            self.table_Q6.setItem(x,5, QtWidgets.QTableWidgetItem(Ubicacion))
            self.table_Q6.setItem(x,6, QtWidgets.QTableWidgetItem(str(DiaEvento)))
            self.table_Q6.setItem(x,7, QtWidgets.QTableWidgetItem(Fecha))
            self.table_Q6.setItem(x,8, QtWidgets.QTableWidgetItem(TipoTicket))
            self.table_Q6.setItem(x,9, QtWidgets.QTableWidgetItem(str(Tarifa)))
            self.table_Q6.setItem(x,10, QtWidgets.QTableWidgetItem(Descripcion))
            self.table_Q6.setItem(x,11, QtWidgets.QTableWidgetItem(str(HoraInicia)))
            self.table_Q6.setItem(x,12, QtWidgets.QTableWidgetItem(str(HoraTermina)))

    def question7_extra(self):
        _translate = QtCore.QCoreApplication.translate
        Presupuesto = self.txt_EstrellasQ7.toPlainText()
        Provincia = self.txt_ProvinciaQ7.toPlainText()
        items = t.buscar_hoteles(Presupuesto,Provincia) 
        self.list_ansQ7.clear()
        for e in items:
            self.list_ansQ7.addItem(e)

    def question8_extra(self):
        _translate = QtCore.QCoreApplication.translate
        DondeEstoy = self.txt_DondeEstoyQ8.toPlainText()
        Perimetro = self.txt_PerimetroQ8.toPlainText()
        items = t.miperimetro(DondeEstoy,Perimetro) 
        self.list_ansQ8.clear()
        for e in items:
            self.list_ansQ8.addItem(e)

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = visual(MainWindow)

MainWindow.show()
app.exec_()