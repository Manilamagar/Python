# #list and tuple
# list = [1, 3, 6, "python", "ai" ]
# print(type(list))
# print(len(list))
# tuple = (2,4,7, "machine", "learning")
# print(type(tuple))
# print(len(tuple))


# # for i in list:
# #     print(i)

# # for i in tuple:
# #     print(i)

# print(list[0])

# for i in enumerate(list):
#     print(i)
# list.append(45)
# print(list)


# #to add the element in the desired index
# list.insert(0,"first")
# print(list)
# #to remove the element
# list.remove("6")

# list2 = [2,4,6,4,8,10]
# list2.remove(4)

# print(list2.pop(3))

list1  = ["machine", "python", "learning",5,7]
print(list1.pop(2))
print(  list1)

list3 = ["233","java"]
print(list1 + list3)

tuple1 = (1,3,4,6,7)
tuple2 = (3,4,6,8)

print(tuple1+tuple2)


#list comprehension
list_num = [2,3,4,5,6,7]
list_square = []
for i in list_num:
    i = i**2
    list_square.append(i)
print(list_square)


list_num = [2,3,4,5,6,7]
squared = [i**2 for i in list_num]
print (squared)


    # 1 to 20 range ma even number find out comprehension
list_num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
even = [i for i in list_num if i%2 ==0]
print(even)


#disctionary in python
dict1 = {"first":1, "second":2, "third":3, }
print(type(dict1))
print(dict1)
print(dict1.keys())
print(dict1.values())

dict1["fourth"]= 4
print(dict1)

for i in dict1.items():
    print(i)



dict2 = {"subject":["python", "java", ""]}