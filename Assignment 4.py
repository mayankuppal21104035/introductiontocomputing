#Answer 1
print("Answer 1")
#Creating a recursive function
def Tower_Of_Hanoi(n,from_rod,to_rod,aux_rod):
    if n==1:
        print("Move Disk 1 from rod",from_rod,"to rod",to_rod)
        return
    Tower_Of_Hanoi(n-1,aux_rod,to_rod,from_rod)
    print("Move Disk",n,"from rod",from_rod,"to rod",to_rod)
    Tower_Of_Hanoi(n-1,aux_rod,to_rod,from_rod)
    
#Getting the number of disk input
n=int(input("Enter the number of disk:"))
#Getting the final output
Tower_Of_Hanoi(n,"A","B","C")   #A,B,C are the names of rods
print()


#Answer 2
print("Answer 2")
#Using Iteration
print("Using Iteration")
#Getting the number of rows input from the user
n=int(input("Enter the number of rows:"))
#using for loop
for i in range(0,n+1):
    for j in range(0,n-i+1):
        print(" ",end=" ")

    A=1
    for j in range(1,i+1):
        print(" ",A,end=" ")
#Getting the final output
        A=A*(i-j)//j
    print()
print()

#Using Recursion
print("Using Recursion")
#Creating the function
def triangle(n,original_length=n):
    if n==0:
        return
    triangle(n-1,original_length)

    print(" "*(original_length-n),end=" ")
    a=1
    for i in range(1,n+1):
        print(a,end=" ")

        a=a*(n-i)//i
    print() #Getting the final output
triangle(n)
print()

#Answer 3
print("Answer 3")
#Getting the input from the user
a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
#Getting the quotient and remainder of the numbers
c1=a//b #Quotient
c2=a%b #Remainder
#Creating a new list
list1=list()
list1.append(c1) #adding the values in the list
list1.append(c2)
#Getting the final output
print("The Quotient of the number is:",c1)
print("The Remainder of the number is:",c2)
print()

#Answer 3(a)
print("Answer 3(a)")
#Checking whether function is callable or not
a1=callable(list1)
#Applying the condition
if a1:
    print("Function is Callable")
else:
    print("Function is not Callable")
print()   

#Answer 3(b)
print("Answer 3(b)")
#Applying the condition
if c1==0:
    print("The Quotient is zero")
if c2==0:
    print("The Remainder is zero")
if(c1!=0 and c2!=0):
    print("All the values are non zero")
print()    

#Answer 3(c)
print("Answer 3(c)")
#applying the loop
for i in range(4,7):
    list1.append(i)   #adding (4,5,6) in the list
list2=list()
for i in list1:
    if i>4:           #getting the list of values greater than 4
        list2.append(i)
print("The list which contains number greater than 4 are",list2)
print()

#Answer 3(d)
print("Answer 3(d)")
#creating a new set
set1=set()
for i in list2:
    set1.add(i) #adding the values of list2 in the set
print(set1)
print()

#Answer 3(e)
print("Answer 3(e)")
#making the set immutable
frozenset(set1)
print("The above set has been converted to immutable")
print()

#Answer 3(f)
print("Answer 3(f)")
print("The max value from the above set is:",max(set1))
print()
      
#Answer 4
print("Answer 4")
#Creating a class
class Student:
    def __init__(self,student,roll_no):
        self.name = student
        self.roll_no = roll_no

    def __del__(self):
        print("Object Destroyed")

student1=Student("Mayank",21104035)
print("Object Created")

#Getting the final output
print("The name of the student is:",student1.name,"and SID is:",student1.roll_no)

del student1
print()

#Answer 5
print("Answer 5")
#Creating a class
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def __del__(self):
        print(f"Employee {self.name} record deleted")

#Creating the employee records 
employee_1=Employee("Mehak",40000)
employee_2=Employee("Ashok",50000)
employee_3=Employee("Viren",60000)

#Answer 5(a)
#updating the salary
employee_1.salary = 70000
print("(a) The updated salary of",employee_1.name,"is",employee_1.salary)

#Answer 5(b)
#Deleting a record
print("(b) Record of Viren deleted",end=" ")
del employee_3
print()

#Answer 6
print("Answer 6")
#Getting the input (player name)
player1=str(input("Enter Player_1 name:"))
player2=str(input("Enter Player_2 name:"))
print()
#Getting the input word from the players
word1=str(input("Enter the word:"))
word2=str(input("Enter a new  meaningful word to test your friendship:")) 
#creating a function for checking the length of the words
def count_in_dict(word):
    count={}
    list1=list(word1)

    n=len(list1)
#Applying the loop and condition
    for i in range(n):
        if list1[i] in count:
            count[list1[i]]+=1
        else:
            count[list1[i]]=1
    return count
def userinput():
    if count_in_dict(word1)!= count_in_dict(word2):
        print("The letters are not exact, friendship is fake")
        return
    a=str(input("Does the Word make sense?(Y or N)"))
#Applying the condition
    if a=="y" or a=="Y":
        print("The Friends pass the friendship test")
    elif a=="n" or a=="N":
        print("Friendship is fake, word doesn't have a meaning")
    else:
        print("Please Enter Valid Data(Y/N")
        userinput()
userinput()










