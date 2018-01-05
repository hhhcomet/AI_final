beta=0.9
R=[100,90,80,70,60,50,40,30,20,-250]
e=0.001
delta=0
time=0
u=[0,0,0,0,0,0,0,0,0,0]
price=250
while price>0:
	flag=0;
	while True:
		delta=0
		tmp=[0,0,0,0,0,0,0,0,0,0]
		udead=R[9]+beta*u[0]
		time+=1
		use=-price+beta*0.5*(u[1]+u[2])
		for i in reversed(range(10)):
			if i==9:
				tmp[i]=max(udead,use)
				if use>udead:
					flag=1
					udead=use
				else:
					#price=-udead+beta*0.5*(u[1]+u[2])
					price-=1
			elif i==0:
				tmp[i]=max(udead,R[i]+beta*u[i+1])
			else:
				tmp[i]=max(udead,R[i]+beta*((1-0.1*i)*u[i]+0.1*i*u[i+1]))
			if abs(tmp[i]-u[i])>delta:
				delta=(tmp[i]-u[i])
		for i in range(10):
			u[i]=tmp[i]
		if delta>=e*(1-beta)/beta:
			break
	if flag==1:
		print(price)
		break
#for x in range(10):
#	print (u[x])
	


