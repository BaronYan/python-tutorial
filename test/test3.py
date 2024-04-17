# 定义一个变量，用来记录钱包的余额
balance = 1000

# 定义一个函数，用来计算余额
def calculate_balance():
    return balance

# 调用函数，打印余额
print(calculate_balance()) # 输出1000



# 定义一个函数，用来增加余额
def add_balance(amount):
    global balance # 声明全局变量
    balance += amount # 增加余额
    return balance


# 调用函数，增加1000元
print(add_balance(1000)) # 输出2000


# 调用函数，增加500元
print(add_balance(500)) # 输出2500


https://www.bilibili.com/video/BV1qW4y1a7fU?p=16&vd_source=e38682275909f351a497603a45ea21d2
P16 看完了