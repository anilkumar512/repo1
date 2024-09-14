'''Arithmetic Operators(+,-,*,/,//,%,**)'''
''' + operator'''
num1=36.0
num2=4
result=num1+num2
print(result)  #40.0

word1='good'
word2='morning'
result=word1+' '+word2   #string concatenation
print(result)  #good morning

list1=[32,2,13,12]
list2=[54,23,32,9]
result=list1+list2       #list concatenation
print(result)  #[32, 2, 13, 12, 54,23,32,9]

''' - opeator'''
num1=16.0
num2=4
result=num1-num2
print(result)  #12.0

setA={23,22,43,11}
setB={54,22,4,25}
result=setA-setB  #set difference
print(result)  #{23, 43, 11}
'''* operator'''
num1=46.0
num2=5
result=num1*num2
print(result)  #230.0

word='luck'
result=word*5
print(result)  #fuckfuckfuckfuckfuck

'''/ operator'''
num1=56
num2=8.0
result=num1/num2
print(result)  #7.0

num1=64.0
num2=8.2
result=num1/num2
print(result)  #7.0

'''// operator'''
num1=56
num2=6
result=num1//num2
print(result)  #9

num1=78
num2=96.0
result=num1//num2
print(result)  #0.0

'''% operator'''
num1=55
num2=8.7
result=num1%num2
print(result)  #7.0

num1=55
num2=87
result=num1%num2
print(result)  #55

'''** operator'''
num1=15
num2=3
result=num1**num2
print(result)

'''Assignment operators'''
'''+= operator - it performs addition and concatenation based on operands and stores the result in same variable'''
num1=56.4
num1+=3.6
print(num1)

str1='hey'
str1+='huu'
print(str1)

list1=[24,5,34]
list1+=[55,66]
print(list1)

# set1={23,53,34}
# set1+={53,23,68}      TypeError: unsupported operand type(s) for +=: 'set' and 'set'
# print(set1)     

# dict1={'a':4,'b':6}
# dict1+={'c':6}                   #TypeError: unsupported operand type(s) for +=: 'dict' and 'int'
# print(dict1)   


'''-= - it performs substraction and set difference based on operands and stores the result in same variable'''
num1=76.4
num1-=6.6
print(num1)

set1={23,53,34}
set1-={53,23,68}
print(set1)

'''*= - it performs multiplication and creates duplicate elements based on operands and stores the result in same variable'''
num1=6.4
num1+=3.2
print(num1)

str1='fuck'
str1*=5
print(str1)

list1=[12,4,6]
list1*=4
print(list1)

tuple1=(2,4,6)
tuple1*3
print(tuple1)

# set1={3,5,7}
# set1*=2        TypeError: unsupported operand type(s) for *=: 'set' and 'int'
# print(set1)

# dict1={'a':4,'b':6}
# dict1*=2                   TypeError: unsupported operand type(s) for *=: 'dict' and 'int'
# print(dict1) 

'''/= operator - it performs true division operation on integer/float operands and stores the result in same variable'''
num1=15
num1/=3
print(num1)

num1=34.4
num1/=2
print(num1)

'''//= - it performs floor division operation on the operands and stores the result in same variable'''
num1=35
num1//=4
print(num1)

num1=35
num1//=4.2
print(num1)

'''%= operator - it stores remainder in same variable after performing division operation '''
num1=38
num1%=4
print(num1)

num1=25.4
num1%=4
print(num1)

'''**= operator - it finds power of a number stores result in same variable'''
num1=2
num1**=10
print(num1)

'''Comparision Operators'''
'''== operator - it used to check if two values are exactly same, if so it returns true otherwise false'''
print(100==100.0)
print(True==1.0)
print('hunt'=='hunt')
print([10,20]==[10.0,20])
print((30,50)==(50,30))     #checks based on index positions
print({3,5,7}=={7,3,5})     #checks if same elements present or not in both sets
print({'a':5,'t':8}=={'t':8.0,'a':5.0}) #checks based on keys


'''!= operator - it used to check if two values are different,if so it returns true otherwise false'''
print(40!=100)
print(True!=0.0)
print('Hunt'!='hunt')
print([False,1.0]!=[0.0,True])
print((30,50)!=(50,30))     
print({3,False}!={False,3.0})     
print({'a':5,'t':8}!={'p':8.0,'a':5.0}) 
print([1]!={True})

'''> operator - it used to check one value greater than other, if so it reurns true otherwise false'''
print(120>100)
print(True>False)
print('hunttt'>'hunt')
print([50,3,6]>[10.0,20,30])  
print([20,40,60]>[20,40]) 
# First elements: 50 (from the first list) is compared with 10.0 (from the second list). 
# Since 50 > 10.0, the comparison is True.
# Since the first comparison is True, Python doesn't need to compare the other elements. 
# It concludes that the first list is greater than the second list.
#output will be true
# In Python, when comparing two lists, the comparison is done element by element.
# As soon as Python can determine that one list is greater or smaller based on the first differing pair of elements, it stops and returns the result.
# When lists are compared, they are evaluated element by element.
# If all compared elements are equal and one list is shorter, the shorter list is considered "less than" the longer one.

print((10,20,4)>(50,30)) 
print((10,20,30)>(10,20))
# First elements: 10 (from the first tuple) is compared with 50 (from the second tuple). 
# Since 10 < 50, the comparison is False.
# Since the first comparison is False, Python doesn't need to compare the other elements. It concludes that the first tuple is not greater than the second tuple.
# Thus, the output of this expression will be False.
# In Python, when comparing two tuples, the comparison is done element by element.
# As soon as Python can determine that one tuple is greater or smaller based on the first differing pair of elements, it stops and returns the result.    
# In Python, when comparing tuples, if the tuples are of different lengths and the elements compared so far are equal, 
# the shorter tuple is considered "less than" the longer one.


print({6,8,5,3,9,7}>{7,3,5})     
# print({'a':5,'t':8,'s':4}>{'t':8.0,'a':5.0}) '>' not supported between instances of 'dict' and 'dict'
# print([34]>{23}) TypeError: '>' not supported between instances of 'list' and 'set'

'''>= operator - it used to check one value greater than or equal to other, if so it returns true otherwise false'''
print(120>=110)
print(True>=1)
print('hunttt'>='hunt')
print([10,20,30.0]>=[10.0,20])
print((30,50)>=(50,30))     
print({3,5,7,9}>={3,5,9})     
# The >= operator in Python checks if set1 is either a superset or equal to set2.

# print({'a':5,'t':8,'s':4}>={'t':8.0,'a':5.0}) '>' not supported between instances of 'dict' and 'dict'
# print([34]>={23}) TypeError: '>' not supported between instances of 'list' and 'set'

'''< operator - it used to check one value less than other, if so it reurns true otherwise false'''
print(12<100)
print(False<True)
print('huntt'<'hunttt')
print([10,20,30.0]<[10.0,20,30.0,40.0])
print((30,50)<(30,50,40))     
print({3,5,7}<{7,3,5,9,4})  
# The < operator checks if set1 is a proper subset of set2

# print({'a':5,'t':8}<{'t':8.0,'a':5.0,'s':4}) '<' not supported between instances of 'dict' and 'dict'
# print([35]<{55}) TypeError: '<' not supported between instances of 'list' and 'set'

'''<= operator - it used to check one value less than or equal to other, if so it reurns true otherwise false'''
print(10<=100)
print(True<=False+1)
print('hunttt'<='hunttt')
print([10,20,30.0]<=[10.0,20,30.0,40.0])
print((30,50)<=(30,50,60))     
print({3,5}<={7,3,5,9})  
# The >= operator in Python checks if set1 is either a subset or equal to set2.

# print({'a':5,'t':8}<={'t':8.0,'a':5.0}) '<=' not supported between instances of 'dict' and 'dict'
# print([34]<={34.0}) TypeError: '<=' not supported between instances of 'list' and 'set'

'''LOGICAL OPERATORS'''

'''and - It returns true when both condtions are true
it checks for False 
In case of values it searches for Default value(0,0.0,0j,False,'',[],(),set(),{}),
if default value is found it is returned else not found it returns last scanned value
'''
print(10>5 and 20>10)
print(1 and 0 and 1.0)
print([] and '')
print(20 and '' and 0)
print(10 and 'a' and {})

'''or - It returns true when if atleast one condtion is true
it checks for True 
In case of values it searches for Non-Default value( otherthan this 0,0.0,0j,False,'',[],(),set(),{}),
if non-default value is found it is returned else not found it returns last scanned value
'''
print(10<5 or 20>10)
print(10.0 or False or True)
print({10,False}!={0,10.0} or 'a')
print('hello' or [10,20] or False)
print('' or [] or () or set() or {})

print(10>-5 and "" or set() or 15)

'''not - returns true if condition is false,returns false if condition is true'''
print(not not False)
print(not(20>30))
print(not(20 and '' and 0))
print(not(''))

'''BITWISE OPERATORS(&,|,^,~,<<,>>)
the oprands are converted into binary format and bit by bit operation is performed based on operator
'''

'''Bitwise and(&) - if both bits are 1 it returns 1 else 0 for any remaining pairs'''
print(16 & 16)
print(120 & 17)
print(26 & 81)

'''Bitwise or(|) - if any one bit is 1 it returns 1 else if both bits are 0 it returns 0'''
print(15 | 15)
print(180 | 17)
print(77 | 8)

'''Bitwise not(~)- performs negation of number
~op=-(op+1)
'''
print(~43)
print(~-32)
print(~232)

'''Bitwise xor(^) it returns 1 if both bits are different else 0 '''
print(16 ^ 16)
print(120 ^ 17)
print(26 ^ 81)

'''Bitwise left shift(<<) - after converting to binary format, number of zeroes are added at the end which is equal to second operand
a<<n = a*2**n
'''
print(34<<3)
print(154<<4)
print(90<<6)

'''Bitwise right shift(>>) - after converting to binary format, number of bits are cancelled from RHS which is equal to second operand
a>>n = a/2**n
'''
print(34>>3)
print(154>>4)
print(90>>6)

'''Special Operators'''
'''Identity Operators(is , is not)'''
'''is operator
checks for value along with data type address, if everything matches it returns true
is operators is similar to '==' but '==' checks for only value where as is checks for value,datatype,address
'''
'''Immutable datatype only have same addresses for same values
Mutable datatype has different addresses for same values

'''
list1=[10,20,30]
list2=[10,20,30]
print(id(list1))
print(id(list2))
print(list1 is list2)

tuple1=(10,20,30)
tuple2=(10,20,30)
print(id(tuple1))
print(id(tuple2))
print(tuple1 is tuple2)
print({3,5,7} is {5,3.0,7}) 
print({'s':5,'g':6} is {'g':6,'s':5})
print('bloody' is 'bloody')
print(10 is 10.0)
print(True is 1)

'''is not operator
it returns true if value or data type or address are different
e
is not operators is similar to '!=' but '!=' checks for only value where as is not checks for value,datatype,address
'''
print(30 is not 30.0)
print('python' is not 'java')
print([10,20] is not [10.0,20.0])
print((10,20) is not (10,20))

'''Membership operators(in, not in)'''
'''in operator
checks if element or substring present in a collection if present it returns true otherwise false
'''
print('possible' in 'impossible')
print(2 in [3,2,4,6])
print([4,5] in [8,'a',9,[4,5]])
print(4 in (5,3,4))
# print(10 in 1000)  TypeError: argument of type 'int' is not iterable
print('10' in '1000')
print(True in {2,1.0,6})
print('name' in {'name':'ani','age':23})

'''not in operator
gives true if value is not present in a collection
'''
print('god' not in 'goddess')
print([10,40] not in [10,40,50])
print({10,20} not in [10.0,False,{10,20}])
print('email' not in {'name':'ani','age':23})




















