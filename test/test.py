import random

amount = 10000

for i in range(1, 21):
    if amount <= 0:
        print(f"余额不足，活动结束！")
        break
    j = random.randint(1, 11)
    if j < 5:
        print(f"您的绩效分为{j}，不足5分，请继续努力！")
    else:
        amount -= 1000
        print(f"恭喜您，您是第{i}位员工，您的绩效分数为{j}，您获得了1000元工资！")
print(f"本次活动共发放{10000 -amount}元工资,还剩{amount}元未发放！")