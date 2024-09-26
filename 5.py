a=int(input("輸入三位數字:"))
b=a//100
c=a//10-b*10
d=a-b*100-c*10
print("結果:", d*100+c*10+b)