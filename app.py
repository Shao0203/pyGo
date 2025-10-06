# import random


# # # 1. 素数
# num = int(input('输入正整数: '))
# end = int(num ** 0.5)
# is_prime = True
# for i in range(2, end+1):
#     if num % i == 0:
#         is_prime = False
#         break
# if is_prime:
#     print(f'{num}是素数')
# else:
#     print(f'{num}不是素数')


# nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 13, 12, 21, 23, 27, 29]
# primes = []


# def get_prime(num):
#     if num < 2:
#         return False
#     end = int(num ** 0.5)
#     for i in range(2, end + 1):
#         if num % i == 0:
#             return False
#     return True


# for num in nums:
#     if get_prime(num):
#         primes.append(num)

# print(f'Prime numbers are: {primes}')
# # Prime numbers are: [2, 3, 5, 7, 11, 13, 23, 29]


# primes = []
# for i in range(2, 101):
#     is_prime = True
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(i)


# # 2. 最大公约数
# x = int(input('x = '))
# y = int(input('y = '))
# for i in range(x, 0, -1):
#     if x % i == 0 and y % i == 0:
#         print(f'{i} 是最大公约数')
#         break

# # 下面<<欧几里得算法>>: 上面的求最大公约数有效率问题，比如x=9999998，y=9999999
# # 核心原理是：两个整数的最大公约数（GCD），等于其中较小数与两数相除余数的最大公约数。
# # 用数学公式表示：gcd(a,b) = gcd(b,a mod b). gcd: greatest common divisor
# a = int(input('a = '))
# b = int(input('b = '))
# while a % b != 0:
#     a, b = b, a % b     # a 变成原来的 b, b 变成余数 a%b
# print(f'{b} 是最大公约数')


# # 3. 猜数字
# answer = random.randrange(1, 101)
# counter = 0
# while True:
#     counter += 1
#     guess = int(input('please guess: '))
#     if guess > answer:
#         print('小一点')
#     elif guess < answer:
#         print('大一点')
#     else:
#         print(f'答对了，您猜了{counter}次!')
#         break


# 4. 斐波那契数列 Fibonacci sequence

def fabonacci(num):
    fab_nums = []
    a, b = 0, 1
    for i in range(0, num):
        fab_nums.append(a)
        a, b = b, a + b
    return fab_nums


print(fabonacci(1))
print(fabonacci(5))
print(fabonacci(8))
print(fabonacci(10))
print(fabonacci(15))
