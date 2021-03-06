import dash_html_components as html
# -----------
# HELPERS TO MAKE PARTIAL SECTIONS
# -----------

def make_section_type3(div1, div2, div3, name1='', name2='', name3=''):
  return html.Div([
    html.Div([html.Label(name1), div1], style={'width': '33%'}),
    html.Div([html.Label(name2), div2], style={'width': '33%'}),
    html.Div([html.Label(name3), div3], style={'width': '33%'}),
    ],
    style={'display': 'flex'}
  )

def make_section_type4(div1, div2, div3, div4):
  return html.Div([
    html.Div(div1, style={'width': '13%'}),
    html.Div(div2, style={'width': '29%'}),
    html.Div(div3, style={'width': '29%'}),
    html.Div(div4, style={'width': '29%'}),
    ],
    style={'display': 'flex'}
  )

def make_section_type2(div1, div2):
  return html.Div([
    html.Div(div1, style={'width': '50%'}),
    html.Div(div2, style={'width': '50%'}),
    ],
    style={'display': 'flex'}
  )