import random


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


# # 4. 斐波那契数列 Fibonacci sequence
# # 4.1
# def fibonacci(num):
#     fib_nums = []
#     a, b = 0, 1
#     for _ in range(num):
#         fib_nums.append(a)
#         a, b = b, a + b
#     return fib_nums


# print(fibonacci(1))
# print(fibonacci(5))
# print(fibonacci(10))

# # 4.2
# def fibonacci(n):
#     """
#     返回第n个斐波那契数
#     约定: F(0)=0, F(1)=1, F(2)=1, ...
#     """
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)


# print(fibonacci(9))

# 4.3
# a, b = 0, 1
# for _ in range(20):
#     print(a)
#     a, b = b, a + b


# # 5. 寻找水仙花数narcissistic number,: 153 = 1**3+5**3+3**3, 1634 = 1**4+6**4+3**4+4**4
# 拆分一个数的小技巧 百位: num // 100  十位: num % 100 // 10   个位数: num % 10
# for num in range(100, 1000):
#     high = num // 100
#     mid = num % 100 // 10
#     low = num % 10
#     if num == high**3 + mid**3 + low**3:
#         print(num)


# # 6. 数字反转: 12389 -> 98321
# # num		reversed_num
# # 12389	0
# # 1238 	0*10 + 9 = 9
# # 123 	9*10 + 8 = 98
# # 12 		98*10 + 3 = 983
# # 1 		983*10 + 2 = 9832
# # 0 		9832*10 + 1 = 98321
# num = int(input('num = '))
# reversed_num = 0
# while num > 0:
#     reversed_num = reversed_num * 10 + num % 10
#     num = num // 10
# print(reversed_num)


# # 7. 百钱百鸡问题
# for x in range(0, 21):
#     for y in range(0, 34):
#         for z in range(0, 100, 3):
#             if x + y + z == 100 and 5 * x + 3 * y + z // 3 == 100:
#                 print(f'公鸡: {x}只, 母鸡: {y}只, 小鸡: {z}只')

# for x in range(0, 21):
#     for y in range(0, 34):
#         z = 100 - x - y
#         if z % 3 == 0 and 5 * x + 3 * y + z // 3 == 100:
#             print(f'公鸡: {x}只, 母鸡: {y}只, 小鸡: {z}只')


# # 8. 6面色子掷6000次，记录每面多少次
# import random

# counters = [0] * 6
# for _ in range(6000):
#     face = random.randrange(1, 7)
#     counters[face - 1] += 1
# for face in range(1, 7):
#     print(f'{face}出现的次数是{counters[face-1]}次;')
# print(f'一共抛了{sum(counters)}次色子。')


# # 9. 构造一个字典，用zip方式
# item1 = dict(zip('abcdefg', list(range(1, 8))))
# print(item1)
# item2 = dict(zip('abcdefg', '1234567'))
# print(item2)
# item2 = {x: x**3 for x in range(1, 6)}
# print(item2)


# # 10. 查找一句话中每个字母出现字数，从高到低排序
# message = 'Man is distinguished, not only by his reason, but by this singular passion from other animals, which is a lust of the mind, that by a perseverance of delight in the continued and indefatigable generation of knowledge, exceeds the short vehemence of any carnal pleasure.'
# counter = {}
# for letter in message:
#     if 'A' <= letter <= 'Z' or 'a' <= letter <= 'z':
#         counter[letter] = counter.get(letter, 0) + 1
# # sorted_keys = sorted(counter, key=counter.get, reverse=True)
# # print(sorted_keys)
# # for key in sorted_keys:
# #     print(f'{key} 出现了 {counter[key]} 次.')
# result = sorted(counter.items(), reverse=True, key=lambda item: item[1])
# print(result)
# print(dict(result))


# # 11. 股票排序筛选高价
# stocks = {
#     'AAPL': 191.88,
#     'GOOG': 1186.96,
#     'IBM': 149.24,
#     'ORCL': 48.44,
#     'ACN': 166.89,
#     'FB': 208.09,
#     'SYMC': 21.29
# }
# high_stocks = {stock for stock in stocks.items() if stock[1] > 100}
# print(high_stocks)
# stock2 = {key: value for key, value in stocks.items() if value > 100}
# print(stock2)
# stock3 = {key: value for key, value in sorted(
#     stocks.items(), key=lambda item: item[1], reverse=True) if value > 100}
# print(stock3)
# sorted_stocks = dict(sorted(stocks.items(), key=lambda x: x[1], reverse=True))
# print(sorted_stocks)
