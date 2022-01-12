

#answer 1
#enter the three numbers
print('ANSWER 1')
i=input('enter number 1: ');
j=input('enter number 2: ');
k=input('enter number 3: ');
#finding the average of these numbers
avg=(int(i)+int(j)+int(k))/3
#final answer
print('the average of these numbers is: '+str(avg))

print()


#answer 2
print('ANSWER 2')
#getting input from the user 
i=input('enter your gross income: ')
l=input('enter number of decendents: ')

#gross income 
ti=int(i)-10000-(3000*int(l))
#finding the tax
tax=ti*1/5
#getting the final tax
print('Tax is: ',tax)


print()

#answer 3
print('ANSWER 3')
#getting input from student
sid=int(input('enter your SID: '))
a=input('enter your name: ')
b=input('enter your gender(F/M/U): ')
cn=input('enter your coursename: ')
cg=float(input('enter your CGPA: '))
#forming the list
student=[sid,a,b,cn,cg]
#final answer
print('Student:',student)

print()

#answer 4
print('ANSWER 4')
#getting the marks of students
s1=int(input('enter the marks of 1st student:'))
s2=int(input('enter the marks of 2nd student:'))
s3=int(input('enter the marks of 3rd student:'))
s4=int(input('enter the marks of 4th student:'))
s5=int(input('enter the marks of 5th student:'))
#getting it in the form of  list
list=[s1,s2,s3,s4,s5]
#final answer
print('Marks of 5 students are:',list)

print()

#answer 5(a)
print('ANSWER 5(a)')
#writing all the colors
color=['Red','Green','White','Black','Pink','Yellow']
#removing the 4th element
color.remove('Black')
#getting the final output
print(color)


#answer 5(b)
print('ANSWER 5(b)')
#removing 'Black' and 'Pink' and getting purple
color[3:5]={'Purple'}
#final output
print(color)
