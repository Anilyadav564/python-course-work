#operators 
#Operators are symbols that 
# tell Python to do something
# with values—like math signs
#math operators are:
'''a =10
b =20
print(a+b)#add
print(a-b)#subtract
print(a*b)#multiply
print(a/b)#divide
print(a//b)#remainder left over
print(a**b)#power'''
#Comparison operators
'''These ask questions and answer 
with True or False.'''
'''a = 20
b = 10

print(a > b)   # True
print(a < b)   # False
print(a == b)  # False: are they equal?
print(a != b)   True: are they different?'''
#important
'''a =20
b =30
a =  b     # puts b's value into a
a == b    # asks whether a and b are equal
print(a,b)
a = b
print(a)
a == b
print(a)'''

#Assignment operators
'''c = 10
c += 5   # same as c = c + 5; now c is 15
c *= 2   # same as c = c * 2; now c is 30
c -= 10 ''' # same as c = c - 10; now c is 20

#Logical operators
'''#They join questions together.
#(AND)# True: both are true else false
a = True
b = False
print(a and b)
#OR# True: at least one is true
print(a or b)
#ex
n = 10

n % 2 == 0 and n % 5 == 0  # True: both are true
n % 2 == 0 or n % 3 == 0   # True: at least one is true
not n < 5 
# True: reverses False to True'''

# membership operators
#in operator#
'''mainly used  in str ,list,tuple,dict checking is present or not
print("i" in "anil")       # True
print(1 in [1, 2, 3])      # True
print(4 in (1, 2, 3))      # False
'''
# is operator
#used to check  object reference is same or not

'''l = [1,2,3,4,]
m = [1,2,3,4]
print(id(l))
print(id(m))
print(l is m)
n = l
print(id(n))
print(l is n)'''
#Bitwise operators using 0,1 bits 
# if 0and 1=0 and 1and1= 1 but in 0 or 0 = 0 and 1 or 0= 1
#And operation
'''AND: &
Only gives 1 when both places have 1.
print(9 & 10)  # 8'''
'''9 = 1001
 10 = 1010
------------
&    1000 = 8'''
# or operation
#Gives 1 if either number has 1.
print(9 | 10)   # AND → 11

'''9 = 1001
 10 = 1010
------------
|    1011 = 11'''

#XOR: ^
#XOR means “different.” It gives 1 only when the two bits are different.
'''like 0,0 =0
     1,1,0
     but
     0,1 = 1
     1,0 = 1'''
print(9 ^ 10)   # XOR → 3
'''9 = 1001
 10 = 1010
------------
|    1011 = 11'''
# shifts

#left
'''Left shift: <<
Moves the bits to the left. Add zeros on the right'''
'''print(8 << 2)'''   # Left shift → 32

'''8 = 1000

8 << 2

1000 → 100000 = 32'''

#right
'''Right shift: >>
Moves the bits to the right. The bits falling off disappear.
'''
'''print(8 >> 2)'''   # Right shift → 2

'''8 = 1000

8 >> 2

1000 → 10 = 2'''
## output formating##
'''think of print() as Python’s way of speaking to
us on the screen'''

a = 10
b = 10.3
c = "anilyadav" # we have int float str

# print(a b c) get errors because we have int str float not directlu print so we use
#for diff data types comma seperation


# 1)The commas tell Python to print each item with a space between them.
print(a,b,c)

# 2)(i) sep
'''sep — what goes between items
sep means separator.'''
print(a, b, c, sep="")# removing spacess bettween them
#No space because the separator is empty.

#2)(ii)
print(a, b, c, sep="\n")
#\n means “go to the next line.”
 
 #2)(iii)
print(a, b, c, sep="\t")
#\t means a big tab space.

#3)end — what happens after printing
#Usually, print() ends by moving to a new line.
print(a, b, c, end="@")
#Instead of moving to the next line, it puts @.

#)4Best beginner style: f-strings
print(f"a={a},b={b},c={c}")
'''Anything inside { } is replaced by its value. This is the easiest and most 
common modern way to format output.'''

#4)(1)
print(f"Student: {c}; marks: {a}")


#5)Showing only 2 decimal places
print(f"b = {b:.2f}")
#.2f means “show a decimal number with two digits after the dot.”