#-*-coding:utf-8-*-
# page 19

def factorial(n, product=1):
    if n == 1:
        return product
    else:
        return factorial(n-1, n * product)

# 递归求阶乘，输入n输出n!。函数不应该有参数product。
# 采用函数嵌套，将参数product隐藏在内部函数中。
def factorial_2(n):
    def recurse(n, product=1):
        if n == 1:
            return product
        else:
            return factorial(n - 1, n * product)
    return recurse(n)

# 书中该例子不恰当，阶乘可以很便捷的实现。书中是为了讲嵌套。
def factorial_3(n):
    if n == 1:
        return 1
    else:
        return n*factorial_3(n-1)


# print(factorial(4))
# print(factorial_2(4))
# print factorial_3(4)
a = factorial_3(4)
