import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards
from docker_application.functions.viewer import SimpleAppViewer
from docker_application.functions.logic import SimpleAppLogic


def build_input_sidebar():
    st.title("Input parameters")
    poly_degree = st.selectbox(label="Select the polynom degree", options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    input_data_str = st.text_input(label="Enter the input data", help='Format: x1,y1;x2,y2;...;x_n,y_n')
    fit_button = st.button(label='Fit Data')
    if fit_button:
        x, y, x_fit, y_fit = SimpleAppLogic.fit_input_data(data_points_str=input_data_str, fit_degree=poly_degree)
        return x, y, x_fit, y_fit
    return None, None, None, None


def build_graph(x, y, x_fit, y_fit):
    plotly_fig = SimpleAppViewer.plot_fit_graph(x, y, x_fit, y_fit)
    style_metric_cards(background_color='rgba(255,255,255,0)')
    st.plotly_chart(plotly_fig, use_container_width=True)


st.set_page_config(layout="wide")
with st.sidebar:
    x, y, x_fit, y_fit = build_input_sidebar()
st.title('Simple App Interface')
if x_fit is not None and len(x_fit) > 0:
    build_graph(x, y, x_fit, y_fit)
