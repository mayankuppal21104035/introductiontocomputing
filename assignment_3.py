#Answer 1
print("Answer 1")
#getting the input string from the user
s=str(input("Enter the string:"))
#getting the input word of which occurrence is to be find
w=str(input("Enter the word of which you want to find the number of occurrence:"))
#splitting the input string and creating their list
count=0
a=list()
a=s.split()
#applying the condition
for i in range(0,len(a)):
    if w==a[i]:
        count+=1
    
#getting the final output
print("The Number of Occurrence of",w,"is:",count)
print()


#Answer 2
print("Answer 2")
#creating a function of year
def leapyear(y:int)->bool:
    if(y%400==0)and(y%100!=0)and(y%4==0):
        return True
    else:
        return False
while True:
#getting the input from the user
    y=int(input("Enter the year:"))
    m=int(input("Enter the month:"))
    d=int(input("Enter the day:"))
    #applying the condition for different posibilities
    if(d<1)or(d>31)or(m<1)or(m>12)or(y<1800)or(y>2025):
        print("Error Occurred \n Please Enter valid data")
        continue
    if m in (4,6,9,11)and d==31:
        print("This month has only 30 days\n    Please enter valid data")
        continue
    elif m==2 and d>=29:
        if leapyear(y) and d!=29:
            print("This month has only 29 days")
            continue
        elif not leapyear(y):
            print("this month has only 28 days")
            continue
    break
if m==2:
    if leapyear(y):
        m_length=29
    else:
         m_length=28
elif m in(4,6,9,11):
    m_length=30
else:
    m_length=31
if d==m_length:
    d=1
    if m==12:
        m=1
        y+=1
    else:
        m+=1
else:
    d+=1
#getting the final output
print("Next Date is:",d,"-",m,"-",y)
print()


#Answer 3
print("Answer 3")
#creating a list
list1=[]
#getting the input from the user for numner of elements in list
n=int(input("Enter the number of elements you want to add in the list:"))
#applying the condition 
for i in range(0,n):
    a=int(input("Enter the element:"))
    list1.append(a)
print("The first list is:",list1)
list2=[]
for i in range(0,n):
    list2.append(list1[i]**2)
#getting the final output
print(list(zip(list1,list2)))
print()

    
#Answer 4
print("Answer 4")
#getting the grade points from the user
gp=int(input("Enter your Grade points:"))
#creating a dictionary for different grades and performance
a={4:"Your Grade is D and Poor Performance",
   5:"Your Grade is C and Below Average Performance",
   6:"Your Grade is C+ and Average Performance",
   7:"Your Grade is B and Good Performance",
   8:"Your Grade is B+ and Very Good Performance",
   9:"Your Grade is A and Excellent Performance",
   10:"Your Grade is A+ and Outstanding Performance"}
#applying the condition for grade points between [4-10]
if 4<=gp<=10:
    b=a.get(gp)
    #getting the final output
    print(b)
else:
    print("Error Occurred")
    print("Please enter grade points between (4-10)")
print()

    
#Answer 5
print("Answer 5")
#writing te string
a="ABCDEFGHIJK"
b=11
#applying the while loop
while b>0:
#getting the final output
    print(" "*int((11-b)/2),a[0:b])
    b=b-2
print()


#Answer 6
print("Answer 6")
#initializing the string
a="Y"
#creating two new empty dictionaries
dict1={}
dict2={}
#Applying the loop
while(a=="y")or(a=="Y"):
#getting the input from the user
       n=str(input("Enter the name:"))
       sid=int(input("Enter the Sid:"))
       b=str(input("Enter Y to continue and N to stop:"))
       dict1.update({sid:n})
       dict2.update({n:sid})
#applying the condition to stop
       if(b=="N")or(b=="n"):
              break
print()

#Answer 6(a)
print("Answer 6(a)")
#getting the final output
print("The Student Details are:",dict1)
print()

#Answer 6(b)
print("Answer 6(b)")
#sorting the dictionary using name
dict4= {sid:n for sid,n in sorted(dict2.items())}
print("Dictionary that is sorted using Students name is:",dict4)
print()

#answer 6(c)
print("answer 6(c)")
#sorting the dictionary using sid
dict3={sid:n for sid,n in sorted(dict1.items())}
print("Dictionary that is sorted using SID is:",dict3)
print()

#Answer 6(d)
print("Answer 6(d)")
#getting the input(SID) from the user
s=int(input("Enter the SID:"))
#getting the name from the Sid
n=str(dict1.get(s))
#getting the final output
print("Name of the Student with SID",s,"is:",n)
print()

#Answer 7
print("Answer 7")
#Using Recursion
def Fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
n=int(input("Enter the number:"))
print(Fibonacci(n))


#Answer 8(a)
print("Answer 8(a)")
#writing all the sets
s1={1,2,3,4,5}
s2={2,4,6,8}
s3={1,5,9,13,17}
#getting the new set which contains element of s1 and s2 but not in both
c=(s1|s2)-(s1&s2)
#getting the final output
print("New set of elements that are in set1 and set2 but not in both is:",c)
print()

#Answer 8(b)
print("Answer 8(b)")
#getting the new set which contains elements which are present only in one of the set
c=s1^s2^s3
#getting the final output
print("New set which contains elements which are only in one of the three sets is:",c)
print()

#Answer 8(c)
print("Answer 8(c)")
#getting the intersection of the sets
s6=(s1|s2|s3)-(s1^s2^s3)-(s1&s2&s3)
#getting the final output
print("New sets of elements that are exactly two of the sets among the three sets is:",s6)
print()

#Answer 8(d)
print("Answer 8(d)")
#creating a set
s4=set()
#adding numbers in it from 1-10
for i in range(1,11):
    s4.add(i)
#getting the new set of elements which are present in s4 but not in s1
s5=s4-s1
print("New set of all integers in the range(1-10) that are not in set1 is:",s5)
print()

#Answer 8(e)
print("Answer 8(e)")
#creating a set
s6=set()
for i in range(1,11):
    s6.add(i)
#getting the new set of elements which are present in s6 but not in s1,s2,s3
s7=s6-s1-s2-s3
print("New seet of all integers in the range(1-10)that are not in set1,set2 and set3 is:",s7)
print()




























