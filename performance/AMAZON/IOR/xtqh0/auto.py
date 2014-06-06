#!/usr/bin/python

#auto process expironment data
import xlwt
import os

excel = xlwt.Workbook()
sheet = excel.add_sheet('sheet 1')
sheet.write(0,1,'write')
sheet.write(0,2,'read')
i=1
pwd=os.getcwd()
for file in os.listdir(pwd+'/data'):
	f=open(pwd+'/data/'+file,'r')
	sheet.write(i,0,file)
	content=f.read().split('\n')
	sheet.write(i,1,float(content[35][11:16]))
	sheet.write(i,2,float(content[36][11:16]))
	i=i+1
	f.close()
excel.save('AMAZON IOR xtqh0.xls')
