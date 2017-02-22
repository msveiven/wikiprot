#!/usr/bin/python

import sys
import os
import glob

# def runCreateLinks(url):
def runCreateLinks():
#    def createLinks(directory, url):
    def createLinks(directory):
        f = open('index.html', 'r')

        f.seek(0)
        s = f.read()
        R = s.split('</body>')
#        Path = os.getcwd().split('GitHub')
 #       PathLink = Path[1]
        PathLink = os.environ['WIKIPROTPATH']
    #    print(str(PathLink))
        f.close()

        f = open('index.html', 'w')
        f.write(R[0])
        f.write('<p>\n')
#        f.write('<font size="5"><A HREF = "'+ url + str(PathLink) + '/' + directory + '">' + directory.split('.htm')[0].replace("_"," ") + '</A></font>')
        f.write('<font size="5"><A HREF = "https://msveiven.github.io' + str(PathLink) + '/' + directory + '">' + directory.split('.htm')[0].replace("_"," ") + '</A></font>')
        f.write('</p>\n')
        f.write('</body>\n')
        f.write('</html>\n')

        f.close()

        return


    directoryList = next(os.walk('.'))[1]

    i = 0
    while (i < len(directoryList)):
        if (directoryList[i] != 'apps'):
            if (directoryList[i] != 'files'):
                if (directoryList[i] != 'uploads'):
#                    createLinks(directoryList[i], url)
                    createLinks(directoryList[i])
    #                print(directoryList[i])
        i = i + 1

    currentPath = os.getcwd()
    path = currentPath+"/*.htm"
    #print(path)
    for fname in glob.glob(path):
        if (fname != 'index.htm'):
            fname = fname.split("/")
            #print(fname)
#            createLinks(fname[len(fname)-1], url)
            createLinks(fname[len(fname)-1])

    return