list1 = [1,2,3]
list1 = ['a','c','r','o','p','o','l','i','s',[8,2,7]]
print(list1[1:5])

list=[]
list1 = [1,2,3]
list1 = [1,"hello",3.4]
list1 = [1,[1,2,3],3.4]
list1 = ['c','s','i','t',[2,4,8]]


list1 = [1,2,4]
list1.extend([7,8,9])


list1.insert(3 , 16)


odd=[1,9,10,9,11]
odd[1:2] = [5,7,8]


odd.remove(8)


odd.pop()

odd=[1,23,3,4,55,5,5,5,6,7,8]


pow = [x**2 for x in range(10)]


pow = [2**x for x in range(10) if x>5]


even = [x for x in range(100) if x%2==0]
print(even)
odd = [x for x in range(100) if x%2!=0]
print(odd)

number_list = [ x for x in range(30) if x % 2 == 0]
print(number_list)

num_list = [y for y in range(50) if y % 2 == 0 if y % 5 == 0]
print(num_list)