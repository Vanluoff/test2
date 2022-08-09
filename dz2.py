D=109
v=int(input())
t=int(input())
S=int(v*t)
ost=0
if S<D:
	print(S)
else:
	ost=S%D
	print(ost)