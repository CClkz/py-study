# if-else 条件判断示例
def check_number(num):
    if num > 0:
        print("正数")
    elif num < 0:
        print("负数")
    else:
        print("零")

# for 循环示例
def print_numbers(n):
    for i in range(n):
        print(i)

# while 循环示例


def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("发射！")

# 嵌套控制结构示例


def find_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


# 示例使用
if __name__ == "__main__":
    check_number(10)
    print_numbers(5)
    countdown(3)
    print("100以内的质数：", find_primes(100))
