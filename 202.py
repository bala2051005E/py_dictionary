##a = [1,2,3]
##b = [2,4,6]
####print(a)
####print(b)
####print(type(a), type(b)) 
##
##print(a[2])
##print(b[2])
##
##print(a, "before")
##a[0] = 6
##a.append(9)
##print(a, "after")
##
##print(b, "before")
##a[2] = 12
##a.append(10)
##print(b, "after")

numbers= [1,2,3,4,5,6,7,8,9,10]

even = []
odd = []

for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even number:", even)
print("Odd number:", odd) 


##a = "Python programmer"
##print(a[-17::-1])
