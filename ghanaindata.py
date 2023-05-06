from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd

app = Dash(__name__)

app.layout = html.Div(
    children={
          html.Header(
                children={
                    html.Div(children={
                        html.H1(children='Ghana In Data')
        }),

    }),
})
if __name__ == '__main__':
    app.run_server(debug=True)