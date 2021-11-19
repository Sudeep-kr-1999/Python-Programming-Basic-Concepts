# vvi here x is of "generator class"........!!!!!!!!!!
# Furthermore, the generator object can be iterated only once. ... This is because a for loop takes an iterator and iterates over it using next() function. It automatically ends when StopIteration is raised. Check here to know how a for loop is actually implemented in Python.
x=(i for i in range(3))
print(type(x))
for i in x:
        print(i)

for i in x:
        print(i)
