print("Input string: Python is a case sensitive language")
#answer 1(a)
print("answer 1(a)")
#entering the input
a="Python is a case sensitive language"
#getting the length of the  string
print("The length of the input string is:",len(a))
print()

#answer 1(b)
print("answer 1(b)")
#reversing the order of the string
print("The reverse order of the input string is:",a[::-1])
print()

#answer 1(c)
print("answer 1(c)")
#slicing the input string
print(a[9:27])
print()

#answer 1(d)
print("answer 1(d)")
#replacing "a case sensitive" with "object oriented"
x=a.replace( "a case sensitive","object oriented")
#getting the final output
print(x)
print()

#answer 1(e)
print("answer 1(e)")
#getting the index of "a" in given string
y=a.index("a")
print("the index of a in input string is: ",y)
print()

#answer 1(f)
print("answer 1(f)")
#removing the white spaces from the string
c=a.replace(" ","")
#getting the final output
print("The final output is:",c)
print()

#answer 2
print("answer 2")
#storing the different values like name,SID,department name and CGPA 
a="Mayank"
b="21104035"
c="Electrical"
d="9.9"
#printing the different value in given format
print("Hey,",a,"Here!")
print("My SID is",b)
print("I am from",c,"Department and my CGPA is",d)
print()

#answer 3
print("answer 3")
#bitwise operator
#       32  16  8  4  2  1
#a=56   1   1   1  0  0  0
#b=10   0   0   1  0  1  0


a=56
b=10
#finding a&b
print("a&b is:",a&b)
#finding a|b
print("a|b is:",a|b)
#finding a^b
print("a^b is: ",a^b)
#shifting both a and b left with 2 bits
print("a<<2:",a<<2,"b<<2:",b<<2)
#shifting both a and b right with 2 bits and 4 bits
print("a>>2:",a>>2,"b>>4:",b>>4)
print()

#answer 4
print("answer 4")
#getting the input from the user
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
num3=float(input("Enter third number:"))
#getting the greatest of three  number entered by the user
if(num1 > num2) and (num1 > num3):
 greatest=num1
elif(num2 > num1) and (num2 > num3):
 greatest=num2
else:
 greatest=num3
#getting the final output
print("the greatest of three numbers entered by the user is:",greatest)
print()

#answer 5
print("answer 5")
#getting the input string from the user
x=input("Enter the string:")
#writing the word to be checked
y="name"
#checking whether the input string contains "name" in it or not
if y in x:
    print("Yes")
else:
    print("No")
print()

#answer 6
print("answer 6")
#entering the length of three sides of a triangle
a=int(input("enter the length of side 1:"))
b=int(input("enter the length of side 2:"))
c=int(input("enter the length of side 3:"))
print("the lengths of three sides of triangle are:",a,",",b,",",c)
#checking whether it can form a triangle or not
if (a+b > c) and (a+c > b) and (b+c > a):
    print("yes")
    print("It can form a triangle")
else:
    print("no")
    print("It will not form a triangle")
