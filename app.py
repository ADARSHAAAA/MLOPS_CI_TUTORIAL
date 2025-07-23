import streamlit as st

st.title("Power calculator")

st.write ("Enter  a number to calculate the square, cube and fifth power ")


n = st.number_input("Enter a number", value=1, step=1)

square = n ** 2
cube = n ** 3 
fifth_power = n**5


st.write(f"the square of {n} is {square}")
st.write(f"the cube of {n} is {cube}")
st.write(f"the fifth power of {n} is {fifth_power}")