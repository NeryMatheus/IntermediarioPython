x = [1,2,3,4,5]
y = [i**2 for i in x] #List Comprehension
z = [i for i in x if i%2 == 1]
"""
for i in x:
	y.append(i**2)
"""

print(x)
print(y)
print(z)

