import numpy as np
data=np.genfromtxt("ex1data2.txt",delimiter=',')
global t0
t0=0
global t1,sums0,sums1,sums2

sums0=0
sums1=0
sums2=0
t1=0
global t2,sum1,sum2,sumsd1,sumsd2
t2=0
sum1=0
sum2=0
sumsd2=0
sumsd1=0
h=lambda x1,x2:t0+t1*x1+t2*x2

n=len(data)

for i in range(n):
	sum1+=data[i,0]
	sum2+=data[i,1]

mean1=sum1/n
mean2=sum2/n

for i in range(n):
	sumsd1+=(data[i,0]-mean1)**2
	sumsd2+=(data[i,1]-mean2)**2

sd1=(sumsd1/n)**0.5
sd2=(sumsd2/n)**0.5

for i in range(n):
	data[i,0]=((data[i,0]-mean1)/sd1)
	data[i,1]=((data[i,1]-mean2)/sd2)


def s0():
	
	sums0=0
	for i in range(n):
		x1=data[i,0]
		x2=data[i,1]
		y=data[i,2]
		sums0+=(h(x1,x2)-y)
	return sums0

def s1():
	sums1=0
	for i in range(n):
		x1=data[i,0]
		x2=data[i,1]
		y=data[i,2]
		sums1+=(h(x1,x2)-y)*x1
	return sums1

def s2():
	sums2=0
	for i in range(n):
		x1=data[i,0]
		x2=data[i,1]
		y=data[i,2]
		sums2+=(h(x1,x2)-y)*x2
	return sums2


global chk
chk=0

def jsum():
	chk=0
	for i in range(n):
		x1=data[i,0]
		x2=data[i,1]
		y=data[i,2]
		chk+=(h(x1,x2)-y)**2
	return chk

prev=0

while s0()!=0 and s1()!=0 and s2()!=0:
	temp0=t0-(0.2*s0())/n
	temp1=t1-(0.2*s1())/n
	temp2=t2-(0.2*s2())/n
	t0=temp0
	t1=temp1
	t2=temp2
	j=jsum()/(2*n)
	if prev==j:
		break;
	prev=j



	


