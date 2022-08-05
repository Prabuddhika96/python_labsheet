#part 1
#rectangle
def Rectangle():
    length = float(input("Length of rectangle : "))
    width = float(input("Width of rectangle : "))

    print("Area of rectangle : ",length*width)
    print("Circumstance of rectangle : ",2*(length+width))

#Circle
def Circle():
    radius = float(input("\nRadius of circle : "))

    print("Area of circle : ",((22/7)*radius*radius))
    print("Circumstance of circle : ",(2*(22/7)*radius))

#Triangle
def Triangle():
    a = float(input('\nEnter first side: '))
    b = float(input('Enter second side: '))
    c = float(input('Enter third side: '))

    # calculate the semi-perimeter
    s = (a + b + c) / 2

    # calculate the area
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

    print("Area of triangle : ",area)
    print("Circumstance of triangle : ",(a+b+c))


#Parallelogram
def Parallelogram():
    base = float(input("\nBase of parallelogram : "))
    angle_width = float(input("Angle width of parallelogram : "))
    height = float(input("Height of parallelogram : "))

    print("Area of parallelogram : ",base*height)
    print("Circumstance of parallelogram : ",2*(base+angle_width))   

Rectangle()
Circle()
Triangle()
Parallelogram()

###################################################################################

#part 2
#factorial
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)


number = float(input("\nEnter number : "))
fac=factorial(number)
print("Factorial of ",number," is ",fac)

###################################################################################

#part 3
#fibbonaci
def fibbonaci(n):
    n1=0
    n2=1
    
    if n<=0:
        print("Enter positive number")
    elif n==1:
        print("Fibonacci sequence upto ",n," :")
        print(n1)
    else:
        count=0
        print("Fibonacci sequence :")

        while count<n:
            print(n1)
            next=n1+n2
            n1=n2
            n2=next
            count+=1


number = int(input("\nEnter number : "))
fibbonaci(number)

####################################################################################

#part4
#solving the quadratic equation
def solving_equation(a,b,c):
    delta=pow(((pow(b,2))-(4*a*c)),0.5)

    if isinstance(delta, complex):
        print("this equation have complex solutions")
    
    x1=((-b)+delta)/(2*a)
    x2=((-b)-delta)/(2*a)

    print("a={} b={} c={}".format(a,b,c),"\nsolutions are x=",x1," and x=",x2,"\n")


print("\n")
solving_equation(5,17,-10)
solving_equation(12,10,20)
solving_equation(1,5,6)


###################################################################################
#part 5
#calculating the distance between two points

def distance_between_two_points(x1,y1,x2,y2):
    x1=float(x1)
    x2=float(x2)
    y1=float(y1)
    y2=float(y2)
    a=pow(x1-x2,2)+pow(y1-y2,2)
    distance=pow(a,0.5)

    print("Distance between ({},{}) and ({},{}) is {}".format(x1,y1,x2,y2,distance))

    
x1,y1 = input("\nfirst point (x,y): ").split(",")
x2,y2 = input("second point (x,y): ").split(",")

distance_between_two_points(x1,y1,x2,y2)


###################################################################################
#part 6
def read_marks(file_name):
    file1 = open(file_name, 'r')
    Lines = file1.readlines()
      
    count = 0
    # Strips the newline character
    for line in Lines:
        Lines[count]=int(line[:-1])
        count+=1
        
    file1.close()
    return Lines



list=read_marks("mark_list.txt")
print("\nList\n",list)

#sorting
sorted_list=sorted(list)
print("\nSorted list\n",sorted_list)

###total,mean,median
def total(list):
    total=0
    
    for i in list:
        total+=i

    return total

print("\ntotal of list : {}".format(total(list)))

# Importing the statistics module
import statistics
mean= statistics.mean(list)
print("\nMean is ", mean)

median= statistics.median(list)
print("Median is ", median)

mode= statistics.mode(list)
print("Mode is ", mode)

#grading
def grading(list):
    for i in list:
        if i>=80:
            print("{} - Grade A".format(i))
        elif i>=60:
            print("{} - Grade B".format(i))
        elif i>=50:
            print("{} - Grade C".format(i))
        elif i>=30:
            print("{} - Grade D".format(i))
        else:
            print("{} - Grade F".format(i))
print("\n")
grading(list)




###################################################################################
#part 7
def word_counter(file_name):
    file=open(file_name,"r")

    read=file.read()
    
    import re
    #res = len(read.split())
    res=re.split(', | |-',read)

    print("\nWords in file : ",str(len(res)))
    file.close()



word_counter("words_file.txt")
