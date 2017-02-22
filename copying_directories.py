
import sys
import os
from shutil import copyfile

def copying_directories():

    Path = os.environ['WIKIPROTPATH']


    newpath = os.getcwd() + '/apps'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    newpath = os.getcwd()+ '/files'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

#    print(os.getcwd())
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

    if os.path.isfile(Path+'/htmlFiles/'+ 'index.html') == True:
        copyfile(Path+'/htmlFiles/'+ 'index.html', 'index.html')
    else:
        print('File not found. Ending program')
        sys.exit()

    if os.path.isfile(Path + 'htmlFiles/' + 'apps/audioPlayer2.swf') == True:
        copyfile(Path + 'htmlFiles/' + 'apps/audioPlayer2.swf', 'apps/audioPlayer2.swf')
    else:
        print('File not found. Ending program')
        sys.exit()

    if os.path.isfile(Path + 'htmlFiles/' + 'files/main_style.css') == True:
        copyfile(Path + 'htmlFiles/' + 'files/main_style.css', 'files/main_style.css')
    else:
        print('File not found. Ending program')
        sys.exit()

    if os.path.isfile(Path + 'htmlFiles/' + 'files/theme/custom.js') == True:
        copyfile(Path + 'htmlFiles/' + 'files/theme/custom.js', 'files/theme/custom.js')
    else:
        print('File not found. Ending program')
        sys.exit()

    if os.path.isfile(Path + 'htmlFiles/' + 'files/theme/plugins.js') == True:
        copyfile(Path + 'htmlFiles/' + 'files/theme/plugins.js', 'files/theme/plugins.js')
    else:
        print('File not found. Ending program')
        sys.exit()


    if os.path.isfile(Path + 'htmlFiles/' + 'files/theme/manifest.json') == True:
        copyfile(Path + 'htmlFiles/' + 'files/theme/manifest.json', 'files/theme/manifest.json')
    else:
        print('File not found. Ending program')
        sys.exit()

    if os.path.isfile(Path + 'htmlFiles/' + 'files/theme/images/select-dropdown.png') == True:
        copyfile(Path + 'htmlFiles/' + 'files/theme/images/select-dropdown.png', 'files/theme/images/select-dropdown.png')
    else:
        print('File not found. Ending program')
        sys.exit()

    if os.path.isfile(Path + 'htmlFiles/' + 'files/theme/images/default-bg.jpg') == True:
        copyfile(Path + 'htmlFiles/' + 'files/theme/images/default-bg.jpg', 'files/theme/images/default-bg.jpg')
    else:
        print('File not found. Ending program')
        sys.exit()


    if os.path.isfile(Path + 'htmlFiles/' + 'uploads/9/9/0/7/99074558/umclogo.jpg') == True:
        copyfile(Path + 'htmlFiles/' + 'uploads/9/9/0/7/99074558/umclogo.jpg','uploads/9/9/0/7/99074558/umclogo.jpg')
    else:
        print('File not found. Ending program')
        sys.exit()

    if os.path.isfile(Path + 'htmlFiles/' + 'uploads/9/9/0/7/99074558/umclogo_orig.jpg') == True:
        copyfile(Path + 'htmlFiles/' + 'uploads/9/9/0/7/99074558/umclogo_orig.jpg','uploads/9/9/0/7/99074558/umclogo_orig.jpg')
    else:
        print('File not found. Ending program')
        sys.exit()


    return