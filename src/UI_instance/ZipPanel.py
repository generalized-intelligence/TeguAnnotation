from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from model.ZipUtil import *
from config import defaults as DEF
from UI_instance.UI_Model.ZipPanel import Ui_zippanel
import os
class ZipPanel(QWidget,Ui_zippanel):
    updatingTxtDisplay=pyqtSignal()
    def __init__(self,parent=None):
        super(ZipPanel, self).__init__(parent)
        self.setupUi(self)
        self.serval_dict={}
        self.txt_display="This function requires 7z, please show the correct path of 7z.exe\n"
        self.ziptool_Path=""
        self.zip_Path=""
        self.btnServal.clicked.connect(self.select_serval)
        self.btnZipTool.clicked.connect(self.select_zip)
        self.updatingTxtDisplay.connect(self.updateTxtDisplay)
        self.btnSave.clicked.connect(self.select_save)
        self.btnStart.clicked.connect(self.zip_pack)
        self.updatingTxtDisplay.emit()
    def select_save(self):
        file_path_diag = QFileDialog.getSaveFileName(self, "Save File", "C:/Users/",
                                                     "7z files (*.7z);;all files(*.*)")
        file_path = file_path_diag[0]
        if file_path != "":
            self.zip_Path = file_path
            self.txt_display += "Saving to the following path：" + file_path + '\n'
            self.updatingTxtDisplay.emit()
    def zip_pack(self):
        if self.zip_Path=="":
            QMessageBox.warning(self, "Packing failed", "Please select the save path first!" , QMessageBox.Ok)
            return
        elif self.ziptool_Path=="":
            QMessageBox.warning(self, "Packing failed", "Please select the 7z.exe path first!", QMessageBox.Ok)
            return
        elif len(self.serval_dict.keys())<=1:
            QMessageBox.warning(self, "Packing failed", "Please open the serval file first!", QMessageBox.Ok)
            return
        ZP = Ziputil(self.ziptool_Path, self.zip_Path)
        temp_path=os.path.splitext(self.zip_Path)[0]+"_folder"
        self.txt_display += "Copying files, it may takes a long time, please wait."  + '\n'
        self.updatingTxtDisplay.emit()
        ls=write_folder_from_dict(temp_path,self.serval_dict)
        if len(ls)==0:
            self.txt_display += "Copying complete!" + '\n'
        else:
            self.txt_display+="The following files missing：\n"
            for item in ls:
                self.txt_display+=item
                self.txt_display+='\n'
        self.updatingTxtDisplay.emit()
        self.txt_display += "Compressing files, it may takes a long time, please wait." + '\n'
        self.updatingTxtDisplay.emit()
        code = ZP.genzipfile(temp_path)
        if code==0:
            self.txt_display += "Compressing complete! Saved 7z file to："+self.zip_Path + '\n'
            self.updatingTxtDisplay.emit()
        else:
            self.txt_display += "Compressing failed! Please make sure 7z.exe works as expected." +  '\n'
            self.updatingTxtDisplay.emit()

    def updateTxtDisplay(self):
        self.txtOut.setPlainText(self.txt_display)
    def select_serval(self):
        file_path_diag = QFileDialog.getOpenFileName(self, "Open File", "C:/Users/",
                                                     "serval files (*.serval);;all files(*.*)")
        file_path = file_path_diag[0]
        print(file_path)
        try:
            with open(file_path, encoding='utf-8') as f:
                file_read = f.read()
        except Exception as e:
            QMessageBox.warning(self, "Opening File Failed", "Cannot open the file:" + file_path, QMessageBox.Ok)
            return False
        serval_decrypt=decrypt(DEF.ENCRYPT_KEY,file_read)
        if validateHeader(serval_decrypt)!=0:
            QMessageBox.warning(self, "Validation Failed", "Serval file illegal:" + file_path, QMessageBox.Ok)
            return False
        self.serval_dict=load_serval(decrypt(DEF.ENCRYPT_KEY,file_read))
        self.txt_display+="Serval file opened："+file_path+'\n'
        self.txt_display += "Compressing the following files：" +'\n'
        for key in self.serval_dict.keys():
            if key != 'label_line':
                path = self.serval_dict[key]['path']
                full_pic = path + '/' + key
                self.txt_display+=(full_pic+'\n')
        self.updatingTxtDisplay.emit()
        return True
    def select_zip(self):
        file_path_diag = QFileDialog.getOpenFileName(self, "Open File", "C:/Users/",
                                                     "exe files (*.exe);;all files(*.*)")
        file_path = file_path_diag[0]
        if file_path!="":
            self.ziptool_Path=file_path
            self.txt_display+="Using the following 7z.exe file："+file_path+'\n'
            self.updatingTxtDisplay.emit()



