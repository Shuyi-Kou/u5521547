mood_index = int(input("对象今天的心情指数是： "))
if mood_index >= 60:
    print("恭喜，今晚可以打游戏")
else:
    print("为了自个儿不打了")
user_weight = float(input("请输入您的体重 (单位： kg) ： "))
user_height = float(input("请输入您的身高 (单位： m) ： "))
user_BMI = user_weight /(user_height) ** 27
print("您的BMI值为： " + str(user_BMI))
if user_BMI <= 18.5:
    print("此时BMI值属于偏瘦范围")
elif 18.5 < user_BMI <= 25:
    print("此时BMI属于正常范围")
elif 25 < user_BMI <= 30:
    print("此时BMI值属于偏胖范围")
else:
    print("此时BMI属于肥胖范围")
    
shopping_list = []
shopping_list.append("键盘")
shopping_list.append("鼠标")
shopping_list.remove("鼠标")
shopping_list.append("电竞椅")
shopping_list[1] = "硬盘"

print(shopping_list)
print(len(shopping_list))
print(shopping_list[0])


    