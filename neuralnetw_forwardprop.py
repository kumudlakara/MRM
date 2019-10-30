import scipy.io as sio
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)
global m
m=5000
mat=sio.loadmat('ex3data1.mat')
th=sio.loadmat('ex3weights.mat')
th1=np.array(th['Theta1'])
th2=np.array(th['Theta2'])
x=np.array(mat['X'])
x=np.insert(x,0,1,axis=1)
y=np.array(mat['y'])
#print(x.shape)
#print(th1.shape)
#print(y.shape)
#print(y)
for i in range(5000):
	if(y[i,0]==10):
		y[i,0]=0

#print(y)
z=np.dot(x,th1.T)
b=[]
hv=[]
#print(z)
#print(z.shape)
def sigm(p):
	g=1/(1+np.exp(-p))
	return g
a=[]
for i in range(5000):
	for j in range(25):
		zel=z[i,j]
		h=sigm(zel)
		a.append(h)
a=np.array(a)
a=a.reshape(5000,25)
a=np.insert(a,0,1,axis=1)
#print(a)
print(a.shape)
print(th2.shape)
z2=np.dot(a,th2.T)
hx=[]
print(z2.shape)
for i in range(5000):
	for j in range(10):
		zel2=z2[i,j]
		h2=sigm(zel2)
		hx.append(h2)
hx=np.array(hx)
hx=hx.reshape(5000,10)
print(hx)
print(hx.shape)
numb=[]
for i in range(5000):
	maxm=np.max(hx[i])
	#print(maxm)
	_,pos=np.where(hx==maxm)
	if pos==9:
		
		ele=0
	else:
		ele=pos+1
	numb.append(ele)

numb=np.array(numb)
numb=numb.reshape(5000,1)
print(numb)
global sums
sums=0
for i in range(5000):
	if(numb[i]==y[i]):
		sums=sums+1

acc=(sums/5000)*100
print(acc)
#print(hv)
#print(hv.shape)
#maxm=np.max(hv)
#print(maxm)
#pos, =np.where(hv==maxm)
#b=np.array(b)
#print(pos)
#print(b)
#print(b.shape)
#dcst=np.dot(x.T,b)/m
#print(dcst)
#print(dcst.shape)
