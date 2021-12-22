from PyQt5 import QtCore, QtGui, QtWidgets
import MySQLdb as mdb
from FrmUnit import *
from FrmUnit_prog import *
from FrmAccessCard import *
from FrmFasilitas import *
from FrmFasilitas_prog import *

a=0

def signals(self):
    global a

    self.PB_add.clicked.connect(self.InsertData)
    self.PB_update.clicked.connect(self.UpdateData)
    self.PB_del.clicked.connect(self.DeleteData)
    # self.PB_Submit.clicked.connect(self.DisplayFasilitas1)
    self.PB_Refresh.clicked.connect(self.AddIdFasilitas)
    self.Txt_id_AccessCard.textChanged.connect(self.select_data)
    self.Cmb_Fasilitas1.currentTextChanged.connect(self.DisplayFasilitas1)
    self.Cmb_Fasilitas2.currentTextChanged.connect(self.DisplayFasilitas2)
    self.Cmb_Fasilitas3.currentTextChanged.connect(self.DisplayFasilitas3)
    
    self.PB_Fasilitas.clicked.connect(self.fasilitas)
    if (a==0):
        AddIdFasilitas(self)
        a=1

def pesan(self, ikon, judul, isipesan):
        msgBox = QMessageBox()
        msgBox.setIcon(ikon)
        msgBox.setText(isipesan)
        msgBox.setWindowTitle(judul)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

def InsertData(self): 
    id_card = self.Txt_id_AccessCard.text()
    id_fasilitas1 = self.Cmb_Fasilitas1.currentText()
    id_fasilitas2 = self.Cmb_Fasilitas2.currentText()
    id_fasilitas3 = self.Cmb_Fasilitas3.currentText()
    
    try:
        con = mdb.connect('localhost','root','','pbe_final_project_db')
        
        query = ("INSERT INTO accesscard(IdAccess, IdFasilitas1, IdFasilitas2, IdFasilitas3) VALUES(%s, %s, %s, %s)")
        cur = con.cursor()
        cur.execute(query, (id_card, id_fasilitas1, id_fasilitas2, id_fasilitas3))
        con.commit()    
        pesan(self, QMessageBox.Information,"Info","Data Inserted Successfully")

    except mdb.Error as e:
        pesan(self, QMessageBox.Information,"Error","Failed")

def UpdateData(self):
    id_card = self.Txt_id_AccessCard.text()
    id_fasilitas1 = self.Cmb_Fasilitas1.currentText()
    id_fasilitas2 = self.Cmb_Fasilitas2.currentText()
    id_fasilitas3 = self.Cmb_Fasilitas3.currentText()
    
    try:
        con = mdb.connect('localhost','root','','pbe_final_project_db')
        
        query = ("UPDATE accesscard SET IdFasilitas1 = %s, IdFasilitas2 = %s, IdFasilitas3 = %s WHERE IdAccess = %s")
        cur = con.cursor()
        cur.execute(query, (id_fasilitas1, id_fasilitas2, id_fasilitas3, id_card))
        con.commit()    
        
        pesan(self, QMessageBox.Information,"Info","Data Updated Successfully")

    except mdb.Error as e:
        pesan(self, QMessageBox.Information,"Error","Update Failed")

def DeleteData(self): 
    id_card = self.Txt_id_AccessCard.text()
            
    try:
        con = mdb.connect('localhost','root','','pbe_final_project_db')
        
        cur = con.cursor()
        cur.execute("DELETE FROM accesscard WHERE IdAccess = %s", [id_card])
        con.commit()

        pesan(self, QMessageBox.Information,"Info","Data Deleted Successfully")

    except mdb.Error as e:
        pesan(self, QMessageBox.Information,"Error","Failed")

def select_data(self):
    try:
        con = mdb.connect('localhost','root','','pbe_final_project_db')

        id_card = self.Txt_id_AccessCard.text()

        cur = con.cursor()
        cur.execute("SELECT * FROM accesscard WHERE IdAccess= %s", [id_card])

        result = cur.fetchall()

        if result == ():
            self.Cmb_Fasilitas1.setCurrentText("")
            self.Cmb_Fasilitas2.setCurrentText("")
            self.Cmb_Fasilitas3.setCurrentText("")
        else:
            for row_number, row_data in enumerate(result):
                for column_number, data in enumerate(row_data):
                    if (column_number==1):
                        self.Cmb_Fasilitas1.setCurrentText(str(data))
                    elif (column_number==2):
                        self.Cmb_Fasilitas2.setCurrentText(str(data))
                    elif (column_number==3):
                        self.Cmb_Fasilitas3.setCurrentText(str(data))
        
    except mdb.Error as e:
        self.Cmb_Fasilitas1.setCurrentText("")
        self.Cmb_Fasilitas2.setCurrentText("")
        self.Cmb_Fasilitas3.setCurrentText("")
        # pesan(self, QMessageBox.Information,"Error","Id User kosong")

def AddIdFasilitas(self):
    con = mdb.connect('localhost','root','','pbe_final_project_db')

    cur = con.cursor()
    cur.execute("SELECT * FROM fasilitas")

    result = cur.fetchall()
    self.Cmb_Fasilitas1.clear()
    self.Cmb_Fasilitas2.clear()
    self.Cmb_Fasilitas3.clear()
    self.Cmb_Fasilitas1.addItem("")
    self.Cmb_Fasilitas2.addItem("")
    self.Cmb_Fasilitas3.addItem("")
    # print(result)
    # print(result[0][0])
    if result == ():
        self.Cmb_Fasilitas1.setCurrentText("")
        self.Cmb_Fasilitas2.setCurrentText("")
        self.Cmb_Fasilitas3.setCurrentText("")
    else:
        for row_number, row_data in enumerate(result):
            self.Cmb_Fasilitas1.addItem(str(row_data[0]))
            self.Cmb_Fasilitas2.addItem(str(row_data[0]))
            self.Cmb_Fasilitas3.addItem(str(row_data[0]))

def DisplayFasilitas1(self):
    id_facility = self.Cmb_Fasilitas1.currentText()

    try:
        con = mdb.connect('localhost','root','','pbe_final_project_db')
        
        cur = con.cursor()
        cur.execute("SELECT * FROM fasilitas WHERE IdFasilitas = %s", [id_facility])

        result = cur.fetchall()
        # print(result)

        if result == ():
            self.Lbl_Nama1.setText("")
            self.Lbl_Operation1.setText("")
        else:
            for row_number, row_data in enumerate(result):
                self.Lbl_Nama1.setText(str(row_data[1]))
                operational=str(row_data[2]) + " - " + str(row_data[3])
                self.Lbl_Operation1.setText(operational)
    
    except mdb.Error as e:
        self.Lbl_Nama1.setText("")
        self.Lbl_Operation1.setText("")

def DisplayFasilitas2(self):
    id_facility = self.Cmb_Fasilitas2.currentText()

    try:
        con = mdb.connect('localhost','root','','pbe_final_project_db')
        
        cur = con.cursor()
        cur.execute("SELECT * FROM fasilitas WHERE IdFasilitas = %s", [id_facility])

        result = cur.fetchall()
        # print(result)

        if result == ():
            self.Lbl_Nama2.setText("")
            self.Lbl_Operation2.setText("")
        else:
            for row_number, row_data in enumerate(result):
                self.Lbl_Nama2.setText(str(row_data[1]))
                operational=str(row_data[2]) + " - " + str(row_data[3])
                self.Lbl_Operation2.setText(operational)
    
    except mdb.Error as e:
        self.Lbl_Nama2.setText("")
        self.Lbl_Operation2.setText("")

def DisplayFasilitas3(self):
    id_facility = self.Cmb_Fasilitas3.currentText()

    try:
        con = mdb.connect('localhost','root','','pbe_final_project_db')
        
        cur = con.cursor()
        cur.execute("SELECT * FROM fasilitas WHERE IdFasilitas = %s", [id_facility])

        result = cur.fetchall()
        # print(result)

        if result == ():
            self.Lbl_Nama3.setText("")
            self.Lbl_Operation3.setText("")
        else:
            for row_number, row_data in enumerate(result):
                self.Lbl_Nama3.setText(str(row_data[1]))
                operational=str(row_data[2]) + " - " + str(row_data[3])
                self.Lbl_Operation3.setText(operational)
    
    except mdb.Error as e:
        self.Lbl_Nama3.setText("")
        self.Lbl_Operation3.setText("")

def fasilitas(self):
    self.FrmFasilitas = QtWidgets.QMainWindow()
    self.ui_fasilitas = Ui_FrmFasilitas()
    self.ui_fasilitas.setupUi(self.FrmFasilitas)
    self.ui_fasilitas.signals()
    self.FrmFasilitas.show()


Ui_FrmAccessCard.signals=signals
Ui_FrmAccessCard.pesan=pesan
Ui_FrmAccessCard.InsertData = InsertData
Ui_FrmAccessCard.UpdateData = UpdateData
Ui_FrmAccessCard.DeleteData = DeleteData
Ui_FrmAccessCard.select_data = select_data
Ui_FrmAccessCard.AddIdFasilitas = AddIdFasilitas
Ui_FrmAccessCard.DisplayFasilitas1 = DisplayFasilitas1
Ui_FrmAccessCard.DisplayFasilitas2 = DisplayFasilitas2
Ui_FrmAccessCard.DisplayFasilitas3 = DisplayFasilitas3
Ui_FrmAccessCard.fasilitas = fasilitas


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmAccessCard = QtWidgets.QMainWindow()
    ui = Ui_FrmAccessCard()
    ui.setupUi(FrmAccessCard)
    ui.signals()
    FrmAccessCard.show()
    sys.exit(app.exec_())
