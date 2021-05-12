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
import dash_table

if platform.system() == "Windows":
    path = '//192.168.0.113/Imagoworks'
else:
    path = '//Volumes/Imagoworks'

# Start the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server


train_data_folder=(['//192.168.0.113/Imagoworks/AITeam/_Experiments/SingleCrown\\train_data_46_depth10\DDH-cut\\train\\18','//192.168.0.113/Imagoworks/AITeam/_Experiments/SingleCrown\\train_data_46_depth10\\DDH-cut\\train\\19'])
depth_df = pd.DataFrame({'path':train_data_folder})
depth_df['x'] = depth_df['path']+'/x.jpg'
# depth_df['y'] = depth_df['path']+'/y.jpg'
# depth_df['z'] = depth_df['path']+'/z.jpg'


depth_df['x']=[html.Img(src='data:image/png;base64,{}'.format(base64.b64encode(open(i, 'rb').read()).decode())) for i in depth_df['x']]
print(depth_df['x'][0])

# app.layout=dash_table.DataTable(
#     data=depth_df.to_dict('records'),
#     columns=[
#         {'id': 'x' , 'name':'x.jpg', 'presentation':'markdown'},
#         {'id':'path', 'name':'path'}
#     ]
# )

app.layout=html.Div([
        dbc.Table.from_dataframe(depth_df, striped=True, bordered=True, hover=True, responsive="sm")
        ],
        style = {'margin-right':'10px','margin-left':'10px'})

if __name__ == "__main__":
    app.run_server(debug=True)