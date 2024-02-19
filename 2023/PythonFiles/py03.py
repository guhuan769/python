# print("执行第一行")
# print(2/1)
# print("执行第三行啦")
# a = 123.22
# print(a)


"""

定义 f(x,y,z) = 3x + 2y +z -4 

求 f(1,2,3) = ??? 6
求 f(3,2,1) = ??? 10

相关概念:
形参:arg1,arg2,..
实参:实参1，实参2
.
缩进:行开头处的空白,可以用来表达程序的层级结构，一般一次缩进4个空格,Tab键实现
当函数被调用时，会将实参传递给对应的形参，然后执行函数体


定义函数格式:

def func_name(arg1,arg2,...):
    func_body

调用函数:
func_name()

return 的作用:
- 将return后面跟着的对象返回给函数调用方xd
"""


def f(x, y, z):
    # 3x+2y+z-4
    return 3 * x + 2 * y + z - 4


a = f(1, 2, 3)
print(a)

# 传关键字参数:实参会根据关键字传给同名的形参(与位置无)
# f(1, 2, 3)
# f(3, 2, 1)

# 如果位置参数和关键字参数同时存在，那么关键字参数一定药放在位置参数的后方
print(f(1, 2, z=3))
