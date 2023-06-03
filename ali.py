import requests
import streamlit as st
from streamlit_lottie import st_lottie
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")
def load_lottieur1(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
#----LOAD ASSESTS----
lottie_coding = load_lottieur1("https://assets1.lottiefiles.com/packages/lf20_iv4dsx3q.json")


# ----HEADER SECTION----
st.subheader(" Hi, I am Ali Alharbe")
st.title("A Data Analyst From Kuwait")
st.write("Ali Alharbe one of those guys who want to learn more about web developing")
st.write("[learn More With Ali Alharbe>](https://www.instagram.com/_8u3/?hl=en&__coig_restricted=1)")



#---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("what i do?")
        st.write("##")
        st.write("""
        On my instagram you can DM me and i will help you
       - are looking for a way to leverage the power of Python in their day-to-day work.
       -are struggling with repetitive tasks in Excel and are looking for a way to use Python and BA. want to learn Data Analysis & Data Science to perform meaningful and impactful analyses. are working with Excel and found themselves thinking - "there has to be a better way."
""")
        st.write("[Instagram Page >](https://www.instagram.com/_8u3/?hl=en)")
with right_column:
    st_lottie(lottie_coding, height=300, key="coding")
