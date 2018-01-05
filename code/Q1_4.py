import numpy as np
import random
np.set_printoptions(threshold=np.inf)

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

def blockMatrix(data):
	b=np.zeros([37,37])
	neigh=np.array([[1,0],[-1,0],[0,-1],[0,1],[1,1],[1,-1],[-1,1],[-1,-1]])
	for i in range(37):
		for j in range(37):
			if data[i][j]=='1':
				for k in range(8):
					nx=i+neigh[k][0]
					ny=j+neigh[k][1]
					if nx>=0 and nx<37 and ny>=0 and ny<37 and data[nx][ny]!='1':
						b[nx][ny]+=1
				b[i][j]=-1
	return b

def reDisP(pMat,bMat,obs):
	total=0.0
	for i in range(37):
		for j in range(37):
			if bMat[i][j]==obs:
				total+=pMat[i][j]
			else:
				pMat[i][j]=0
	#print(total)

	for k in range(37):
		for p in range(37):
			if pMat[k][p]!=0.0:
				pMat[k][p]=pMat[k][p]/total

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

def q1():
	data=loaddata()
	c=count(data)
	p=pMatrix(c,data)
	b=blockMatrix(data)
	reDisP(p,b,5)
	p=move(p,data,'l')
	reDisP(p,b,5)
	p=move(p,data,'l')
	reDisP(p,b,5)
	for i in range(37):
		for j in range(37):
			if p[i][j]!=0:
				print(i,",",j,":",p[i][j])


a=input("input 1 for question (1) or input else for question (2)： ")
if a=='1':
	q1();


print("Q2\ninput observation and split by space, eg: \"1 2 3\"")
obs=[int(x) for x in input().split()]
print("input actions(u,d,l,r) and split by space, eg: \"u u u\"")
act=[str(y) for y in input().split()]
data=loaddata()
c=count(data)
p=pMatrix(c,data)
b=blockMatrix(data)
reDisP(p,b,obs[0])
for i in range(len(act)):
	p=move(p,data,act[i])
	reDisP(p,b,obs[i+1])
maxList=[]
for i in range(37):
	maxList.append(max(p[i]))
maxP=max(maxList)
for i in range(37):
		for j in range(37):
			if p[i][j]==maxP:
				print(i,",",j,":",p[i][j])
