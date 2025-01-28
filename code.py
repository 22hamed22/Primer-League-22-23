import streamlit as st

# HTML content with inline CSS
html_code = """
<div class="h1" style="background-color: #FFFFFF; color: #470B63; padding: 20px; font-size: 45px; max-width: 3500px; margin: auto; margin-top: 50px; display: flex; align-items: center; text-align: center; text-shadow: 1px 1px 1px #13A7AC;">
    <img src="https://logowik.com/content/uploads/images/premier-league-lion8499.jpg" alt="Image" width="300" style="float: left;">
    <span style="margin: auto; font-weight: bold;">Analysis of the Premier League season 2022-2023</span>
    <img src="https://logowik.com/content/uploads/images/premier-league-lion8499.jpg" alt="Image" width="300" style="float: right;">
</div>
"""

# Render the HTML in Streamlit
st.markdown(html_code, unsafe_allow_html=True)
