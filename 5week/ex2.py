import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

def addtext(x,y):
    for i in range(len(x)):
        plt.text(i,y[i]+0.5,y[i],ha='center')

hat = pd.read_csv('singer_youtube.csv')#hat변수에 데이터셋 입력


font_path="malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font',family=font_name)
plt.figure(figsize=(15,10))

plt.bar(hat['name'],hat['youtube count'],color=('red','orange','yellow','green','blue','navy','purple','black',))
plt.title('ha')
plt.xlabel('yout')
plt.ylabel('nam')

addtext(hat['name'],hat['youtube count'])
plt.show()
