# 整数类型 (int)
integer_var = 42
print(f"整数类型: {integer_var}, 类型: {type(integer_var)}")

# 浮点数类型 (float)
float_var = 3.14
print(f"浮点数类型: {float_var}, 类型: {type(float_var)}")

# 字符串类型 (str)
string_var = "Hello, Python!"
print(f"字符串类型: {string_var}, 类型: {type(string_var)}")

# 布尔类型 (bool)
bool_var = True
print(f"布尔类型: {bool_var}, 类型: {type(bool_var)}")

# 列表类型 (list)
list_var = [1, 2, 3, 4, 5]
print(f"列表类型: {list_var}, 类型: {type(list_var)}")

# 元组类型 (tuple)，长度和元素都不能改
tuple_var = (1, 2, 3, 4, 5)
print(f"元组类型: {tuple_var}, 类型: {type(tuple_var)}")

# 集合类型 (set)
set_var = {1, 2, 3, 4, 5}
print(f"集合类型: {set_var}, 类型: {type(set_var)}")

# 字典类型 (dict)
dict_var = {"name": "Alice", "age": 25}
print(f"字典类型: {dict_var}, 类型: {type(dict_var)}")

# None 类型
none_var = None
print(f"None 类型: {none_var}, 类型: {type(none_var)}")


# 类型判断
def check_type(value):
    if isinstance(value, int):
        print(f"{value} 是整数类型")
    # elif isinstance(value, float):
    elif type(value) == float:
        print(f"{value} 是浮点数类型")
    elif isinstance(value, str):
        print(f"{value} 是字符串类型")
    elif isinstance(value, bool):
        print(f"{value} 是布尔类型")
