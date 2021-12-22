from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from FrmLogin import *
from FrmLogin_prog import *
from FrmUnit import *
from FrmUnit_prog import *
from FrmUser import *
import MySQLdb as mdb

a=0

def signals(self):
    global a
    self.PB_add.clicked.connect(self.InsertData)
    self.PB_update.clicked.connect(self.UpdateData)
    self.PB_del.clicked.connect(self.DeleteData)
    self.Txt_id_user.textChanged.connect(self.select_data)
    if (a==0):
        AddRoleItem(self)
        a=1

def pesan(self, ikon, judul, isipesan):
        msgBox = QMessageBox()
        msgBox.setIcon(ikon)
        msgBox.setText(isipesan)
        msgBox.setWindowTitle(judul)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

def InsertData(self): 
    id_user = self.Txt_id_user.text()
    nama = self.Txt_nama.text()
    password = self.Txt_password.text()
    role = self.Cmb_role.currentText()
    
    try:
        con = mdb.connect('localhost','root','','pbe_final_project_db')
        
        query = ("INSERT INTO user(IdUser, Nama, Pass, Role) VALUES(%s, %s, %s, %s)")
        cur = con.cursor()
        cur.execute(query, (id_user, nama, password, role))
        con.commit()    
        pesan(self, QMessageBox.Information,"Info","Data Inserted Successfully")

    except mdb.Error as e:
        pesan(self, QMessageBox.Information,"Error","Failed")

def UpdateData(self):
    id_user = self.Txt_id_user.text()
    nama = self.Txt_nama.text()
    password = self.Txt_password.text()
    role = self.Cmb_role.currentText()
    
    try:
        con = mdb.connect('localhost','root','','pbe_final_project_db')
        
        query = ("UPDATE user SET Nama = %s, Pass = %s, Role = %s WHERE IdUser = %s")
        cur = con.cursor()
        cur.execute(query, (nama, password, role, id_user))
        con.commit()    
        
        pesan(self, QMessageBox.Information,"Info","Data Updated Successfully")

    except mdb.Error as e:
        pesan(self, QMessageBox.Information,"Error","Update Failed")

def DeleteData(self): 
    id_user = self.Txt_id_user.text()
            
    try:
        con = mdb.connect('localhost','root','','pbe_final_project_db')
        
        cur = con.cursor()
        cur.execute("DELETE FROM user WHERE IdUser = %s", [id_user])
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

        id_user = self.Txt_id_user.text()

        cur = con.cursor()
        
        # cur.execute("SELECT * FROM {} ".format('user'))
        query = ("SELECT * FROM user WHERE IdUser= %s")
        cur = con.cursor()
        cur.execute(query, (id_user))

        result = cur.fetchall()

        if result == ():
            self.Txt_nama.setText("")
            self.Txt_password.setText("")
            self.Cmb_role.setCurrentText("")
        else:
            for row_number, row_data in enumerate(result):
                for column_number, data in enumerate(row_data):
                    if (column_number==1):
                        self.Txt_nama.setText(str(data))
                    elif (column_number==2):
                        self.Txt_password.setText(str(data))
                    elif (column_number==3):
                        self.Cmb_role.setCurrentText(str(data))
        
    except mdb.Error as e:
        self.Txt_nama.setText("")
        self.Txt_password.setText("")
        self.Cmb_role.setCurrentText("")
        # pesan(self, QMessageBox.Information,"Error","Id User kosong")

def AddRoleItem(self):
    cmb1=self.Cmb_role.currentText()

    self.Cmb_role.clear()
    self.Cmb_role.addItem("User")
    self.Cmb_role.addItem("Admin")

    self.Cmb_role.setCurrentText(cmb1)
    
        
Ui_FrmUser.signals=signals
Ui_FrmUser.pesan=pesan
Ui_FrmUser.InsertData = InsertData
Ui_FrmUser.UpdateData = UpdateData
Ui_FrmUser.DeleteData = DeleteData
Ui_FrmUser.select_data = select_data


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmUser = QtWidgets.QMainWindow()
    ui = Ui_FrmUser()
    ui.setupUi(FrmUser)
    ui.signals()
    FrmUser.show()    
    sys.exit(app.exec_())