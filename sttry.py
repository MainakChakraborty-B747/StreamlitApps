import sqlite3 as sq
import streamlit as st
st.title("Demo")
try:
    s=sq.connect('data.db')
    c=s.cursor()
    c.execute('''CREATE TABLE datab (name TEXT(50), age INT(3));''')
except sq.OperationalError:
    pass
def feeddata(n,a):
    c.execute('''INSERT INTO datab(name,age) VALUES (?,?);''',(n,a))
    s.commit()
    s.close()
with st.form("sample data",clear_on_submit=True):
    na=st.text_input("Enter Your Name: ")
    ag=st.number_input("Enter your age: ",min_value=1.0,max_value=150.0)
    subm=st.form_submit_button("Submit",on_click=feeddata(na,ag))
    if subm:
        pass
