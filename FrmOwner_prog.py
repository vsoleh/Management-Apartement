from FrmOwner import *
from FrmUnit import *
from FrmUnit_prog import *
from FrmLogin import *
from FrmLogin_prog import *
from FrmUser import *
from FrmUser_prog import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
import MySQLdb as mdb


def signals(self):
    self.PB_add.clicked.connect(self.InsertData)
    self.PB_update.clicked.connect(self.UpdateData)
    self.PB_del.clicked.connect(self.DeleteData)
    self.PB_exit.clicked.connect(self.keluar)
    self.Txt_id_owner.textChanged.connect(self.select_data)


def pesan(self, ikon, judul, isipesan):
        msgBox = QMessageBox()
        msgBox.setIcon(ikon)
        msgBox.setText(isipesan)
        msgBox.setWindowTitle(judul)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()


def DBConnection(self):
    try:
        db = mdb.connect('localhost', 'root', '', 'pbe_final_project_db')
        pesan(self, QMessageBox.Information,"Connection","Database Connected Successfully")
    except mdb.Error as e:
        pesan(self, QMessageBox.Information,"Connection","Failed to connect to Database")

        sys.exit(1)


def InsertData(self): 
    id_owner = self.Txt_id_owner.text()
    nama = self.Txt_nama.text()
    tempatlahir = self.Txt_tempatlahir.text()
    tanggallahir = self.Txt_tanggallahir.date().toPyDate()
    kelamin = self.Cmb_kelamin.currentText()
    telepon = self.Txt_telepon.text()
    print(tanggallahir)
    
    #try:
    con = mdb.connect('localhost','root','','pbe_final_project_db')
    
    #query = ("INSERT INTO user(INSERT INTO `owner`(`IdOwner`, `Nama`, `TempatLahir`, `TanggalLahir`, `Kelamin`, `Telepon`)VALUES(%s, %s, %s, %s, %s, %s)",)
    cur = con.cursor()
    #cur.execute(query, (id_owner, nama, tempatlahir, tanggallahir, kelamin, telepon))
    cur.execute("INSERT INTO `owner`(`IdOwner`, `Nama`, `TempatLahir`, `TanggalLahir`, `Kelamin`, `Telepon`)VALUES(%s, %s, %s, %s, %s, %s)",([id_owner],[nama],[tempatlahir],[tanggallahir],[kelamin],[telepon]))
    con.commit()    
    pesan(self, QMessageBox.Information,"Info","Data Inserted Successfully")

    #except mdb.Error as e:
     #   pesan(self, QMessageBox.Information,"Error","Failed")


def UpdateData(self):
    id_owner = self.Txt_id_owner.text()
    nama = self.Txt_nama.text()
    tempatlahir = self.Txt_tempatlahir.text()
    tanggallahir = self.Txt_tanggallahir.date()
    kelamin = self.Cmb_kelamin.currentText()
    telepon = self.Txt_telepon.text()
    
    try:
        con = mdb.connect('localhost','root','','pbe_final_project_db')
        
        query = ("UPDATE user SET Nama = %s, TempatLahir = %s, TanggalLahir = %s, Kelamin = %s, Telepon = %s WHERE IdOwner = %s")
        cur = con.cursor()
        cur.execute(query, (nama, tempatlahir, tanggallahir, kelamin, telepon, id_owner))
        con.commit()    
        
        pesan(self, QMessageBox.Information,"Info","Data Updated Successfully")

    except mdb.Error as e:
        pesan(self, QMessageBox.Information,"Error","Update Failed")


def DeleteData(self): 
    id_owner = self.Txt_id_owner.text()
            
    try:
        con = mdb.connect('localhost','root','','pbe_final_project_db')
        
        cur = con.cursor()
        cur.execute("DELETE FROM owner WHERE IdOwner = %s", [id_owner])
        con.commit()    

        pesan(self, QMessageBox.Information,"Info","Data Deleted Successfully")

    except mdb.Error as e:
        pesan(self, QMessageBox.Information,"Error","Failed")

def select_data(self):
    try:
        con = mdb.connect(
            host="localhost",
            user="root",
            password="",
            database='pbe_final_project_db'
        )

        id_owner = self.Txt_id_owner.text()

        cur = con.cursor()
        
        # cur.execute("SELECT * FROM {} ".format('user'))
        query = ("SELECT * FROM owner WHERE IdOwner= %s")
        cur = con.cursor()
        cur.execute(query, (id_owner))

        result = cur.fetchall()
        # print(str(result))

        if result == ():
            self.Txt_nama.setText("")
            self.Txt_tempatlahir.setText("")
            self.Txt_tanggallahir.date()
            self.Cmb_kelamin.setCurrentText("")
            # print(result)
        else:
            for row_number, row_data in enumerate(result):
                # print(row_number)
                # print(row_data)
                for column_number, data in enumerate(row_data):
                    # print(column_number)
                    if (column_number==1):
                        self.Txt_nama.setText(str(data))
                    elif (column_number==2):
                        self.Txt_tempatlahir.setText(str(data))
                    elif (column_number==3):
                        self.Cmb_kelamin.setCurrentText(str(data))
        
    except mdb.Error as e:
        self.Txt_nama.setText("")
        self.Txt_tempatlahir.setText("")
        self.Txt_tanggallahir.date()
        self.Cmb_kelamin.setCurrentText("")
        self.Txt_telepon.setText("")
        # pesan(self, QMessageBox.Information,"Error","Id User kosong")

def keluar(self):
    sys.exit(1)

Ui_FrmOwner.signals=signals
Ui_FrmOwner.pesan=pesan
Ui_FrmOwner.DBConnection = DBConnection
Ui_FrmOwner.InsertData = InsertData
Ui_FrmOwner.UpdateData = UpdateData
Ui_FrmOwner.DeleteData = DeleteData
Ui_FrmOwner.select_data = select_data
Ui_FrmOwner.keluar = keluar

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmOwner = QtWidgets.QMainWindow()
    ui = Ui_FrmOwner()
    ui.setupUi(FrmOwner)
    ui.signals()
    FrmOwner.show()    
    sys.exit(app.exec_())