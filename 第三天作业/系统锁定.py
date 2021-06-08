name = "root"
password = "admin"
i = 0
while i < 3:
    a = input("请输入用户名:")
    p = input("请输入密码:")
    if a == name and password == p:
        print("系统登录成功")
        break
    else:
        print("密码错误，请重新输入。")
        i = i + 1
else:
    print("输入错误密码超过三次，系统已锁定！")