import random
print("你有5000金币！")
num = random.randint(0,1000)
print("每猜错一次减去500金币，直扣完为止。15次没猜中，系统锁定，猜中加3000。")
money = 5000
i = 0
i = int(i)
while i < 15:
    number = input("请输入您要猜的数:")
    number = int(number)
    if i < 10:
        if number > num:
            money = money - 500
            print("大了，扣除500金币。剩余",money)
        elif number < num:
            money = money - 500
            print("小了，扣除500金币。剩余",money)
        elif number == num:
            money = money + 3000
            print("猜中数字增加3000金币。")
            break
    elif i>=10:
        print("输入的次数超过十次，系统锁定")
        break
    i=i+1




