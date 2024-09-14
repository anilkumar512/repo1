'''TYPE CASTING- process of converting data in one datatype to data in another datatype
                      DEST_VAR=DEST_TYPE(SOURCE_VAR)
'''
'''Converting integer to other datatypes
SOURCE_TYPE            DEST_TYPE
int                    float,bool,complex,str (possible)
                       list,tuple,set,dict(Not possible)


'''
integer=77
print(float(integer))
print(complex(integer))
print(bool(integer))
print(str(integer))

# TypeError: 'int' object is not iterable
# print(list(integer))
# print(tuple(integer))         
# print(set(integer))
# print(dict(integer))

'''Converting float to other datatypes
SOURCE_TYPE            DEST_TYPE
float                    int,bool,complex,str (possible)
                       list,tuple,set,dict(Not possible)
'''
float_num=99.88
print(int(float_num))
print(complex(float_num))
print(bool(float_num))
print(str(float_num))

# TypeError: 'float' object is not iterable
# print(list(float_num))
# print(tuple(float_num))         
# print(set(float_num))
# print(dict(float_num))

'''Converting bool to other datatypes
SOURCE_TYPE            DEST_TYPE
bool                   int,float,complex,str (possible)
                       list,tuple,set,dict(Not possible)

'''
bool_val=True
print(int(bool_val))
print(float(bool_val))
print(complex(bool_val))
print(str(bool_val))

# TypeError: 'bool' object is not iterable
# print(list(bool_val))
# print(tuple(bool_val))         
# print(set(bool_val))
# print(dict(bool_val))

'''Converting complex to other datatypes
SOURCE_TYPE            DEST_TYPE
complex                bool,str (possible)
                       int,float,list,tuple,set,dict(Not possible)
'''
complex_num=42+10j
print(bool(complex_num))
print(str(complex_num))

# print(int(complex_num)) TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
# print(float(complex_num)) TypeError: float() argument must be a string or a real number, not 'complex'

# TypeError: 'complex' object is not iterable
# print(list(complex_num))
# print(tuple(complex_num))         
# print(set(complex_num))
# print(dict(complex_num))

'''Converting string to other datatypes
SOURCE_TYPE            DEST_TYPE
string                    int(possible if str have integer value),
                         float(possible if str have float value),
                         complex(possible if str have float value),
                         bool(checks for default/non-default value),
                         list,tuple,set,(possible)
                         dict(Not possible)
'''
str_val="123"
print(int(str_val))
str_val="54.8"
print(float(str_val))
str_val="54"
print(float(str_val))
str_val="56+4j"
print(complex(str_val))
str_val="56"
print(complex(str_val))
str_val="56.8"
print(complex(str_val))
str_val=""
print(bool(str_val))

str1="Mary Jane Watson"
print(list(str1))
print(tuple(str1))
print(set(str1))
# print(dict(str1))  ValueError: dictionary update sequence element #0 has length 1; 2 is required
str2="AC"
# print(dict(str2))   ValueError: dictionary update sequence element #0 has length 1; 2 is required 


'''Converting list to other datatypes
SOURCE_TYPE            DEST_TYPE
list                    bool,str,tuple, set (possible) 
                        dict(possible only for 1 condition)

                        int,float,complex(not possible)
'''

list1=[10,20,30,40]
print(bool(list1))
print(str(list1))
print(tuple(list1))
print(set(list1))
# print(dict(list1))  TypeError: cannot convert dictionary update sequence element #0 to a sequence
'''A list consisting of nested collection of length can be converted to dict'''
list1=[[12,30],("hey","hello"),{3,6},"ab",{'d':75,'e':66}]
print(dict(list1))

'''Converting tuple to other datatypes
SOURCE_TYPE            DEST_TYPE
tuple                    bool,str,list, set (possible) 
                        dict(possible only for 1 condition)

                        int,float,complex(not possible)
'''

tuple1=(10,20,30,40)
print(bool(tuple1))
print(str(tuple1))
print(list(tuple1))
print(set(tuple1))
# print(dict(tuple1))  TypeError: cannot convert dictionary update sequence element #0 to a sequence
tuple1=([12,30],("hey","hello"),{3,6},"ab",{'d':75,'e':66})
print(dict(tuple1))
'''Converting set to other datatypes
SOURCE_TYPE            DEST_TYPE
set                    bool,str,list,tuple(possible) 
                        dict(possible only for 1 condition)

                        int,float,complex(not possible)
'''

set1={10,20,30,40}
print(bool(set1))
print(str(set1))
print(list(set1))
print(tuple(set1))
# print(dict(set1))  TypeError: cannot convert dictionary update sequence element #0 to a sequence
set1={("hey","hello"),"ab"}
print(dict(set1))

'''Converting dict to other datatypes
SOURCE_TYPE            DEST_TYPE
dict                   bool,str,list,tuple,set(possible) 
                        
                        int,float,complex(not possible)
'''

dict1={'p':3,'h':4,'k':7}
print(bool(dict1))
print(str(dict1))
print(list(dict1))
print(tuple(dict1))
print(set(dict1))  




