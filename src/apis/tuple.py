# 元组常用操作示例

# 1. 创建元组
numbers = (1, 2, 3)

# 2. 查找元素
index = numbers.index(2)    # 查找元素首次出现的索引
count = numbers.count(2)    # 统计元素出现的次数
exists = 3 in numbers       # 检查元素是否存在

# 3. 切片操作
sub_numbers = numbers[1:3]  # 获取子元组 (2, 3)

# 4. 其他常用操作
length = len(numbers)       # 获取元组长度
