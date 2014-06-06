#!/usr/bin/python

#auto process expironment data
import xlwt
import os

excel = xlwt.Workbook()
sheet = excel.add_sheet('sheet 1')
i=0
pwd=os.getcwd()
for file in os.listdir(pwd+'/data'):
	f=open(pwd+'/data/'+file,'r')
	sheet.write(i,0,file.split('-')[1])
	content=f.read().split('\n')
	data=content[len(content)-2][:-2]
	sheet.write(i,1,int(data))
	i=i+1
	f.close()
excel.save('test.xls')
