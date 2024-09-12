import pandas as pd
col_names=['과목번호','과목명','강의실','시간수']#list형태로 넣는것이고
#행 단위로 묶어서 리스트를 만드는것. 한 줄씩 채우는거.
list1=list([['C1','인공지능개론','R1',3],
        ['C2','웃음치료','R2','2'],
        ['C3','경영학','R3','3'],
        ['C4','3D디자인','R4','4'],
        ['C5','스포츠경영','R2','2'],
        ['C6','예술의 세계','R3','1']
])
#csv파일은 ","로 형성 되어있는 것들
df=pd.DataFrame(list1,columns=col_names)
print(df)

data={#열중심으로 채우는것 (키와 값이 존재한다.)컬럼이 생긴 이유도 컬럼의 값이 없어서 만들어 주는것.
    '과목번호' :['C1','C2','C3','C4','C5','C6'],
            '과목명' :['인공지능개론','웃음치료','경영학','3D디자인','스포츠경영','예술의 세계'],
            '강의실' :['R1','R2','R3','R4','R2','R3'],
            '시간수' :[3,2,3,4,2,1]}
df=pd.DataFrame(data)
print(df, end='\n\n')

sr_name=df['과목명']
print(sr_name,end='\n\n')

sr_no=df.loc[2]
print(sr_no,end='\n\n')

cell_name=df.loc[2]['과목명']
print(cell_name)

df.to_csv('file.csv',index=False)#내용을 csv로 만들어서 탐색기에 올려서 나타냄.

print("########################################################")

df['담당교수']=['홍길동','김철수','이영희','박영수','최영희','김영수']
print(df,end='\n\n')

df.loc[6]=['C7','통계학','R7',3,'이철수']
print(df,end='\n\n')

df1=df.drop(['강의실'],axis=1)
print(df1,end='\n\n')

df2=df.drop([5],axis=0)
print(df1,end='\n\n')
print("########################################################")

print(df.loc[0:2],end='\n\n')#0,1,2까지 출력이 됨. iloc일때만 1까지 출력
#이 것만 0~2까지 출력됨.
#iloc에만 숫자에대한 의미가 있다.(iloc는 순서에 관해서+@)
print(df.loc[0:2],end='\n\n')

#print(df[['과목명','담당교수']],end='\n\n')
print(df.loc[:,'강의실':'담당교수'],end='\n\n')