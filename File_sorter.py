import os
import shutil

path = '/home/wargun/Videos/'
names = os.listdir(path)
folder_name = ['mkv', 'mp4', 'py', 'txt', 'js', 'html', 'css']
for x in range(0, 2):
    if not os.path.exists(path+folder_name[x]):
        os.makedirs(path+folder_name[x])
for files in names:
    if '.mkv' in files and not os.path.exists(path+'mkv/'+files):
        shutil.move(path+files, path+'mkv/'+files)
    if '.mp4' in files and not os.path.exists(path+'mp4/'+files):
        shutil.move(path+files, path+'mp4/'+files)
    if '.py' in files and not os.path.exists(path+'py/'+files):
        shutil.move(path+files, path+'py/'+files)
    if '.html' in files and not os.path.exists(path+'html/'+files):
        shutil.move(path+files, path+'html/'+files)
    if '.txt' in files and not os.path.exists(path+'txt/'+files):
        shutil.move(path+files, path+'txt/'+files)
    if '.js' in files and not os.path.exists(path+'js/'+files):
        shutil.move(path+files, path+'js/'+files)
    if '.css' in files and not os.path.exists(path+'css/'+files):
        shutil.move(path+files, path+'css/'+files)
