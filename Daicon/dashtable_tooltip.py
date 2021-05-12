import os
import glob
import pandas as pd 
import platform
from PIL import Image
import dash_html_components as html
import dash_bootstrap_components as dbc
import io
import base64
import dash 
import dash_core_components as dcc
from dash.dependencies import Input, Output
import multiprocessing


if platform.system() == "Windows":
    path = '//192.168.0.113/Imagoworks'
else:
    path = '//Volumes/Imagoworks'

# Start the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server



def get_thumbnail(path):   
   i = Image.open(path)
   i.thumbnail((100, 100), Image.LANCZOS)
   buff = io.BytesIO()
   i.save(buff, format="PNG")
#    encoded_image = base64.b64encode(open(path, 'rb').read())
   encoded_image = base64.b64encode(buff.getvalue()).decode('UTF-8')
   return (html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode())))


# train_data_folder = list(filter(os.path.isdir, glob.glob(path+'/AITeam/_Experiments/SingleCrown/train**/**/**/**')))
train_data_folder=(['//192.168.0.113/Imagoworks/AITeam/_Experiments/SingleCrown\\train_data_46_depth10\DDH-cut\\train\\18','//192.168.0.113/Imagoworks/AITeam/_Experiments/SingleCrown\\train_data_46_depth10\\DDH-cut\\train\\19'])
depth_df = pd.DataFrame({'path':train_data_folder})




x=[]
y=[]
z=[]
for path in depth_df['path']:
    x.append(get_thumbnail(path+'/x.jpg'))
    y.append(get_thumbnail(path+'/y.jpg'))
    z.append(get_thumbnail(path+'/z.jpg'))


print(x)
print(y)
print(z)


depth_df['x']=x
depth_df['y']=y
depth_df['z']=z

depth_df['path']=depth_df['path'].str.split('\\').str[1]


print(depth_df)




app.layout=html.Div([
        dbc.Table.from_dataframe(depth_df, striped=True, bordered=True, hover=True, responsive="sm")
        ],
        style = {'margin-right':'10px','margin-left':'10px'})


if __name__ == "__main__":
    app.run_server(debug=True)
