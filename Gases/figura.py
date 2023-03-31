
import plotly.graph_objs as go
from triangulo_app.models import transformador
import re


def triangulo_1 (ch4, c2h2, c2h4, name):
    trace1 = {
        "name": "PD",
        "uid": "a1a8b8",
        "a": [98, 1, 98],
        "b": [0, 0, 2],
        "c": [2, 0, 0],
        "fill": "toself",
        "line": {"color": "#444"},
        "mode": "lines",
        "text": "PD",
        "type": "scatterternary",
        "fillcolor": "#8dd3c7"
        }
    trace2 = {
        "name": "D1",
        "uid": "c72344",
        "a": [0, 0, 64, 87],
        "b": [100, 77, 13, 13],
        "c": [0, 23, 23, 0],
        "fill": "toself",
        "line": {"color": "#444"},
        "mode": "lines",
        "text": "D1",
        "type": "scatterternary",
        "fillcolor": "#ffffb3"
        }
    trace3 = {
        "name": "D2",
        "uid": "3eab74",
        "a": [0, 0, 31, 47, 64],
        "b": [77, 29, 29, 13, 13],
        "c": [23, 71, 40, 40, 23],
        "fill": "toself",
        "line": {"color": "#444"},
        "mode": "lines",
        "text": "D2",
        "type": "scatterternary",
        "fillcolor": "#bebada"
        }
    trace4 = {
        "name": "DT",
        "uid": "b9dc9f",
        "a": [0, 0, 35, 46, 96, 87, 47, 31],
        "b": [29, 15, 15, 4, 4, 13, 13, 29],
        "c": [71, 85, 50, 50, 0, 0, 40, 40],
        "fill": "toself",
        "line": {"color": "#444"},
        "mode": "lines",
        "text": "DT",
        "type": "scatterternary",
        "fillcolor": "#fb8072"
        }
    trace5 = {
        "name": "T1",
        "uid": "381ad2",
        "a": [76, 80, 98, 98, 96],
        "b": [4, 0, 0, 2, 4],
        "c": [20, 20, 2, 0, 0],
        "fill": "toself",
        "line": {"color": "#444"},
        "mode": "lines",
        "text": "T1",
        "type": "scatterternary",
        "fillcolor": "#80b1d3"
        }
    trace6 = {
        "name": "T2",
        "uid": "8cc163",
        "a": [46, 50, 80, 76],
        "b": [4, 0, 0, 4],
        "c": [50, 50, 20, 20],
        "fill": "toself",
        "line": {"color": "#444"},
        "mode": "lines",
        "text": "T2",
        "type": "scatterternary",
        "fillcolor": "#fdb462"
        }
    trace7 = {
        "name": "T3",
        "uid": "6f33dc",
        "a": [0, 0, 50, 35],
        "b": [15, 0, 0, 15],
        "c": [85, 1, 50, 50],
        "fill": "toself",
        "line": {"color": "#444"},
        "mode": "lines",
        "text": "T3",
        "type": "scatterternary",
        "fillcolor": "#b3de69"
        }
    trace8 = {
        'name': 'Falla',                    
        "a": ch4,
        "b":c2h2,
        "c": c2h4,
        "mode": "markers",
        "type": "scatterternary", 
        'hovertext': name,       
        "marker": {
            "size": 20,
            "color": "black",
            "symbol": 100
            }
        }
    layout = {
        "title": "Triangulo 1 de Duval",
        "ternary": {
            "sum": 100,
            "aaxis": {
                "min": 0.01,
                "ticks": "outside",
                "title": "CH4(Methane)",
                "linewidth": 2,
                "ticksuffix": "%"
                },
            "baxis": {
                "min": 0.01,
                "ticks": "outside",
                "title": "C2H2(Acetylene)",
                "linewidth": 2,
                "ticksuffix": "%"
                },
            "caxis": {
                "min": 0.01,
                "ticks": "outside",
                "title": "C2H4(Ethylene)",
                "linewidth": 2,
                "ticksuffix": "%"
                }
            },
        "autosize": True,
        "showlegend": False
        }
    fig = go.Figure([trace1,trace2,trace3,trace4,
                  trace5, trace6, trace7,trace8], layout=layout)
    return fig

def triangulo_4 (h2, c2h6, ch4, name):
    trace1 = {
        "name": "O",
        "uid": "a1a8b8",
        "a": [0, 9, 9, 0],
        "b": [30, 30, 91, 100],
        "c": [70, 61, 0, 0],
        "fill": "toself",
        "line": {"color": "#444"},
        "mode": "lines",
        "text": "O",
        "type": "scatterternary",
        "fillcolor": "#8dd3c7"
        }
    trace2 = {
        "name": "S",
        "uid": "c72344",
        "a": [9, 9, 15, 15, 40, 64, 85, 84, 97, 98, 100, 54],
        "b": [46, 30, 30, 24, 24, 0, 0, 1, 1, 0, 0, 46],
        "c": [45, 61, 55, 61, 36, 36, 15, 15, 2, 2, 0, 0],
        "fill": "toself",
        "line": {"color": "#444"},
        "mode": "lines",
        "text": "S",
        "type": "scatterternary",
        "fillcolor": "#ffffb3"
        }
    trace3 = {
        "name": "C",
        "uid": "3eab74",
        "a": [0, 0, 64, 40, 15, 15],
        "b": [30, 0, 0, 24, 24, 30],
        "c": [70, 100, 36, 36, 61, 55],
        "fill": "toself",
        "line": {"color": "#444"},
        "mode": "lines",
        "text": "C",
        "type": "scatterternary",
        "fillcolor": "#bebada"
        }
    trace4 = {
        "name": "PD",
        "uid": "b9dc9f",
        "a": [84, 85, 98, 97],
        "b": [1, 0, 0, 1],
        "c": [15, 15, 2, 2],
        "fill": "toself",
        "line": {"color": "#444"},
        "mode": "lines",
        "text": "PD",
        "type": "scatterternary",
        "fillcolor": "#fb8072"
        }
    trace5 = {
        "name": "",
        "uid": "381ad2",
        "a": [9, 9, 54],
        "b": [91, 46, 46],
        "c": [0, 45, 0],
        "fill": "toself",
        "line": {"color": "#444"},
        "mode": "lines",
        "text": "",
        "type": "scatterternary",
        "fillcolor": "#80b1d3"
        }
    trace6 = {
        "name": "Falla",
        "a": h2,
        "b": c2h6,
        "c": ch4,
        "mode": "markers",
        "type": "scatterternary",
        "hovertext": name,
        "marker": {
            "size": 20,
            "color": "black",
            "symbol": 100
            }
        }
    layout = {
        "title": "Triangulo 4 de Duval",
        "ternary": {
            "sum": 100,
            "aaxis": {
                "min": 0.01,
                "ticks": "outside",
                "title": "H2",
                "linewidth": 2,
                "ticksuffix": "%"
                },
            "baxis": {
                "min": 0.01,
                "ticks": "outside",
                "title": "C2H6",
                "linewidth": 2,
                "ticksuffix": "%"
                },
            "caxis": {
                "min": 0.01,
                "ticks": "outside",
                "title": "CH4",
                "linewidth": 2,
                "ticksuffix": "%"
                }
            },
        "autosize": True,
        "showlegend": False
        }
    fig = go.Figure([trace1, trace2, trace3, trace4, trace5, trace6], layout=layout)
    return fig

def triangulo_5 (ch4, c2h6, c2h4, name):
    trace1 = {
        "name": "PD",
        "uid": "a1a8b8",
        "a": [84, 97, 98, 85],
        "b": [15, 2, 2, 15],
        "c": [1, 1, 0, 0],
        "fill": "toself",
        "line": {"color": "#444"},
        "mode": "lines",
        "text": "PD",
        "type": "scatterternary",
        "fillcolor": "#8dd3c7"
        }
    trace2 = {
        "name": "O",
        "uid": "c72344",
        "a": [75, 90, 100, 98, 98, 85, 0, 0, 36, 46],
        "b": [15, 0, 0, 2, 2, 15, 100, 90, 54, 54],
        "c": [10, 10, 0, 0, 1, 1, 0, 10, 10, 0],
        "fill": "toself",
        "line": {"color": "#444"},
        "mode": "lines",
        "text": "O",
        "type": "scatterternary",
        "fillcolor": "#ffffb3"
        }
    trace3 = {
        "name": "T2",
        "uid": "3eab74",
        "a": [53, 65, 90, 78],
        "b": [12, 0, 0, 12],
        "c": [35, 35, 10, 10],
        "fill": "toself",
        "line": {"color": "#444"},
        "mode": "lines",
        "text": "T2",
        "type": "scatterternary",
        "fillcolor": "#bebada"
        }
    trace4 = {
        "name": "T3",
        "uid": "b9dc9f",
        "a": [0, 65, 53, 40, 38, 16, 0, 35, 0],
        "b": [0, 0, 12, 12, 14, 14, 30, 30, 65],
        "c": [100, 35, 35, 48, 48, 70, 70, 35, 35],
        "fill": "toself",
        "line": {"color": "#444"},
        "mode": "lines",
        "text": "T3",
        "type": "scatterternary",
        "fillcolor": "#fb8072"
        }
    trace5 = {
        "name": "C",
        "uid": "381ad2",
        "a": [0, 16, 38, 40, 78, 60],
        "b": [30, 14, 14, 12, 12, 30],
        "c": [70, 70, 48, 48, 10, 10],
        "fill": "toself",
        "line": {"color": "#444"},
        "mode": "lines",
        "text": "C",
        "type": "scatterternary",
        "fillcolor": "#80b1d3"
        }
    trace6 = {
        "name": "S",
        "uid": "6f33dc",
        "a": [46, 36, 75, 85],
        "b": [54, 54, 15, 15],
        "c": [0, 10, 10, 0],
        "fill": "toself",
        "line": {"color": "#444"},
        "mode": "lines",
        "text": "S",
        "type": "scatterternary",
        "fillcolor": "#b3de69"
        }
    trace7 = {
        "name": "",
        "uid": "8cc163",
        "a": [0, 35, 60, 0],
        "b": [65, 30, 30, 90],
        "c": [35, 35, 10, 10],
        "fill": "toself",
        "line": {"color": "#444"},
        "mode": "lines",
        "text": "",
        "type": "scatterternary",
        "fillcolor": "#fdb462"
        }
    trace8 = {
        "name": "falla",
        "a": ch4,
        "b": c2h6,
        "c": c2h4,
        "mode": "markers",
        "type": "scatterternary",
        "hovertext": name,
        "marker": {
            "size": 20,
            "color": "black",
            "symbol": 100
            }
        }
    layout = {
        "title": "Triangulo 5 de Duval",
        "ternary": {
            "sum": 100,
            "aaxis": {
                "min": 0.01,
                "ticks": "outside",
                "title": "CH4(Methane)",
                "linewidth": 2,
                "ticksuffix": "%"
                },
            "baxis": {
                "min": 0.01,
                "ticks": "outside",
                "title": "C2H6",
                "linewidth": 2,
                "ticksuffix": "%"
                },
            "caxis": {
                "min": 0.01,
                "ticks": "outside",
                "title": "C2H4(Ethylene)",
                "linewidth": 2,
                "ticksuffix": "%"
                }
            },
        "autosize": True,
        "showlegend": False
        }
    fig = go.Figure([trace1, trace2, trace3, trace4, trace5, trace6,
                     trace7, trace8], layout=layout)
    return fig

def an_triangulo_1 (a_ch4, b_c2h2, c_c2h4):
    if 0<=a_ch4<87 and 0<=c_c2h4<=23 and 13<b_c2h2<100:
        return ('D1')        
    elif 0<=a_ch4<50 and 30<c_c2h4<77 and 23<=b_c2h2<70:
        return ('D2')        
    elif 29<a_ch4<64 and 23<c_c2h4<=40 and 13<b_c2h2<30:
        return ('D2')        
    elif 98<=a_ch4<=100 and 0<=c_c2h4<2 and 0<=b_c2h2<2:
        return ('PD')        
    elif 76<=a_ch4<98 and 0<=c_c2h4<20 and 0<=b_c2h2<=4:
        return ('T1')         
    elif 46<=a_ch4<80 and 20<c_c2h4<=50 and 0<=b_c2h2<=4:
        return ('T2')        
    elif 0<=a_ch4<50 and 50<c_c2h4<100 and 0<=b_c2h2<15:
        return ('T3')         
    elif 0<=a_ch4<=47 and 40<c_c2h4<100 and 15<=b_c2h2<30:
        return ('DT')         
    elif 35<a_ch4<96 and 0<=c_c2h4<50 and 4<b_c2h2<15:
        return ('DT')
    else :
        return ('-')
         
def an_triangulo_5 (a_ch4, b_c2h6, c_c2h4):
    if 0<a_ch4<46 and 0<c_c2h4<10 and 54<b_c2h6<100:        
        return 'O'
    elif 75<a_ch4<98 and 1<c_c2h4<10 and 0<b_c2h6<15:        
        return 'O'
    elif 88<a_ch4<100 and 0<c_c2h4<10 and 0<b_c2h6<2:        
        return 'O'
    elif 36<a_ch4<85 and 0<c_c2h4<10 and 15<b_c2h6<54:        
        return 'S'
    elif 84<a_ch4<98 and 0<c_c2h4<=1 and 2<b_c2h6<15:        
        return 'PD'
    elif 53<a_ch4<90 and 10<c_c2h4<35 and 0<b_c2h6<12:        
        return 'T2'
    elif 0<a_ch4<35 and 35<c_c2h4<=70 and 30<b_c2h6<65:        
        return 'T3'
    elif 0<a_ch4<30 and 70<c_c2h4<100 and 0<b_c2h6<30:        
        return 'T3'
    elif 0<a_ch4<52 and 48<c_c2h4<100 and 0<b_c2h6<14:        
        return 'T3'
    elif 0<a_ch4<65 and 35<c_c2h4<100 and 0<b_c2h6<12:        
        return 'T3'
    elif 0<a_ch4<88 and 10<c_c2h4<70 and 14<b_c2h6<30:        
        return 'C'
    elif 22<a_ch4<88 and 10<c_c2h4<48 and 12<b_c2h6<30:        
        return 'C'
    else:
        return ''

def an_triangulo_4 (a_h2, b_c2h6, c_ch4):
    if 0<a_h2<=9 and 0<c_ch4<70 and 30<=b_c2h6<100:        
        return 'O'
    elif 84<a_h2<98 and 2<c_ch4<15 and 0<b_c2h6<=1:        
        return 'PD'
    elif 0<a_h2<64 and 36<c_ch4<100 and 0<b_c2h6<24:        
        return 'C'
    elif 0<a_h2<=15 and 85<c_ch4<100 and 0<b_c2h6<30:        
        return 'C'
    elif 9<a_h2<70 and 0<c_ch4<61 and 30<b_c2h6<46:        
        return 'S'
    elif 15<a_h2<76 and 0<c_ch4<61 and 24<=b_c2h6<30:        
        return 'S'
    elif 40<a_h2<100 and 0<c_ch4<36 and 0<b_c2h6<24:        
        return 'S'
    else:
        return ''

def porcient (list1, list2, list3):
    mul = [100*(x)/(x+y+z) for x,y,z in zip(list1,list2,list3)]
    return mul

def porcient1 (x, y, z):
    mul = 100*(x)/(x+y+z)
    return mul



   
