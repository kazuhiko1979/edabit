import random
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output

coin_list = ["表","裏"]
results_list = []
db_probability = []

#事前に行われる11回の試行
for i in range(1, 11):
    results_list.append(random.choice(coin_list))
    db_probability.append(results_list.count("表")/len(results_list))

markdown_text = '''
#### <参考サイト>
* [Dash by plotly(公式サイト)](https://plot.ly/products/dash/)
* [Blow Up By Black Swan](https://blowup-bbs.com/python-dash-framework-plotly1/)
'''

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1("Python Web Application Framework: Dash"),
        html.Div(id="the number"),
        dcc.Graph(id="graph"),
        dcc.Markdown(markdown_text),
        dcc.Interval(
            id="interval-component",
            interval=1*1000,
            n_intervals=0
        )
    ]
)

@app.callback(Output("the number", "children"),
               [Input("interval-component", "n_intervals"),
                Input("interval-component", "interval")])
def display_num(n_intervals, intervals):
    style = {'padding': '5px', 'fontSize': '16px'}
    return html.Div('"n_intervals"={}回, "intervals"={}ミリ秒'.format(n_intervals, intervals),
                     style=style)

@app.callback(Output("graph", "figure"),
              [Input("interval-component", "n_intervals")])

def making_figure(n):
    # making figure object
    c_results_list = results_list
    c_db_probability = db_probability
    c_results_list.append(random.choice(coin_list))
    c_db_probability.append((c_results_list.count("表"))/len(c_results_list))
    id_map = map(lambda x: x, range(1, len(c_results_list)+1))
    trace = go.Scatter(x=list(id_map),
                       y=c_db_probability,
                       mode="markers+lines",  # グラフの表示の仕方
                       marker={'symbol': 0, 'size': 5, 'color': 'darkblue',
                               'line': {'color': 'blue', 'width': 2}}
                       )
    ex_layout = {'title': 'コインで表が出る確率が1/2に収束していく図(大数の法則)',
                 'width': 1300,
                 'height': 600,
                 'yaxis': {'range': [0, 1],
                           'dtick':0.1}
                 }
    figure = go.Figure(data=[trace], layout=ex_layout)
    return figure

if __name__ == "__main__":
    app.run_server(debug=True)