#tuple
tuple1=("Lahore","Pakistan","India","Afghanistan","Australia")
print(tuple1)
# tuple1[3]='Belgium'      Immutable, ca n not change its value
print(tuple1.index('Lahore')) # to get index pf an element in a tuple
#concatenation of tuple
tup1=(1,2,3,4)
tup2=(5,6,7,8)
tup3=tup1+tup2
print(tup3)
#tup1.append()       can not append or add any item in tuple
#tup1.insert(8)      can not insert any thing in tuple
# We can add a list as a element inside a tuple
tuple1=(1,2,3,[4,5,6],7)
print(tuple1)

thistuple=("apple","banana","cherry","apple","cherry")
print(thistuple[2],thistuple[-1])

tuple5=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
print(tuple5[:])
print(tuple5[:4])
print(tuple5[4:])
print(tuple5[4::2])
print(tuple5[::-1])
