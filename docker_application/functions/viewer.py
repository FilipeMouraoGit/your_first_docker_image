import plotly.graph_objects as go


class SimpleAppViewer:
    @staticmethod
    def plot_fit_graph(x, y, x_fit, y_fit):
        """
        Given 2 datasets (x,y) and (x_fit, y_fit) plot the first one as scatter and the second as line
        """
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name='Data Points'))
        fig.add_trace(go.Scatter(x=x_fit, y=y_fit, mode='lines', name='Model fit'))
        fig.update_layout(
            title={'text': 'Selected function data fit', 'x': 0.5, 'xanchor': 'center'},
            xaxis_title='X',
            yaxis_title='Y',
            legend=dict(orientation="v", yanchor="bottom", y=1.02, xanchor="center"),
            template='plotly_dark')
        fig.show()
