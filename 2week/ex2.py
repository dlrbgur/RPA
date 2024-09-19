a=123
b=15.556
print(a,"and",b,sep='@',end='\n\n')

print("a:{0} b:{1}".format(a,b))#포맷팅 방법들중 하나
#.format이라는 함수를 이용하는 방식이다.
#
print(f"a:{a}b:{b:2f}")#<-키워드를 이용하여 하는 방식

print(f"a:{a:05d} b:{b:2f}")
print("a:%05d b:%.2f"%(a,b))#<-연사를 이용하여 하는 방식
#출력하고자 할때 %d<-정수형태 %c<--실수형태로 사용 %s = 문자열형태