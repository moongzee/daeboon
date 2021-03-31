from bokeh.models import Legend
from bokeh.core.properties import value
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, LabelSet
from bokeh.plotting import figure
from bokeh.transform import dodge
from bokeh.models import Legend,axes
import pandas as pd 
import seaborn as sns
from matplotlib import pyplot as plt


# 파일 불러와서 center별 score 평균값 dataframe 만들기

df=pd.read_csv(r'C:\Users\imagoworks-moongzeee\Desktop\exp\CBCT\exp15\exp15_result_eval.csv')

df.rename(columns={'Unnamed: 0':'center'},inplace=True)
df['a']=df.center.str.split('/').str[7]
df['Center']=df.a.str.split('\\').str[0]

b=df.drop(['center','a'],axis=1)
c=b.groupby('Center').mean()
c.reset_index(level=0,inplace=True)
d=c.round(decimals=3)
#print(d)



#그래프 그리기 시작
output_file('dodged_bars.html')

output_file("dodged_bars.html")

Score = ['PixelAccuracy','IOU','DiceCoefficient']
Center = d['Center'].tolist()

data = {'Score' : Score,
        'CBCT-CAU'   : d.iloc[0,1:].tolist(),
        'MDCT-KEOSAN'   : d.iloc[1,1:].tolist(),
        'MDCT-KHU'   : d.iloc[2,1:].tolist()}

source = ColumnDataSource(data=data)
tools='wheel_zoom reset save'.split()

#그래프 툴 (타이틀 이름 변경해야함)
p = figure(x_range=Score, y_range=(0,1.1), plot_height=400, plot_width=600, title="Mean value of score_exp15",
           toolbar_location='right', tools=tools) 


p.title.text_font_size = '15pt'
p.title.align='center'
p.xaxis.major_label_text_font_size = "20px"

labels15=LabelSet(x=dodge('Score', -0.25, range=p.x_range),y='CBCT-CAU',text='CBCT-CAU',source=source,text_align='center',text_font_size='13pt')
labels16=LabelSet(x=dodge('Score', 0.0, range=p.x_range),y='MDCT-KEOSAN',text='MDCT-KEOSAN',source=source,text_align='center',text_font_size='13pt')
labels17=LabelSet(x=dodge('Score', 0.25, range=p.x_range),y='MDCT-KHU',text='MDCT-KHU',source=source,text_align='center',text_font_size='13pt')



r0=p.vbar(x=dodge('Score', -0.25, range=p.x_range), top='CBCT-CAU', width=0.2, source=source,
       color="#c9d9d3")

r1=p.vbar(x=dodge('Score',  0.0,  range=p.x_range), top='MDCT-KEOSAN', width=0.2, source=source,
       color="#718dbf")

r2=p.vbar(x=dodge('Score',  0.25, range=p.x_range), top='MDCT-KHU', width=0.2, source=source,
       color="#e84d60")




legend=Legend(items=[('CBCT-CAU',[r0]),('MDCT-KEOSAN',[r1]),("MDCT-KHU",[r2])])
p.add_layout(legend,'below')
p.x_range.range_padding = 0.01
p.xgrid.grid_line_color = None

#group_text_font_size
#major_label_text_font_size


#p.legend.location = "bottom_center"
p.legend.orientation = "horizontal"

p.add_layout(labels15)
p.add_layout(labels16)
p.add_layout(labels17)

show(p)