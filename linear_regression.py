import numpy as np
data=np.genfromtxt("ex1data1.txt",delimiter=',')
global t0,t1,sums0,sums1,sumchk
sums0=0
sums1=0
sumchk=0
t0=0
t1=0
h=lambda x:t0+t1*x
n=len(data)
def sum0():
	sums0=0
	for i in range(n):
		x=data[i,0]
		y=data[i,1]
		sums0+=(h(x)-y)
	return sums0

def sum1():
	sums1=0
	for i in range(n):
		x=data[i,0]
		y=data[i,1]
		sums1+=((h(x)-y)*x)
	return sums1

def chk():
	sumchk=0
	for i in range(n):
		x=data[i,0]
		y=data[i,1]
		sumchk+=(h(x)-y)**2
	return sumchk
prev=0
while sum0()!=0 and sum1()!=0:
	temp0=t0-(0.025*sum0())/n
	temp1=t1-(0.025*sum1())/n
	t0=temp0
	t1=temp1
	j=chk()/(2*n)
	if prev==j:
		break
	prev=j
	print(j)

