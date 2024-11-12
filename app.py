import streamlit as st
import pandas as pd

st.title('Employees Data Dashboard')
uploaded_file = st.file_uploader('Choose a CSV file', type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Data:")
    st.write(df)

    columns = df.columns.tolist()
    column_to_plot = st.selectbox("Select a column to plot", columns)

    # Plot the selected column
    st.write(f"Plotting column: {column_to_plot}")
    st.line_chart(df[column_to_plot])