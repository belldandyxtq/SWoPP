#!/usr/bin/python

#auto process expironment data
import xlwt
import os

excel = xlwt.Workbook()
sheet = excel.add_sheet('sheet 1')
i=1
sheet.write(0,1,'bandwidth')
pwd=os.getcwd()
for file in os.listdir(pwd+'/data'):
	f=open(pwd+'/data/'+file,'r')
	content=f.read().split('\n')
	if 15 < len(content):
		sheet.write(i,0,file[3:])
		data=float(content[15][38:42])
		if 10 > data:
			data=data*1000
		sheet.write(i,1,data)
		i=i+1
	f.close()
excel.save('iperf.xls')
