def getMax(a, b):
    if a > b:
        return a
    else:
        return b

# 定义一个简单的函数


def greet(name):
    return f"你好, {name}!"

# 带默认参数的函数


def greet_with_default(name="Python"):
    return f"你好, {name}!"

# 多个参数的函数


def add(a, b):
    return a + b

# 返回多个值的函数


def calculate(a, b):
    return a + b, a - b, a * b, a / b

# 可变参数函数


def sum_all(*args):
    return sum(args)

# 关键字参数函数


def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# 示例使用
if __name__ == "__main__":
    print(getMax(1, 2), getMax(3, 4), getMax(5, 6))
    # print(greet("Alice"))
    # print(greet_with_default())
    # print(greet_with_default("Bob"))
    # print(add(3, 5))
    # print(calculate(10, 2))
    # print(sum_all(1, 2, 3, 4, 5))
    # print_info(name="Alice", age=25, city="Beijing")
