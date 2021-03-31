import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 
import pandasql as psql 

#파일 불러오기
ddh=pd.read_csv(r'C:\Users\imagoworks-moongzeee\Desktop\과제\2021.01.21 과제\ddh-eda.csv')
daeyou=pd.read_csv(r'C:\Users\imagoworks-moongzeee\Desktop\과제\2021.01.21 과제\daeyou-eda.csv')

#ddh, daeyou dataframe
ddh.columns=['x','y','z','gt','guess']
daeyou.columns=['x','y','z','gt','guess']
ddh['category']='ddh'
daeyou['category']='daeyou'

#ddh와 daeyou의 gt&guess 열을 비교하기 위해 numpy로 변환
ddh_gt=np.array(ddh['gt'])
ddh_guess=np.array(ddh['guess'])
daeyou_gt=np.array(daeyou['gt'])
daeyou_guess=np.array(daeyou['guess'])

#ddh, daeyou의 gt와 guess를 비교해 boolean형태로 반환
ddh_A=pd.Series(ddh_gt==ddh_guess)
daeyou_A=pd.Series(daeyou_gt==daeyou_guess)

#gt와 guess 비교한 accuracy 열 DATA dataframe에 삽입
ddh['Accuracy']=ddh_A
daeyou['Accuracy']=daeyou_A

#merge
DATA=pd.concat([ddh,daeyou],ignore_index=True)


#만든 daeyou,ddh 데이터 csv파일 변환
#DATA.to_csv(r'C:\Users\imagoworks-moongzeee\Desktop\과제\2021.01.21 과제\EDA_DATA.csv')




#ddh, daeyou data갯수 dataframe
Data_count=pd.DataFrame(
                            {'ddh_data': [ddh.shape[0]],
                            'daeyou_data': [daeyou.shape[0]]
                            }
)





ddh_pointer=np.array(ddh['gt'].value_counts(sort=False, ascending=True, normalize=False))
ddh_pointer_per=np.array(ddh['gt'].value_counts(sort=False, ascending=True, normalize=True))
daeyou_pointer=np.array(daeyou['gt'].value_counts(sort=False, ascending=True, normalize=False))
daeyou_pointer_per=np.array(daeyou['gt'].value_counts(sort=False, ascending=True, normalize=True))


#ddh 포인터 갯수 daeyou 갯수와 같게 만들어서 예측치
ddh_=np.array(ddh['gt'].value_counts(sort=False, ascending=True, normalize=False))*(daeyou.shape[0]/ddh.shape[0])
ddh_predict=ddh_.astype('int64')


#포인터 추출
gt_=ddh['gt'].unique()
gt=np.sort(gt_)


pointer_count=pd.DataFrame(
                            {
                            'pointer' : gt,
                            'ddh_pointer(count)' : ddh_pointer,
                            'ddh_pointer(percent)' : ddh_pointer_per,
                            'ddh_pointer_predict(count)' : ddh_predict,
                            'daeyou pointer(count)' : daeyou_pointer,
                            'daeyou pointer(percent)' : daeyou_pointer_per,
                            'distance(count)' : ddh_predict - daeyou_pointer,
                            'distance(percent)' : ddh_pointer_per - daeyou_pointer_per
                            }
)


Accuracy=pd.DataFrame(
    {'ddh count' :ddh_A.value_counts(normalize=False),
    'ddh percent':ddh_A.value_counts(normalize=True),
    'daeyou count':daeyou_A.value_counts(normalize=False),
    'daeyou percent':daeyou_A.value_counts(normalize=True)}
)


print(Data_count)
#print(pointer_count)
print(Accuracy)



#pointer_count와 Accuracy csv파일로 생성
#pointer_count.to_csv(r'C:\Users\imagoworks-moongzeee\Desktop\과제\2021.01.21 과제\pointer_count.csv')
#Accuracy.to_csv(r'C:\Users\imagoworks-moongzeee\Desktop\과제\2021.01.21 과제\Accuracy.csv')




#daeyou 좌표값 2D-scatter 
#N=daeyou.shape[0]
#x=daeyou['x']
#y=daeyou['y']
#colors=np.random.rand(N)
#area=(1*np.random.rand(N))**2

#plt.scatter(x,y,s=area,c=colors,alpha=0.1)
#plt.show()

#ddh 좌표값 2D-scatter
#N=ddh.shape[0]
#x=ddh['x']
#y=ddh['y']
#colors=np.random.rand(N)
#area=(1*np.random.rand(N))**2

#plt.scatter(x,y,s=area,c=colors,alpha=0.1)

#plt.show()