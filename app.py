from dash import Dash
import dash_mantine_components as dmc

app = Dash(__name__)

app.layout = dmc.Text("Hello World!")


if __name__ == "__main__":
    app.run(debug=True)
