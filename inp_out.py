# value=input('Enter value:')
# print(type(value))
# print(value)

# value=int(input('Enter value:'))
# print(type(value))
# print(value)

# value=float(input('Enter value:'))
# print(type(value))
# print(value)

# value=complex(input('Enter value:'))
# print(type(value))
# print(value)

# value=bool(input('Enter value:'))
# print(type(value))
# print(value)

# user_list=list(input('Enter a list:'))
# print(type(user_list))
# print(user_list)

# user_list=eval(input('Enter a list:'))
# print(type(user_list))
# print(user_list)

# value=eval(input('enter any collection:'))
# print(type(value))
# print(value)

print('hey',sep='',end='\n')

print('hello',end='-')
print(10,20,sep='\n')
print('bye',end='+')

print()
print([12,4],sep='^',end='-')
print('python',sep='^',end='\n')
print((3,7),sep='#',end='\n-\n-')

print()
print('hello','buddy',sep='$$')
print('oops!',end='...')
print('bye')
print()
name = "Anil"
age = 22
print(f"Name: {name}, Age: {age}")  
print(f"Name: {name+'kumar'}, Age: {age+1}")  

print("Name: {}, Age: {}".format(name, age))  

print("Name: %s, Age: %d" % (name, age))

'''getting value of required decimal points'''
res=eval('17/3')
print(f"{res:.4f}")