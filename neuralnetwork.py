import scipy.io as sio
import numpy as np
import scipy.optimize as opt
global m
m=5000
weights = sio.loadmat('ex4weights.mat')
theta1 = weights['Theta1']    
theta2 = weights['Theta2']    
mat=sio.loadmat('ex4data1.mat')
x=np.array(mat['X'])
x=np.insert(x,0,1,axis=1)
y=np.array(mat['y'])
params = np.hstack((theta1.ravel(order='F'), theta2.ravel(order='F')))    
ilayersize = 400
hlayersize = 25
num_labels = 10
lmbda = 1
#print(theta2.shape)
#print(params.shape)
for i in range(5000):
	if y[i]==10:
		y[i]=0
yn=np.zeros((5000,10))

for i in range(5000):
	if y[i]==0:
		yn[i,0]=1
	if y[i]==1:
		yn[i,1]=1
	if y[i]==2:
		yn[i,2]=1
	if y[i]==3:
		yn[i,3]=1
	if y[i]==4:
		yn[i,4]=1
	if y[i]==5:
		yn[i,5]=1
	if y[i]==6:
		yn[i,6]=1
	if y[i]==7:
		yn[i,7]=1
	if y[i]==8:
		yn[i,8]=1
	if y[i]==9:
		yn[i,9]=1
ym=yn
yn=np.hstack((yn.ravel()))
#print(yn)
#print(yn.shape)

def sigm(p):
	g=1/(1+np.exp(-p))
	return g


#print(a1)
def costfunc(params,ilayersize,hlayersize,num_labels,x,y,lmbda):
	theta1=np.reshape(params[:(hlayersize)*(ilayersize+1)],(hlayersize,ilayersize+1))
	theta2=np.reshape(params[(hlayersize)*(ilayersize+1):],(num_labels,hlayersize+1))

	ones=np.ones((5000,1))

	a1=x
	z1=a1.dot(theta1.T)
	a2=sigm(z1)
	a2=np.hstack((ones,a2))
	z2=a2.dot(theta2.T)
	h=sigm(z2)

	trm1=np.multiply(ym,np.log(h))
	trm2=np.multiply((1-ym),np.log(1-h))

	sum1=np.sum(trm1+trm2)
	return (sum1)*(-1/m)
global k
k=0

def randomint(inl,outl):
	e=0.12
	return np.random.rand(outl,inl+1)*2*e-e

itheta1=randomint(ilayersize,hlayersize)
itheta2=randomint(hlayersize,num_labels)

iparams=np.hstack((itheta1.ravel(),itheta2.ravel()))
#print(iparams.shape)


def grad(params,ilayersize,hlayersize,num_labels,x,y,lmbda):
	itheta1=np.reshape(params[:(hlayersize)*(ilayersize+1)],(hlayersize,ilayersize+1))
	itheta2=np.reshape(params[(hlayersize)*(ilayersize+1):],(num_labels,hlayersize+1))

	delta1=np.zeros(itheta1.shape)
	delta2=np.zeros(itheta2.shape)
	for i in range(5000):
		ones=np.ones(1)
		a1=np.hstack(x[i])
		z2=np.dot(a1,itheta1.T)
		#print(z1.shape)
		a2=sigm(z2)
		#print(a1.shape)
		a2=np.hstack((ones,a2))
		#print(a2.shape)

		#print(itheta2.shape)
		z3=np.dot(a2,itheta2.T)
		#print(z2.shape)
		a3=sigm(z3)
		#print(a3.shape)
		d3=np.subtract(a3,ym[i])
		
		d3=np.reshape(d3,(1,10))
		#print(d3.shape)
		z2=np.hstack((ones,z2))
		#print(itheta2.shape)
		#print(d3,shape)
		#d2=np.multiply(np.multiply(np.dot(itheta2.T,d3.T),a2),(1-a2))
		r=itheta2.T@d3.T
		#print(r.shape)
		a2=np.reshape(a2,(26,1))
		r=np.multiply(r,a2)
		r=np.multiply(r,(1-a2))
		d2=r
		#print(itheta1.shape)

		#print(itheta1)
		#d1=np.multiply(np.multiply(np.dot(itheta1.T,d2),a1),(1-a1))
		a2=np.reshape(a2,(26,))
		d2=d2[1:,:]
		delta1=delta1+d2@a1[np.newaxis,:]
		delta2=delta2+d3.T@a2[np.newaxis,:]

		delta1 /=m
		delta2 /=m
		#print(D1.shape)
		#print(D2.shape)
	return np.hstack((delta1.ravel(order='F'),delta2.ravel(order='F')))


		#print(D2)
#print(y.shape)
print(x.shape)
thetaopt=opt.fmin_cg(f=costfunc,x0=params,fprime=grad,args=(ilayersize,hlayersize,num_labels,x,y.flatten(),lmbda),maxiter=1)

theta1opt=np.reshape(thetaopt[:hlayersize*(ilayersize+1)],(hlayersize,ilayersize+1),'F')
theta2opt=np.reshape(thetaopt[hlayersize*(ilayersize+1):],(num_labels,hlayersize+1),'F')
print(x.shape)

def predict(theta1,theta2,x,y):
	ones=np.ones((5000,1))
	a1=np.hstack((x))
	a1=np.reshape(a1,(5000,401))
	a2=sigm(a1.dot(theta1.T))
	a2=np.hstack((ones,a2))
	h=sigm(a2.dot(theta2.T))
	return np.argmax(h,axis=1)+1

pred=predict(theta1opt,theta2opt,x,y)
print(np.mean(pred==y.flatten())*100)






	





