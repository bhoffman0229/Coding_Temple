from pathlib import Path
import streamlit as st
import sys
import os

filepath = os.path.join(Path(__file__).parents[1])
print(filepath)

sys.path.insert(0, filepath)

from to_mongo import ToMongo

c = ToMongo()
st.header('Which Student')
st.write('This is where you will search for each piece of data on a student youre looking for')

answer = st.text_input('Enter a student name:', value = 'Sol Ring')
st.write(list(c.student.find({'name': answer})))