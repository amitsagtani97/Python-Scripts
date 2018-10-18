import sys
try:
    input = raw_input
except NameError:
    pass
def password(k,pwd):
	if pwd=="M":
		while k>68:
			k=k-68
		return k
	else:
		while k>61:
			k=k-61
		return k
from numpy import random
from datetime import *
now=datetime.now()
d=now.day
m=now.month
y=now.year
h=now.hour
mi=now.minute
s=now.second
date=str(d)+'/'+str(m)+'/'+str(y)+' '+str(h)+':'+str(mi)+':'+str(s)
print(date)
name=input("Enter the name of site : ")
n=int(input("Enter the lenth of password : "))
r=range(n)
mix="Qz@Aa#Zq$Xw%Ss&W*x1E2cD3dC4eV5rF6fR7vT8bG9gB0tNyHhYnUmJjMuKiIkOlLoPp"
alpha="ZqAaQzW1x3S2s5X4wCe6D8d9EcR7vFfVrBtGgTbYnHhNyMuJjUmIkKiLlOoPp"
A=len(alpha)
M=len(mix)
bk=" "
s=[]
p=" "
ch=input("Enter A for only alphanumeric password \n Enter M for AlphaNumeric and special charector password :  ")
for i in r:
	a=random.rand(1)
	c=a*100
	b=int(c)
	g=password(b,ch)
	if ch=="A":
		h=alpha[g]
		s.append(h)
		
	else:
		h=mix[g]
		s.append(h)
	bk=bk+h
print(bk)
j=0
for i in s:
	j=j+1
	if i.islower():
		p=p+str(j)+"/"
print(p)	

		     
f=open("password.txt","a+")
f.write(date+'    '+name+'    '+p+'    '+bk+"\n\n")
f.close
