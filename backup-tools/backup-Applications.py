#! /usr/bin/env python
#
#  For the full copyright and license information, please view the LICENSE
#  file that was distributed with this source code.
#
#  Copyright 2010 (c) Augusto Morais
#  All rights reserved.

__author__="Augusto Morais <aflavio at smartlinks.com.br>"
__date__ ="$Jan 11, 2010 6:14:02 PM$"

class Compress:

  def doCompress(self, files, path = "/home/"):
    import tarfile
    import os
    import datetime
    from datetime import datetime

    #try:
    dirformat = datetime.strftime(datetime.today(), "%Y%m%d-%H%M")
    os.makedirs("/home/aflavio/backups/applications/" + dirformat)

    self.dirsSuccess = []

    print ("\n\nIniciando backup dos Aplicativos...")

    for file in files:
      compressedFile = tarfile.open("/home/aflavio/backups/applications/" + dirformat + "/" + file + ".tar.gz", "w:gz")
      compressedFile.add(path + file)
      compressedFile.close()

      self.dirsSuccess += ["Backup com Sucesso: " + file]
      print ("OK - " + file)

    return self.dirsSuccess

class SysUtils:

  def listDir(self, path = "/home"):
    import os
    dirList=os.listdir(path)
    files=[]
    for fname in dirList:
      if fname is not None:
        files+=[fname]

    #excluding homes
    files.remove("aflavio")

    return files

  def createFile(self):
    import os
    import datetime
    from datetime import datetime

    try:
      os.makedirs("/home/aflavio/backups/log/")
    except:
      pass

    fileformat = datetime.strftime(datetime.today(), "%Y%m%d-%H%M") + ".log"
    file = open("/home/aflavio/backups/log/" + fileformat, "w")
    file.write ("####           BACKUP LOG            ####\n")
    file.write ("#### CREATED AT: "+datetime.strftime(datetime.today(), "%d/%m/%Y %H:%M:%S")+" ####\n\n")

    self.fileLogName = fileformat
    self.fileHandle = file
    return self.fileHandle

  def insertMsg(self, message):
    self.fileHandle.write (message + "\n")

  def closeLog(self):
    self.fileHandle.close()




SU = SysUtils()
files = SU.listDir("/home")
SU.createFile()

CompactFiles = Compress()
abc = CompactFiles.doCompress(files)

#Changing permission to AFLAVIO USER
import os
os.system('chown aflavio:aflavio -R /home/aflavio/backups')

for retorno in abc:
  SU.insertMsg(retorno)

SU.insertMsg("#### Fim do log #####")
SU.closeLog()
