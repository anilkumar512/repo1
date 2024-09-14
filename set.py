''' Set - collection of elements separated by comma and enclosed in curly braces
Unordered
Doesn't allow duplicates
Doesn't support Indexing and Slicing
Mutable
stores homogenous & immutable elements i.e string,tuple,integer,float,boolean,complex



'''

'''Default Value of Set'''
set=set()
print(type(set))  
print(set)

# string='Shape of you'
# set=set(string)
# print(type(set))   
# print(set)   

# list=[43,3,65,'haha',5.3,6+7j,43]
# set=set(list)
# print(type(set))
# print(set)

# tuple=(37,'hii',5.33,'hii',5+4j)
# set=set(tuple)
# print(type(set))
# print(set)

# set={8,[32,43]}    TypeError: unhashable type: 'list'
set={2,'roy',(4,6),-4.6,3+4j}
print(set)

supercars={'ferrari','bujji','porsche','lamborghini','bugatti','ferrari'}
print(supercars)
print(type(supercars))

'''add(x) -  Adds item x to the set'''
supercars.add('Mc Laren')
print(supercars)

'''update(x,y,z) - This method is used to add multiple items to the set. Arguments are not individual elements and these are Iterable objects like List,range etc.'''
cars={'bmw','audi','kia'}
supercars.update(cars)
print(supercars)
supercars.update('r',range(2))
# supercars.update(5)   TypeError: 'int' object is not iterable
print(supercars)

'''remove(x) -  It removes specified element x from the set.If the specified element not present in the Set then we will get KeyError'''
supercars.remove('kia')
# supercars.remove('Winova')   KeyError: 'Winova'
print(supercars)


'''discard(x) - It removes the specified element x from the set. If the specified element not present in the set then we won't get any error.'''
supercars.discard('bmw')
supercars.discard('audi')
supercars.discard('tata')

'''pop() -  It removes and returns some random element from the set '''
print(supercars.pop())
print(supercars.pop())
# supercars.pop(4)      TypeError: set.pop() takes no arguments (1 given)
s={2,2}
print(type(s))
print(s.pop())  
# print(s.pop())          KeyError: 'pop from an empty set'

'''copy() -  Returns copy of the set. It is cloned object (Backup copy)'''
supercars_copy=supercars.copy()
print(type(supercars_copy))
print(supercars_copy)

'''clear - To remove all elements from the Set'''
supercars_copy.clear()
print(supercars_copy)

supercars2={'Rimac Nevera','ferrari','lotus Evija','lamborghini','Pagani Utopia'}

'''union() -  This operation returns all elements present in both sets x and y (without duplicate elements)'''
union_set=supercars.union(supercars2)
union_set2=supercars|supercars2
print(union_set)
print(union_set2)




'''intersection() - returns a new set containing elements common to both sets, it doesnot modify original set'''
intersection_set=supercars.intersection(supercars2)
intersection_set2=supercars&supercars2
print(intersection_set)
print(intersection_set2)
'''intersection_update()-updates the original set to keep only elements that are common to both set, it modifies the original set'''
supercars.intersection_update(supercars2)
print(supercars)

'''difference() - returns a new set containing elements that are in set1 but not in set2, it doesnot modify original set'''
diff_set=supercars.difference(supercars2)
diff_set2=supercars-supercars2
diff_set3=supercars2-supercars
print(diff_set)
print(diff_set2)
print(diff_set3)
'''difference_update()- updates the original set(set1) to remove elements that are also in set2,it modifies the original set'''
supercars.difference_update(supercars2)
print(supercars)

'''symmetric_difference() -returns a new set containing elements that are in either set1 or set2 but not in both, it doesnot modify original set '''
sym_diff=supercars.symmetric_difference(supercars2)
sym_diff2=supercars^supercars2
print(sym_diff)
print(sym_diff2)
'''symmetric_difference_update- updates the original set(set1) to contain elements that are in either set1 or set2 but not in both,it modifies the original set'''
supercars.symmetric_difference_update(supercars2)
print(supercars)