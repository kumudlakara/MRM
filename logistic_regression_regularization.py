import numpy as np
ls=[]
data=np.genfromtxt("ex2data2.txt",delimiter=',')
global a,pos
a=0.3		#lrng rate
pos=3
global m
m=118		#no of training exs
y=np.array(data[:,2])		
y=np.reshape(y,(118,1))
#print(y)
data=np.insert(data,0,1,axis=1)		#insrtng 1 in frnt of all rows
#print(data)
for i in range(118):
	ls.append(data[i,:3])
x=np.array(ls)
for i in range(1,6):
	for j in range(0,i):
		
		for k in range(118):		#finding the othr features which are frmd by mult the ones given
			vals=[]
			x1=x[k,1]
			x2=x[k,2]
			val=(x1**(i-j))*(x2**j)
			vals.append(val)		#vals is a list which will store all the resp features of the row
									#then cn make into an ary nd use insrt in x at the end pos
									#pos used find pos of the plce whre to insrt nd is incremntd 
		vals=np.array(vals)
		print(vals)
		x=np.insert(x,pos,vals,axis=1)
		pos=pos+1
		
#print(x)
th=np.zeros((18,1))
print(np.size(x[0]))
def sall(k):
	sum=0
	for i in range(m):			#will fnd sum for o'*x for that x and find h also
								#then uses h nd correspndng y nd x to fnd sum
		z=th.T.dot(x[i])
		h=1/(1+np.exp(-z))
		sum+=(h-y[i,0])*x[i,k]
	return sum
temp=np.zeros((18,1))				#temp will be used to store intial values fr thetas bfore simultneous updte

for j in range(150):
	temp0=th[0]-(a*sall(0))/m
	for i in range(1,18):
		temp[i]=(th[i]*(1-(a*1)/m)-((a*(sall(i)))/m)+(th[i]/m))
	for i in range(1,18):
		th[i]=temp[i]				#upadtion prt
	th[0]=temp0						#updation is diff for theta-0

print(th)










