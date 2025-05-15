# 数值类型常用操作示例

# 1. 创建数值
num1 = 10
num2 = 3.14

# 2. 基本运算
sum_result = num1 + num2      # 加法
diff_result = num1 - num2     # 减法
prod_result = num1 * num2     # 乘法
quot_result = num1 / num2     # 除法
floor_div = num1 // num2      # 整除
mod_result = num1 % num2      # 取模
power_result = num1 ** 2     # 幂运算

# 3. 类型转换
int_num = int(num2)          # 转换为整数
float_num = float(num1)      # 转换为浮点数

# 4. 数学函数
import math
abs_value = abs(-num1)        # 绝对值
sqrt_value = math.sqrt(num1) # 平方根
log_value = math.log(num1)   # 自然对数
sin_value = math.sin(num2)   # 正弦值
cos_value = math.cos(num2)   # 余弦值
tan_value = math.tan(num2)  # 正切值

# 5. 比较运算
is_equal = num1 == num2      # 等于
is_greater = num1 > num2     # 大于
is_less = num1 < num2        # 小于
is_not_equal = num1 != num2  # 不等于

# 6. 其他常用操作
rounded = round(num2, 1)     # 四舍五入
min_value = min(num1, num2)  # 最小值
max_value = max(num1, num2)  # 最大值
