from PyQt5.QtCore import pyqtSlot, Qt,QTranslator
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QListWidgetItem, QMessageBox,QStackedWidget,QFileDialog
from PyQt5.QtGui import QPixmap
from UI_instance.UI_Model.MainWindow import Ui_MainWindow
from model.AnnotateImageModel import *
import model.EncryptTools as T
import config.defaults as DEF
from UI_instance.ConfigPane import ConfigPane
from UI_instance.AnnotatorPane import AnnotatorPane
from UI_instance.StartPanel import StartPanel
from UI_instance.ZipPanel import *
import cgitb
cgitb.enable( format ='text')

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow,self).__init__()
        self.aim=AnnotatedImageModel()
        self.recent_dict = {}
        self.json_load()
        self.configPane=ConfigPane(self.aim)
        self.annoPane=AnnotatorPane(self.aim)
        self.start=StartPanel(self.aim, self.recent_dict)
        self.zipPanel=ZipPanel()
        self.setupUi(self)
        self.trans=QTranslator()
        self.initUi()
        self.configPane.ConfigStartAnnotation.connect(self.startAnnotationRequested)
        self.configPane.returnBtn.clicked.connect(self.returnMain)
        self.annoPane.pushButtonSave.clicked.connect(self.SaveAll)
        self.annoPane.endAnnotation.connect(self.exitApplication)
        self.start.button_new.clicked.connect(self.newProj)
        self.start.button_open.clicked.connect(self.OpenAll)
        self.start.button_pack.clicked.connect(self.startZip)
        self.picture_path=[]
        self.proj_name=""
        self.load_proj=False

    def json_load(self):
        import os
        import json
        if os.path.exists(DEF.RECENT_JSON):
            with open(DEF.RECENT_JSON,'r',encoding='utf-8') as f:
                self.recent_dict=json.loads(f.read())
    def json_dump(self):
        import json
        with open(DEF.RECENT_JSON,'w',encoding='utf-8') as f:
            f.write(json.dumps(self.recent_dict))
    def initUi(self):
        self.stack.addWidget(self.start)
        self.stack.addWidget(self.configPane)
        self.stack.addWidget(self.annoPane)
        self.stack.addWidget(self.zipPanel)
        self.stack.setCurrentWidget(self.start)
        self.setCentralWidget(self.stack)
        #self.configPane.action_list.startAnnotation.connect(self.startAnnotationRequested)
    def startZip(self):
        self.stack.setCurrentWidget(self.zipPanel)
    def returnMain(self):
        self.stack.setCurrentWidget(self.start)
    def startAnnotationRequested(self):
        if not self.load_proj:
            self.picture_path = self.configPane.picture_path
            self.proj_name=self.configPane.proj_name
        if len(self.picture_path)<1:
            print(self.picture_path)
            QMessageBox.information(self,"Alert","No pictures selected!",QMessageBox.Ok)
            return
        if len(self.aim.labels)<1:
            QMessageBox.information(self, "Alert", "No labels added!", QMessageBox.Ok)
            return

        self.annoPane.setImageFileList(self.picture_path)
        self.annoPane.updateLabels()
        self.stack.setCurrentWidget(self.annoPane)
        self.annoPane.loadFirstImage()
    def exitApplication(self):
        reply = QMessageBox.question(self, ("Confirm Exit"),
                                      ("Are you sure you want to exit the Application? All unsaved progess will be lost."),QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QApplication.exit();
    def OpenServalFile(self):
        file_path_diag=QFileDialog.getOpenFileName(self, "Open file", "C:/Users/",
                                                "serval files (*.serval);;all files(*.*)")
        file_path=file_path_diag[0]
        print(file_path)
        try:
            with open(file_path,encoding='utf-8') as f:
                file_read=f.read()
        except Exception as e:
            if len(file_path)!=0:
                QMessageBox.warning(self, "Open file failed!", "Cannot open file:" + file_path, QMessageBox.Ok)
            return False
        serval_content=T.decrypt(DEF.ENCRYPT_KEY,file_read)
        print(serval_content)
        if T.validateHeader(serval_content)!=0:
            QMessageBox.warning(self, "Validation failed!", "Not a legal serval file:" + file_path, QMessageBox.Ok)
            return False
        self.aim.initWithSerializeString(serval_content)
        print(self.aim.imgAnnos)
        return True
    def newProj(self):
        self.stack.setCurrentWidget(self.configPane)
    def SaveAll(self):
        if self.SaveServalFile():
            reply = QMessageBox.question(self, ("Save the project file?"),
                                         ("A project file contains labels and paths only, you can use it to continue the project."), QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply==QMessageBox.Yes:
                if self.SaveProjFile():
                    self.json_dump()
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    def OpenAll(self):
        proj=self.OpenProjFile()
        if proj:
            reply = QMessageBox.question(self, ("Open a serval file?"),
                                         ("You can load the annotated results with a serval file."), QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                serval=self.OpenServalFile()
            self.startAnnotationRequested()

    def OpenProjFile(self):
        import json
        #proj_dict = {'images': self.picture_path, 'labels': self.aim.getLabels()}
        file_path_diag = QFileDialog.getOpenFileName(self, "Open project file", "C:/Users/",
                                                     "json files (*.json);;all files(*.*)")
        file_path = file_path_diag[0]
        try:
            with open(file_path,encoding='utf-8') as f:
                proj_dict=json.loads(f.read())
            if 'images' in proj_dict.keys() and 'labels' in proj_dict.keys():
                print(proj_dict)
                self.picture_path=proj_dict['images']
                self.aim.labels=proj_dict['labels']
                self.load_proj = True
            QMessageBox.information(self, "Open complete!", "Project loaded:" + file_path, QMessageBox.Ok)
            return True
        except Exception as e:
            QMessageBox.warning(self, "Open failed!", "Can't open file:" + file_path, QMessageBox.Ok)
            return False
    def SaveProjFile(self):
        import json
        proj_dict={'images':self.picture_path,'labels':self.aim.getLabels()}
        file_path_diag = QFileDialog.getSaveFileName(self, "Save project file", "C:/Users/"+self.proj_name,
                                                     "json files (*.json);;all files(*.*)")
        file_path = file_path_diag[0]
        try:
            file_save=open(file_path,'w',encoding="utf-8")
            data_to_write = json.dumps(proj_dict)
            file_save.write(data_to_write)
            file_save.close()
            self.recent_dict[self.proj_name]['proj']=file_path
            QMessageBox.information(self,"File Saved","Project saved to:"+file_path,QMessageBox.Ok)
            return True
        except Exception as e:
            QMessageBox.warning(self, "Saving failed!", "Can't open file to save:" + file_path, QMessageBox.Ok)
            return False

    def SaveServalFile(self):
        file_path_diag = QFileDialog.getSaveFileName(self, "Save serval file", "C:/Users/"+self.proj_name,
                                                "serval files (*.serval);;all files(*.*)")
        #print(file_path)
        file_path=file_path_diag[0]
        try:
            file_save=open(file_path,'w',encoding="utf-8")
            data_to_write = T.addHeader(self.aim.toSerializeString())
            print(data_to_write)
            data_encrypt=T.encrypt(DEF.ENCRYPT_KEY,data_to_write)
            file_save.write(data_encrypt)
            file_save.close()
            self.recent_dict[self.proj_name]={'serval':file_path}
            QMessageBox.information(self,"File Saved","Serval saved to:"+file_path,QMessageBox.Ok)
            return True
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Saving failed", "Can't open file to save:" + file_path, QMessageBox.Ok)
            return False



if __name__ == "__main__":
    app = QApplication(sys.argv)
    qshow = MainWindow()
    qshow.show()
    sys.exit(app.exec_())