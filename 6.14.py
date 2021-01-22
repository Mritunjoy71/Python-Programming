str = 'X-DSPAM-Confidence:0.8475'
index=str.find(':')
print(index)
floating=str.split(':')
num=float(floating[1])
print(num)