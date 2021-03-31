import pandas as pd 
import seaborn as sns
from matplotlib import pyplot as plt
from bokeh.models import Legend
from bokeh.core.properties import value
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, LabelSet
from bokeh.plotting import figure
from bokeh.transform import dodge
from bokeh.models import Legend,axes

pd.set_option('mode.chained_assignment',  None)

df=pd.read_csv(r'C:\Users\imagoworks-moongzeee\Desktop\exp\구강스캔\11\exp11_result.csv')

#center, data, mn&mx info col 추출
df['center']=df.CenterPath.str.split('\\').str[1]
df['num']=df.CenterPath.str.split('\\').str[3]
df['cat']=df.CenterPath.str.split('\\').str[4]

#mn&mx 구분
mn=df['cat']=='137.vtp'
mx=df['cat']=='136.vtp'

df_mn=df[mn]
df_mn['center']='mn-'+df_mn['center']
df_mn.drop(['CenterPath','tooth_num','cat'],axis=1,inplace=True)

df_mx=df[mx]
df_mx['center']='mx-'+df_mx['center']
df_mx.drop(['CenterPath','tooth_num','cat'],axis=1,inplace=True)

#data merge
data_=pd.concat([df_mn,df_mx],ignore_index=False)

#print(data_)




#mean value by center
mean=data_.groupby('center').mean()
mean=mean.round(decimals=3)




output_file("dodged_bars.html")

Center=mean.index.tolist()
IoU=mean['IoU'].tolist()
Dice=mean['Dice'].tolist()
Precision=mean['Precision'].tolist()
Recall=mean['Recall'].tolist()


#print(Precision)


data={'Center' : Center,
      'IoU' : IoU,
      'Dice' : Dice,
      'Precision' : Precision,
      'Recall' : Recall}

source = ColumnDataSource(data=data)
tools='wheel_zoom reset save'.split()

p = figure(x_range=Center, y_range=(0,1), plot_height=500, plot_width=1200, title="Experiment 11",
           toolbar_location='right', tools=tools) 

p.title.text_font_size = '15pt'
p.title.align='center'
p.xaxis.major_label_text_font_size = "16px"
p.xaxis.major_label_text_font_style='bold'

labels15=LabelSet(x=dodge('Center', -0.3375, range=p.x_range),y='IoU',text='IoU',source=source,text_align='center',text_font_size='10pt')
labels16=LabelSet(x=dodge('Center', -0.1125, range=p.x_range),y='Dice',text='Dice',source=source,text_align='center',text_font_size='10pt')
labels17=LabelSet(x=dodge('Center', 0.1125, range=p.x_range),y='Precision',text='Precision',source=source,text_align='center',text_font_size='10pt')
labels18=LabelSet(x=dodge('Center', 0.3375, range=p.x_range),y='Recall',text='Recall',source=source,text_align='center',text_font_size='10pt')

r0=p.vbar(x=dodge('Center', -0.3375, range=p.x_range), top='IoU', width=0.225, source=source,
       color="#C9D9D3")

r1=p.vbar(x=dodge('Center', -0.1125,  range=p.x_range), top='Dice', width=0.225, source=source,
       color="#718DBF")

r2=p.vbar(x=dodge('Center',  0.1125, range=p.x_range), top='Precision', width=0.225, source=source,
       color="#E84D60")

r3=p.vbar(x=dodge('Center', 0.3375, range=p.x_range), top='Recall', width=0.225, source=source,
       color="#FFE08C")


legend=Legend(items=[('IoU',[r0]),('Dice',[r1]),('Precision',[r2]),('Recall',[r3])])
p.add_layout(legend,'below')
p.x_range.range_padding = 0.01
p.xgrid.grid_line_color = None


p.legend.orientation = "horizontal"

p.add_layout(labels15)
p.add_layout(labels16)
p.add_layout(labels17)
p.add_layout(labels18)

show(p)
