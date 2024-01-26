name = "itheima is a brand of itcast"
n = 0
for x in name:
    if x == "a":
        n += 1
print(int(n))

# range(num)    
# 获取一个从0开始，到num结束的数字序列（不含num本身）
# 如range(5)取得的数据是：【0，1，2，3，4】
# range(num1, num2)
# 获得一个从num1开始的，到num2结束的数字序列（不含num2b本身）
count = 0
for x in range(1, 100):
    if int(x)%2 == 0:
        count +=1
print(count)
    
        
    
    

        