import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

#  st.write("""
#  # Hello world
#  
#  This is a hello world message
         #  """)

st.write(pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40]
    }))

st.markdown("""
# This is a markdown cell
markdown is a way to write text in a more readable way
""")

st.title("This is a title")

st.header("This is a header")

st.subheader("This is a subheader")

st.caption("Copyright 2021")

code = """def hello():
    print("Hello, Streamlit!")
"""

st.code(code, language='python')

st.text("This is a text")

st.latex(r"""
         \sum_{k=0}^{n-1} ar^k =
         a \left(\frac{1-r^{n}}{1-r}\right)
         """)

df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40]
})

st.dataframe(df, width=500, height=150)
st.table(df)

st.metric(label="Temperature", value="32 C", delta="1 C")
st.json({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40]
    })

x = np.random.normal(15, 5, 250)

fig, ax = plt.subplots()
ax.hist(x, bins=15)
st.pyplot(fig)

name = st.text_input(label='Nama Lengkap', value='')
st.write('Nama: ', name)

text = st.text_area('Feedback')
st.write('Feedback: ', text)

number = st.number_input(label='Umur')
st.write('Umur: ', int(number), ' tahun')

date = st.date_input(label='Tanggal lahir', min_value=datetime.date(1900, 1, 1))
st.write('Tanggal lahir:', date)

uploaded_file = st.file_uploader('Choose a CSV file')
 
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

picture = st.camera_input('Take a picture')
if picture:
    st.image(picture)


if st.button('Say hello'):
    st.write('Hello there')

agree = st.checkbox('I agree')
 
if agree:
    st.write('Welcome to MyApp')

genre = st.radio(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary'),
    horizontal=True
)

genre = st.selectbox(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

genre = st.multiselect(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

with st.sidebar:
    st.write('This is a sidebar')
    values = st.slider(
            label='Select a range of values',
            min_value=0, max_value=100, value=(0, 100))
    st.write('Values:', values)

col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    st.header('A cat')
    st.image('https://static.streamlit.io/examples/cat.jpg')

with col2:
    st.header('A dog')
    st.image('https://static.streamlit.io/examples/dog.jpg')

with col3:
    st.header('An owl')
    st.image('https://static.streamlit.io/examples/owl.jpg')

tab1, tab2, tab3 = st.tabs(['Tab 1', 'Tab 2', 'Tab 3'])

with tab1:
    st.write('This is tab 1')
    st.image('https://static.streamlit.io/examples/dog.jpg')

with tab2:
    st.write('This is tab 2')
    st.image('https://static.streamlit.io/examples/cat.jpg')

with tab3:
    st.write('This is tab 3')
    st.image('https://static.streamlit.io/examples/owl.jpg')

with st.container():
    st.write('This is inside the container')
    
    fig, ax = plt.subplots()
    ax.hist(x, bins=15)
    st.pyplot(fig)

st.write('This is outside the container')


with st.expander('See explanation'):
    st.write("""
        Here is some explanation
        """)
