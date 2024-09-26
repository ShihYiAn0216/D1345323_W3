a=int(input("請輸入一個三位數 :"))
b=a//100
c=a//10-b*10
d=a-b*100-c*10
print("每位數字的總和 :",b+c+d)