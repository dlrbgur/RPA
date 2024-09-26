n = int(input("정수를 입력하세요"))
a=0
b=1
i=1
for i in range(1,n+1):
    a+=i
if(n<1):
    print("잘못입력하셨습니다.")
else:
    print(a)
