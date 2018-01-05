import numpy as np
import random
import math

def loaddata():
	a=np.genfromtxt("Localization.txt",dtype='str')
	return a

def count(x):
	x[30][30]='0'
	count=0
	for i in x.flat:
		if i=='0':
			count+=1
	return count

def pMatrix(count,data):
	p=np.zeros([37,37])
	for i in range(37):
		for j in range(37):
			if data[i][j]=='0':
				p[i][j]=1/count
	return p

def move(pMat,data,action):
	p=np.zeros([37,37])
	act=np.array([[0,1],[0,-1],[-1,0],[1,0]])
	dic={'r':0, 'l':1, 'd':2, 'u':3}
	for i in range(1,36):
		for j in range(1,36):
			nx=i+act[dic[action]][0]
			ny=j+act[dic[action]][1]
			if data[nx][ny]=='1':
				p[i][j]+=pMat[i][j]
			else:
				p[nx][ny]+=pMat[i][j]
	return p

def nextStep(pMap,data,fringeH,fringeP,pPast,g):
	ptmp=[pMap,pMap,pMap,pMap]
	act=np.array([[0,1],[0,-1],[-1,0],[1,0]])
	dic={0:'r', 1:'l', 2:'d', 3:'u'}
	comp=[g,g,g,g]
	for i in range(4):
		ptmp[i]=move(ptmp[i],data,dic[i])
		for j in range(1,36):
			for k in range(1,36):
				if ptmp[i][j][k]!=0:
					comp[i]+=ptmp[i][j][k]*(np.sqrt(np.square(30-j)+np.square(30-k)))
	for x in range(4):
		for y in range(len(pPast)):
			print(len(pPast))
			if (pPast[y]==ptmp[x]).all()!=True:
				fringeP.append(ptmp[x])
				fringeH.append(comp[x])
	#	fringeP.append(ptmp[x])
	#	fringeH.append(comp[x])
	return fringeP,fringeH


data=loaddata()
c=count(data)
p=pMatrix(c,data)
seq=['start']
h0=0
for j in range(1,36):
			for k in range(1,36):
				if p[j][k]!=0:
					h0+=p[j][k]*(np.sqrt(np.square(30-j)+np.square(30-k)))
fringeH=[h0]
fringeP=[p]
pPast=[]
g=0
while p[30][30]<50:
	index=fringeH.index(min(fringeH))
	p=fringeP[index]
	pPast.append(p)
	del fringeH[index]
	del fringeP[index]
	fringeP,fringeH=nextStep(p,data,fringeH,fringeP,pPast,g)
	print(p[30][30])
	g+=1
