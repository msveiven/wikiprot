#!/usr/bin/python

import os
import sys
import glob
import time
#import elementtree
import xml.etree.ElementTree as ET  #imports element tree function
#tree = ET.parse('HYPER ACUTE STROKE.xml')  #uses ET function on the xml file

#path = 'c/Users/msveiven/Desktop/Professor_Saranathan_Research/WIKIPROTPATHTEST'
#print('Path is ' + path)
#f = os.path.getmtime('webpageCreator.py')


#path = os.environ['WIKIPROTPATH']+'websiteCreator.py'
#print('this is the ' + path)
#f = os.path.getmtime(path)

def runParser():
    def ProtParser (series):

        tree = ET.parse(series)  #uses ET function on the xml file
        root = tree.getroot()   #creates root function for calling roots from the xml file. root[0] calls the first child in the element tree

        tocExists = 0
        currentPath = os.getcwd()
    #    print(currentPath.split("Scanners")[0]+'customParameters')
    #    print(currentPath.split("Scanners")[0]+'complexParameters')

        if root[0].tag == 'PrintTOC':
            tocExists = 1
        if os.path.isfile('customParameters.txt') == True and os.path.isfile('complexParameters.txt') == True:
            parameterList = [line.rstrip('\n') for line in open('customParameters.txt')]  # creates a list by reading parameters from text file

            complexParameterList = [line.rstrip('\n') for line in open('complexParameters.txt')]
        elif os.path.isfile(os.environ['WIKIPROTPATH']+'customParameters.txt') == True and os.path.isfile(os.environ['WIKIPROTPATH']+'complexParameters.txt') == True:
            parameterList = [line.rstrip('\n') for line in open(os.environ['WIKIPROTPATH']+'customParameters.txt')]    #creates a list by reading parameters from text file
            complexParameterList = [line.rstrip('\n') for line in open(os.environ['WIKIPROTPATH']+'complexParameters.txt')]
        else:
            print('No text files found!')
            sys.exit()


        scanTimeSearched = 0

        protocolCount = 0
        loopCounter = 0
        scanLooper = 0


        parameterListSize = len(parameterList)  #size up the number of parameters
        complexParameterListSize = len(complexParameterList)

        while loopCounter < 100:   #this while loop finds the number of protocols
            try:
                print(root[loopCounter].text)
                loopCounter += 1
            except Exception:
                protocolCount = loopCounter - tocExists
                loopCounter = 100
                pass

        parameterListSize += 1  #adds 1 to size of parametersList so we have extra column
        complexParameterListSize += 1

        Matrix1 = [['-' for x in range(parameterListSize)] for y in range(protocolCount+1)]    #creates a 2D array with size parameter list by protocol number
        Matrix2 = [['-' for x in range(protocolCount+1)] for y in range(complexParameterListSize + 1)]
        Matrix1[0][0] = 'Series'
        Matrix2[0][0] = 'Sequence Paramters'

        Matrix3 = [['-' for x in range(2)] for y in range(protocolCount+1)]

        parameterLooper = 0

        while parameterLooper < parameterListSize - 1:  #populates first row with parameters

            Matrix1[0][parameterLooper+1] = parameterList[parameterLooper].split('->')[1]
            parameterLooper += 1

        parameterLooper = 0

        while parameterLooper < complexParameterListSize - 1:  #populates first row with parameters

            Matrix2[parameterLooper + 1][0] = complexParameterList[parameterLooper].split('->')[1]  #First column for localizer
            parameterLooper += 1

        try:
            localizerLooper = 0

            while localizerLooper < protocolCount:  # populates first row with parameters

                Matrix2[0][localizerLooper+1] = root[localizerLooper][0][1][0][0].text[50:]
                localizerLooper += 1

        except Exception:
            localizerLooper = 1
            while localizerLooper < protocolCount+1:  #populates first row with parameters

                Matrix2[0][localizerLooper] = root[0][0][2][0][0][0][localizerLooper-1].get('name')
                localizerLooper += 1


        try:
            scanLooper = 0
            while scanLooper < protocolCount:  # this while loop populates the name of scans in the first column
                Matrix1[scanLooper+1][0] = root[scanLooper][0][1][0][0].text[50:]
                scanLooper += 1
        except Exception:
            scanLooper = 0
            while scanLooper < protocolCount:  #this while loop populates the name of scans in the first column
                Matrix1[scanLooper+1][0] = root[0][0][2][0][0][0][scanLooper].get('name')
                scanLooper += 1


        def findSearchItem (Matrix, searchitem, num, searchItemFound):   #define function that searches for each term
                j = 0
                totalScanTime = '0:0'
                while j < 100:
                    k = 0
                    if searchitem.split('->')[0] == 'Scan time' and (j < protocolCount + 1):
                        try:
                            if Matrix == 1:
                                Matrix1[j + 1 - tocExists][num + 1] = root[j][0][1][0][1].text[3:9]
                                totalScanTime = str(
                                    int(totalScanTime.split(':')[0]) + int(root[j][0][1][0][1].text[3:9].split(':')[0]) + (
                                    int(totalScanTime.split(':')[1]) + int(root[j][0][1][0][1].text[3:9].split(':')[1])) // int(
                                        60)) + ':' + str((
                                    int(totalScanTime.split(':')[1]) + int(root[j][0][1][0][1].text[3:9].split(':')[1]))%60)
                            if Matrix == 2:
                                Matrix2[num + 1][j + 1 - tocExists] = root[j][0][1][0][1].text[3:9]
                                totalScanTime = str(
                                    int(totalScanTime.split(':')[0]) + int(root[j][0][1][0][1].text[3:9].split(':')[0]) + (
                                        int(totalScanTime.split(':')[1]) + int(
                                            root[j][0][1][0][1].text[3:9].split(':')[1])) // int(
                                        60)) + ':' + str((
                                                             int(totalScanTime.split(':')[1]) + int(
                                                                 root[j][0][1][0][1].text[3:9].split(':')[1])) % 60)
                        except Exception:
                            pass

                    while k < 100:
                        l = 0
                        while l < 100:
                            try:
                                if root[j][0][1][k][l][0].text == searchitem.split('->')[0]:   #check to see if search item has been found
                                    if Matrix == 1:
                                        Matrix1[j+1-tocExists][num + 1] = root[j][0][1][k][l][1].text  # places the parameter value in the Matrix1
                                    if Matrix == 2:
                                        Matrix2[num + 1][j+1-tocExists] = root[j][0][1][k][l][1].text
                                    searchItemFound = 1 #variable that shows that a search item has been found
                                    k = 100     #sets k and l to 100 to break out of the two while loops so that we can move to the next
                                    l = 100     #protocol, which prevents redundancies

                                    if Matrix == 1:
                                        Matrix1[j][num+1] = root[j][0][1][k][l][1].text  #adding value of parameter to Matrix1
                                    if Matrix == 2:
                                        Matrix2[num + 1][j] = root[j][0][1][k][l][1].text


                                if searchitem.split('->')[0] == 'PAT':
                                    if Matrix == 1:
                                        Matrix1[j + 1 - tocExists][num + 1] = root[j][0][1][0][1].text.split()[8]
                                    if Matrix == 2:
                                        Matrix2[num + 1][j + 1 - tocExists] = root[j][0][1][0][1].text.split()[8]

                            except Exception:   #prevents error from stopping script when element does not exist
                                pass
                            l += 1
                        k += 1
                    j += 1
                return (searchItemFound, totalScanTime)

        parameterCounter = 0
        scanTimeSum = '0:0'

        for parameter in parameterList:     #for loop to search for each parameter key word in parameterlist
            searchItemExists = 0
            if parameter.split('->')[0] == 'Scan time':
                scanTimeSum = findSearchItem(1, parameter, parameterCounter, searchItemExists)[1]
            elif parameter.split('->')[0] == 'PAT':
                findSearchItem(1, parameter, parameterCounter, searchItemExists)
            elif parameter.split('->')[0] == 'Matrix':
                matrix1Looper = 1

                while matrix1Looper < protocolCount+1:  # multiplies the values of the phase and base resolution and inputs to the Matrix1
                    try:
                        Matrix1[matrix1Looper][8] = str(Matrix1[matrix1Looper][6]) + 'X ' + str(int(Matrix1[matrix1Looper][6]) * int(Matrix1[matrix1Looper][7].split("%")[0]) / 100)
                    except Exception:
                        Matrix1[matrix1Looper][6] or [matrix1Looper][7].split("%")[0] == '-'
                        pass
                    matrix1Looper += 1

                searchItemExists = 1

            elif parameter == 'Notes':
                searchItemExists = 1
            elif  findSearchItem(1, parameter, parameterCounter, searchItemExists)[0] == 0 and parameter.split('->')[0] != 'Notes': #calls search function to find each search parameter in parameterList
                print ("Warning! Parameter %s not found! Check spelling and full parameter name \n" % parameter.split('->')[0])    #prints a warning if the parameter called does not exist
            parameterCounter += 1

        parameterCounter = 0
        for complexParameter in complexParameterList:     #for loop to search for each parameter key word in parameterlist
            searchItemExists = 0
            if complexParameter.split('->')[0] == 'Scan time':
                scanTimeSum = findSearchItem(2, complexParameter, parameterCounter, searchItemExists)[1]
            elif complexParameter.split('->')[0] == 'PAT':
                findSearchItem(2, complexParameter, parameterCounter, searchItemExists)
            elif complexParameter.split('->')[0] == 'Matrix':
                matrix2Looper = 1

                while matrix2Looper < protocolCount + 1:  # multiplies the values of the phase and base resolution and inputs to the Matrix2

                    try:
                        Matrix2[10][matrix2Looper] = str(Matrix2[8][matrix2Looper]) + 'X '+ str(int(Matrix2[8][matrix2Looper]) * int(Matrix2[9][matrix2Looper].split("%")[0]) / 100)
                    except Exception:
                        Matrix2[8][matrix2Looper] or Matrix2[9][matrix2Looper] == '-'
                        pass
                    matrix2Looper += 1
                searchItemExists = 1
            elif complexParameter == 'Notes':
                searchItemExists = 1
            elif  findSearchItem(2, complexParameter, parameterCounter, searchItemExists)[0] == 0 and complexParameter.split('->')[0] != 'Notes': #calls search function to find each search parameter in parameterList
                print ("Warning! Parameter %s not found! Check spelling and full parameter name \n" % complexParameter.split('->')[0])    #prints a warning if the parameter called does not exist
            parameterCounter += 1


        printLooper1 = 0

        while printLooper1 < protocolCount + 1:    #prints the Matrix1 one row at a time
            print(Matrix1[printLooper1])
            printLooper1 += 1

        printLooper2 = 0

        while printLooper2 < complexParameterListSize:    #prints the Matrix2 one row at a time
            print(Matrix2[printLooper2])
            printLooper2 += 1

        Matrix1[0][parameterListSize-1] = '____________Notes____________'
        seriesName = root[0][0][2][0][0][0].get('name')
        seriesNameFile = seriesName.replace(" ", "_")
        seriesNameFile=seriesName.replace("/", "_")+'.htm'

        #f1 = open('masterList.htm', 'r')

        #f1.write('<!DOCTYPE html> \n')
        #f1.write('<html>\n')
        #f1.write('<body>\n')
        #f1.write('<A HREF = "file:///C:/Users/msveiven/PycharmProjects/untitled/scriptOutput1.htm">B5 - BRN MS</A>\n')
        #f1.write('</body>\n')
        #f1.write('</html>\n')

        #f1.seek(0)
        #s = f1.read()
        #R = s.split('</body>')

        #f1.close()

        #f1 = open('masterList.htm', 'w')
        #f1.write(R[0])
        #f1.write('<p>\n')
        #f1.write('<A HREF = "file:///C:/Users/kevcron35/PycharmProjects/untitled/')
        #f1.write(seriesNameFile)
        #f1.write('">')
        #f1.write(seriesName+' Updated '+time.strftime("%d.%m.%Y"))
        #f1.write('</A>\n')
        #f1.write('</p>\n')
        #f1.write('</body>\n')
        #f1.write('</html>\n')

        #f1.close()
        currentPath = os.getcwd()
        seriesNameFile = currentPath +"/" + seriesNameFile
        f = open(seriesNameFile, 'w+')   #REST OF SCRIPT IS WRITING HTML FILE

        f.write('<!DOCTYPE html> \n')
        f.write('<html>\n')
        f.write('<head>\n')
        f.write('<style>\n')
        f.write('table, th, td {\n')
        f.write('\t border: 1px solid black;\n')
        f.write('}\n')
        f.write('th, td { \n \t padding: 15px;\n}')
        f.write('</style>\n')
        f.write('</head>\n')
        f.write('<body>\n')

        if tocExists == 1:

            f.write('<h1>')
            f.write(root[0][0][2][0][0][0].get('name'))

            f.write(' (Total scan time: '+scanTimeSum.split(':')[0] + ':'+ scanTimeSum.split(':')[1]+')' )
            f.write('</h1>\n')
            f.write('<h2>')
            f.write('Overview')
            f.write('</h2>\n')

        else:
            f.write('<h1>')
            f.write(root[0][0][1][0][0].text[35:49])
            f.write(' (Total scan time: '+scanTimeSum.split(':')[0] + ':' + scanTimeSum.split(':')[1] + ' min)')
            f.write('</h1>\n')

        f.write('<table style="width:100%">\n')

        writeCounterColumn1 = 0

        while writeCounterColumn1 < 1:

            writeCounterRow1 = 0

            f.write('<table style="background-color:#FFFFE0;"> \n')
            f.write('<tr style="background-color:#BDB76B;color:ffffff;"> \n')
            while writeCounterRow1 < parameterListSize:
                f.write('<th>')
                f.write(str(Matrix1[writeCounterColumn1][writeCounterRow1]))
                f.write('</th>')
                writeCounterRow1 += 1
            f.write('</tr>')
            f.write('\n')
            writeCounterColumn1 += 1

        writeCounterColumn1 = 1

        while writeCounterColumn1 < protocolCount + 1:

            writeCounterRow1 = 0
            f.write('<tr>')
            while writeCounterRow1 < parameterListSize:
                f.write('<td>')
                f.write(Matrix1[writeCounterColumn1][writeCounterRow1])
                f.write('</td>')
                writeCounterRow1 += 1
            f.write('</tr>')
            f.write('\n')
            writeCounterColumn1 += 1


        f.write('</table>\n')
        f.write('<br>')
        f.write('</br>')
        f.write('\n')
        f.write('<table style="width:100%">\n')

        writeCounterColumn2 = 0

        while writeCounterColumn2 < 1:

            writeCounterRow2 = 0

            f.write('<table style="background-color:#CAE8FC;"> \n')
            f.write('<tr style="background-color:#0613D7;color:#FBFBFC;"> \n')
            while writeCounterRow2 < protocolCount+1:
                f.write('<th>')
                f.write(Matrix2[writeCounterColumn2][writeCounterRow2])
                f.write('</th>')
                writeCounterRow2 += 1
            f.write('</tr>')
            f.write('\n')
            writeCounterColumn2 += 1

        f.write('<h2>\n')
        f.write('Detailed')
        f.write('\n')
        f.write('</h2>\n')


        writeCounterColumn2 = 1

        while writeCounterColumn2 < complexParameterListSize:

            writeCounterRow2 = 0
            f.write('<tr>')
            while writeCounterRow2 < protocolCount+1:
                f.write('<td>')
                f.write(Matrix2[writeCounterColumn2][writeCounterRow2])
                f.write('</td>')
                writeCounterRow2 += 1
            f.write('</tr>')
            f.write('\n')
            writeCounterColumn2 += 1


        f.write('</table>\n')
        f.write('\n')
        f.write('<br>')
        f.write('</br>')
        f.write('<textarea rows="6" cols="140">')
        f.write('Insert notes here')
        f.write('</textarea>')
        f.write('<br>')
        f.write('</br>')
        f.write('<textarea rows="6" cols="140">')
        f.write('Indications')
        f.write('</textarea>')
        f.write('<br>')
        f.write('</br>')
        f.write('<img src=')
        f.write('"')
        f.write(series.split('xml')[0])
        f.write('jpg')
        f.write('"')
        f.write( ' alt="Placer Image" style="width:304px;height:228px;">')
        f.write('</body>\n')
        f.write('<html>\n')
        f.close()
        return

    currentPath = os.getcwd()
    path = currentPath + "/*.html"
    for fname in glob.glob(path):
        f = os.path.getmtime(fname)

        path = currentPath + "/*.xml"

        for fname in glob.glob(path):

            g = os.path.getmtime(fname)
            if f <= g:
                ProtParser(fname)
            elif f > g:
                print('ProtParser has already run on ' + fname)
            else:
                ProtParser(fname)
        return

    currentPath = os.getcwd()
    path = currentPath+"/*.html"
    for fname in glob.glob(path) :
        f = os.path.getmtime(fname)

        path = currentPath+"/*.xml"

        for fname in glob.glob(path):

            g = os.path.getmtime(fname)
            if f >= g:
                ProtParser(fname)
            elif f < g:
                print('ProtParser has already run on ' + fname)
            else:
                ProtParser(fname)
        return
    return