# 异常处理示例
def divide(a, b):
    try:
        result = a / b
        print(f"{a} 除以 {b} 的结果是: {result}")
    # except 可看成一个整体的块，包含多个异常类型捕获
    # try 报错进入except块，再匹配具体的异常类型（如没有匹配的异常类型，程序会异常，不是进else，要注意）
    # try 没报错进入else块
    except ZeroDivisionError:
        print("错误：除数不能为零！")
    except TypeError:
        print("错误：输入必须是数字！")
    except Exception as e:
        print(f"发生未知错误: {e}")
    else: # 如果没有异常发生，则执行else块
        print("计算成功！")
    finally:
        print("计算结束。")

# 示例使用
if __name__ == "__main__":
    divide(10, 2)  # 正常情况
    divide(10, 0)  # 除零错误
    divide("10", 2)  # 类型错误
