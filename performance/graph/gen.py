#!/usr/bin/python

import xlwt

def m1(n1):
	return 100*n1

def I(n1,n2):
	min=((n1<n2) and [n1] or [n2])[0]
	return 10*min

def e2(n1):
	return 100*n1

def C2_Money(T1):
	return 0.1*T1

def C2_High_Money(T1):
	return 0.2*T1

def D1(n1):
	return n1

def min(a,b,c):
	list=[a,b,c]
	return sorted(list)[0]

workbook=xlwt.Workbook()

sheet=workbook.add_sheet('1')
sheet.write(0,0,'n1')
sheet.write(0,1,'n2')
sheet.write(0,2,'C2')
sheet.write(0,3,'m1(n1)')
sheet.write(0,4,'I(n1,n2)')
sheet.write(0,5,'e2(n2)')
sheet.write(0,6,'T1')
sheet.write(0,7,'T2')
sheet.write(0,8,'C2_Money(T1)')
sheet.write(0,9,'C2_Money(T2)')
sheet.write(0,10,'C2_High_Money(T2)')
sheet.write(0,11,'A')
sheet.write(0,12,'B')

count=1
for n1 in range(1,5):
	for n2 in range(1,5):
		for c2 in range(5,11) :
			sheet.write(count,0,n1)
			sheet.write(count,1,n2)
			sheet.write(count,2,c2)
			sheet.write(count,3,m1(n1))
			sheet.write(count,4,I(n1,n2))
			sheet.write(count,5,e2(n2))
			T1=float(1.0/D1(c2))
			T2=float(1.0/min(m1(n1),I(n1,n2),e2(n2)))
			sheet.write(count,6,T1)
			sheet.write(count,7,T2)
			sheet.write(count,8,float(C2_Money(T1)))
			sheet.write(count,9,float(C2_Money(T2)))
			sheet.write(count,10,float(C2_High_Money(T2)))
			sheet.write(count,11,c2*C2_Money(T1))
			sheet.write(count,12,c2*C2_Money(T2)+n1*C2_Money(T2)+n2*C2_High_Money(T2))
			count=count+1
workbook.save('graph.xls')
