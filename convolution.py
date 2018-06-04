import numpy as np
import matplotlib.pyplot as plt
n1 = int(input('length of s1: '))
n2 = int(input('length of s2: '))
s1 = []
s2 = []

for i in range(n1):
	i1 = input('enter input signal: ')
	s1.append(int(i1))

for i in range(n2):
	i2 = input('enter response signal: ')
	s2.append(int(i2))


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

print(out)
