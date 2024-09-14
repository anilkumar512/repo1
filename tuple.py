'''Tuple- 'collection of elements separated by comma and enclosed in parenthesis'
Immutable
homo & heterogenous data
Ordered
supports indexing and slicing
Allows Duplicates

'''
#Default Value of Tuple
tuple=()
print(type(tuple)) 
print(tuple)

names='Rolex',
print(type(names))
a=()
print(type(a))
a=(2)
print(type(a))

# favmovie=tuple('Sita Ramam')
# print(type(favmovie))
# print(favmovie)
# list=[43,22,53,24,53]
# tuple=tuple(list)
# print(type(tuple))
# print(tuple)

superheros=('iron man','hulk','thor','cap','clint')
print(superheros[3])
print(superheros[-4])
print(superheros[2::2])
print(superheros[::-1])
print(len(superheros))
print(superheros.count('hulk'))
print(superheros.index('thor'))

heroes=sorted(superheros)
print(type(heroes))
print(heroes)
print(type(superheros))
rheroes=sorted(superheros,reverse=True)
print(type(rheroes))
print(rheroes)

info=32,53,53,654,23,8,43
dinfo=(x*x for x in range(1,20) if x%2==0)
print(type(dinfo))
for i in dinfo:
    print(i)




