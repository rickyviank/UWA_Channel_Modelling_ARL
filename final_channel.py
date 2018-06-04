import scipy.signal 
import matplotlib.pyplot as plt
import numpy as np

#input function
selector = int(input("Enter type of waves: Gaussian (0), Sine(1), Cosine(2), Square(3): "))
t = 2*np.pi
x = np.linspace(0,t,10)
correct = True
while(correct == True):
	if selector == 0:
		a,b,c = input("input parameters for the gaussian curve (scalar, mean, variance): ").split()
		a,b,c = (float(a),float(b), float(c))
		gaussian = a*np.exp(-((x-b)**2)/2*c**2)
		Tx = gaussian
	elif selector==1:
		a,b,c = input("input parameters for the sine curve(amplitude, frequency(Hz), phase): ").split()
		a,b,c = (float(a),float(b), float(c))
		sine = a*np.sin(x*b-c)
		Tx = sine
	elif selector==2:
		a,b,c = input("input parameters for the cosine curve (amplitude, frequency(Hz), phase): ").split() 
		a,b,c = (float(a),float(b), float(c))
		cosine = a*np.cos(x*b-c)
		Tx = cosine
	elif selector==3:
		t = float(input("Time taken for square wave(s): "))
		x = np.linspace(0,t,10)
		square = scipy.signal.square(2*np.pi*x)
		Tx = square
	else:
		Tx = 1

	print (Tx)

	plt.plot(np.linspace(0,t,10),Tx)
	plt.show()
	plt.close()
	check = input("is this the intended input wave? (Yes/No) ")

	if(check == "yes" or check == "Yes"):
		correct = False
	else:
		print("Please re-input the waves parameters.")
		correct = True

print("Proceeds to Channel with the following signal: ", Tx)

#channel characteristics
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
	tao = (distance1 - distance2)/1500 #speed of light
	return tao

#def findDelay(tao,distance, distanceD):
#	findTao(distance, distanceD)
#	d = round(tao*10**9,0)/10**9 #frequency sampling
#	delay.append(d)

def findBj(DirectDelta,s,b,e):
	findDistance(h,r,d1,d2,s,b)
	findAngle(h,r,d1,d2,s,b)
	findTao(distance, distanceD)
	d = round(tao*10**9,0) #frequency sampling
	delay.append(d)
	print ("value of s: ", s, "and value of b:", b)
	print ("Distance for the ", e, "eigen path is: ", round(distance,4))
	findla(salinity, ft, f, distance)
	Bj = lss*la*(findlb(angle,m,n,s,b)**b)*(DirectDelta)
	if s>b:
		Bj = -Bj
	Hn.append(Bj)

	return Hn


findlss(r)
distanceD = findDistance(h,r,d1,d2,0,0)
print ("lss is: ", round(lss,3))

#Direct Delta function
DirectDelta = 1

#iterating function (non-recursive)
Hn = []
delay = []
s,b,e = [0,0,0]
for j in range (int(eigen/3)+1):
	for i in range (3):
		if eigen == e:
			break
		e += 1
		findBj(DirectDelta,s,b,e)
		#to change the s and b values
		if i == 0 or i == 2:
			s+= 1
		elif i == 1:
			s-= 1
			b+= 1

s1 = Tx
s2 = Hn
print ('s1: ', s1)
print ('s2: ', s2)
s3 = np.flip(s2,0)
length = len(s1)+len(s2)-1

s1_zeros = length - len(s1)
s3_zeros = length - len(s3)

temp_s1 = np.concatenate((np.zeros(s1_zeros),s1))
temp_s2 = np.concatenate((s3, np.zeros(s3_zeros)))
print('temp_s1 (pure input): ', temp_s1)
print('temp_s2 (pure input): ', temp_s2)

mul = 0
out = np.zeros(length)

for i in range(length):
	if(i==0):
		mul = temp_s1*temp_s2
		print('temp_s2 (when i==0): ', temp_s2)
		print('temp_s1 (when i==0): ', temp_s1)
		out[i] = sum(mul)
	else:
		temp_s1 = np.concatenate((temp_s1[1:],temp_s1[:1]))#left shift, not sure how to do right shift
		print('temp_s2: ', temp_s2)
		print('temp_s1: ', temp_s1)
		mul = temp_s1*temp_s2
		out[i] = sum(mul)


#plotting the model
print ("Delay Value: ", delay)
print ("Impulse Response:", Hn)
print ("Final signal: ", out)
x_axis = np.linspace(1,len(out),len(out))
plt.plot(x_axis,out)
plt.show()
