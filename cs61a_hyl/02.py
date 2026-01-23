def ex():
    """
    >>> pow(2, 10)
    1024
    >>> max = pow    # 知识点1：函数别名
    >>> pow(2, 10)
    1024
    >>> pow = max    # 知识点2：变量重新赋值
    >>> pow(2, 10)
    1024
    >>> max = pow    # 这里的 max 依然指向原 pow 函数
    >>> pow(2, 10)
    1024

    >>> def g(y):
    ...     x = 2 * y      # 局部变量 x
    ...     return x + 1
    ... 
    >>> x = 2              # 全局变量 x
    >>> g(x)               # 调用 g(2)，内部 x 变成 4，返回 5
    5
    >>> g(3 * x) + 3       # g(6) -> 内部 x=12 -> 返回 13; 13+3=16
    16
    >>> x                  # 知识点3：局部作用域不影响全局
    2
    """
    pass

# 函数名（如 pow）只是一个指向函数对象的标签。你可以把 pow 赋值给 max，
# 此时 max 和 pow 指向同一个功能相同的函数对象。
# 重新赋值 pow 不会影响 max，因为 max 仍然指向原来的函数对象。

# https://pythontutor.com/cp/composingprograms.html#code=def%20g%28y%29%3A%0A%20%20%20%20x%20%3D%202%20*%20y%0A%20%20%20%20return%20x%20%2B%201%0A%20%20%20%20%0Ax%20%3D%202%0Aprint%28g%28x%29%29%0Aprint%28g%283%20*%20x%29%20%2B%203%29%0A&cumulative=true&curInstr=0&mode=display&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%5D

# Name conflicts

from operator import mul

def square(square):
    return mul(square, square)
square(3)
'''LEGB 规则：Python 查找 变量名 的顺序是 Local (局部) -> Enclosing (嵌套) -> Global (全局) -> Built-in (内置)。

参数屏蔽：函数定义 def square(square): 中，参数名 square（局部变量）屏蔽了函数名 square（全局变量）。

在函数内部执行 mul(square, square) 时，Python 看到的 square 是传入的数字 3，而不是函数本身。

这虽然合法，但不是好的编程习惯，容易让人困惑。'''


# https://pythontutor.com/cp/composingprograms.html#code=from%20operator%20import%20mul%0Adef%20square%28square%29%3A%0A%20%20%20%20return%20mul%28square,%20square%29%0Aprint%28square%283%29%29&cumulative=true&curInstr=0&mode=display&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%5D

# Multiple Assignment

def diff(x, y):
    x, y = y, x    # 交换 x 和 y 的值
    return y - x

# 测试过程：
# >>> x, y = 6, 1        # 初始化：x=6, y=1
# >>> x, y = y, x-y      # 关键点：先计算右边，再赋值给左边
#     右边计算：y=1, x-y=5
#     赋值：x变成了1, y变成了5
# >>> diff(y, x)         # 调用 diff(5, 1)
#     进入 diff(5, 1):
#         参数 x=5, y=1
#         x, y = y, x -> x变1, y变5
#         return y - x -> 5 - 1 = 4
    
# https://pythontutor.com/cp/composingprograms.html#code=def%20diff%28x,%20y%29%3A%0A%20%20%20%20x,%20y%20%3D%20y,%20x%0A%20%20%20%20return%20y%20-%20x%0A%20%20%20%20%0Ax,%20y%20%3D%206,%201%0Ax,%20y%20%3D%20y,%20x-y%0Aprint%28diff%28y,%20x%29%29&cumulative=true&curInstr=0&mode=display&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%5D

# Print and None

def triple(x):
    return x # 没有 print，只有返回值

def noisy(x):
    print('NOISY', x) # 副作用：打印输出
    return x + 1      # 返回值

# >>> noisy(noisy(2) + noisy(3))
# 执行顺序：
# 1. 先执行内部的 noisy(2):
#    - 打印 "NOISY 2"
#    - 返回 3
# 2. 再执行内部的 noisy(3):
#    - 打印 "NOISY 3"
#    - 返回 4
# 3. 计算中间结果：3 + 4 = 7
# 4. 最后执行外层的 noisy(7):
#    - 打印 "NOISY 7"
#    - 返回 8 
# 交互式环境（如终端），最后一行代码的返回值会自动显示出来（所以最后看到了 8）

# Small expressions

def f(x):
    return x - 1
def g(x):
    return 2 * x
def h(x, y):
    return int(str(x) + str(y)) # 如果 x=2, y=3，则返回 23

class Number:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def calls(self): # 不是函数，而是方法 o.calls()而不是 calls(o)
        return 0

    def chars(self): # 表达式的复杂度（用了多少次函数调用，字符长度
        return 1

class Call:
    """A call expression.
    __str__：决定了 print(对象) 时显示什么（例如显示 "f(5)" 而不是 <Object at 0x...>）"""
    def __init__(self, f, operands):
        self.f = f
        self.operands = operands # list of expressions
        self.value = f(*[e.value for e in operands]) # 如add(*[5, 10])

    def __str__(self):
        return f'{self.f.__name__}({",".join(map(str, self.operands))})' # 如打印出 f(5,10)
# 把 operands 列表里的每一个对象都变成字符串，然后用逗号连接起来 如列表是 ['5', '5']，连起来就变成了 "5,5"
# 对象.方法()
# map(功能函数, 列表)
# # 这里的 self.f.__name__ 会自动变成 "f"、"g" 或 "h"
    def calls(self):
        return 1 + sum(o.calls() for o in self.operands)

    def chars(self):
        return 3 + sum(o.chars() for o in self.operands) + (len(self.operands) - 1)
# 字符长度 = 函数名+括号(3个字符) + 参数的长度 + 逗号的数量 h(5, 5)
def smalls(n):
    if n == 0:
        yield Number(5) # yield 不结束执行 而暂时中断函数执行的return
    else:
        for operand in smalls(n-1): # n-1 级别的所有表达式
            yield Call(f, [operand]) # n 级别的表达式
            yield Call(g, [operand])
        for k in range(n):
            for first in smalls(k):# 如5
                for second in smalls(n-k-1):# 如5
                    if first.value > 0 and second.value > 0:
                        yield Call(h, [first, second])

def print_smallest():
    result = []
    for i in range(9): # 尝试复杂度从 0 到 8
        result.extend([e for e in smalls(i) if e.value == 2024])

    for e in result:
        assert eval(str(e)) == e.value
        print(e, '->', e.value, 'has', e.calls(), 'calls and', e.chars(), 'characters.')

gen = smalls(1) # 生成器对象 可以 list(gen) 查看所有元素 或者for遍历

for item in gen:
    # 每次循环，gen 会吐出一个对象给 item
    # 此时 item 就是实实在在的 Call 对象了
    print(f"拿到一个对象: {item}, 它的值是: {item.value}")
'''拿到一个对象: f(5), 它的值是: 4
拿到一个对象: g(5), 它的值是: 10
拿到一个对象: h(5,5), 它的值是: 55'''
# 当函数中包含yield时，它就变成了一个生成器函数，
# 执行时返回一个生成器对象，而不是立即执行函数体内的代码
list_a = [1, 2]
list_b = [3, 4]

# 用 append
list_a.append(list_b)
print(list_a) 
# 输出: [1, 2, [3, 4]]  <- 注意：列表里套了个列表

# 用 extend (我们要的)
list_a = [1, 2] # 重置
list_a.extend(list_b)
print(list_a)
# 输出: [1, 2, 3, 4]    <- 注意：所有元素融合在一起了


def dumpling_machine():
    # --- 机器启动区 ---
    print("  [机器] 1. 开始工作，正在捏第一个饺子...")
    yield "饺子A"  
    # 【暂停点 1】机器停在这里！把 "饺子A" 递出去，然后冻结状态。
    
    # --- 中间休息区 ---
    print("  [机器] 2. 你拿走了A，我继续做第二个...")
    yield "饺子B"
    # 【暂停点 2】机器停在这里！把 "饺子B" 递出去，然后冻结状态。
    
    # --- 结束区 ---
    print("  [机器] 3. 做完了，下班！")
    # 函数结束，如果再有人还要吃，就会报错 (StopIteration)

# ================= 华丽的分割线 =================

# 1. 实例化：这行代码只是把机器买回家，机器根本没通电，一行代码都不会跑
gen = dumpling_machine() 

print("---- 我要吃第一个 ----")
# 2. 第一次索取：调用 next(gen)
#    机器从头开始跑，跑到 【暂停点 1】 停下
#    机器吐出 "饺子A"，被 print 打印在屏幕上
print(next(gen)) 

print("\n---- 我要吃第二个 ----")
# 3. 第二次索取：调用 next(gen)
#    机器从 【暂停点 1】 醒来！
#    先执行 yield 后面的 print("...你拿走了A...")
#    然后跑到 【暂停点 2】 停下
#    机器吐出 "饺子B"，被 print 打印在屏幕上
print(next(gen))


def simple_generator():
    yield 1
    yield 2
    yield 3

# 使用生成器
gen = simple_generator()
print(type(gen))  # <class 'generator'>

# 获取生成器的值
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
# print(next(gen))  # 如果再执行一次会抛出StopIteration异常

def stateful_generator():
    """展示yield如何保持函数状态"""
    value = 0
    while True:
        received = yield value
        if received is not None:
            value = received
        value += 1

gen = stateful_generator()
next(gen)  # 初始化生成器

print(next(gen))  # 输出: 1
print(next(gen))  # 输出: 2
print(gen.send(10))  # 发送10给生成器，输出: 11
print(next(gen))  # 输出: 12