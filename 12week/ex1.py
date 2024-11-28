import pandas as pd
from sklearn.model_selection import train_test_split

w = pd.read_csv('ch5-1.csv')
x_data=w.iloc[:,2:5].values#독립변수(결과가 되는 변수)
#
y_data=w.iloc[:,1].values#weight이다

x_train, x_test, y_train, y_test=train_test_split(x_data,y_data,test_size=0.2)
#학습에 사용되는건 x_train과y_train이다.
#test_size=0.2<-이 말이 테스트사이즈를 20퍼센트를 사용하겠다.

from sklearn.neural_network import MLPRegressor
model_mlp = MLPRegressor().fit(x_train,y_train)
#실질적으로 학습이 되고 있는 부분은 여기이다. fit(학습데이터)
y_pred_mlp=model_mlp.predict(x_test)
#x_test를 가지고 시험 데이터를 예측

df_x_test=pd.DataFrame(x_test,columns=['egg_weight','movement','food'])
df_y_pred=pd.DataFrame(y_pred_mlp,columns=['perdict'])
df_y_test=pd.DataFrame(y_test,columns=['real'])
df=pd.concat([df_x_test,df_y_pred],axis=1)
print(df,end='\n\n')

from sklearn.metrics import r2_score
R2=r2_score(y_test,y_pred_mlp)
#검증하는 부분. 정답과 비슷한지 검증하는것.
print("R2 = ",R2,end='\n\n')