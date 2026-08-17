'''
Data types & Type conversion

--------------------
1 Numeric datatype
----> Float and integer is called as numeric datatype

float

-------
---> A nuber which contains decimal values , we call it as a float data type 

eg v= 56.5

integer (int)
-----------
----------> A normal value without any decimal values is called as int

2 string

-------------

---> string is dequence of char that are enclosed in '',"",""" """

----> string is immutable

eg

-----------------

any_ ='pythin is a language '
all_='ab-*6%9()'

3 list

--------------

----->list is a collection of different of data types
----->list is a repsented by [] that are seperated by ,
-----> inside the list we call it as items 
-----> list is mutable

v='[vouib]'
print(v)

4 tuple

------>tuplpe is a collection of different data types
------>tuple is enclosed  in parenthesis
------>these data types are seperated by commas
------> tuple is immutable

eg

---

nums =(1,89.6,)

5 dictionary

----------

----> Dictionary is collection of key:value pairs , keys and values are seperated by :
----> key and value pair are called as item
----> this items are seperated by , 
---->dictionary are represented by {}
----> key is immutable
----> in value place there can be any data type

eg data={1:2,'name'='vijju}
-----------

6 set 

----> set is represented by {}
----> is colection of unique data types
an={1,2,3}

-----

Type conversion

float ---> int,str
price =5.8
print(int(price))
print(str(price))
-----> 

eg----> int()
do='3456'
print(int(do))

-----> float



list----> tuple,string
eg----> tuple()
nums[1,2,3,4]
print(tuple(nums))

tuple--->list
eg ---> list()
all_=(5,6,7)
print(tuple(all))
'''
s=[1]
v=[s]
print(type(v))
x = ([1, 2], [3, 4])
x[0].append(3)
dict(x)
print(x)
