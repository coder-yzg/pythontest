
"""
元祖、数组、字典的取值都是用[]
元祖、数组、字典的定义分别是 ()，[],{}
"""

#元祖
a = (1,2,3,4,5,1)
print(a)  #有序
print(a[0])
print(a[-5])
print(a[1:3])      #切片，左闭右开，可以不写，默认开头、结尾
print(a.count(1))  #查找1的数量
print(a.index(1))  #查找第一个1的下标

b = (a,3,4)
print(b[0][1])     #二维元祖

#数组和元祖一样，只不过元祖不可修改,数组可以修改
b = [7,3,9,2]
c = [1,2]
b.append(5)        #增加数据
print(b)
b.extend(c)        #合并数组
print(b)
b.remove(3)        #删除某个值
print(b)
b.insert(0,6)      #指定位置插入
print(b)
b.pop(2)           #剪切数据
print(b)
b.sort()           #排序
print(b)
b.clear()          #清空
print(b)


#字典特点：1.没有顺序；2.字典的结构必须是键值对 key：value

d = {"name":"张三","age":18}
#取值,不存在的key，第一种会报错
print(d["name"])
print(d.get("age"))
#新增
d["phone"]=15038118651
d.update(high=15)
print(d)
#修改
d["name"] = "李四"
print(d)
#剪切key
d.pop("name")
print(d)


#数组和字典的删除还可以用del
del d["name"]
del b[0]

user = {}
user["name"] = input("请输入用户名：")
user["age"]  = input("请输入年龄：")
print(user)