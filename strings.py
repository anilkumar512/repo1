'''Strings - collection of characters which are enclosed between either a pair of single quotes('') , double quotes("") or triple single quotes('''''') or triple double quotes("""""")
   characters can be A-Z,a-z,0-9
   Immutable
   Ordered
   supports Indexing and slicing
   allows duplicate characters 
   '''
#Default Value of String
string=''                         
print(type(string)) 
print(string)

vibe='Chilling with nature'
print(type(vibe))
print(vibe)
vibe2='Chilling with nature'
print(id(vibe),id(vibe2))
# vibe3='fulfilling 'mental' pleasures'     SyntaxError: invalid syntax
vibe3='fulfilling \'cool\' pleasures'     
vibe3='fulfilling "heart" pleasures'
print(vibe3)    
vibe3='fulfilling "mental" pleasures'
print(vibe3)
# vibe3='fulfilling '''heart''' pleasures'     SyntaxError: invalid syntax
vibe3='fulfilling \'''heart\''' pleasures'  

vibe3="fulfilling 'mental' pleasures"
# vibe3="fulfilling "mental" pleasures"        SyntaxError: invalid syntax
vibe3="fulfilling \"mental\" pleasures" 
vibe3="fulfilling '''mental''' pleasures" 
vibe3 = '''Getting 'lost'
in the "mother"
nature
'''
print(vibe3)

'''Indexing'''
print(vibe[-4])
# print(vibe[20])                   IndexError: string index out of range
print(vibe[4+2])
# print(vibe[4+2.0])               TypeError: string indices must be integers, not 'float'
# print(vibe[-4,3])                TypeError: string indices must be integers, not 'tuple'

'''Slicing'''
print(vibe[1:9])                 
print(vibe[8::-1])  
print(vibe[-5::-1])                 
print(vibe[::-1])                 
print(vibe[:-6])                 
print(vibe[-6:])   

wish='morning'
name='Anil'
print(wish+name)       #concatenation
print(wish*7)          #repetition
         
print(chr(65))
print(chr(90))
# print(chr('A'))          TypeError: 'str' object cannot be interpreted as an integer
# print(chr(67,69))        TypeError: chr() takes exactly one argument (2 given)
print(ord('P'))        
# print(ord(65))           TypeError: ord() expected string of length 1, but int found
# print(ord('M','N'))      TypeError: ord() takes exactly one argument (2 given)
print(chr(97))             
print(chr(122))
print(ord('h'))
print(chr(48))
print(chr(57))
print(ord('6'))

'''upper() - takes no arg,returns a string where in all alphabets are converted to uppercase'''
print('salaar'.upper())

'''lower() - takes no arg,returns a string where in all alphabets are converted to lowercase'''
print('SALAAR'.lower())

'''swapcase()- takes no arg returns a string where uppercase are converted to lowercase and lowercase are converted to uppercase'''
print('SaLaAr'.swapcase())

'''capitalise() - takes no arg and returns a string where in the 1st letter of entire string is uppercase and everything is lowercase'''
print('bahaabubali the begining'.capitalize())
print('300 the rise of empire'.capitalize())

'''title()- takes no arg and returns a string in title format where 1st letter of each word is uppercase and everything lowercase'''
print('baahubali the conclusion'.title())

'''index()- takes 3 args out of which 1 is compulsory and returns index position of given substring
 string.index(substring,startpoint,endpoint)
'''
string1="See You Again"
print(string1.index('a'))
print(string1.index('A',5,12))
# print(string1.index('z'))        ValueError: substring not found

'''find() - takes 3 args out of which 1 is compulsory and returns index position of given substring 
 it is similar to index() but if substring is not found it won't throw error instead it returns -1
 string.find(substring,startpoint,endpoint)'''
string1="Legends Never Die"
print(string1.find('Die'))
print(string1.find('e',5,12))
print(string1.find('f'))   

'''count() - takes 3 args out of which 1 is compulsory and returns number of occurences of given substring
 string.count(substring,startpoint,endpoint)'''
string1="Mississippi"
print(string1.count('s'))
print(string1.count('si'))
print(string1.count('s',4,14))
   




'''textwrap'''
import textwrap
'''The wrap() function wraps a single paragraph in text (a string) so that every line is width characters long at most.
It returns a list of output lines.'''
string = "This is a very very very very very long string."
result=textwrap.wrap(string,8)
print(result)
'''The fill() function wraps a single paragraph in text and returns a single string containing the wrapped paragraph.'''
string = "This is a very very very very very long string."
result=textwrap.fill(string,8)
print(result)

'''strip() - takes 1 arg which is not compulsory, 
it will remove the given characters from starting and end of the string,
if characters not given it will remove white spaces from starting and end of the string,
after removing the characters, it will return the string
'''
name="  Sita  "
print(name)
print(name.strip())
name="@@@Sita@@@"
print(name.strip('@'))

'''lstrip() - it is similar to strip() but removes characters only from left hand side and returns remaining string'''

name="    Sita   "
print(name.lstrip())
name="%%Sita%%"
print(name.lstrip('%'))

'''rstrip()-it is similar to strip() but removes characters only from right hand side and returns remaining string'''
name="    Sita   "
print(name.rstrip())
name="!!!Sita!!!"
print(name.rstrip('!'))

'''center() - it takes number as an argument,
it puts the given string in the center of the given number of spaces and returns the same
we can pass a character as the 2nd argument,then instead of space we get the given character
'''
city='Bangalore'
print(city)
print(city.center(20))
print(city.center(20,'^'))

'''ljust() - it similar to center() but puts the string to the left hand side and returns same'''
place='ladakh'
print(place)
print(place.ljust(15))
print(place.ljust(15,'$'))
'''rjust() - it is similar to center() but puts the string to the right hand side and returns same'''
place='paris'
print(place)
print(place.rjust(15))
print(place.rjust(15,'~'))

'''boolean methods'''
'''isupper() - returns true if all the characters in given string are uppercase else false '''
print('GHOST'.isupper())
print('GHOST2'.isupper())
print('GhOST'.isupper())
'''islower() -  returns true if all the characters in given string are lowercase else false '''
print('spiderman'.islower())
print('spiderman3'.islower())
print('spiderMan'.islower())

'''istitle()  returns true if the given string is in title format else false '''
print('Spiderman Home Coming'.istitle())
print('Spiderman home Coming'.istitle())
print('Spiderman 1home Coming'.istitle())

'''isnumeric() -  returns true if all the characters in given string are numbers else false '''
print('300'.isnumeric())
print('300the rise of empire'.isnumeric())
'''isalpha() -  returns true if all the characters in given string are alphabhets else false '''
print('baahubali'.isalpha())
print('baahubali2'.isalpha())
'''isalnum() -  returns true if all the characters in given string are alphabets or numbers or combination of both else false '''
print('kalki'.isalnum())
print('24'.isalnum())
print('kalki2898'.isalnum())





