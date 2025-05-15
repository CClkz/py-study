# 字符串常用操作示例

# 1. 创建字符串
text = "Hello, World!"

# 2. 查找和替换
index = text.find("World")  # 查找子字符串首次出现的索引
replaced = text.replace("World", "Python")  # 替换子字符串

# 3. 分割和连接
words = text.split(",")     # 分割字符串 ["Hello", " World!"]
joined = " ".join(words)    # 连接字符串 "Hello World!"

# 4. 大小写转换
lower = text.lower()        # 转换为小写
upper = text.upper()        # 转换为大写

# 5. 去除空白
stripped = text.strip()    # 去除两端空白

# 6. 其他常用操作
length = len(text)         # 获取字符串长度
substring = text[7:12]     # 获取子字符串 "World"
