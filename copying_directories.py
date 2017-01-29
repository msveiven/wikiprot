
import sys
import os
from shutil import copyfile
Path= os.getcwd().split('Scanners')
PathLink = Path[0]



newpath = os.getcwd()+'/apps'
if not os.path.exists(newpath):
    os.makedirs(newpath)

newpath = os.getcwd()+'/files'
if not os.path.exists(newpath):
    os.makedirs(newpath)

#print(os.getcwd())
newpath = os.getcwd()+'/files/theme'
if not os.path.exists(newpath):
    os.makedirs(newpath)

newpath = os.getcwd()+'/files/theme/images'
if not os.path.exists(newpath):
    os.makedirs(newpath)

newpath = os.getcwd()+'/uploads'
if not os.path.exists(newpath):
    os.makedirs(newpath)

newpath = os.getcwd()+'/uploads/9'
if not os.path.exists(newpath):
    os.makedirs(newpath)

newpath = os.getcwd()+'/uploads/9/9'
if not os.path.exists(newpath):
    os.makedirs(newpath)

newpath = os.getcwd()+'/uploads/9/9/0'
if not os.path.exists(newpath):
    os.makedirs(newpath)

newpath = os.getcwd()+'/uploads/9/9/0/7'
if not os.path.exists(newpath):
    os.makedirs(newpath)

newpath = os.getcwd()+'/uploads/9/9/0/7/99074558'
if not os.path.exists(newpath):
    os.makedirs(newpath)

copyfile(PathLink+'/htmlFiles/'+ 'index.html', 'index.html')
copyfile(PathLink+'htmlFiles/'+ 'apps/audioPlayer2.swf', 'apps/audioPlayer2.swf')
copyfile(PathLink+'htmlFiles/'+ 'files/main_style.css', 'files/main_style.css')
copyfile(PathLink+'htmlFiles/'+ 'files/theme/custom.js', 'files/theme/custom.js')
copyfile(PathLink+'htmlFiles/'+ 'files/theme/plugins.js', 'files/theme/plugins.js')
copyfile(PathLink+'htmlFiles/'+ 'files/theme/manifest.json', 'files/theme/manifest.json')
copyfile(PathLink+'htmlFiles/'+ 'files/theme/images/select-dropdown.png', 'files/theme/images/select-dropdown.png')
copyfile(PathLink+'htmlFiles/'+ 'files/theme/images/default-bg.jpg', 'files/theme/images/default-bg.jpg')

copyfile(PathLink+'htmlFiles/'+ 'uploads/9/9/0/7/99074558/umclogo.jpg', 'uploads/9/9/0/7/99074558/umclogo.jpg')
copyfile(PathLink+'htmlFiles/'+ 'uploads/9/9/0/7/99074558/umclogo_orig.jpg', 'uploads/9/9/0/7/99074558/umclogo_orig.jpg')