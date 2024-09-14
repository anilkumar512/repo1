'''List- 'collection of elements separated by comma and enclosed in square brackets'
mutable
homo & heterogenous data
Ordered
supports indexing and slicing
Allows Duplicates

'''
#Default Value of List
list = []
print(type(list))
print(list)

rollnumbers=[331,643,745,224,976,224,33,54,763,745,343]
print(rollnumbers[2])
print(rollnumbers[-4])
print(rollnumbers[-3:])
print(rollnumbers[:-5])
print(rollnumbers[2::2])
print(id(rollnumbers[3]))
print(id(rollnumbers[5]))
data=[12,(32,[2,3]),'lucy',{6,5},['today',['is','wow'],(4,9),3+4j]]
print(data[4][0][2])

#len() - returns the numer of elements of the list
print(len(rollnumbers))

#count() - to count the number of occurences of specified item in the list
print(rollnumbers.count(224))

#index() - returns the index of first occurence of specified item
print(rollnumbers.index(976))
print(rollnumbers.index(745,4,10))

#append() - to add elements at end of list
rollnumbers.append(777)
print(rollnumbers)

#insert() - insert element at specified index position
rollnumbers.insert(3, 979)

#extend() - to add all items of one list to another list
names=['Sita','Radha','sparkle']
rollnumbers.extend(names)
print(rollnumbers)

#remove() - to remove specified item from the list
rollnumbers.remove(643)
print(rollnumbers)

#pop() - remove and returns the last element, also index used to remove specified index item
print(rollnumbers.pop())
print(rollnumbers)
print(rollnumbers.pop(2))
print(rollnumbers)

#reverse() - reverse the order of elements
list=[32,123,654,22,87]
list.reverse()
print(list)

#sort() - sort the list, it sorts based on ASCII values
list.sort()
print(list)
friends=['sita','gita','raj','alex']
friends2=['sita','Gita','Raj','alex']
friends.sort()
friends2.sort()
print(friends)
print(friends2)
print(friends2)
# friends3=['rosy',21,'peter']
# print(friends3.sort())                #TypeError: '<' not supported between instances of 'int' and 'str'

#copy() -to copy a list into a variable name
frnd=friends.copy()
print(frnd)

#clear() -to clear a list
frnd.clear()
print(frnd)


cubeven=[x*x*x for x in range(0,10)if x%2==0]
print(type(cubeven))
print(cubeven)
