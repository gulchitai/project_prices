import streamlit as st
import pandas as pd

@st.cache
def read_excel(file):
    return pd.read_excel(file)

uploaded_file = st.file_uploader('Выберите файл прайс-листа:')
df = None

if uploaded_file is not None:
    df = read_excel(uploaded_file)
    st.dataframe(df.head(n=10))

    col1, col2, col3 = st.beta_columns(3)
    with col1:
        add_selectbox_header = st.selectbox("Заголовок",df.columns.to_list())
    with col2:
        add_selectbox_price = st.selectbox("Цена",df.columns.to_list())
    with col3:
        first_row = st.number_input("Первая строка",min_value=1, max_value=20, step=1)
    vendor = st.text_input("Поставщик")

    submit = st.button("Загрузить прайс")
    if submit:
        st.write('ok')
