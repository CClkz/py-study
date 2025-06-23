"""
Python中 == 和 is 的比较规则详解
"""

# 1. == 操作符的比较规则
def value_comparison():
    """
    比较值的类型（== 比较内容）：
    - 基本类型：int, float, str, bool
    - 序列类型：list, tuple, range
    - 集合类型：set, frozenset
    - 映射类型：dict
    """
    # 示例
    a = [1,2]
    b = [1,2]
    print(a == b)  # True (比较元素值)
    
    x = "hello"
    y = "hello"
    print(x == y)  # True (比较字符串内容)

def reference_comparison():
    """
    比较内存地址的类型（除非重写__eq__方法）：
    - 自定义类实例
    - 模块对象
    - 函数对象
    """
    class MyClass: pass
    c1 = MyClass()
    c2 = MyClass()
    print(c1 == c2)  # False (默认比较内存地址)

# 2. is 操作符的规则
def identity_comparison():
    """
    is 总是比较内存地址（对象标识符）：
    - 对于None, True, False等单例对象有效
    - 小整数(-5~256)和短字符串会缓存复用
    - 其他对象每次创建新实例
    """
    # 特殊案例
    m = 256
    n = 256
    print(m is n)  # True (小整数缓存)
    
    p = 257
    q = 257
    print(p is q)  # False (超出缓存范围)

# 3. 综合比较案例
def compare_examples():
    # 列表比较
    lst1 = [1,2,3]
    lst2 = [1,2,3]
    print(lst1 == lst2)  # True (值比较)
    print(lst1 is lst2)  # False (不同对象)
    
    # 字符串驻留
    s1 = "hello"
    s2 = "hello"
    print(s1 is s2)  # True (短字符串缓存)

if __name__ == "__main__":
    value_comparison()
    reference_comparison()
    identity_comparison()
    compare_examples()
