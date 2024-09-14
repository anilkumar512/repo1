'''Dictionary - collection of key-value pairs where key and values seperated by colon(:) , each key-value pair seperated by commas(,) and everhything enclosed with in flower-brackets({}).
Mutable.
Ordered Collection.
values can be duplicated but keys should be unique.
values can be any datatype but keys should be immutable datatype i.e string,tuple,integer,float,boolean,complex.
It doesn't support indexing and slicing.

'''
#Default Value of Dictionary
dictionary={}
print(type(dictionary))
print(dictionary)

# data={['a']:9} TypeError: unhashable type: 'list' then key can't be list coz it is mutable
data={('a'):7}  #Key can be tuple
# data={{'a'}:7}   TypeError: unhashable type: 'set'  then key can't be set coz it is mutable
# data={{'a':7}:43}  TypeError: unhashable type: 'dict' then key can't be dictionary coz it is mutable
data={'a':4,'a':8}
print(data) #if duplicate keys are given, it stores only last key and value deletes other duplicate keys

#Value can be of any datatype
data={'info1':'name','info2':[3,8,9],'info3':(9,23,65),'info4':{53,42,53,22,44},'info5':{'a':12.4,'b':('huu','hii','hoo'),'c':4+2j}}
print(type(data))
print(data)
print(data['info2'])
print(data['info1'][-2])
print(data['info2'][2])
print(data['info3'][1])
# print(data['info4'][1])  TypeError: 'set' object is not subscriptable 
print(data['info5'])
print(data['info5']['b'])
print(data['info5']['b'][1][1])
# print(data['info6'])  KeyError: 'info6'
data['info6']={(4.6,3),'wowww'}
print(data)

car1={'name':'mercedes-benz','price':'1.11 crore','engine':'1991 cc','colors_avail':5}
print(car1['name'])

'''copy()- takes no arg,returns shallow copy of dictionary'''
car_copy=car1.copy()
print(car_copy)

'''clear()- takes no arg, removes all key-value pairs from dict,returns NONE'''
car_copy.clear()
print(car_copy)

'''keys()- takes no arg, returns a list of keys present in dict'''
result=car1.keys()
print(result)
'''values()- takes no arg, returns a list of values present in dict'''
result=car1.values()
print(result)

'''items()- takes no arg,returns list of tuples of key and values as its elements '''
result=car1.items()
print(result)

'''get()- takes key as arg,returns the value of that key, if key is not present returns NONE'''
result=car1.get('engine')
print(result)
print(car1.get('safety'))

'''pop()- takes key as arguement, returns value of that key and removes the key-value pair from the dict'''
result=car1.pop('price')
print(result)
print(car1)
# result=car1.pop() TypeError: pop expected at least 1 argument, got 0
# result=car1.pop('speed') KeyError: 'speed' if key is not present

'''popitem()- takes no arg,returns last key-value pair in form of tuple and removes it from the dict'''
result=car1.popitem()
print(result)
print(car1)
# result=car1.popitem('engine')  TypeError: dict.popitem() takes no arguments (1 given)

'''update()- takes another dict as arg and adds the contents of another dict into main dict and returns NONE'''
car1_addnl_info={'fuel Type':'Petrol','Top Speed':'250kmph','Acceleration':'4.8 sec'}
car1.update(car1_addnl_info)
print(car1)

