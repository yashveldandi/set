#SETS
"""A set is an unordered collection of items.
Every set element is unique(no duplicates)and must
be immutable(cannot be changed).
However,a set itself a mutable.We can add or remove items from it
Sets can also be used to perform mathematical set operations like union
,intersection,symmetric difference,etc.

Characteristics:
.Unordered
.mutable
.No Duplicates
.Can't contain mutable data types"""

#Create  sets
#empty set
#show dic
s={}
print(s)
#empt set
s=set()
print(type(s))

#1D and 2D set--cannt create 2d sett throw error
s1 = {1,2,3}
print(s1)
#Hetro (Ture will not print true value is 1 because 1 already present in set)
s3={1,'hello',4.5,True}
print(s3)

#using ttype conversion
s4 = set([2,3,1])
print(s4)
#Duplicates not allowed
s5={1,1,2,2,3}
print(s5)
#set cant have mutable items
#error 
# s6={1,2,[3,4]}
# print(s6)

s1={1,2,3}
s2={3,2,1}
print(s1==s2)

#Acessing items
#not possible through error set is unordered
# s1={1,2,3}
# s1=[0]

#Editing--not possible error 

#adding-->single item
s={1,2,3,4}
s.add(5)
print(s)

#update-->multiple item in list format
s.update([5,6,7])
print(s)

#Deleting items
#del
s={1,2,3,4,5}
# del s
# print(s)

#Discard--
s.discard(5)
print(s)
#item not present it will print the og set not throw error
s.discard(50)
print(s)

#remove-->remove item not exist through error
s.remove(4)
print(s)

#pop--->randomly del item
s.pop()
print(s)

#clear---empty set
s.clear()
print(s)

#Set Operations
#union (print one time)
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print(s1 | s2)

#intersection(common print)
print(s1 & s2)

#Difference(-)(s1 item which not present in s2)
print(s1-s2)

#Symmetric Difference(^)---except common everything print
print(s1^s2)

#Membership Test
print(1 in s1)
print(1 not in s1)
#Iteration
for i in s1:
    print(i)

#Functions
#len/sum/min/max/sorted
s={5,6,8,9,7}
print(len(s))
print(sum(s))
print(min(s))
print(max(s))
print(sorted(s))

#union/Update
s1={1,2,3,4,5}
s2={4,5,6,7,8}

#s1|s2
print(s1.union(s1))
s1.update(s2)
#update s1 and s2 remains same
print(s1)
print(s2)

#intersection/intersetion_update
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print(s1.intersection(s2))
#s1 inter sected s2 will print
s1.intersection_update(s2)
print(s1)
print(s2)

#difference/difference_update

#intersection/intersetion_update
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print(s1.difference(s2))
#s1 inter sected s2 will print
s1.difference_update(s2)
print(s1)
print(s2)

#symmetric_difference/symemetric_difference_update
#intersection/intersetion_update
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print(s1.symmetric_difference(s2))
#s1 inter sected s2 will print
s1.symmetric_difference_update(s2)
print(s1)
print(s2)

#isdisjoint/issubset/issuperset
#isdisjoint--> no item is common
s1={1,2,3,4}
s2={3,4,5,6}
print(s1.isdisjoint(s2))#return false

s1={1,2,3,4}
s2={5,6,7,8}
print(s1.isdisjoint(s2))#return True

#issubsets
s1={1,2,3,4,5}
s2={3,4,5}
print(s2.issubset(s1))

#issuperset
s1={1,2,3,4,5}
s2={3,4,5}
print(s1.issuperset(s2))

#copy--create shallow copy
s1={1,2,3}
s2=s1.copy()
print(s1)
print(s2)

#Froznset
#Frozen set is just an immutable veersion of a Python set object
#create frozenset 
fs= frozenset([1,2,3])
print(fs)
#IMP-works-->all read functions
#does'nt work-->write fucntions

#2d frozen set

fs=frozenset([1,2,3,4,frozenset[3,4]])
print(fs)

#set comprehension
print({i for i in range(1,11)})
print({i for i in range(1,11)if i >5})

