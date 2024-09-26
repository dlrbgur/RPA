import pandas as pd

data={'이름':['Kim','Park','Lee','Ho'],
    '국어':[90,58,88,100],
    '영어':[100,60,80,70],
    '수학':[55,65,76,88]}
print('1----------------------------------------')
df=pd.DataFrame(data)
print(df,end='\n\n')

print('2----------------------------------------')
name=df['이름']
print(name)

print('3----------------------------------------')
pscore=df.loc[1]
print(pscore)

print('4----------------------------------------')
revise=df.loc[df['이름']=='Ho','수학']=90
print(df,end="\n\n")

print('5----------------------------------------')
df.loc[4]=['Oh',100,70,80]
print(df,end="\n\n")

print('6----------------------------------------')
df=df.drop([2],axis=0)
print(df,end="\n\n")
#df.iloc(loc는 셀을 찾는다는 뜻) 뒤에[행표시(순서, 범위, 값, 리스트) , 열표시(순서) ]
#범위를 쓴다는것은 시작 : 끝 구조 라는 것이고 시작~끝-1 구조가 적용된다.
#ex)df.iloc[2]는 0행과 1행을 나타내는 것이다.
#ex2)df.iloc[0:3]은 0~2행 이라는 뜻
#ex3)df.iloc[[1,3]]
#ex1_1)df.iloc[:,1] :<==은 행을 전부 선택한다는 뜻이다
#ex1_2)df.iloc[:,0:2] 이건 "이름", "국어" 까지 라는 뜻이다.
#ex1_3)df.iloc[0:3,0:2] 2열 3행까지 사용하는것(태두리 제외)