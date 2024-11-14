#상관분석-관계성 =>"ㅇㅇㅇ과ㅁㅁㅁ 간 관계"ㅇ=독립변수 ㅁ=종속변수
#회귀분석-인과성=>"ㅇㅇㅇ가ㅁㅁㅁ 미치는 영향"

#회귀분석에서는 독립변수를x 결과를 y로 저장한다.
#x1,x2,x3처럼 늘어난다.

#회귀분석과 상관분석은 선형이라는 점이다.
# (직선으로 그어서 판단 한다는 것.)+회귀분석은 예측!!(직선 방정식으로)

# 상관분석은 관계를 파악하는 것.

# ex)데이터를 보고 가장 비슷하게 그어진게 정답이다.
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

w = pd.read_csv('ch5-1.csv')
w_n = w.iloc[:, 1:5]

model_lm=smf.ols(formula='weight~ egg_weight',data=w_n)#시험 여기서 나옴 무조건!!!
#formula에서 "결과 ~ 원인" 순서 중요하니 외워두기.
result_lm=model_lm.fit()#fit로학습을 시키고 리절트에 담는것.
result_lm.summary()#결과 담당.

print(result_lm.summary())

plt.figure(figsize=(10,7))
plt.scatter(w.egg_weight,w.weight,alpha=.5)
plt.plot(w.egg_weight,w.egg_weight*2.3371-14.5475,color='red')
plt.text(66,132,'weight=2.337legg_weight-14.5475',fontsize=12)
plt.title('Sctter Plot')
plt.xlabel('egg_weight')
plt.ylabel('weight')
plt.show()