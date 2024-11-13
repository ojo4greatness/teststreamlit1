import streamlit as st

st.title("Welcome to my app")

df = {
    'students': ['Ade', 'Tola', 'Ope', 'Amos'],
    'points': [900, 674, 294, 674]
}

st.bar_chart(df, x='students', y='points', horizontal=True)
