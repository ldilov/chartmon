import plotly.graph_objects as go
from plotly.subplots import make_subplots


class PlotBuilder:
    def __init__(self):
        self.fig = make_subplots(rows=7, cols=1)

    def add_trace(self, x, y, row, col, **kwargs):
        self.fig.add_trace(go.Scatter(x=x, y=y, **kwargs), row=row, col=col)

    def show_plot(self):
        self.fig.update_layout(
            height=1280,
            width=1680,
            title_text="Performance Metrics",
            hovermode='x unified',
            template="ggplot2",
            annotations=[dict(
                x=1,
                y=1,
                xref='paper',
                yref='paper',
                showarrow=True
            )]
        )

        self.fig.update_layout(updatemenus=[
            dict(
                direction="down",
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0.1,
                xanchor="left",
                y=1.1,
                yanchor="top"
            ),
        ])

        self.fig.show(config={'displaylogo': False, 'scrollZoom': True, 'responsive': True, 'editable': False})
