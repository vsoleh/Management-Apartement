from FrmUnit import *
from FrmLogin import *
from FrmLogin_prog import *
from FrmUser import *
from FrmUser_prog import *
from FrmAccessCard import *
from FrmAccessCard_prog import *
from FrmFasilitas import *
from FrmFasilitas_prog import *
from FrmDataKen import *
from FrmDataKen_prog import *
from FrmOwner import *
from FrmOwner_prog import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
import MySQLdb as mdb

a=0

def signals(self):
    global a

    self.PB_add.clicked.connect(self.InsertData)
    self.PB_update.clicked.connect(self.UpdateData)
    self.PB_del.clicked.connect(self.DeleteData)
    self.PB_Login.clicked.connect(self.login)
    self.PB_Logout.clicked.connect(self.logout)
    self.PB_User.clicked.connect(self.user)
    self.PB_AccessCard.clicked.connect(self.AccessCard)
    self.Txt_nounit.textChanged.connect(self.select_data)
    self.PB_Vehicle.clicked.connect(self.kendaraan)
    self.PB_Owner.clicked.connect(self.Owner)
    self.PB_Owner_Refresh.clicked.connect(self.AddIdOwner)
    self.PB_Vehicle_Refresh.clicked.connect(self.AddIdKendaraan)
    self.PB_AccessCard_Refresh.clicked.connect(self.AddIdAccessCard)
    self.Combo_aksescard1.currentTextChanged.connect(self.DisplayAccessCard1)
    self.Combo_aksescard2.currentTextChanged.connect(self.DisplayAccessCard2)
    self.Combo_aksescard3.currentTextChanged.connect(self.DisplayAccessCard3)
    self.Combo_aksescard4.currentTextChanged.connect(self.DisplayAccessCard4)
    self.Combo_aksescard5.currentTextChanged.connect(self.DisplayAccessCard5)
    self.Combo_kendaraan1.currentTextChanged.connect(self.DisplayKendaraan1)
    self.Combo_kendaraan2.currentTextChanged.connect(self.DisplayKendaraan2)
    self.Combo_kendaraan3.currentTextChanged.connect(self.DisplayKendaraan3)
    self.Combo_kendaraan4.currentTextChanged.connect(self.DisplayKendaraan4)
    self.Combo_kendaraan5.currentTextChanged.connect(self.DisplayKendaraan5)
    self.Combo_IdOwner.currentTextChanged.connect(self.DisplayOwner)
    if (a == 0):
        AddIdAccessCard(self)
        AddIdKendaraan(self)
        AddIdOwner(self)
        logout(self)
        a=1    

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
    if (self.Lbl_user_role.text()=='Admin'):
        no_unit = self.Txt_nounit.text()
        tipe = self.Txt_tipe.text()
        luas = int(self.Txt_luas.text())
        id_owner = self.Combo_IdOwner.currentText()
        id_aksescard1=self.Combo_aksescard1.currentText()
        id_aksescard2=self.Combo_aksescard2.currentText()
        id_aksescard3=self.Combo_aksescard3.currentText()
        id_aksescard4=self.Combo_aksescard4.currentText()
        id_aksescard5=self.Combo_aksescard5.currentText()
        id_kendaraan1=self.Combo_kendaraan1.currentText()
        id_kendaraan2=self.Combo_kendaraan2.currentText()
        id_kendaraan3=self.Combo_kendaraan3.currentText()
        id_kendaraan4=self.Combo_kendaraan4.currentText()
        id_kendaraan5=self.Combo_kendaraan5.currentText()
        iuranstatus = self.Combo_StatusIuran.currentText()
        
    
        try:
            con = mdb.connect('localhost','root','','pbe_final_project_db')
            
            query = ("INSERT INTO unit(NoUnit, Tipe, Luas, IdOwner, IdAksesCard1, IdAksesCard2, IdAksesCard3, IdAksesCard4, IdAksesCard5, IdKendaraan1, IdKendaraan2, IdKendaraan3, IdKendaraan4, IdKendaraan5, IuranStatus) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
            cur = con.cursor()
            cur.execute(query, (no_unit,tipe,luas,id_owner,id_aksescard1,id_aksescard2,id_aksescard3,id_aksescard4,id_aksescard5,id_kendaraan1,id_kendaraan2,id_kendaraan3,id_kendaraan4,id_kendaraan5,iuranstatus))
            con.commit()    
            pesan(self, QMessageBox.Information,"Info","Data Inserted Successfully")

        except mdb.Error as e:
            pesan(self, QMessageBox.Information,"Error","Failed")
    else:
        pesan(self,QMessageBox.Information,"Warning","you dont have authorisation, Please contact Admin")

def UpdateData(self):
    if (self.Lbl_user_role.text()=='Admin'):
        no_unit = self.Txt_nounit.text()
        tipe = self.Txt_tipe.text()
        luas = int(self.Txt_luas.text())
        id_owner = self.Combo_IdOwner.currentText()
        id_aksescard1=self.Combo_aksescard1.currentText()
        id_aksescard2=self.Combo_aksescard2.currentText()
        id_aksescard3=self.Combo_aksescard3.currentText()
        id_aksescard4=self.Combo_aksescard4.currentText()
        id_aksescard5=self.Combo_aksescard5.currentText()
        id_kendaraan1=self.Combo_kendaraan1.currentText()
        id_kendaraan2=self.Combo_kendaraan2.currentText()
        id_kendaraan3=self.Combo_kendaraan3.currentText()
        id_kendaraan4=self.Combo_kendaraan4.currentText()
        id_kendaraan5=self.Combo_kendaraan5.currentText()
        iuranstatus = self.Combo_StatusIuran.currentText()
    
    
        try:
            con = mdb.connect('localhost','root','','pbe_final_project_db')
        
            query = ("UPDATE unit SET Tipe = %s, Luas = %s, IdOwner = %s, IdAksesCard1 = %s, IdAksesCard2 = %s, IdAksesCard3 = %s, IdAksesCard4 = %s, IdAksesCard5 = %s, IdKendaraan1 = %s, IdKendaraan2 = %s, IdKendaraan3 = %s, IdKendaraan4 = %s, IdKendaraan5 = %s, IuranStatus = %s WHERE NoUnit = %s")
            cur = con.cursor()
            cur.execute(query, (tipe, luas, id_owner, id_aksescard1, id_aksescard2, id_aksescard3, id_aksescard4, id_aksescard5, id_kendaraan1, id_kendaraan2, id_kendaraan3, id_kendaraan4, id_kendaraan5, iuranstatus, no_unit))
            con.commit()    
            
            pesan(self, QMessageBox.Information,"Info","Data Updated Successfully")

        except mdb.Error as e:
            pesan(self, QMessageBox.Information,"Error","Update Failed")
    else:
        pesan(self,QMessageBox.Information,"Warning","you dont have authorisation, Please contact Admin")

def DeleteData(self): 
    if (self.Lbl_user_role.text()=='Admin'):
        no_unit = self.Txt_nounit.text()
    
        try:
            con = mdb.connect('localhost','root','','pbe_final_project_db')
            
            cur = con.cursor()
            cur.execute("DELETE FROM unit WHERE NoUnit = %s", [no_unit])
            con.commit()    

            pesan(self, QMessageBox.Information,"Info","Data Deleted Successfully")
            self.Txt_nounit.setText("")

        except mdb.Error as e:
            pesan(self, QMessageBox.Information,"Error","Failed")
    else:
        pesan(self,QMessageBox.Information,"Warning","you dont have authorisation, Please contact Admin")

def select_data(self):
    try:
        con = mdb.connect('localhost','root','','pbe_final_project_db')

        no_unit = self.Txt_nounit.text()

        # query = ("SELECT * FROM unit WHERE NoUnit= %s")
        cur = con.cursor()
        # cur.execute(query, (no_unit))
        cur.execute("SELECT * FROM unit WHERE NoUnit= %s", [no_unit])

        result = cur.fetchall()
        # print(result)


        if result == ():
            ClearDataUnitForm(self)
        else:
            # print(result[0][1])
            self.Txt_tipe.setText(result[0][1])
            self.Txt_luas.setText(str(result[0][2]))
            self.Combo_IdOwner.setCurrentText(result[0][3])
            self.Combo_aksescard1.setCurrentText(result[0][4])
            self.Combo_aksescard2.setCurrentText(result[0][5])
            self.Combo_aksescard3.setCurrentText(result[0][6])
            self.Combo_aksescard4.setCurrentText(result[0][7])
            self.Combo_aksescard5.setCurrentText(result[0][8])
            self.Combo_kendaraan1.setCurrentText(result[0][9])
            self.Combo_kendaraan2.setCurrentText(result[0][10])
            self.Combo_kendaraan3.setCurrentText(result[0][11])
            self.Combo_kendaraan4.setCurrentText(result[0][12])
            self.Combo_kendaraan5.setCurrentText(result[0][13])
            self.Combo_StatusIuran.setCurrentText(result[0][14])
        
    except mdb.Error as e:
            self.ClearDataUnitForm(self)

def user(self):
    if (self.Lbl_user_role.text()=='Admin'):
        self.window_user = QtWidgets.QMainWindow()
        self.ui_user = Ui_FrmUser()
        self.ui_user.setupUi(self.window_user) 
        self.ui_user.signals()
        self.window_user.show()   
    else:
        pesan(self,QMessageBox.Information,"Warning","you dont have authorisation, Please contact Admin")
    
def login(self):
    global a

    self.FrmLoginMainWindow = QtWidgets.QMainWindow()
    self.ui_login = Ui_FrmLoginMainWindow()
    self.ui_login.setupUi(self.FrmLoginMainWindow)
    self.ui_login.signals()
    self.FrmLoginMainWindow.show()
    a=0

def logout(self):
        self.Lbl_CurrentUser.setText("Guest")
        self.Lbl_user_role.setText("")

def AccessCard(self):
    if (self.Lbl_user_role.text()=='Admin'):
        self.FrmAccessCard = QtWidgets.QMainWindow()
        self.ui_login = Ui_FrmAccessCard()
        self.ui_login.setupUi(self.FrmAccessCard)
        self.ui_login.signals()
        self.FrmAccessCard.show()
    else:
        pesan(self,QMessageBox.Information,"Warning","you dont have authorisation, Please contact Admin")

def kendaraan(self):
    if (self.Lbl_user_role.text()=='Admin'):
        self.FrmDataKen = QtWidgets.QMainWindow()
        self.ui_login = Ui_FrmDataKen()
        self.ui_login.setupUi(self.FrmDataKen)
        self.ui_login.signals()
        self.FrmDataKen.show()
    else:
        pesan(self,QMessageBox.Information,"Warning","you dont have authorisation, Please contact Admin")

def Owner(self):
    if (self.Lbl_user_role.text()=='Admin'):
        self.FrmOwner = QtWidgets.QMainWindow()
        self.ui_owner = Ui_FrmOwner()
        self.ui_owner.setupUi(self.FrmOwner)
        self.ui_owner.signals()
        self.FrmOwner.show()
    else:
        pesan(self,QMessageBox.Information,"Warning","you dont have authorisation, Please contact Admin")

def AddIdAccessCard(self):
    
    cmb1=self.Combo_aksescard1.currentText()
    cmb2=self.Combo_aksescard2.currentText()
    cmb3=self.Combo_aksescard3.currentText()
    cmb4=self.Combo_aksescard4.currentText()
    cmb5=self.Combo_aksescard5.currentText()

    con = mdb.connect('localhost','root','','pbe_final_project_db')

    cur = con.cursor()
    cur.execute("SELECT * FROM accesscard")

    result = cur.fetchall()
    self.Combo_aksescard1.clear()
    self.Combo_aksescard2.clear()
    self.Combo_aksescard3.clear()
    self.Combo_aksescard4.clear()
    self.Combo_aksescard5.clear()
    # self.Combo_aksescard1.addItem("")
    # self.Combo_aksescard2.addItem("")
    # self.Combo_aksescard3.addItem("")
    # self.Combo_aksescard4.addItem("")
    # self.Combo_aksescard5.addItem("")
    
    if result == ():
        ClearDataAccessCard(self)
      
    else:
        for row_number, row_data in enumerate(result):
            self.Combo_aksescard1.addItem(str(row_data[0]))
            self.Combo_aksescard2.addItem(str(row_data[0]))
            self.Combo_aksescard3.addItem(str(row_data[0]))
            self.Combo_aksescard4.addItem(str(row_data[0]))
            self.Combo_aksescard5.addItem(str(row_data[0]))

    self.Combo_aksescard1.setCurrentText(cmb1)
    self.Combo_aksescard2.setCurrentText(cmb2)
    self.Combo_aksescard3.setCurrentText(cmb3)
    self.Combo_aksescard4.setCurrentText(cmb4)
    self.Combo_aksescard5.setCurrentText(cmb5)
    
def AddIdKendaraan(self):
    
    cmb1=self.Combo_kendaraan1.currentText()
    cmb2=self.Combo_kendaraan2.currentText()
    cmb3=self.Combo_kendaraan3.currentText()
    cmb4=self.Combo_kendaraan4.currentText()
    cmb5=self.Combo_kendaraan5.currentText()

    con = mdb.connect('localhost','root','','pbe_final_project_db')

    cur = con.cursor()
    cur.execute("SELECT * FROM kendaraan")

    result = cur.fetchall()
    self.Combo_kendaraan1.clear()
    self.Combo_kendaraan2.clear()
    self.Combo_kendaraan3.clear()
    self.Combo_kendaraan4.clear()
    self.Combo_kendaraan5.clear()
    # self.Combo_kendaraan1.addItem("")
    # self.Combo_kendaraan2.addItem("")
    # self.Combo_kendaraan3.addItem("")
    # self.Combo_kendaraan4.addItem("")
    # self.Combo_kendaraan5.addItem("")
    
    if result == ():
        ClearDataKendaraan(self)
    else:
        for row_number, row_data in enumerate(result):
            self.Combo_kendaraan1.addItem(str(row_data[0]))
            self.Combo_kendaraan2.addItem(str(row_data[0]))
            self.Combo_kendaraan3.addItem(str(row_data[0]))
            self.Combo_kendaraan4.addItem(str(row_data[0]))
            self.Combo_kendaraan5.addItem(str(row_data[0]))
    
    self.Combo_kendaraan1.setCurrentText(cmb1)
    self.Combo_kendaraan2.setCurrentText(cmb2)
    self.Combo_kendaraan3.setCurrentText(cmb3)
    self.Combo_kendaraan4.setCurrentText(cmb4)
    self.Combo_kendaraan5.setCurrentText(cmb5)

def AddIdOwner(self):
    cmb1=self.Combo_IdOwner.currentText()
    
    con = mdb.connect('localhost','root','','pbe_final_project_db')

    cur = con.cursor()
    cur.execute("SELECT * FROM owner")

    result = cur.fetchall()
    self.Combo_IdOwner.clear()
    # self.Combo_IdOwner.addItem("")
    
    if result == ():
        self.Combo_IdOwner.setCurrentText("")
    else:
        for row_number, row_data in enumerate(result):
            self.Combo_IdOwner.addItem(str(row_data[0]))
            
    self.Combo_IdOwner.setCurrentText(cmb1)

def ClearDataAccessCard(self):
    self.Combo_aksescard1.setCurrentText("")
    self.Combo_aksescard2.setCurrentText("")
    self.Combo_aksescard3.setCurrentText("")
    self.Combo_aksescard4.setCurrentText("")
    self.Combo_aksescard5.setCurrentText("")

def ClearDataKendaraan(self):
    self.Combo_kendaraan1.setCurrentText("")
    self.Combo_kendaraan2.setCurrentText("")
    self.Combo_kendaraan3.setCurrentText("")
    self.Combo_kendaraan4.setCurrentText("")
    self.Combo_kendaraan5.setCurrentText("")

def ClearDataUnitForm(self):
    self.Txt_tipe.setText("")
    self.Txt_luas.setText("")
    self.Combo_IdOwner.setCurrentText("")
    ClearDataAccessCard(self)
    ClearDataKendaraan(self)

def DisplayAccessCard1(self):
    con = mdb.connect('localhost','root','','pbe_final_project_db')

    AccessCard = self.Combo_aksescard1.currentText()

    cur = con.cursor()
    cur.execute("SELECT * FROM accesscard WHERE IdAccess= %s", [AccessCard])

    result = cur.fetchall()

    if result == ():
        self.Lbl_AC1_Fasilitas1.setText("")
        self.Lbl_AC1_Fasilitas2.setText("")
        self.Lbl_AC1_Fasilitas3.setText("")
    else:
        IdFasilitas1=result[0][1]
        IdFasilitas2=result[0][2]
        IdFasilitas3=result[0][3]
        
        cur1 = con.cursor()
        cur1.execute("SELECT * FROM fasilitas WHERE IdFasilitas= %s", [IdFasilitas1])

        result1 = cur1.fetchall()
        if result1 == ():
            self.Lbl_AC1_Fasilitas1.setText("")
        else:
            self.Lbl_AC1_Fasilitas1.setText(result1[0][1])

        cur2 = con.cursor()
        cur2.execute("SELECT * FROM fasilitas WHERE IdFasilitas= %s", [IdFasilitas2])

        result2 = cur2.fetchall()
        if result2 == ():
            self.Lbl_AC1_Fasilitas2.setText("")
        else:
            self.Lbl_AC1_Fasilitas2.setText(result2[0][1])

        cur3 = con.cursor()
        cur3.execute("SELECT * FROM fasilitas WHERE IdFasilitas= %s", [IdFasilitas3])

        result3 = cur3.fetchall()
        if result3 == ():
            self.Lbl_AC1_Fasilitas3.setText("")
        else:
            self.Lbl_AC1_Fasilitas3.setText(result3[0][1])

def DisplayAccessCard2(self):
    con = mdb.connect('localhost','root','','pbe_final_project_db')

    AccessCard = self.Combo_aksescard2.currentText()

    cur = con.cursor()
    cur.execute("SELECT * FROM accesscard WHERE IdAccess= %s", [AccessCard])

    result = cur.fetchall()

    if result == ():
        self.Lbl_AC2_Fasilitas1.setText("")
        self.Lbl_AC2_Fasilitas2.setText("")
        self.Lbl_AC2_Fasilitas3.setText("")
    else:
        IdFasilitas1=result[0][1]
        IdFasilitas2=result[0][2]
        IdFasilitas3=result[0][3]
        
        cur1 = con.cursor()
        cur1.execute("SELECT * FROM fasilitas WHERE IdFasilitas= %s", [IdFasilitas1])

        result1 = cur1.fetchall()
        if result1 == ():
            self.Lbl_AC2_Fasilitas1.setText("")
        else:
            self.Lbl_AC2_Fasilitas1.setText(result1[0][1])

        cur2 = con.cursor()
        cur2.execute("SELECT * FROM fasilitas WHERE IdFasilitas= %s", [IdFasilitas2])

        result2 = cur2.fetchall()
        if result2 == ():
            self.Lbl_AC2_Fasilitas2.setText("")
        else:
            self.Lbl_AC2_Fasilitas2.setText(result2[0][1])

        cur3 = con.cursor()
        cur3.execute("SELECT * FROM fasilitas WHERE IdFasilitas= %s", [IdFasilitas3])

        result3 = cur3.fetchall()
        if result3 == ():
            self.Lbl_AC2_Fasilitas3.setText("")
        else:
            self.Lbl_AC2_Fasilitas3.setText(result3[0][1])

def DisplayAccessCard3(self):
    con = mdb.connect('localhost','root','','pbe_final_project_db')

    AccessCard = self.Combo_aksescard3.currentText()

    cur = con.cursor()
    cur.execute("SELECT * FROM accesscard WHERE IdAccess= %s", [AccessCard])

    result = cur.fetchall()

    if result == ():
        self.Lbl_AC3_Fasilitas1.setText("")
        self.Lbl_AC3_Fasilitas2.setText("")
        self.Lbl_AC3_Fasilitas3.setText("")
    else:
        IdFasilitas1=result[0][1]
        IdFasilitas2=result[0][2]
        IdFasilitas3=result[0][3]
        
        cur1 = con.cursor()
        cur1.execute("SELECT * FROM fasilitas WHERE IdFasilitas= %s", [IdFasilitas1])

        result1 = cur1.fetchall()
        if result1 == ():
            self.Lbl_AC3_Fasilitas1.setText("")
        else:
            self.Lbl_AC3_Fasilitas1.setText(result1[0][1])

        cur2 = con.cursor()
        cur2.execute("SELECT * FROM fasilitas WHERE IdFasilitas= %s", [IdFasilitas2])

        result2 = cur2.fetchall()
        if result2 == ():
            self.Lbl_AC3_Fasilitas2.setText("")
        else:
            self.Lbl_AC3_Fasilitas2.setText(result2[0][1])

        cur3 = con.cursor()
        cur3.execute("SELECT * FROM fasilitas WHERE IdFasilitas= %s", [IdFasilitas3])

        result3 = cur3.fetchall()
        if result3 == ():
            self.Lbl_AC3_Fasilitas3.setText("")
        else:
            self.Lbl_AC3_Fasilitas3.setText(result3[0][1])

def DisplayAccessCard4(self):
    con = mdb.connect('localhost','root','','pbe_final_project_db')

    AccessCard = self.Combo_aksescard4.currentText()

    cur = con.cursor()
    cur.execute("SELECT * FROM accesscard WHERE IdAccess= %s", [AccessCard])

    result = cur.fetchall()

    if result == ():
        self.Lbl_AC4_Fasilitas1.setText("")
        self.Lbl_AC4_Fasilitas2.setText("")
        self.Lbl_AC4_Fasilitas3.setText("")
    else:
        IdFasilitas1=result[0][1]
        IdFasilitas2=result[0][2]
        IdFasilitas3=result[0][3]
        
        cur1 = con.cursor()
        cur1.execute("SELECT * FROM fasilitas WHERE IdFasilitas= %s", [IdFasilitas1])

        result1 = cur1.fetchall()
        if result1 == ():
            self.Lbl_AC4_Fasilitas1.setText("")
        else:
            self.Lbl_AC4_Fasilitas1.setText(result1[0][1])

        cur2 = con.cursor()
        cur2.execute("SELECT * FROM fasilitas WHERE IdFasilitas= %s", [IdFasilitas2])

        result2 = cur2.fetchall()
        if result2 == ():
            self.Lbl_AC4_Fasilitas2.setText("")
        else:
            self.Lbl_AC4_Fasilitas2.setText(result2[0][1])

        cur3 = con.cursor()
        cur3.execute("SELECT * FROM fasilitas WHERE IdFasilitas= %s", [IdFasilitas3])

        result3 = cur3.fetchall()
        if result3 == ():
            self.Lbl_AC4_Fasilitas3.setText("")
        else:
            self.Lbl_AC4_Fasilitas3.setText(result3[0][1])

def DisplayAccessCard5(self):
    con = mdb.connect('localhost','root','','pbe_final_project_db')

    AccessCard = self.Combo_aksescard5.currentText()

    cur = con.cursor()
    cur.execute("SELECT * FROM accesscard WHERE IdAccess= %s", [AccessCard])

    result = cur.fetchall()

    if result == ():
        self.Lbl_AC5_Fasilitas1.setText("")
        self.Lbl_AC5_Fasilitas2.setText("")
        self.Lbl_AC5_Fasilitas3.setText("")
    else:
        IdFasilitas1=result[0][1]
        IdFasilitas2=result[0][2]
        IdFasilitas3=result[0][3]
        
        cur1 = con.cursor()
        cur1.execute("SELECT * FROM fasilitas WHERE IdFasilitas= %s", [IdFasilitas1])

        result1 = cur1.fetchall()
        if result1 == ():
            self.Lbl_AC5_Fasilitas1.setText("")
        else:
            self.Lbl_AC5_Fasilitas1.setText(result1[0][1])

        cur2 = con.cursor()
        cur2.execute("SELECT * FROM fasilitas WHERE IdFasilitas= %s", [IdFasilitas2])

        result2 = cur2.fetchall()
        if result2 == ():
            self.Lbl_AC5_Fasilitas2.setText("")
        else:
            self.Lbl_AC5_Fasilitas2.setText(result2[0][1])

        cur3 = con.cursor()
        cur3.execute("SELECT * FROM fasilitas WHERE IdFasilitas= %s", [IdFasilitas3])

        result3 = cur3.fetchall()
        if result3 == ():
            self.Lbl_AC5_Fasilitas3.setText("")
        else:
            self.Lbl_AC5_Fasilitas3.setText(result3[0][1])

def DisplayKendaraan1(self):
    con = mdb.connect('localhost','root','','pbe_final_project_db')

    KendaraanId = self.Combo_kendaraan1.currentText()

    cur = con.cursor()
    cur.execute("SELECT * FROM kendaraan WHERE NoPlat= %s", [KendaraanId])

    result = cur.fetchall()

    if result == ():
        self.Lbl_Kend1_Jenis.setText("")
        self.Lbl_Kend1_Warna.setText("")
        self.Lbl_Kend1_Parkir.setText("")
    else:
        self.Lbl_Kend1_Jenis.setText(result[0][1])
        self.Lbl_Kend1_Warna.setText(result[0][2])
        
        mobil=result[0][3]
        # print(mobil)
        if (mobil==""):
            self.Lbl_Kend1_Parkir.setText("")
        else:
            cur1 = con.cursor()
            cur1.execute("SELECT * FROM parkir WHERE IdParkir= %s", [mobil])
            result1 = cur1.fetchall()
            # print(result1)
            if result1 == ():
                self.Lbl_Kend1_Parkir.setText("")
            else:
                parkir=str(result1[0][1]) + "-" + str(result1[0][2]) + "-" + str(result1[0][3])
                self.Lbl_Kend1_Parkir.setText(parkir)

def DisplayKendaraan2(self):
    con = mdb.connect('localhost','root','','pbe_final_project_db')

    KendaraanId = self.Combo_kendaraan2.currentText()

    cur = con.cursor()
    cur.execute("SELECT * FROM kendaraan WHERE NoPlat= %s", [KendaraanId])

    result = cur.fetchall()

    if result == ():
        self.Lbl_Kend2_Jenis.setText("")
        self.Lbl_Kend2_Warna.setText("")
        self.Lbl_Kend2_Parkir.setText("")
    else:
        self.Lbl_Kend2_Jenis.setText(result[0][1])
        self.Lbl_Kend2_Warna.setText(result[0][2])
        
        mobil=result[0][3]
        
        if (mobil==""):
            self.Lbl_Kend2_Parkir.setText("")
        else:
            cur1 = con.cursor()
            cur1.execute("SELECT * FROM parkir WHERE IdParkir= %s", [mobil])
            result1 = cur1.fetchall()
            # print(result1)
            if result1 == ():
                self.Lbl_Kend2_Parkir.setText("")
            else:
                parkir=str(result1[0][1]) + "-" + str(result1[0][2]) + "-" + str(result1[0][3])
                self.Lbl_Kend2_Parkir.setText(parkir)

def DisplayKendaraan3(self):
    con = mdb.connect('localhost','root','','pbe_final_project_db')

    KendaraanId = self.Combo_kendaraan3.currentText()

    cur = con.cursor()
    cur.execute("SELECT * FROM kendaraan WHERE NoPlat= %s", [KendaraanId])

    result = cur.fetchall()

    if result == ():
        self.Lbl_Kend3_Jenis.setText("")
        self.Lbl_Kend3_Warna.setText("")
        self.Lbl_Kend3_Parkir.setText("")
    else:
        self.Lbl_Kend3_Jenis.setText(result[0][1])
        self.Lbl_Kend3_Warna.setText(result[0][2])

        mobil=result[0][3]

        if (mobil==""):
            self.Lbl_Kend3_Parkir.setText("")
        else:
            cur1 = con.cursor()
            cur1.execute("SELECT * FROM parkir WHERE IdParkir= %s", [mobil])
            result1 = cur1.fetchall()
            # print(result1)
            if result1 == ():
                self.Lbl_Kend3_Parkir.setText("")
            else:
                parkir=str(result1[0][1]) + "-" + str(result1[0][2]) + "-" + str(result1[0][3])
                self.Lbl_Kend3_Parkir.setText(parkir)

def DisplayKendaraan4(self):
    con = mdb.connect('localhost','root','','pbe_final_project_db')

    KendaraanId = self.Combo_kendaraan4.currentText()

    cur = con.cursor()
    cur.execute("SELECT * FROM kendaraan WHERE NoPlat= %s", [KendaraanId])

    result = cur.fetchall()

    if result == ():
        self.Lbl_Kend4_Jenis.setText("")
        self.Lbl_Kend4_Warna.setText("")
        self.Lbl_Kend4_Parkir.setText("")
    else:
        self.Lbl_Kend4_Jenis.setText(result[0][1])
        self.Lbl_Kend4_Warna.setText(result[0][2])

        mobil=result[0][3]

        if (mobil==""):
            self.Lbl_Kend4_Parkir.setText("")
        else:
            cur1 = con.cursor()
            cur1.execute("SELECT * FROM parkir WHERE IdParkir= %s", [mobil])
            result1 = cur1.fetchall()
            # print(result1)
            if result1 == ():
                self.Lbl_Kend4_Parkir.setText("")
            else:
                parkir=str(result1[0][1]) + "-" + str(result1[0][2]) + "-" + str(result1[0][3])
                self.Lbl_Kend4_Parkir.setText(parkir)

def DisplayKendaraan5(self):
    con = mdb.connect('localhost','root','','pbe_final_project_db')

    KendaraanId = self.Combo_kendaraan5.currentText()

    cur = con.cursor()
    cur.execute("SELECT * FROM kendaraan WHERE NoPlat= %s", [KendaraanId])

    result = cur.fetchall()

    if result == ():
        self.Lbl_Kend5_Jenis.setText("")
        self.Lbl_Kend5_Warna.setText("")
        self.Lbl_Kend5_Parkir.setText("")
    else:
        self.Lbl_Kend5_Jenis.setText(result[0][1])
        self.Lbl_Kend5_Warna.setText(result[0][2])

        mobil=result[0][3]
        if (mobil==""):
            self.Lbl_Kend5_Parkir.setText("")
        else:
            cur1 = con.cursor()
            cur1.execute("SELECT * FROM parkir WHERE IdParkir= %s", [mobil])
            result1 = cur1.fetchall()
            # print(result1)
            if result1 == ():
                self.Lbl_Kend5_Parkir.setText("")
            else:
                parkir=str(result1[0][1]) + "-" + str(result1[0][2]) + "-" + str(result1[0][3])
                self.Lbl_Kend5_Parkir.setText(parkir)

def DisplayOwner(self):
    con = mdb.connect('localhost','root','','pbe_final_project_db')

    OwnerId = self.Combo_IdOwner.currentText()

    cur = con.cursor()
    cur.execute("SELECT * FROM owner WHERE IdOwner= %s", [OwnerId])

    result = cur.fetchall()

    if result == ():
        self.Lbl_OwnerNama.setText("")
        self.Lbl_OwnerPhone.setText("")
    else:
        self.Lbl_OwnerNama.setText(result[0][1])
        self.Lbl_OwnerPhone.setText(result[0][5])


Ui_FrmUnit.signals=signals
Ui_FrmUnit.pesan=pesan
Ui_FrmUnit.DBConnection = DBConnection
Ui_FrmUnit.InsertData = InsertData
Ui_FrmUnit.UpdateData = UpdateData
Ui_FrmUnit.DeleteData = DeleteData
Ui_FrmUnit.select_data = select_data
Ui_FrmUnit.user = user
Ui_FrmUnit.login = login
Ui_FrmUnit.logout = logout
Ui_FrmUnit.AccessCard = AccessCard
Ui_FrmUnit.kendaraan = kendaraan
Ui_FrmUnit.Owner = Owner
Ui_FrmUnit.AddIdAccessCard = AddIdAccessCard
Ui_FrmUnit.AddIdKendaraan = AddIdKendaraan
Ui_FrmUnit.AddIdOwner = AddIdOwner
Ui_FrmUnit.ClearDataAccessCard = ClearDataAccessCard
Ui_FrmUnit.ClearDataKendaraan = ClearDataKendaraan
# Ui_FrmUnit.ClearDataUnitForm = ClearDataUnitForm
Ui_FrmUnit.DisplayAccessCard1 = DisplayAccessCard1
Ui_FrmUnit.DisplayAccessCard2 = DisplayAccessCard2
Ui_FrmUnit.DisplayAccessCard3 = DisplayAccessCard3
Ui_FrmUnit.DisplayAccessCard4 = DisplayAccessCard4
Ui_FrmUnit.DisplayAccessCard5 = DisplayAccessCard5
Ui_FrmUnit.DisplayKendaraan1 = DisplayKendaraan1
Ui_FrmUnit.DisplayKendaraan2 = DisplayKendaraan2
Ui_FrmUnit.DisplayKendaraan3 = DisplayKendaraan3
Ui_FrmUnit.DisplayKendaraan4 = DisplayKendaraan4
Ui_FrmUnit.DisplayKendaraan5 = DisplayKendaraan5
Ui_FrmUnit.DisplayOwner = DisplayOwner


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmUnit = QtWidgets.QMainWindow()
    ui = Ui_FrmUnit()
    ui.setupUi(FrmUnit)
    ui.signals()
    FrmUnit.show()    
    sys.exit(app.exec_())
