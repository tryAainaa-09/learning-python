import streamlit as st  # type: ignore[reportMissingImports]
import datetime

st.title(" Personal Dashboard")

#Sidebar for inputs
st.sidebar.header("👤 Personal Information")

name = st.sidebar.text_input("Your Name")
age = st.sidebar.number_input("Your Age", min_value=1, max_value=120, value=25)
favorite_color = st.sidebar.color_picker("Favorite Color", "#130985")
hobbies = st.sidebar.multiselect(
    "Your Hobbies",
    ["Reading", "Gaming", "Sports", "Music", "Cooking", "Travel"],
    default=["Reading"] 
)

#Main content

if name:
    st.header(f"Welcome, {name}! 🙋‍♀️")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Age", f"{age} years")

    with col2:
        st.metric("Hobbies", len(hobbies))

    with col3:
        birth_year = datetime.datetime.now().year  - age
        st.metric("Birth Year", birth_year)

    #Display  favorite color
    st.subheader("Your Favorite  Color")
    st.color_picker("", favorite_color, disabled=True)

    #Display Hobbies
    if hobbies:
        st.subheader("Your Hobbies")
        for hobby in hobbies:
            st.write(f". {hobby}")

    #Fun fact
    st.subheader("Fun Fact")
    days_lived = age * 365
    st.info(f"You've lived approximately {days_lived:,} days!")

else:
    st.info("Please enter your name in the sidebar to get started!")

#################################################################################################