slang = {"觉醒年代":"还不错的战争片", "YYDS":"永远的神"}
slang["双减"] = "进一步缩减作业"
query = input("请输入你想查询的流行语: ")
if query in slang:
    print("您查询的" + query + "含义如下")
    print(slang[query])
else:
    print("您查询的流行语暂时未收录")


i=0
while i < 10:
    print("我喜欢你")
    i += 1
sum=0
l=1
while l <= 10:
    sum += l
    l += 1
print(sum)