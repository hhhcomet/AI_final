betaList=[0.1,0.3,0.5,0.7,0.9,0.99,0.992,0.994,0.996,0.998,0.999]
R=[100,90,80,70,60,50,40,30,20,-250]
e=0.001
delta=0
time=0
for beta in betaList:
	u=[0,0,0,0,0,0,0,0,0,0]
	choice=["","","","","","","","","",""]	
	while True:
		delta=0
		tmp=[0,0,0,0,0,0,0,0,0,0]
		udead=R[9]+beta*u[0]
		time+=1
		#print("Turn ",time,": udead=",udead)
		for i in reversed(range(10)):
			if i==9:
				tmp[i]=udead
			elif i==0:
				tmp[i]=max(udead,R[i]+beta*u[i+1])
			else:
				tmp[i]=max(udead,R[i]+beta*((1-0.1*i)*u[i]+0.1*i*u[i+1]))
			if abs(tmp[i]-u[i])>delta:
				delta=(tmp[i]-u[i])
		for i in range(10):
			u[i]=tmp[i]
			if u[i]==udead:
				choice[i]="Replace"
			else:
				choice[i]="Use"
		if delta<=e*(1-beta)/beta:
			break
	print("beta=",beta)
	for x in range(10):
		print (x,": ",u[x]," ",choice[x])
	


