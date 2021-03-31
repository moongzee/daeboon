import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt

pd.options.display.float_format='{;.4f}'.format #데이터 값 실수형 소수점 두째자리까지 표현

Train=pd.read_csv('/Users/jeongming/Desktop/3/run-1_Each_Epoch_Compare_Train_Loss-tag-1_Each_Epoch_Compare.csv')
Validation=pd.read_csv('/Users/jeongming/Desktop/3/run-1_Each_Epoch_Compare_Validation_Loss-tag-1_Each_Epoch_Compare.csv')


# Train=pd.read_csv('/Users/jeongming/Desktop/3/run-1_Each_Epoch_Compare_Train_Loss-tag-1_Each_Epoch_Compare.csv', encoding='utf-8')
# Validation=pd.read_csv('/Users/jeongming/Desktop/3/run-1_Each_Epoch_Compare_Validation_Loss-tag-1_Each_Epoch_Compare.csv', encoding='u')

step=Train['Step']
T_value=Train['Value']
V_value=Validation['Value']

plt.figure(figsize=(15,9)) # 캔버스 크기
plt.plot(step, T_value)
plt.plot(step, V_value)

y_t=Train.iloc[199,2]
y_v=Validation.iloc[199,2]

y_t4=y_t.astype('float16')
y_v4=y_v.astype('float16')


#plt.text(200,y_t,str(y_t))
#plt.text(200,y_v,str(y_v))

plt.annotate(str(y_t4),xy=(200,y_t),xytext=(200,0.1),arrowprops=dict(facecolor='lightblue', arrowstyle='->',connectionstyle='arc3'),size='10')
plt.annotate(str(y_v4),xy=(200,y_v),xytext=(200,0.025),arrowprops=dict(facecolor='orange', shrink=0.001),fontsize='10')
plt.ylabel('loss', fontsize=15, rotation=0, loc='top',fontweight='bold')
plt.xlabel('epoch', fontsize=15,fontweight='bold')
plt.yticks(np.arange(0,0.5,0.05))
plt.xticks(np.arange(0,200,25))
plt.legend(['Train','Validation'],fontsize=15)
plt.grid(True)

plt.title('Experiment 3', fontsize=20)
plt.show()