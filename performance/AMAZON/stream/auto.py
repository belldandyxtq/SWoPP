#!/usr/bin/python

#auto process expironment data
import xlwt
import os

excel = xlwt.Workbook()
sheet = excel.add_sheet('sheet 1')
pwd=os.getcwd()
sheet.write(0,1,'Copy')
sheet.write(0,2,'Scale')
sheet.write(0,3,'Add')
sheet.write(0,4,'Triad')
i=1
for file in os.listdir(pwd+'/data'):
	f=open(pwd+'/data/'+file,'r')
	sheet.write(i,0,file.split('-')[1])
	content=f.read().split('\n')
	sheet.write(i,1,float(content[23][17:23]))
	sheet.write(i,2,float(content[24][17:23]))
	sheet.write(i,3,float(content[25][17:23]))
	sheet.write(i,4,float(content[26][17:23]))
	i=i+1
	f.close()
excel.save('stream.xls')
