import numpy as np
import random
import math

def loaddata(filename):
	file=np.loadtxt(filename)
	x1=file[0:5].copy()
	x2=file[5:10].copy()
	x3=file[10:15].copy()
	x4=file[15:20].copy()
	x5=file[20:25].copy()
	x=(x1,x2,x3,x4,x5)
	return x

def train_data(data,expected_out,weight,b):
	error=expected_out-predict(data,weight,b)
	b+=0.4*error
	for i in range(5):
		for j in range(5):
			weight[i][j]+=0.4*error*data[i][j]
			#print(weight[i][j])
	return error

def predict(data,weight,b):
	y=b
	for i in range(5):
		for j in range(5):
			y+=data[i][j]*weight[i][j]
	return 1.0 if y>0 else 0.0

def addnoise(data):
	for x in range(5):
		for y in range(5):
			noise = np.random.normal(0,0.1,25)
			for z in range(5):
				data[x][y][z]+=noise[z+5*y]
	return data

i1=loaddata("ClassA.txt")
i2=loaddata("ClassB.txt")
i3=loaddata("Mystery.txt")
i1=addnoise(i1)
i2=addnoise(i2)

w=[[random.random() for i in range(5)]for i in range (5)]
b=random.random()
while True:
	e=0
	for i in range(5):
		e+=abs(train_data(i1[i],0,w,b))
	for j in range(5):
		e+=abs(train_data(i2[j],1,w,b))
	if e==0:
		break

for i in range(5):
	print(predict(i3[i],w,b))