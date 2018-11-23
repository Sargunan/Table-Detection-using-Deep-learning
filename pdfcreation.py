from fpdf import FPDF
from PIL import Image
import glob
import os
'''
image_directory = '/Users/myuser/pics/'
extensions = ('*.jpg','*.png','*.gif')
pdf = FPDF()
imagelist=['c:\\temp\\0.7483.png']

for imageFile in imagelist:
    cover = Image.open(imageFile)
    width, height = cover.size
    pdf.add_page()
    # 1 px = 0.264583 mm (FPDF default is mm)
    pdf.image(imageFile, 0, 0, float(width * 0.264583), float(height * 0.264583))
pdf.output('c:\\temp\\' + "file.pdf", "F")

'''
from tabula import read_pdf

df = read_pdf("D:\\Sargunan\\Table\\001.pdf", area = (165.0,72.0,635.794,524.944), )
#df = read_pdf("c:\\temp\\data.pdf")
print (df)