# list1 = [0, 1, 2]
# list2 = [3, 4, 5]
# list3 = zip(list1, list2)
# for item in list3:
#     print(item)
#
# print("a", "b", "c", sep="_")
# print("*", end=" ")
# print("*")
#
# *a, b, c = "我是齐天大圣"
# d = "我是齐天大圣"
# print(a)
# print(b)
# print(c)
# print(d[3])
#
#
# def func02(p1):
#     p1[0] = 100
#     print(p1[0])
#
#
# data01 = [10]
# func02(data01)
# print(data01)
#
#
# class MyClass:
#     def __init__(self, data01=0):
#         self.data01 = data01
#         self.data02 = 100
#
#     @property
#     def data01(self):
#         return self.__data01
#
#     @data01.setter
#     def data01(self, value):
#         self.__data01 = value
#
#
#
# m01 = MyClass(1)
# print(m01.data01)
# print(m01.data02)

# list01 = [10,20,30,40]
# print(list01[:2])

# dict={"a":1,"b":2}
# for item in dict:
#     print(item)
#
#
# print(dict["a"])
# dict["a"]+=1
# print(dict["a"])
import copy

#
# list01 = [10, [20, 30]]
# list02 = copy.deepcopy(list01)
# list02 = list01[:]
# list02[0] = 100
# list02[1][1] = 300
# print(list01)
# print(list02)
#
# # list01 = ["a", "b", "c"]
# # result = " ".join(list01)
# # print(result)
#
# # list_result = []
# # for i in range(1,11,2):
# #     list_result.append(str(i))
# # result = " ".join(list_result)
# # print(result)
#
# list_result = []
# while True:
#     content = input("请输入内容:")
#     if content == "":
#         break
#     list_result.append(str(content))
# result = "_".join(list_result)
# print(result)

# list_result = "a-b-c".split("-")
# print(list_result[::-1])
# message= "-".join(list_result[::-1])
# print(message)
# print(list_result[0])

# list01=[1,2,3]
# list01.insert(1,10)
# print(list01)

# dict01 = {"name":"a"}
# print(dict01)
# if "name" in dict01:
#     dict01["name"] = "b"
# print(dict01)

# for i in range(5,0,-2):
#     print(i)
# print(2+2*3*2**3)

# a = {"one": 1, "two": 2, "three": 3}
# print(a.get("one"))


# a = {1,2,3,4,5,6}
# b = {5, 6, 7, 8, 9}
# c = {5, 6}
# d = {5, 6, 7}
# print(c in b)
# print(list(("aaa",)))

# list01 = [123, 378, 489, 4646378, 894, 315]
# result = []
# result01 = []
# for item in list01:
#     unit = str(item)[-2]
#     if unit in ("3", "7", "8"):
#         result01.append(item)
#         continue
#     result.append(item)
# print(result)
# print(result01)

# list_year = []
# for item in range(1970, 2051):
#     if item % 4 == 0 and item %100 !=0 or item %400 ==0:
#         list_year.append(item)
# print(list_year)
# list_year01 = [item for item in range(1970, 2051)
#             if item % 4 == 0 and item %100 !=0 or item %400 ==0]
# print(list_year01)

# list01 = [1,2,3,4,5,6]
# for i in range(len(list01)-1,-1,-1):
#     print(list01[i])

# def print_rectangle(number):
#     for row in range(number):
#         if row == 0 or row == number - 1:
#             print("*" * number)
#         else:
#             print(f"*{' '*(number-2)}*")
#
# print_rectangle(10)