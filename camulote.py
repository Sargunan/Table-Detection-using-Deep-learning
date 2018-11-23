# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 15:51:00 2018

@author: Murali
"""

from pdf2jpg import pdf2jpg

result = pdf2jpg.convert_pdf2jpg('D:\\Sargunan\\Table\\001.pdf', 'c:\\temp\\p')
print(result)
