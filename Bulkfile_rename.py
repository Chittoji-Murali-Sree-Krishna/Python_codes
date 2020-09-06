import os
os.chdir('/home/wargun/Documents/')
for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    file_title, file_num = file_name
    f_title = file_title.strip()
    f_num = file_num.strip()
    Rename = '{}-{}'.format(f_num, f_title, file_ext)
    os.rename(f, Rename)
