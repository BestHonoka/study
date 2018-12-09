players = ["Harden","Durant","Westbrook"]
for player in players:
    print(player,"is a mvp")
print("Thunder choosed them all.")
#for循环简单练习

list_1 = []
for numbers in range(1,20,2):
    list_1.append(numbers)
print(list_1)
#空列表遍历添加元素

list_2 =[x**3 for x in range(11)]
print(list_2)
#列表解析

list_3 = ["1","2","3","4","5"]
print(list_3[:2])
print(list_3[-1:])
print(list_3[::-1])
# 切片练习
