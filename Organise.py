import shutil
import os

text_documents = [['text_documents'],['txt','md','rtf','doc','docx','odt','wps','pages','pdf','html','xml','tex']]
spreadsheet_documents = [['spreadsheets'],['xls','xlsx','ods','csv','tsv','gsheet']]
presentation_documents = [['presentation'],['ppt','pptx','odp','key','gslides']]
database_files = [['databases'],['mdb','accdb','sql','sqlite','odb']]
image_files = [['images'],['jpg','jpeg','png','gif','bmp','tiff','svg','eps','ai','psd', 'webp']]
audio_files = [['audio'],['wav','aiff','mp3','aac','flac','ogg']]
video_files = [['video'],['mp4','avi','mkv','mov','wmv','flv']]
programming_languages = [['programming'],['py','js','c','cpp','h','java','html','htm','css','md','rb','php','pl']]
other = [['other'],['zip','tar','tar.gz','tgz','rar','7z','gzip','exe','bat','sh','bin','app','conf','cfg','ini','yaml','yml','json','xml','iso', 'vdi', 'vmdk', 'obj', 'stl', 'fbx', 'dae', 'epub', 'mobi', 'azw', 'pdf', 'mat', 'hdf', 'hdf5']]

file_types = [text_documents,spreadsheet_documents,presentation_documents,database_files,image_files,audio_files,video_files,programming_languages,other]

array = os.listdir()

def organise():
    for f in array:

        file = f.split('.')[-1]

        if f == 'o.py':
            continue

        if f in file_types:
            continue
        
        for i in range(len(file_types)):
            if f not in os.listdir():
                continue
            if file in file_types[i][1]:
                shutil.move(f,file_types[i][0][0])

def removeFromRepo():
    for file_type in file_types:
        dir_path = file_type[0][0]
        
        if os.path.exists(dir_path):
            files = os.listdir(dir_path)
            
            for file in files:
                if file == 'o.py':
                    continue
                
                shutil.move(os.path.join(dir_path, file), os.getcwd())

organise()
    
    