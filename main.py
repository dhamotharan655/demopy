import datetime as dt
'''num=int(input("Enter the time : "))
for i in range(num):
    a=int(input("Enter First number : "))
    b=int(input("Enter Second number : "))
    print("First + Second = ",a+b)

for i in range(65,70,1):
    for j in range(65,70,1):
        print(chr(j),end="")
    print("")

a=[1,2,3,4,5]
print(a)
print(type(a))
print(a[1])
print(a[-1])
print(a[:3])
a.clear()
print(a)
a=[2,4,2,5,7,1]
b=a.copy()
print(b)
print(b.count(2))
print(b.index(7))
print(len(b))
print(max(b))
print(min(b))
print(b.pop(4))
print(b)
print(b.remove(5))
print(b)

name={"dhamu","nabil","godson"}
print(name)
name.add("sooriya")
print(name)

a={"blacky","jacky"}
a.update(name)
print(a)
a.remove("sooriya")
print(a)

num=int(input("Enter the Number : "))
res=0
for i in range(1,num):
    if num%i==0:
        res=res+i
if res==num:
    print(num," is a perfect number")
else:
    print("It is not a perfect number")

num=int(input("Enter the number : "))
tem=num
sum=0
while tem>0:
    factor = 1
    digit=tem%10
    print(digit)
    for i in range(1,digit+1):
        factor=factor*i
    print("Factor : ",factor)
    sum=sum+factor
    tem=tem//10
if sum==num:
    print(num," is a strong number")
else:
    print(num," it is not a strong number")

a={2,3,1,5,7}
b={3,2,1,9}
c=a.union(b)
print(c)
c=a.intersection(b)
print(c)

c=a.symmetric_difference(b)
print(c)

c=a.isdisjoint(b)
print(c)

#Dictionary

user={
    "name":"Dhamotharan",
    "age":22,
    "city":"Tuty"
}
print(user)
print(type(user))
print(user["city"])
for i in user:
    print(i," : ", user[i])

if "ae" in user:
    print("yes")
else:
    print("no")

user.update({"gender":"Male"})
print(user)
user["age"]=23
print(user)

current=dt.date.today()
print(current)
a=dt.time(10,45,45,555)
print(a)
ct=dt.datetime.now()
print(ct)
new=dt.datetime(2024,5,31,12,2,10,3444)
print(new)
print(new.date())

name='dhamotharan'
print(name[5:20])
print(len(name))

#List
num=[23,4,5,64,76]
print(num[2:])
print(num[-1])

#function
num.append(24)
print(num)
num.remove(5)
print(num)
num.insert(2,2)
print(num)
num.pop(1)
print(num)
#delete multiple value
del num[3:]
print(num)
#insert multiple value
num.extend([14,36])
print(num)

print(min(num))
print(max(num))
num.sort(reverse=True)
print(num)

#Tuple

tup=(2,4,2,6,7,9)
print(tup)
change=list(tup)
change.pop(2)
tup=tuple(change)
print(tup)
print(tup.index(9))
print(tup.count(4))

#Set

se={2,4,6,3,7,3}
print(se)
se[1]=3
print(se)

#Dictionary
data={
    'name':'dhamu',
    'age':22
      }
print(data.get('key'))
print(data.get('city',"Not Found"))
data=['dhamu','nabil','sooriya']
value=['developer','suppoter','testing']
dic=dict(zip(data,value))
print(dic)
dic['godson']='gov'
print(dic)
del dic['sooriya']
print(dic)
my={'godson':"hen",'dhamu':{'hen':'wood','pegion':'cement'},'nabil':['kanore','pegion']}
print(my['godson'])
print(my['nabil'])
print(my['nabil'][1])
print(my['dhamu']['hen'])
print(~45)

for i in range(5,1,-1):
    for j in range(i):
       print("*",end="")
    print("")

i=5
while i>=1:
    print("dhamu ",end="")
    j=5
    while j>=1:
        print("tharan ",end="")
        j-=1
    print(""
          "")
    i-=1

av=10
ch=int(input("Enter no of candy : "))
i=1
while i <=ch:
    if i>av:
        break;

    print("Candy")
    i+=1

print("we have", av," no of candy")'''

'''num=100
for i in range(1,num):
    if i%2!=0:
        pass;
    else:
        print(i)'''

'''num=[12,18,21]
for i in num:
    if i%5==0:
        print(i)
        break

else:
    print("Not found")'''

'''#Find Prime number

num=int(input("Enter the number : "))
for i in range(2,num):
    if(num%i==0):
        print("It is not a prime number")
        break
    i+=1

else:
    print(num," is a Prime Number ")'''

'''#Array

from array import *

vals=array('i',[2,4,7,4,-2])
newarray=array(vals.typecode,(a for a in vals))
#print(newarray)
#print(vals.buffer_info())

arr=array('i',[])
n=int(input("Enter the idex : "))
for i in range(0,n):
    value=int(input("Enter the value  : "))
    arr.append(value)

choice=input("Your want to search element say yes or no : ")
choice.lower()
if choice=="yes":
    search=int(input("Enter the Searching value : "))
    for j in range(0,n):
        if arr[j]==search:
            print("Element is founded idex in ",j)
            break
        else:
            pass

else:
    print("Thankyou")
from numpy import *
result=matrix('   ;   ;   ;')
m1=matrix('1,2,3; 6,7,5;1,6,7')
m2=matrix('1,2,3;6,8,5;2,6,7')
for i in range(len(m1)):
    for j in range(len(m2[0])):
        for k in range(len(m1)):
            result+=m1[i,k]*m2[k,j]

for i in range(len(m1)):
    for j in range(len(m2)):
        print(result[i,j])'''

'''#function
def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)

person('Dhamu',age=23,city='Tuty',no=7867848909)

#Global variable & Local variable

a=10
print(id(a))
def some():
    a=9
    x=globals()['a']
    print(id(x))
    print('inside the function ',a)
    globals()['a']=14
    print(id(globals()['a']))

some()'''

'''def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

lst=[22,54,12,98,43,90]
even,odd= count(lst)
print("Even no is {} ,Odd no is {}".format(even,odd))'''

#Name more then 5 Character in List
'''def count(name):
    more=0
    less=0
    for i in name:
        count=0
        for j in i:
            count+=1
        if count<5:
            less+=1
        else:
            more+=1
    return more,less

name=['dhamotharan','Sooriya','Godson','Nabil','Ruban','Mathesh',"Pall","Sam","Arun"]
more,less=count(name)
print("In the list more then 5 Character name count is {}, less then 5 name count is {}".format(more,less))'''


'''#Fibonacnni Series

def fib(x):
    a=0
    b=1
    if x==1:
        print(a)
    elif x<=0:
        print("Please enter positive number")
    else:
        print(a)
        print(b)
        for i in range(2,x):
            c=a+b
            a=b
            b=c
            if c<=100:
                print(c)
            else:
                print("Answer is above 100")
                break;


x=int(input("Enter the input : "))
fib(x)'''

'''
#factoril
def fact(num):
    result=1
    if num==0 or num<0:
        print("Factoril is not possible for 0 and Negative number")
    else:
        for i in range(1,num+1):
            result*=i
        return result


num=int(input("Enter the factoril number : "))
print(fact(num))'''

'''#Factoril Using Recursion
def fact(num):
    while num>0:
        if  num<0:
            print("recursion is not possible")
        elif num==1:
            return num
        else:
            return num*fact(num-1)

num=int(input("Enter the number : "))
result=fact(num)
print("Factoril of ",num,"is : ",result )'''

'''from functools import *
#Lambda Function
#Filter
num=[3,6,7,8,2,3,9]
even=list(filter(lambda n:n%2==0,num))
print("Filter : ",even)
#map
double=list(map(lambda n:n*2,even))
print("Map : ",double)
#reduce
sum=reduce(lambda a,b:a+b,num)
print('Reduce : ',sum)'''

'''def div(x,y):
    print(x/y)

def smart_div(fun):
    def inner(x,y):
        if x<y:
            x,y=y,x
        return fun(x,y)
    return inner

div=smart_div(div)
div(2,4)'''

'''from calc import add
def fun():
    add()
    print("main fun1")

def fun2():
    print("main fun2")

def main():
    fun()
    fun2()

print(__name__)
main()'''

'''class computer:

    def __init__(self,model,ram):
        print("Hello")
        self.model=model
        self.\
            ram=ram

    def display(self):
        print("Model",self.model,"Ram",self.ram)

comp1=computer("rayzan7",16)
computer.display(comp1)'''

'''class computer:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("Name : ",self.name," Age : ",self.age)

    def compare(self,other):
        if self.age==other.age:
            print("Both age are equal")
        else:
            print("Both age are different")


c1=computer("dhamu",22)
c2=computer("udhaiya",21)
c3=computer("mathesh",22)

c1.display()
c1.compare(c2)'''

# Methods
# Instance Method
# Class Method
# Static Method

'''class student:

    school="Popes"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        print((self.m1+self.m2+self.m3)/3)

    @classmethod
    def sch(cls):
        print(cls.school)

    @staticmethod
    def info():
        print("We are not use any object and class method")

s1=student(55,37,88)
s2=student(78,45,90)

s2.avg()
student.sch()
student.info()'''

#Inner Class

'''class student:

    def __init__(self,name,age,roll):
        self.name=name
        self.age=age
        self.roll=roll
        self.lap=self.laptop()

    def show(self):
        print("Name : ",self.name," Age : ",self.age," Rollno : ",self.roll)
        self.lap.show()

    class laptop:

        def __init__(self):
            self.brand="Lenova"
            self.version="Ryzen 7"
            self.ram=8

        def show(self):
            print("Lap Name : ",self.brand," Version : "," Ram : ",self.ram)

s1=student("dhamu",23,27)
s2=student("nabil",23,27)

lap=student.laptop()
s1.show()
s2.show()'''

#constructor in inheritance
#super key word
#Method Resolution Order

'''class a:
     def __init__(self):
         print("Class a constructor")

     def feature1(self):
         print("Feature1")

     def feature2(self):
         print("Feature2")

class b:
    def __init__(self):
        print("class b constructor")

    def feature4(self):
        print("Feature4 in b")

class c(a,b):
    def __init__(self):
        super().__init__()
        print("class c constructor")
        super().feature4()
    def feature4(self):
         print("Feature4 in c")


c=c()
c.feature4()'''

#Operator overloading
'''class operator:

    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __sub__(self, other):
        m1=self.m1-other.m1
        m2=self.m2-other.m2
        m3=operator(m1,m2)
        return m3
    def __gt__(self, other):
        m1=self.m1+self.m2
        m2=other.m1+other.m2
        m3=operator(m1,m2)
        if m1>m2:
            return True
        else:
            return False

    def __str__(self):
        return '{}, {}'.format(self.m1,self.m2)

s1=operator(4,65)
s2=operator(45,87)

s3=s1-s2
print(s3.m1)

if s1>s2:
    print("s1 is win")

else:
    print("s2 is win")

print(s1)'''

#Iteration
'''class iterator:
    def __init__(self):
        self.num=1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num+=1
            return val

        else:
            raise StopIteration

value=iterator()
for i in value:
    print(i)'''


#Generator

'''def topten():
    n=1
    while n<=10:
        sq=n*n
        n+=1
        yield sq

value=topten()
print(type(value))
for i in value:
    print(i)'''

#Execption Handling

'''def exe():
    a=5
    b=2
    try:
        c=a/b
        k=int(input("Enter the number : "))
        return c
    except ZeroDivisionError as e:
        print("0 is not divided",e)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)

print(exe())'''

'''from threading import *
from time import *

class hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)


class hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


t1=hello()
t2=hi()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()
print("Bye")'''

#Linear Search
'''pos=0
def search(arr,num):
    i=0
    while i<len(arr):
       if arr[i]==num:
           globals()['pos']=i
           return True
       i+=1
arr=[5,8,4,6,9,2]
num=int(input("Enter Search value : "))
if search(arr,num):
    print("Found at ",pos)

else:
    print("Not Found")'''

#Binary Search
'''pos=0
def search(lis,num):
    s = 0
    l = len(lis)-1

    while s <= l:
        mid = s+l//2
        if lis[mid] == num:
            globals()['pos'] = mid+1
            return True
        else:
            if lis[mid] > num:
                l = mid-1
            else:
                s = mid+1
    return False

list = [4,7,8,12,45,99]
num=int(input("Enter the search element : "))
if search(list,num):
    print("Found at ",pos)
else:
    print("Not found")'''

#bubble short

'''def sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
           if list[j]>list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp

    print(list)

list=[7,3,9,1,5,0]
print(sorted(list))
sort(list)'''

























