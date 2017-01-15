#!/bin/python

'''
mdconvert.py

Script to convert the .md files found in the Raspberry Pi github pages to pdf files for use at jams.

Copyright (C) 2017  michael rimicans
   
   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 3 of the License, or
   (at your option) any later version.
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software Foundation,
   Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA

USAGE: Clone / Download the projects you interested in, copy mdconvert.py into directory and then run: python mdconvert.py
       Files should appear in ./pdf and, as an added bonus, html versions will be in ./html      
 
Requirements:

No Python 3 support just yet...thats next.

Grip: https://github.com/joeyespo/grip / pip install grip
pdfkit: https://github.com/pdfkit/pdfkit / pip install pdfkit
wkhtmltopdf: (debian based): sudo apt get install wkhtmltopdf
'''

import glob,os,pdfkit
from time import sleep
htmldir = "./html/"
pdfdir = "./pdf/"
gittoken = ""

if not os.path.isdir(htmldir):
	os.makedirs(htmldir)
	
if not os.path.isdir(pdfdir):
	os.makedirs(pdfdir)

if os.path.isfile(".gittoken"):
	fh = open(".gittoken","r")
	fileread = fh.read().splitlines()
	gittoken = fileread[0]
	fh.close()
else:
	print "\nUnable to load git token..you will be limited to 60 calls an hour to the github API\n"
	print "Please see: https://github.com/joeyespo/grip#access for more info"

	sleep(5)

if os.path.isfile("LICENCE.md"):
	fh=open("LICENCE.md","r")
	licenceText=fh.read()
	fh.close()
else:
	print "No licence for inclusion found..."
	sleep(5)
 
	
for mdFile in glob.glob("*.md"):
	print "Converting: "+mdFile+" to html\n"
	
	mdFileHTML = htmldir+mdFile+".html"
	pdfmdFile = pdfdir+mdFile+".pdf"

	if licenceText: #if licence text is found then append it to end of file via /tmp

		with open(mdFile,"r") as targetFile:
			contents = targetFile.read()
		targetFile.close()
		
		with open("/tmp/"+mdFile,"a") as tmpFile:
			tmpFile.write(contents)
			tmpFile.write(licenceText)
			mdFile=str(tmpFile.name)
	
	if gittoken:
		os.system("~/.local/bin/grip --pass "+gittoken+" "+mdFile+" --export "+mdFileHTML)
	else:
		os.system("~/.local/bin/grip "+mdFile+" --export "+mdFileHTML)
	pdfkit.from_file(mdFileHTML, pdfmdFile)
	
	if os.path.isfile(mdFile): #tidy up files in /tmp
		os.remove(mdFile)

	os.rename(pdfmdFile,pdfmdFile.replace('.md','')) #remove .md from pdf filename


