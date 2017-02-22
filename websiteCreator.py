#!/usr/bin/python

import sys
import os



owd = os.environ['WIKIPROTPATH']+'Scanners/'
os.chdir(owd)
directoryList1 = next(os.walk('.'))[1]
#print(directoryList1)
import webpageCreator

if len(sys.argv) != 1:
    print('No argument required. Try again')
    sys.exit()

#url = sys.argv[1]
#print(sys.argv[1])
#webpageCreator.webpage(os.getcwd(), url)
webpageCreator.webpage(os.environ['WIKIPROTPATH']+'Scanners')


i = 0
while (i < len(directoryList1)):
    if (directoryList1[i] != 'apps'):
        if (directoryList1[i] != 'files'):
            if (directoryList1[i] != 'uploads'):
                if (directoryList1[i] != '.idea'):

                    import webpageCreator

    #                webpageCreator.webpage(os.path.abspath(directoryList1[i]), url)
                    webpageCreator.webpage(os.path.abspath(directoryList1[i]))


                    directoryList2 = next(os.walk('.'))[1]
                    sowd = os.getcwd()


                    j = 0
                    while (j < len(directoryList2)):
                        if (directoryList2[j] != 'apps'):
                            if (directoryList2[j] != 'files'):
                                    if (directoryList2[j] != 'uploads'):
                                        if (directoryList2[j] != '.idea'):

#                                           webpageCreator.webpage(os.path.abspath(directoryList2[j]), url)
                                            webpageCreator.webpage(os.path.abspath(directoryList2[j]))

#                                            print(os.getcwd())
                                            os.chdir(sowd)
 #                                           print(os.getcwd())

                        j = j + 1

  #                  print(os.getcwd())
                    os.chdir(owd)
   #                 print(os.getcwd())

    i = i + 1

