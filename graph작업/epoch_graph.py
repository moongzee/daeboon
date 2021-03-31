import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

#Train / Validation epoch csv가져오기
Train=pd.read_csv(r'C:\Users\imagoworks-moongzeee\Desktop\exp\CBCT\exp15\run-1_Each_Epoch_Loss_Train_Loss-tag-1_Each_Epoch_Loss.csv')
Validation=pd.read_csv(r'C:\Users\imagoworks-moongzeee\Desktop\exp\CBCT\exp15\run-1_Each_Epoch_Loss_Validation_Loss-tag-1_Each_Epoch_Loss.csv')

step=Train['Step']
T_value=Train['Value']
V_value=Validation['Value']


loss=pd.DataFrame({'step':step,'T_value':T_value,'V_value':V_value})

print(loss)

y_t=loss.iloc[step.count()-1,1]
y_v=loss.iloc[step.count()-1,2]

y_t4=y_t.astype('float16')
y_v4=y_v.astype('float16')



sns.set_theme(context='poster',style='darkgrid',palette='tab10',font_scale=1,color_codes=True)
plt.figure(figsize=(15,9))
sns.lineplot(x='step',y='T_value',data=loss, palette='winter')
sns.lineplot(x='step',y='V_value',data=loss, palette='winter')
plt.xticks(np.arange(1,step.count()+1,1))
#plt.yticks(np.arange(0,1,0.2))
#xytext는 annotate할 텍스트 위치로, 데이터마다 위치조절이 필요함.
plt.annotate(str(y_t4),xy=(step.count(),y_t),xytext=(step.count()+0.5,y_t),arrowprops=dict(color='navy',arrowstyle='-|>',connectionstyle='arc3'),size='20',xycoords='data')
plt.annotate(str(y_v4),xy=(step.count(),y_v),xytext=(step.count()+0.5,y_v),arrowprops=dict(color='orangered',arrowstyle='-|>',connectionstyle='arc3'),size='20',xycoords='data')
plt.ylabel('loss', fontsize=20, rotation=0, loc='top',fontweight='bold')
plt.xlabel('epoch', fontsize=20,fontweight='bold')
plt.legend(['Train','Validation'],fontsize=25)

#그래프 제목
plt.title('Experiment 15', fontsize=25)

plt.show()

