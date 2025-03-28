# 写入文件
def write_to_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"文件 {filename} 写入成功")

# 读取文件
def read_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    print(f"文件 {filename} 的内容：\n{content}")
    return content

# 追加内容到文件
def append_to_file(filename, content):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(content)
    print(f"内容已追加到文件 {filename}")

# 示例使用
if __name__ == "__main__":
    filename = "example.txt"
    
    # 写入文件
    write_to_file(filename, "这是第一行内容。\n")
    
    # 读取文件
    read_from_file(filename)
    
    # 追加内容
    append_to_file(filename, "这是追加的内容。\n")
    
    # 再次读取文件
    read_from_file(filename)
