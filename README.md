# mdconvert
Script to convert the .md files found in the Raspberry Pi github pages to pdf files for use at jams

USAGE: Clone / Download the projects you interested in, copy mdconvert.py into directory and then run: python mdconvert.py
       Files should appear in ./pdf and, as an added bonus, html versions will be in ./html      
 
Requirements:

No Python 3 support just yet...thats next.

Grip: https://github.com/joeyespo/grip / pip install grip

pdfkit: https://github.com/pdfkit/pdfkit / pip install pdfkit

wkhtmltopdf: (debian based): sudo apt get install wkhtmltopdf

