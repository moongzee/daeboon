from pandas_profiling import ProfileReport
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as ss

DATA=pd.read_csv('C:/Users/imagoworks-moongzeee/Desktop/과제/2021.01.21 과제/EDA_DATA.csv')


DATA['real']=DATA['real'].astype(object)
DATA['guess']=DATA['guess'].astype(object)
DATA['Accuracy']=DATA['Accuracy'].astype(object)
#print(DATA.info())
#print(DATA.head())


## 불리언 배열을 사용한 ddh와 daeyou 데이터 필터링
cat_ddh = DATA.category=='ddh'
cat_daeyou = DATA.category=='daeyou'

pointer=DATA[(DATA.real==0) & (DATA.category=='ddh')]



## 카이제곱 검정을 이용해 ddh/daeyou의guess 와 accuracy 범주 교차분석

#result1=pd.crosstab(DATA_ddh.guess,DATA_ddh.Accuracy)
#a=ss.chi2_contingency(observed=result1)

#print('ddh_guess와 accurcy 간의 chi-Square:'+str(a[0]))
#print('p-value:'+str(a[1]))
#print('degree of freedom:'+str(a[2]))
#print('expectation array:\n'+str(a[3]))

#result2=pd.crosstab(DATA_daeyou.guess,DATA_daeyou.Accuracy)
#a=ss.chi2_contingency(observed=result2)

#print('daeyou_guess와 accurcy 간의 chi-Square:'+str(a[0]))
#print('p-value:'+str(a[1]))
#print('degree of freedom:'+str(a[2]))
#print('expectation array:\n'+str(a[3]))




## daeyou/ddh pointer t-test

#tg_ddh=aa['y']
#tg_daeyou=aa['y']



#등분산성 계산 
#print(ss.levene(tg_ddh,tg_daeyou))
#print(ss.fligner(tg_ddh,tg_daeyou))
#print(ss.bartlett(tg_ddh,tg_daeyou))


#t-test
#print(ss.ttest_ind(tg_ddh, tg_daeyou, equal_var=False))







## ddh&daeyou 연속데이터 복센그래프 (향상된 상자그림) // 데이터의 이상치 파악
#sns.set(style='white')

#fig, axs=plt.subplots(nrows=3, figsize=(10,8))
#sns.boxenplot(DATA_ddh.x, ax=axs[0])
#sns.boxenplot(DATA_ddh.y, ax=axs[1])
#sns.boxenplot(DATA_ddh.z, ax=axs[2])
#fig.savefig(r'C:\Users\imagoworks-moongzeee\Desktop\과제\2021.01.21 과제\ddh x,y,z boxenplot.png', dpi=300)


#fig, axs=plt.subplots(nrows=3, figsize=(10,8))
#sns.boxenplot(DATA_daeyou.x, ax=axs[0])
#sns.boxenplot(DATA_daeyou.y, ax=axs[1])
#sns.boxenplot(DATA_daeyou.z, ax=axs[2])
#fig.savefig(r'C:\Users\imagoworks-moongzeee\Desktop\과제\2021.01.21 과제\daeyou x,y,z boxenplot.png', dpi=300)

