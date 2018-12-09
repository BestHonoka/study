list = ["g-self","freedom","exia","reborn"]
# 创建列表


bad = list.pop(0)
print (bad , "cannot come!")
# 弹出一个元素，并输出相应内容


list.append("justice")
for friends in list:
    print ("plz have dinner with me," + friends)
# 加入一个元素，遍历列表并输出相应内容
    
del list[3]
print(list)
# 使用del删除一个元素并打印列表

list.clear()
print(list)
# 清空列表
