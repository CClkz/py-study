import numpy as np

# 加法
def add_numbers(a, b):
    return np.add(a, b)

# 取最大值
def max_value(numbers):
    return np.max(numbers)

# 示例使用
if __name__ == "__main__":
    result_add = add_numbers(10, 20)
    print(f"加法结果: {result_add}")

    result_max = max_value([1, 5, 3, 9, 2])
    print(f"最大值: {result_max}")
