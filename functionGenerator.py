import numpy as np
import matplotlib.pyplot as plt
#input function
selector = int(input("Enter type of waves: Gaussian (0), Sine(1), Cosine(2), Square(3): "))
t = 2*np.pi
x = np.linspace(0,t,5)
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
		x = np.linspace(0,t,1000000)
		square = sp.signal.square(2*np.pi*x)
		Tx = square
	else:
		Tx = 1

	print (Tx)

	plt.plot(np.linspace(0,t,5),Tx)
	plt.show()
	plt.close()
	check = input("is this the intended input wave? (Yes/No) ")

	if(check == "yes" or check == "Yes"):
		correct = False
	else:
		print("Please re-input the waves parameters.")
		correct = True

print("Proceeds to Channel with the following signal: ", Tx)
