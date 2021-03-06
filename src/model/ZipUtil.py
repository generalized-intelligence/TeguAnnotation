import shutil
from model.EncryptTools import *
from config import defaults as DEF
ZIP_PASS=DEF.ZIP_PASS

import os
import zipfile
class Ziputil():
    def __init__(self, ziptoolpath:str, zipfilepath:str):
        self.ziptoolpath=ziptoolpath
        self.zipfilepath=zipfilepath
        self.password=ZIP_PASS
        self.using7z=True
        if len(self.ziptoolpath)==0:
            self.using7z=False
    def setpassword(self,password:str):
        self.password=password
    def getzipfile(self):#create a blank zip file
        if self.using7z: #using outside 7z.exe
            with open('blankfile','w') as f: #create a blankfile to compress
                f.write('\n')
            command=' a '+self.zipfilepath+' '+os.getcwd()+'\\blankfile'
            if len(self.password)!=0:
                command += ' -p'+self.password
            print(self.ziptoolpath+command)
            code=os.system(self.ziptoolpath+command)
            return code
        else:#using zipfile pack, with no password
            try:
                azip = zipfile.ZipFile(self.zipfilepath, 'w')
                azip.write('blankfile', compress_type=zipfile.ZIP_LZMA)
                azip.close()
                return 0
            except Exception as e:
                azip.close()
                print(str(e))
                return str(e)
    def genzipfile(self,folder_path:str):
        if self.using7z:
            command=" a -t7z -scsUTF-8 "+self.zipfilepath+" "+folder_path+"\\* -p"+ZIP_PASS
            print(self.ziptoolpath+command)
            code = os.system(self.ziptoolpath + command)
            return code
        else:
            try:
                azip = zipfile.ZipFile(self.zipfilepath, 'w')
                for current_path, subfolders, filesname in os.walk(folder_path):
                    print(current_path, subfolders, filesname)
                    #  filesname是一个列表，我们需要里面的每个文件名和当前路径组合
                    for file in filesname:
                        # 将当前路径与当前路径下的文件名组合，就是当前文件的绝对路径
                        azip.write(os.path.join(current_path, file))
                azip.close()
                return 0
            except Exception as e:
                azip.close()
                print(str(e))
                return str(e)

def load_serval(str_serval:str): #load a serval file
    lines=str_serval.split('\n')
    serval_dict={}
    for line in lines:
        if line.startswith('aimg'):
            continue
        if line.startswith('0:__background__'):
            serval_dict['label_line']=line
            continue
        line_split=line.split(':')
        line_path_full=':'.join([line_split[0],line_split[1]])
        print("load:",line_path_full)
        line_path_full_split=line_path_full.split('/')
        path_folder='/'.join(line_path_full_split[:-1])
        file_name=line_path_full_split[-1:][0]

        anno_str=line_split[2]
        serval_dict[file_name]={'path':path_folder,'anno':anno_str}
    return serval_dict
def get_path_folder(path):
    path_folder = '_'.join(path.split('/'))
    return path_folder.replace(':','').replace(' ','-')
def split_serval(serval_dict:dict):
    filename_dic={}
    for key in serval_dict.keys():
        if key!='label_line':
            path = serval_dict[key]['path']
            anno = serval_dict[key]['anno']
            str_line = key + ':' + anno
            path_filename=get_path_folder(path)
            if path_filename not in filename_dic.keys():
                filename_dic[path_filename]=[]
            filename_dic[path_filename].append(str_line)
    filename_serval_dic={}
    for key in filename_dic.keys():
        list_to_write=filename_dic[key]
        serval_new='\n'.join(list_to_write)
        serval_new+='\n'
        serval_new_header=addHeader(serval_new)
        filename_serval_dic[key]=serval_new_header
    return filename_serval_dic

def regenerate_serval(serval_dict:dict):
    list_to_write=[]
    list_to_write.append(serval_dict['label_line'])
    for key in serval_dict.keys():
        if key!='label_line':
            path=serval_dict[key]['path']
            anno=serval_dict[key]['anno']
            str_line=get_path_folder(path)+'/'+key+':'+anno
            list_to_write.append(str_line)
    serval_new='\n'.join(list_to_write)
    serval_new+='\n'
    serval_new_header=addHeader(serval_new)
    return serval_new_header
def write_folder_from_dict(path:str, serval_dict:dict):
    if os.path.isdir(path):
        shutil.rmtree(path)
    os.mkdir(path)
    os.chdir(path)
    with open('encrypt_serval.serval','w',encoding='utf-8') as f:
        f.write(encrypt(DEF.ENCRYPT_KEY,regenerate_serval(serval_dict)))
    fail_list=[]
    for key in serval_dict.keys():
        if key!='label_line':
            path = serval_dict[key]['path']
            full_pic =path+'/'+key
            try:
                new_path = get_path_folder(path)
                if not os.path.isdir(new_path):
                    os.mkdir(new_path)
                shutil.copy(full_pic,new_path)
            except Exception as e:
                print(e)
                fail_list.append(key)
    return fail_list


if __name__=="__main__":
    import os
    print(os.getcwd())
    with open('zip_decryped_demo.serval',encoding='utf-8') as f:
        str_serval=f.read()
    #with open('decrypt.serval','w',encoding='utf-8') as f_write:
    #    f_write.write(decrypt(ENCRYPT_KEY,str_serval))
    serval_dict=load_serval(str_serval)
    split_dict=split_serval(serval_dict)

    for key in split_dict.keys():
        print(key)
        print(split_dict[key])

    #print(serval_dict)
    #print(serval_dict['label_line'])
    #import os
    #ls=write_folder_from_dict(os.getcwd(), serval_dict)
    #print(ls)
    #import os
    #os.chdir('../')
    #print(os.getcwd())

    #ZP=Ziputil(os.getcwd()+'\\7zfiles\\7z.exe',os.getcwd()+'\\zipdemo.7z')
    #code=ZP.genzipfile('"'+os.getcwd()+'\\writing_path"')
    #print(code)

