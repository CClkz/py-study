# 字典常用操作示例

# 1. 创建字典
person = {"name": "Alice", "age": 25}

# 2. 添加/更新元素
person["city"] = "New York"  # 添加新键值对
person["age"] = 26           # 更新已有键的值

# 3. 删除元素
del person["city"]           # 删除指定键值对
age = person.pop("age")      # 删除并返回指定键的值
person.clear()               # 清空字典

# 4. 查找元素
name = person.get("name")    # 获取指定键的值，不存在返回 None
exists = "name" in person    # 检查键是否存在

# 5. 遍历字典
for key, value in person.items():  # 遍历键值对
    print(f"{key}: {value}")

# 6. 其他常用操作
keys = person.keys()         # 获取所有键
values = person.values()     # 获取所有值
items = person.items()       # 获取所有键值对
length = len(person)         # 获取字典长度
