from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
import MySQLdb as mdb
from FrmUnit import *
from FrmUnit_prog import *
from FrmAccessCard import *
from FrmAccessCard_prog import *
from FrmFasilitas import *

def signals(self):
    self.PB_add.clicked.connect(self.InsertData)
    self.PB_update.clicked.connect(self.UpdateData)
    self.PB_del.clicked.connect(self.DeleteData)
    # self.PB_submit.clicked.connect(self.select_data)
    self.Txt_id_facility.textChanged.connect(self.select_data)

def pesan(self, ikon, judul, isipesan):
        msgBox = QMessageBox()
        msgBox.setIcon(ikon)
        msgBox.setText(isipesan)
        msgBox.setWindowTitle(judul)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

def timeBuka(self):
    if (self.SpinJamBuka.value()<10):
        JamBuka="0" + str(self.SpinJamBuka.value())
    else:
        JamBuka=str(self.SpinJamBuka.value())

    if (self.SpinMinBuka.value()<10):
        MinBuka="0" + str(self.SpinMinBuka.value())
    else:
        MinBuka=str(self.SpinMinBuka.value())

    timeBuka = JamBuka + ":" + MinBuka
    
    return timeBuka

def timeTutup(self):
    if (self.SpinJamTutup.value()<10):
        JamTutup="0" + str(self.SpinJamTutup.value())
    else:
        JamTutup=str(self.SpinJamTutup.value())

    if (self.SpinMinTutup.value()<10):
        MinTutup="0" + str(self.SpinMinTutup.value())
    else:
        MinTutup=str(self.SpinMinTutup.value())

    timeTutup = JamTutup + ":" + MinTutup
    return timeTutup

def InsertData(self): 
    id_facility = self.Txt_id_facility.text()
    nama = self.Txt_nama.text()
    timeBuka1=timeBuka(self) 
    timeTutup1=timeTutup(self)
    kapasitas = self.Txt_kapasitas.text()
    
    try:
        con = mdb.connect('localhost','root','','pbe_final_project_db')

        query = ("INSERT INTO fasilitas(IdFasilitas, Nama, JamBuka, JamTutup, Kapasitas) VALUES(%s, %s, %s, %s, %s)") 
        cur = con.cursor()
        cur.execute(query, (id_facility, nama, timeBuka1, timeTutup1, kapasitas))
        con.commit()    
        pesan(self, QMessageBox.Information,"Info","Data Inserted Successfully")

    except mdb.Error as e:
        pesan(self, QMessageBox.Information,"Error","Failed")

def UpdateData(self):
    id_facility = self.Txt_id_facility.text()
    nama = self.Txt_nama.text()
    timeBuka1=timeBuka(self)
    timeTutup1=timeTutup(self) 
    kapasitas = self.Txt_kapasitas.text()
    
    try:
        con = mdb.connect('localhost','root','','pbe_final_project_db')
        
        query = ("UPDATE fasilitas SET Nama = %s, JamBuka = %s, JamTutup = %s, Kapasitas = %s WHERE IdFasilitas = %s")
        cur = con.cursor()
        cur.execute(query, (nama, timeBuka1, timeTutup1, kapasitas, id_facility))
        con.commit()    
            
        pesan(self, QMessageBox.Information,"Info","Data Updated Successfully")

    except mdb.Error as e:
        pesan(self, QMessageBox.Information,"Error","Update Failed")

def DeleteData(self): 
    id_facility = self.Txt_id_facility.text()
            
    try:
        con = mdb.connect('localhost','root','','pbe_final_project_db')
        
        cur = con.cursor()
        cur.execute("DELETE FROM fasilitas WHERE IdFasilitas = %s", [id_facility])
        con.commit()

        pesan(self, QMessageBox.Information,"Info","Data Deleted Successfully")

    except mdb.Error as e:
        pesan(self, QMessageBox.Information,"Error","Failed")

def select_data(self):
    try:
        con = mdb.connect('localhost','root','','pbe_final_project_db')

        id_facility = self.Txt_id_facility.text()

        cur = con.cursor()
        cur.execute("SELECT * FROM fasilitas WHERE IdFasilitas = %s", [id_facility])

        result = cur.fetchall()

        # print(result)
        # Buka=result[0][3]
        # Tutup=result[0][4]
        # print(Buka)
        # print(Tutup)

        if result == ():
            self.Txt_nama.setText("")
            self.SpinJamBuka.setValue(int(0))
            self.SpinMinBuka.setValue(int(0))
            self.SpinJamTutup.setValue(int(0))
            self.SpinMinTutup.setValue(int(0))
            self.Txt_kapasitas.setText("")
        else:
            for row_number, row_data in enumerate(result):
                for column_number, data in enumerate(row_data):
                    if (column_number==1):
                        self.Txt_nama.setText(str(data))
                        # self.Cmb_Fasilitas1.setCurrentText(str(data))
                    elif (column_number==2):
                        Buka=str(data)
                        JamBuka=Buka[0:2]
                        MinBuka=Buka[3:5]
                        self.SpinJamBuka.setValue(int(JamBuka))
                        self.SpinMinBuka.setValue(int(MinBuka))
                        # self.Cmb_Fasilitas2.setCurrentText(str(data))
                    elif (column_number==3):
                        Tutup=str(data)
                        JamTutup=Tutup[0:2]
                        MinTutup=Tutup[3:5]
                        self.SpinJamTutup.setValue(int(JamTutup))
                        self.SpinMinTutup.setValue(int(MinTutup))
                        # self.Cmb_Fasilitas3.setCurrentText(str(data))
                    elif (column_number==4):
                        self.Txt_kapasitas.setText(str(data))
                        # self.Cmb_Fasilitas3.setCurrentText(str(data))
        
    except mdb.Error as e:
        self.Txt_nama.setText("")
        self.SpinJamBuka.setValue(int(0))
        self.SpinMinBuka.setValue(int(0))
        self.SpinJamTutup.setValue(int(0))
        self.SpinMinTutup.setValue(int(0)) 
        self.Txt_kapasitas.setText("")
        # pesan(self, QMessageBox.Information,"Error","Id User kosong")


Ui_FrmFasilitas.signals=signals
Ui_FrmFasilitas.pesan=pesan
Ui_FrmFasilitas.InsertData = InsertData
Ui_FrmFasilitas.UpdateData = UpdateData
Ui_FrmFasilitas.DeleteData = DeleteData
Ui_FrmFasilitas.select_data = select_data

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmFasilitas = QtWidgets.QMainWindow()
    ui = Ui_FrmFasilitas()
    ui.setupUi(FrmFasilitas)
    ui.signals()
    FrmFasilitas.show()
    sys.exit(app.exec_())
