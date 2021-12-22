from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
# from FrmDataKen_prog import *
from FrmDataKen import *
import MySQLdb as mdb

def signals(self):
    self.push_add.clicked.connect(self.InsertData)
    self.push_update.clicked.connect(self.UpdateData)
    self.push_delete.clicked.connect(self.DeleteData)

def pesan(self, ikon, judul, isipesan):
        msgBox = QMessageBox()
        msgBox.setIcon(ikon)
        msgBox.setText(isipesan)
        msgBox.setWindowTitle(judul)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

def InsertData(self): 
    line_plat = self.line_plat.text()
    jeniskendaraan = self.jeniskendaraan.text()
    line_modelken_2 = self.line_modelken_2.text()
    line_idparkir  = self.line_idparkir.text()

    blokparkir = self.blokparkir.currentText()
    lantai = self.lantai.currentText()
    noparkir = self.noparkir.currentText()
    statusparkir = self.statusparkir.currentText()
    
    try:
        con = mdb.connect('localhost','root','','pbe_final_project_db')

        query1 = ("INSERT INTO parkir (IdParkir, Block, Lantai, No, status) VALUES (%s, %s, %s, %s, %s)")
        cur1 = con.cursor()
        cur1.execute(query1, (line_idparkir, blokparkir, lantai, noparkir, statusparkir))
        con.commit() 
        
        query = ("INSERT INTO kendaraan (NoPlat, JenisKendaraan, Warna) VALUES(%s, %s, %s)")
        cur = con.cursor()
        cur.execute(query, (line_plat, jeniskendaraan, line_modelken_2))
        con.commit()
        

        pesan(self, QMessageBox.Information,"Info","Data Inserted Successfully")

    except mdb.Error as e:
        pesan(self, QMessageBox.Information,"Error","Failed")


def UpdateData(self):
    line_plat = self.line_plat.text()
    jeniskendaraan = self.jeniskendaraan.text()
    line_modelken_2 = self.line_modelken_2.text()
    line_idparkir  = self.line_idparkir.text()
    blokparkir = self.blokparkir.currentText()
    lantai = self.lantai.currentText()
    noparkir = self.noparkir.currentText()
    statusparkir = self.statusparkir.currentText()
    
    try:
        con = mdb.connect('localhost','root','','pbe_final_project_db')

        query1 = ("UPDATE parkir SET Block = %s, Lantai = %s, No = %s, status = %s WHERE NoPlat=%s")         
        cur1 = con.cursor()
        cur1.execute(query1, (line_idparkir, blokparkir, lantai, noparkir, statusparkir))
        con.commit()   
        
        query = ("UPDATE kendaraan SET JenisKendaraan = %s, Warna = %s WHERE NoPlat=%s")
        cur = con.cursor()
        cur.execute(query, (line_plat, jeniskendaraan, line_modelken_2))
        con.commit()

        pesan(self, QMessageBox.Information,"Info","Data Updated Successfully")

    except mdb.Error as e:
        pesan(self, QMessageBox.Information,"Error","Update Failed")



def DeleteData(self): 
    line_plat = self.line_plat.text()
    line_idparkir  = self.line_idparkir.text()
     
    try:
        con = mdb.connect('localhost','root','','pbe_final_project_db')

        cur1 = con.cursor()
        cur1.execute("DELETE FROM parkir WHERE IdParkir = %s", [line_idparkir])
        con.commit()
        
        cur = con.cursor()
        cur.execute("DELETE FROM kendaraan WHERE NoPlat = %s", [line_plat])
        con.commit()

        pesan(self, QMessageBox.Information,"Info","Data Deleted Successfully")

    except mdb.Error as e:
        pesan(self, QMessageBox.Information,"Error","Failed")


Ui_FrmDataKen.signals=signals
Ui_FrmDataKen.pesan = pesan
Ui_FrmDataKen.InsertData = InsertData
Ui_FrmDataKen.UpdateData = UpdateData
Ui_FrmDataKen.DeleteData = DeleteData


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmDataKen = QtWidgets.QMainWindow()
    ui = Ui_FrmDataKen()
    ui.setupUi(FrmDataKen)
    ui.signals()
    FrmDataKen.show()    
    sys.exit(app.exec_())
