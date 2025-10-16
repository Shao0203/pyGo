import re
import random
import string
import math
import operator
import time
import functools
import json
import csv


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


##### -----~~~~~-----~~~~~-----~~~~~-----~~~~~-----~~~~~-----~~~~~#####
# # 2. 最大公约数 / 最小公倍数
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

# def gcd(a, b):
#     while a % b != 0:
#         a, b = b, a % b
#     return b


# def lcm(a, b):
#     return a * b // gcd(a, b)


# print(f'{gcd(36, 48)}是最大公约数')
# print(f'{lcm(36, 48)}是最小公倍数')


##### -----~~~~~-----~~~~~-----~~~~~-----~~~~~-----~~~~~-----~~~~~#####
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


##### -----~~~~~-----~~~~~-----~~~~~-----~~~~~-----~~~~~-----~~~~~#####
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


##### -----~~~~~-----~~~~~-----~~~~~-----~~~~~-----~~~~~-----~~~~~#####
# # 5. 寻找水仙花数narcissistic number,: 153 = 1**3+5**3+3**3, 1634 = 1**4+6**4+3**4+4**4
# 拆分一个数的小技巧 百位: num // 100  十位: num % 100 // 10   个位数: num % 10
# for num in range(100, 1000):
#     high = num // 100
#     mid = num % 100 // 10
#     low = num % 10
#     if num == high**3 + mid**3 + low**3:
#         print(num)


##### -----~~~~~-----~~~~~-----~~~~~-----~~~~~-----~~~~~-----~~~~~#####
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


##### -----~~~~~-----~~~~~-----~~~~~-----~~~~~-----~~~~~-----~~~~~#####
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


##### -----~~~~~-----~~~~~-----~~~~~-----~~~~~-----~~~~~-----~~~~~#####
# # 8. 6面色子掷6000次，记录每面多少次
# import random

# counters = [0] * 6
# for _ in range(6000):
#     face = random.randrange(1, 7)
#     counters[face - 1] += 1
# for face in range(1, 7):
#     print(f'{face}出现的次数是{counters[face-1]}次;')
# print(f'一共抛了{sum(counters)}次色子。')


##### -----~~~~~-----~~~~~-----~~~~~-----~~~~~-----~~~~~-----~~~~~#####
# # 9. 构造一个字典，用zip方式
# item1 = dict(zip('abcdefg', list(range(1, 8))))
# print(item1)
# item2 = dict(zip('abcdefg', '1234567'))
# print(item2)
# item2 = {x: x**3 for x in range(1, 6)}
# print(item2)


##### -----~~~~~-----~~~~~-----~~~~~-----~~~~~-----~~~~~-----~~~~~#####
# # 10. 查找一句话中每个字母出现字数，从高到低排序
# message = 'Man is distinguished, not only by his reason, but by this singular passion from other animals, which is a lust of the mind, that by a perseverance of delight in the continued and indefatigable generation of knowledge, exceeds the short vehemence of any carnal pleasure.'
# counter = {}
# for char in message:
#     if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
#         counter[char] = counter.get(char, 0) + 1
# # sorted_keys = sorted(counter, key=counter.get, reverse=True)
# # print(sorted_keys)
# # for key in sorted_keys:
# #     print(f'{key} 出现了 {counter[key]} 次.')
# result = sorted(counter.items(), reverse=True, key=lambda item: item[1])
# print(result)
# print(dict(result))


##### -----~~~~~-----~~~~~-----~~~~~-----~~~~~-----~~~~~-----~~~~~#####
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


##### -----~~~~~-----~~~~~-----~~~~~-----~~~~~-----~~~~~-----~~~~~#####
# # 12. 装饰器函数Decorator
# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print('Start')
#         result = func(*args, **kwargs)
#         print('End...')
#         return result
#     return wrapper


# @my_decorator
# def greeting(name, age):
#     return f'Hi {name}, you are {age} years old.'


# print(greeting('bright', 10))   # Start     End     Hi bright, you are 10 years old.


# def record_time(func):
#     # 想去掉装饰器的作用执行原函数, wraps函数放在wrapper函数上, 保留被装饰之前的函数,__wrapped__属性获得被装饰之前的函数
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f'{func.__name__}执行时间: {end - start:.2f}秒')
#         return result
#     return wrapper


# @record_time
# def download(filename):
#     print(f'开始下载{filename}.')
#     time.sleep(random.random() * 6)
#     print(f'{filename}下载完成.')


# @record_time
# def upload(filename):
#     print(f'开始上传{filename}.')
#     time.sleep(random.random() * 6)
#     print(f'{filename}上传完成.')

# # 调用装饰后的函数会记录执行时间
# download('test.pdf')
# upload('yy.avi')
# # 取消装饰器的作用不记录执行时间
# download.__wrapped__('MySQL必知必会.pdf')
# upload.__wrapped__('Python从新手到大师.pdf')


##### -----~~~~~-----~~~~~-----~~~~~-----~~~~~-----~~~~~-----~~~~~#####
# # 13. 递归Recursion， 阶乘math.factorial(5)
# def fac(num):
#     if num in (0, 1):   # 收敛条件
#         return 1
#     return num * fac(num - 1)   # 递归公式


# print(fac(5))

# 递归调用函数入栈
# 5 * fac(4)
# 5 * (4 * fac(3))
# 5 * (4 * (3 * fac(2)))
# 5 * (4 * (3 * (2 * fac(1))))
# 停止递归函数出栈
# 5 * (4 * (3 * (2 * 1)))
# 5 * (4 * (3 * 2))
# 5 * (4 * 6)
# 5 * 24
# 120

# def fac(num):
#     result = 1
#     for i in range(2, num + 1):
#         result *= i
#     return result

# print(fac(5))

# @functools.lru_cache()
# def fib(n):
#     # 执行性能糟糕, 所以用上面的lru_cache缓存执行结果从而避免在递归调用的过程中产生大量的重复运算
#     if n in (1, 2):
#         return 1
#     return fib(n-1) + fib(n-2)


# for i in range(1, 51):
#     print(fib(i))


##### -----~~~~~-----~~~~~-----~~~~~-----~~~~~-----~~~~~-----~~~~~#####
# # 14. pillow package to handle image in Python
# from PIL import Image
# from PIL import ImageFilter

# image = Image.open('Rabbit.jpeg')
# print(image.format)
# print(image.size)
# print(image.mode)
# # image.thumbnail((128, 128))
# # image.show()
# image.filter(ImageFilter.CONTOUR).show()
# # image.crop((80, 20, 310, 360)).show()


##### -----~~~~~-----~~~~~-----~~~~~-----~~~~~-----~~~~~-----~~~~~#####
# # 15. 正则表达式 re module

# username = input('请输入用户名: ')
# qq = input('请输入QQ号: ')
# m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
# if not m1:
#     print('请输入有效的用户名.')
# m2 = re.fullmatch(r'[1-9]\d{4,11}', qq)
# if not m2:
#     print('请输入有效的QQ号.')
# if m1 and m2:
#     print('你输入的信息是有效的!')

# sentence = 'Oh, shit! 你是傻逼吗? Fuck you.'
# purified = re.sub('fuck|shit|[傻煞沙][比笔逼叉缺吊碉雕]',
#                   '*', sentence, flags=re.IGNORECASE)
# print(purified)  # Oh, *! 你是*吗? * you.


# poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
# sentences_list = re.split(r'[，。]', poem)
# print(111, sentences_list)
# # 111 ['窗前明月光', '疑是地上霜', '举头望明月', '低头思故乡', '']
# # 222 ['窗前明月光', '疑是地上霜', '举头望明月', '低头思故乡']
# sentences_list = [sentence for sentence in sentences_list if sentence]
# print(222, sentences_list)
# for sentence in sentences_list:
#     print(sentence)


##### -----~~~~~-----~~~~~-----~~~~~-----~~~~~-----~~~~~-----~~~~~#####
# # 16. 从列表中找出最大的或最小的N个元素
# import heapq

# list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
# list2 = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
# print(heapq.nlargest(3, list1))
# print(heapq.nsmallest(3, list1))
# print(heapq.nlargest(2, list2, key=lambda x: x['price']))
# print(heapq.nsmallest(2, list2, key=lambda x: x['shares']))


##### -----~~~~~-----~~~~~-----~~~~~-----~~~~~-----~~~~~-----~~~~~#####
# # 16. itertools 模块
# import itertools
# # 产生ABCD的全排列
# permutation = itertools.permutations('ABCD')
# result = [item for item in permutation]
# print(result)
# # 产生ABCDE的五选三组合
# c5_3 = itertools.combinations('ABCDE', 3)
# result = [item for item in c5_3]
# print(result)
# # 产生ABCD和123的笛卡尔积
# di = itertools.product('ABCD', '123')
# result = [item for item in di]
# print(result)
# # 产生ABC的无限循环序列
# print(itertools.cycle(('A', 'B', 'C')))


##### -----~~~~~-----~~~~~-----~~~~~-----~~~~~-----~~~~~-----~~~~~#####
# # 16. collections 模块
# from collections import deque, namedtuple, Counter

# # deque：双端队列，是列表的替代实现。Python中的列表底层是基于数组来实现的，而deque底层是双向链表
# queue = deque([1, 2, 3])
# queue.appendleft('abc')
# left = queue.popleft()

# # namedtuple：命令元组，它是一个类工厂，接受类型的名称和属性列表来创建一个类。
# Position = namedtuple('Pos', ['x', 'y', 'z'])
# pos1 = Position(x=1, y=2, z=3)
# pos2 = Position(4, 5, 6)
# # print(pos1 < pos2)

# # Counter：dict的子类，键是元素，值是元素的计数，它的most_common()方法可以帮助我们获取出现频率最高的元素。
# words = [
#     'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
#     'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
#     'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
#     'look', 'into', 'my', 'eyes', "you're", 'under'
# ]
# counter = Counter(words)
# print(counter.most_common(3))
# # [('eyes', 8), ('the', 5), ('look', 4)] Return list of top 3 frequency words
