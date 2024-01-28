# 定义一个函数 calculator, 可以进行两个数值的加减乘除运算，用户可以进行选择
def add(num1, num2):
    return num1 + num2
def substract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        return "除数不能是零"


print("简易计算器")
print("选择1 是加法")
print("选择2 是减法")
print("选择3 是乘法")
print("选择4 是除法")
print("选择5 是退出")


while True:
    choice = input("请输入您要选择的运算 ")
    list = ["1","2","3","4"]
    if choice in list:
        num1 = float(input("请输入第一个值： "))
        num2 = float(input("请输入第二个值： "))
        if choice == "1":
            result = add(num1, num2)
        elif choice =="2":
            result = substract(num1, num2)
        elif choice =="3":
            result = multiply(num1, num2)
        elif choice =="2":
            result = divide(num1, num2)
        print(f"Result: {result}\n")
    elif choice == "5":
        break
    else:
        print("请输入有效的值")


        
        
    
                  
                
    
    

