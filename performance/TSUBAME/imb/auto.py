#!/usr/bin/python

#auto process expironment data
import xlwt
import os

excel = xlwt.Workbook()
sheet = excel.add_sheet('sheet 1')
sheet.write(0,1,'latency')
sheet.write(0,2,'bandwidth-64B')
sheet.write(0,3,'bandwidth-4MB')
i=1
pwd=os.getcwd()
for file in os.listdir(pwd+'/data'):
	f=open(pwd+'/data/'+file,'r')
	content=f.read().split('\n')
	if len(content) > 70:
		sheet.write(i,0,file[3:])
		sheet.write(i,1,float(content[59][33:39]))
		sheet.write(i,2,float(content[66][46:52]))
		sheet.write(i,3,float(content[82][46:52]))
		i=i+1
	f.close()
excel.save('imb.xls')
