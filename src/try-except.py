# 异常处理示例
def divide(a, b):
    try:
        result = a / b
        print(f"{a} 除以 {b} 的结果是: {result}")
    except ZeroDivisionError:
        print("错误：除数不能为零！")
    except TypeError:
        print("错误：输入必须是数字！")
    except Exception as e:
        print(f"发生未知错误: {e}")
    else:
        print("计算成功！")
    finally:
        print("计算结束。")

# 示例使用
if __name__ == "__main__":
    divide(10, 2)  # 正常情况
    divide(10, 0)  # 除零错误
    divide("10", 2)  # 类型错误
