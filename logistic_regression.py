import numpy as np
import math as m

data=np.genfromtxt("ex2data1.txt",delimiter=',')
global t0,t1,t2
t0=0
t1=0
t2=0
global sumn1,sumn2,sumsd1,sumsd2
sumsd2=0
sumsd1=0
sumn1=0
sumn2=0

m=len(data)
z=lambda p,q:t0+t1*p+t2*q

h=lambda z:1/(1+np.exp(-z))

for i in range(m):
	sumn1+=data[i,0]
	sumn2+=data[i,1]

mean1=sumn1/m
mean2=sumn2/m

for i in range(m):
	sumsd1+=(data[i,0]-mean1)**2
	sumsd2+=(data[i,1]-mean2)**2

sd1=(sumsd1/m)**0.5
sd2=(sumsd2/m)**0.5

for i in range(m):
	data[i,0]=((data[i,0]-mean1)/sd1)
	data[i,1]=((data[i,1]-mean2)/sd2)


def s0():
	sum0=0
	for i in range(m):
		x1=data[i,0]
		x2=data[i,1]
		y=data[i,2]
		sum0+=(h(z(x1,x2))-y)
	return sum0

def s1():
	sum1=0
	for i in range(m):
		x1=data[i,0]
		x2=data[i,1]
		y=data[i,2]
		sum1+=(h(z(x1,x2))-y)*x1
	return sum1

def s2():
	sum2=0
	for i in range(m):
		x1=data[i,0]
		x2=data[i,1]
		y=data[i,2]
		sum2+=(h(z(x1,x2))-y)*x2
	return sum2

def jsum():
	chk=0
	for i in range(m):
		x1=data[i,0]
		x2=data[i,1]
		y=data[i,2]
		chk+=(-(y*np.log(h(z(x1,x2)))+(1-y)*np.log(1-h(z(x1,x2)))))
	return chk

global prev
prev=0
s0()
s1()
s2()
while (1):
	temp0=t0-(s0()*0.5)/m
	temp1=t1-(s1()*0.5)/m
	temp2=t2-(s2()*0.5)/m

	t0=temp0
	t1=temp1
	t2=temp2
	j=(jsum())/m
	if j==prev:
		break
	prev=j
	#print(j)
print(t0,t1,t2)
n1=int(input("exam1:"))
n2=int(input("exam2:"))

hn=h(z(n1,n2))		#n1 and n2 need to be normalized
if(hn>0.5):
	print("1")
else:
	print("0")

#n2=data[2,1]

#hn=h(z(n1,n2))

#print(hn)
