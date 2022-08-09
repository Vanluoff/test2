x1=int(input())
y1=int(input())
z1=int(input())
if x1==y1 and y1==z1:
	print(3)
elif (x1==y1 and x1!=z1):
	print(2)
elif (x1==z1 and z1!=y1):
	print(2)
elif (y1==z1 and y1!=x1):
	print(2)
elif (y1!=z1 and y1!=x1):
	print(0)