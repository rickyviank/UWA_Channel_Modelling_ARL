import scipy.signal
import numpy as np
import matplotlib.pyplot as plt
#input function
selector = int(input("Enter type of waves: Gaussian (0), Sine(1), Cosine(2), Square(3) (running for 10 seconds): "))
samplefreq = float(10**3) #Hz
x = np.linspace(0,0.05,(0.05*samplefreq),endpoint = False)
correct = True
while(correct == True):
	if selector == 0:
		#fc,bw = map(float,input("input parameters for the gaussian curve (center frequency, fractional bandwith): ").split())
		#u,q,gaussian = scipy.signal.gausspulse(x,fc,bw,bwr=-1,retquad = True,retenv = True)
		a,b,c = map(float,input("input parameters for the gaussian curve (scalar, mean, variacne):").split())
		gaussian = a*np.exp(-((x-b)**2)/2*c**2)
		Txx = gaussian
	elif selector==1:
		a,b,c = map(float,input("input parameters for the sine curve(amplitude, frequency(Hz), phase): ").split())
		sine = a*np.sin(x*b-c)
		Txx = sine
	elif selector==2:
		a,b,c = map(float,input("input parameters for the cosine curve (amplitude, frequency(Hz), phase): ").split()) 
		cosine = a*np.cos(x*b-c)
		Tx = cosine
	elif selector==3:
		t = float(input("Time taken for square wave(s): "))
		x = np.linspace(0,t,1000000)
		square = scipy.signal.square(2*np.pi*x)
		Txx = square
	else:
		Txx = 1

	print (len(Txx), "piece of data.")

	plt.plot(x,Txx)#,"--",x,q,x,u)
	plt.xlabel('time (s)')
	plt.ylabel('amplitude')
	plt.show()
	plt.close()
	check = input("is this the intended input wave? (Yes/No) ")

	if(check == "yes" or check == "Yes"):
		correct = False
	else:
		print("Please re-input the waves parameters.")
		correct = True

print("Proceeds to Channel with the following signal: ", Txx)
