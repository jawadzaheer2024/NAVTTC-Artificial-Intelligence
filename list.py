
# List
list0=[]
list1=['one', 'two','three','four']
list2=['1','2','3','4']
list3=[[1, 2], [3, 4]]
list4=[1, 'Alex', 12, 1.5]

#len
len(list1)
list1.append('five')
print(list1)

#insert
list1.insert(2, 'three')
list1.remove('four')
print(list1)

#append
list1.append(list4)
print(list1)

#extend
list2.extend(list4)
print(list2)

# del
del (list4[0])
print(list4)

#reverse
list6=['5','6','7','8','9']
list6.reverse()
print(list6)

#sorted
numbers=[67,89,45,32,12,6,4,9,0]
sorted_list=sorted(numbers)
print(sorted_list)

#reverse sorted
numbers=[67,89,45,32,12,6,4,9,0]
sorted_list=sorted(numbers)
print("reverse sorted", sorted(numbers,reverse=True))

#split
list7="'one','two','three','four','five'"
spl=list7.split(",")
print(spl)

list8="A lab is being conducted"
spl1=list8.split()
print(spl1)

#slicing
list9=[78,89,56,77,66,45,32,21]
print(list9[:])
print(list9[:4])
print(list9[4:])
print(list9[2:6])
print(list9[::2])
print(list9[2::2])

#concatenation
list1=[1,2,3,4]
list2=['Alex','John','Harry']
list3=list1+list2
print(list3)


#sqr list
list=[2,3,4,5]
sqr=[x**2 for x in list]
print(sqr)
#cube list
cube=[x**3 for x in list]
print(cube)

list10=[11,12,34,56,76,68,23,45]
find =68 in list10
print(find)

#sum all elements in a list
def sum_list(items):
    sum_numbers=0
    for x in items:
        sum_numbers+=x
    return sum_numbers
print(sum_list([1,2,-8]))

#Mean
n_num=[1,2,3,4,5]
n=len(n_num)
get_sum=sum(n_num)
mean=get_sum/n
print("Mean/Average is: "+str(mean))


#Median
n_num=[1,2,3,4,5]
n=len(n_num)
n_num.sort()
if n%2==0:
    median1=n_num[n//2]
    median2=n_num[n//2-1]
    median3=(median1+median2)/2
else:
    median=n_num[n//2]
print("Median is:  "+str(median))