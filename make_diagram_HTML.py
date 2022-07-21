#
# 2022 Yasushi Ohsugi


## ******************************
## making the list of "node_name" from 'SCMTREE_profile010.csv'
## ******************************
#from PySILib.PySI_search_LEAF_in_SCMTREE import *

# ******************************
# making Diagram from 'common_plan_unit.csv'
# ******************************

# ******************************
# passing "node_name" list
# ******************************
#postorder_node = node_name
#postorder_node = PySILib.PySI_search_LEAF_in_SCMTREE.node_name

from PySILib.make_Common_Plan_Unit2diagram import *

import plotly.graph_objects as go


# ******************************
# passing "node_name" list
# ******************************

node_list = postorder_node


#post order node_name ['YTOLEAF', 'YTO', 'NYC_N', 'NYC_D', 'NYC_I', 'NYC', 'LAX_N', 'LAX_D', 'LAX_I', 'SFOLEAF', 'LAX', 'MEXLEAF', 'MEX', 'SAOLEAF', 'SAO', 'BUELEAF', 'BUE', 'KULLEAF', 'KUL', 'BKKLEAF', 'BKK', 'SINLEAF', 'SIN', 'SGNLEAF', 'SGN', 'ISTLEAF', 'IST', 'JKTLEAF', 'JKT', 'SELLEAF', 'SEL', 'SYDLEAF', 'SYD', 'DELLEAF', 'DEL', 'RUHLEAF', 'RUH', 'SWELEAF', 'NORLEAF', 'DENLEAF', 'HELLEAF', 'GOT', 'LONLEAF', 'LON', 'PARLEAF', 'PAR', 'HAM_N', 'HAM_D', 'HAM_I', 'MUC_N', 'MUC_D', 'MUC_I', 'MUC', 'FRALEAF', 'HAM', 'MXPLEAF', 'MXP', 'JNBLEAF', 'JNB', 'SHA_N', 'SHA_D', 'SHA_I', 'BJS_N', 'BJS_D', 'BJS_I', 'SHA', 'CAN_N', 'CAN_D', 'CAN_I', 'CAN', 'LEDLEAF', 'LED', 'BRULEAF', 'BRU', 'TYOLEAF', 'TYO', 'OSALEAF', 'OSA', 'AMSLEAF', 'AMS', 'AKLLEAF', 'AKL', 'WAWLEAF', 'WAW', 'LISLEAF', 'LIS', 'MADLEAF', 'MAD', 'ZRHLEAF', 'ZRH', 'JPN']


#node_list = ['YTOLEAF', 'YTO', 'NYC_N', 'NYC_D', 'NYC_I', 'NYC', 'LAX_N', 'LAX_D', 'LAX_I', 'SFOLEAF', 'LAX', 'MEXLEAF', 'MEX', 'SAOLEAF', 'SAO', 'BUELEAF', 'BUE', 'KULLEAF', 'KUL', 'BKKLEAF', 'BKK', 'SINLEAF', 'SIN', 'SGNLEAF', 'SGN', 'ISTLEAF', 'IST', 'JKTLEAF', 'JKT', 'SELLEAF', 'SEL', 'SYDLEAF', 'SYD', 'DELLEAF', 'DEL', 'RUHLEAF', 'RUH', 'SWELEAF', 'NORLEAF', 'DENLEAF', 'HELLEAF', 'GOT', 'LONLEAF', 'LON', 'PARLEAF', 'PAR', 'HAM_N', 'HAM_D', 'HAM_I', 'MUC_N', 'MUC_D', 'MUC_I', 'MUC', 'FRALEAF', 'HAM', 'MXPLEAF', 'MXP', 'JNBLEAF', 'JNB', 'SHA_N', 'SHA_D', 'SHA_I', 'BJS_N', 'BJS_D', 'BJS_I', 'SHA', 'CAN_N', 'CAN_D', 'CAN_I', 'CAN', 'LEDLEAF', 'LED', 'BRULEAF', 'BRU', 'TYOLEAF', 'TYO', 'OSALEAF', 'OSA', 'AMSLEAF', 'AMS', 'AKLLEAF', 'AKL', 'WAWLEAF', 'WAW', 'LISLEAF', 'LIS', 'MADLEAF', 'MAD', 'ZRHLEAF', 'ZRH', 'JPN','root']


node_color = []

color_list_10 = [ 
    "rgba(31, 119, 180, 0.8)",  
    "rgba(255, 127, 14, 0.8)",       
    "rgba(44, 160, 44, 0.8)",  
    "rgba(214, 39, 40, 0.8)", 
    "rgba(148, 103, 189, 0.8)",  
    "rgba(140, 86, 75, 0.8)",  
    "rgba(227, 119, 194, 0.8)",  
    "rgba(127, 127, 127, 0.8)", 
    "rgba(188, 189, 34, 0.8)", 
    "rgba(23, 190, 207, 0.8)" 
    ]

for i, node in enumerate(node_list):

    i_mod = i // 10

    color_x = color_list_10[ i_mod ]

    node_color.append( color_x )





title_text = "EV 2023 OUTLOOK supply chain<br>visualise the result of integrated PSI planning "


# **********************************************************


data = {
    "data": [
        {
            "type": "sankey",
            "domain": {
                "x": [
                    0,
                    1
                ],
                "y": [
                    0,
                    1
                ]
            },
            "orientation": "h",
            "valueformat": ".0f",
            "valuesuffix": "Lots",
            "node": {
                "pad": 15,
                "thickness": 15,
                "line": {
                    "color": "black",
                    "width": 0.5
                },

                "label": node_list ,

                "color": node_color
            },
            "link": {

                "source": path_from ,
                "target": path_to   ,

                "value": path_value ,

                "color": path_color ,

                "label": path_label 
            }
        }],
    "layout": {

        "title": {"text": title_text },

        "width": 1118,
        "height": 772,
        "font": {
            "size": 10
        },
        "updatemenus": [
            {
                "y": 1,
                "buttons": [
                    {
                        "label": "Light",
                        "method": "relayout",
                        "args": [ "paper_bgcolor", "white" ]
                    },
                    {
                        "label": "Dark",
                        "method": "relayout",
                        "args": [ "paper_bgcolor", "black"]
                    }
                ]
            },
            {
                "y": 0.9,
                "buttons": [
                    {
                        "label": "Thick",
                        "method": "restyle",
                        "args": [ "node.thickness", 15 ]
                    },
                    {
                        "label": "Thin",
                        "method": "restyle",
                        "args": [ "node.thickness", 8]
                    }
                ]
            },
            {
                "y": 0.8,
                "buttons": [
                    {
                        "label": "Small gap",
                        "method": "restyle",
                        "args": [ "node.pad", 15 ]
                    },
                    {
                        "label": "Large gap",
                        "method": "restyle",
                        "args": [ "node.pad", 20]
                    }
                ]
            },
            {
                "y": 0.7,
                "buttons": [
                    {
                        "label": "Snap",
                        "method": "restyle",
                        "args": [ "arrangement", "snap" ]
                    },
                    {
                        "label": "Perpendicular",
                        "method": "restyle",
                        "args": [ "arrangement", "perpendicular"]
                    },
                    {
                        "label": "Freeform",
                        "method": "restyle",
                        "args": [ "arrangement", "freeform"]
                    },
                    {
                        "label": "Fixed",
                        "method": "restyle",
                        "args": [ "arrangement", "fixed"]
                    }
                ]
            },
            {
                "y": 0.6,
                "buttons": [
                    {
                        "label": "Horizontal",
                        "method": "restyle",
                        "args": [ "orientation", "h" ]
                    },
                    {
                        "label": "Vertical",
                        "method": "restyle",
                        "args": [ "orientation", "v"]
                    }
                ]
            }
        ]
    }
}





# override gray link colors with 'source' colors
opacity = 0.4
# change 'magenta' to its 'rgba' value to add opacity
data['data'][0]['node']['color'] = ['rgba(255,0,255, 0.8)' if color == "magenta" else color for color in data['data'][0]['node']['color']]
data['data'][0]['link']['color'] = [data['data'][0]['node']['color'][src].replace("0.8", str(opacity))
                                    for src in data['data'][0]['link']['source']]

fig = go.Figure(data=[go.Sankey(
    valueformat = ".0f",
    valuesuffix = "Lots",
    # Define nodes
    node = dict(
      pad = 15,
      thickness = 15,
      line = dict(color = "black", width = 0.5),
      label =  data['data'][0]['node']['label'],
      color =  data['data'][0]['node']['color']
    ),
    # Add links
    link = dict(
      source =  data['data'][0]['link']['source'],
      target =  data['data'][0]['link']['target'],
      value =  data['data'][0]['link']['value'],
      label =  data['data'][0]['link']['label'],
      color =  data['data'][0]['link']['color']
))])

fig.update_layout(

title_text = "EV 2023 OUTLOOK supply chain<br>visualise the result of integrated PSI planning "


# ****
,
# ****
                  font_size=10)
fig.show()
