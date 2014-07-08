
# Getting header data from all the FITS files in database
# Standard totextfile was not working, mainly due to presence of 
# unrecognized Keyword "P.I.". 
# Script deletes offending keyword and writes all header text to screen
# which can be collected by command python getheaderdata.py > "output # file name"



import pyfits


filelist = open("alldata",'r')

for line in filelist:
    path = line.strip()
    name = path[26:]
    hdu = pyfits.open(path)
    inhdr = hdu[0].header
    del inhdr['P.I.']
    inhdr.totextfile('%s' % (name), clobber = True)
    hdu.close()


filelist.close()

