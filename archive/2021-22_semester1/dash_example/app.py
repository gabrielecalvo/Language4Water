import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output, State
import plotly.express as px

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv")
df_2007 = df[df.year == 2007]

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.Graph(
            id="graph-with-slider",
            figure=px.scatter(
                df_2007,
                x="gdpPercap",
                y="lifeExp",
                size="pop",
                color="continent",
                hover_name="country",
                log_x=True,
                size_max=55,
            ),
        ),
        html.Button(id="submit-button", n_clicks=0, children="Submit"),
        dash_table.DataTable(
            id="data-table",
            columns=[{"name": i, "id": i} for i in df_2007.columns],
            data=[],
        ),
    ]
)


@app.callback(
    Output("data-table", "data"),
    Input("submit-button", "n_clicks"),
    State("graph-with-slider", "figure"),
)
def update_figure(n_clicks, figure):
    selected_by_continent = {
        continent["legendgroup"]: continent.get("selectedpoints", []) for continent in figure["data"]
    }

    sub_selection_dfs = []
    for continent, indexes in selected_by_continent.items():
        sub_df = df_2007[df_2007.continent == continent].iloc[indexes]
        sub_selection_dfs.append(sub_df)

    selected_df = pd.concat(sub_selection_dfs)

    return selected_df.to_dict("records")


if __name__ == "__main__":
    app.run_server(debug=True)
