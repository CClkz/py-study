# 集合常用操作示例

# 1. 创建集合
numbers = {1, 2, 3}

# 2. 添加元素
numbers.add(4)               # 添加单个元素
numbers.update([5, 6])       # 添加多个元素

# 3. 删除元素
numbers.remove(1)            # 移除指定元素，不存在报错
numbers.discard(2)           # 移除指定元素，不存在不报错
popped = numbers.pop()      # 移除并返回任意元素
numbers.clear()              # 清空集合

# 4. 查找元素
exists = 3 in numbers        # 检查元素是否存在

# 5. 集合运算
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union = set1 | set2          # 并集 {1, 2, 3, 4, 5}
intersection = set1 & set2   # 交集 {3}
difference = set1 - set2     # 差集 {1, 2}
symmetric_diff = set1 ^ set2 # 对称差集 {1, 2, 4, 5}

# 6. 其他常用操作
length = len(numbers)        # 获取集合长度
