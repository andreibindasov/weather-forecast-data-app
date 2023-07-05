import streamlit as st

st.set_page_config(layout="wide")
style = "<style>div{text-align: center; color: #669966;}</style>"

st.markdown(style, unsafe_allow_html=True)

with st.container():
    with st.columns([0.25, 2, 0.25])[1]:
        # st.markdown(f"<div style='text-align:center;'><img src='weather.png' style='width:150px;'/></div>",
        #             unsafe_allow_html=True)
        st.image('weather.png', width=120)
        st.markdown("<h1 style='color: #369369; font-size:2.1rem; text-align:center; font-weight:300; "
                    "font-family: Verdana;'>"
                    "Weather Forecast for the Next Days</h1>", unsafe_allow_html=True)

with st.container():
    with st.columns([1.25, .75, 1.25])[1]:
        place = st.text_input("Place: ")
        days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of days of the forecast")
        option = st.selectbox("Select data to view", ("Temperature", "Sky"))

with st.container():
    with st.columns([.5, 1, .5])[1]:
        st.subheader(f"{option} for the next {days} day(s) in {place}")
