import scipy as sp
import matplotlib.pyplot as plt
import numpy as np

#all inputs
h,r,d1,d2 = input("Channel Characteristics: Height, Range, d1 and d2 (meters): ").split()
h,r,d1,d2 = [int(h),int(r),int(d1),int(d2)]
f = int(input("Frequency of Transmitter (kHz): "))
eigen = int(input("Number of eigenpath: "))

#concerned variables
distance, lss, la, lb, angle = [0,0,0,0,0]

def findDistance(h,r,d1,d2,s,b):
	global distance
	if s>b or s==b :
		distance = np.sqrt(r**2+((2*b*h)+d1-((-1)**(s-b))*d2)**2)
	if b>s :
		distance = np.sqrt(r**2+((2*b*h)+d1-((-1)**(s-b))*d2)**2)
	return distance

def findlss(r):
	global lss
	lss =  1.0/r
	return lss

def findAngle(h,r,d1,d2,s,b):
	global angle
	if s>b or s==b:
		angle = 180*np.arctan2(r,((2*b*h)+d1-((-1)**(s-b))*d2))/np.pi
	if b>s:
		angle = 180*np.arctan2(r,((2*b*h)-d1+((-1)**(s-b))*d2))/np.pi
	if s==0 and b==0:
		angle = 0
	return angle

m = (1500.0/1023)
n = (1539.0/1650)

def findlb (angle, m, n,s,b):
	global lb
	lb = np.absolute((m*np.cos(np.pi*angle/180.0)-np.sqrt((n**2-(np.sin(np.pi*angle/180.0))**2)+0j))/(m*np.cos(np.pi*angle/180.0)+np.sqrt((n**2-(np.sin(np.pi*angle/180.0))**2)+0j)))
	return lb

salinity =  35 #value search on internet based on salinity in singapore
oceanT =  273+26 #26 celsius for shallow water about 70m deep.
ft = 21.9*10**(6-1520/oceanT)

def findla (salinity, ft, f, distance):
	global la
	la = np.exp(-0.998*distance*(((salinity*(2.34*10**-6)*ft*f)/(ft**2+f**2))+(((3.38*10**-6)*f**2)/(ft))))
	return la

tao = 0
def findTao(distance1, distance2):
	global tao
	tao = (distance1 - distance2)/1500 #speed of sound underwater
	return tao

#def findDelay(tao,distance, distanceD):
#	findTao(distance, distanceD)
#	d = round(tao*10**9,0)/10**9 #frequency sampling
#	delay.append(d)

def findBj(Tx,s,b,e):
	findDistance(h,r,d1,d2,s,b)
	findAngle(h,r,d1,d2,s,b)
	findTao(distance, distanceD)
	d = round(tao*500,0) #frequency sampling
	delay.append(d)
	print ("value of s: ", s, "and value of b:", b)
	print ("Distance for the ", e, "eigen path is: ", round(distance,4))
	findla(salinity, ft, f, distance)
	Bj = lss*la*(findlb(angle,m,n,s,b)**b)*(Tx)
	if s>b:
		Bj = -Bj
	Hn.append(Bj)

	return Hn


findlss(r)
distanceD = findDistance(h,r,d1,d2,0,0)
print ("lss is: ", round(lss,3))

#Direct Delta function
Tx = 1

#iterating function (non-recursive)
Hn = []
#delay = np.linspace(0,10,500,endpoint = False)
delay = []
s,b,e = [0,0,0]
for j in range (int(eigen/3)+1):
	for i in range (3):
		if eigen == e:
			break
		e += 1
		findBj(Tx,s,b,e)
		#to change the s and b values
		if i == 0 or i == 2:
			s+= 1
		elif i == 1:
			s-= 1
			b+= 1
#plotting the model
print ("Delay Value: ", delay)
print ("Impulse Response:", Hn)
print(len(Hn)," piece of data")
#plt.plot(delay, Hn)
plt.xlabel("time(s)")
plt.ylabel("Impulse Amplitude")
plt.stem(delay,Hn,'-')
plt.show()
