# Q14.Write a Python program to multiply all the items in a dictionary.


a={1:10,2:20,3:30,4:40}
m=1
m1=1
for i in a:
    m=m*a[i]
    m1=m1*i
print(m*m1)