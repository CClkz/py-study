# 列表（数组）常用操作示例

# 1. 创建列表
numbers = [1, 2, 3]

# 2. 添加元素
numbers.append(4)        # 在末尾添加单个元素 [1, 2, 3, 4]
numbers.extend([5, 6])  # 在末尾添加多个元素 [1, 2, 3, 4, 5, 6]
numbers.insert(0, 0)     # 在指定位置插入元素 [0, 1, 2, 3, 4, 5, 6]
numbers += [7, 8]        # 使用 + 运算符连接列表 [0, 1, 2, 3, 4, 5, 6, 7, 8]

# 3. 删除元素
numbers.remove(0)        # 移除第一个匹配的元素 [1, 2, 3, 4, 5, 6, 7, 8]
popped = numbers.pop()   # 移除并返回最后一个元素 [1, 2, 3, 4, 5, 6, 7]
del numbers[0]           # 删除指定位置的元素 [2, 3, 4, 5, 6, 7]
numbers[1:3] = []        # 使用切片删除元素 [2, 5, 6, 7]
numbers.clear()          # 清空整个列表 []

# 4. 查找元素
numbers = [2, 5, 6, 7, 5]
index = numbers.index(5)  # 查找元素首次出现的索引 1
count = numbers.count(5)  # 统计元素出现的次数 2
exists = 6 in numbers     # 检查元素是否存在 True

# 5. 排序和反转
numbers.sort()            # 升序排序 [2, 5, 5, 6, 7]
numbers.sort(reverse=True)  # 降序排序 [7, 6, 5, 5, 2]
numbers.reverse()         # 反转列表 [2, 5, 5, 6, 7]

# 6. 切片操作
sub_numbers = numbers[1:3]    # 获取子列表 [5, 5]
numbers_copy = numbers[:]     # 复制整个列表

# 7. 列表推导式
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# 8. 其他常用操作
length = len(numbers)     # 获取列表长度
numbers_copy = numbers.copy() # 复制列表
numbers.extend([8, 9])   # 扩展列表 [2, 5, 5, 6, 7, 8, 9]