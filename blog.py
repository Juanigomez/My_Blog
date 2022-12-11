# My Blog - pynet | juanigomez

import streamlit as st
import pandas as pd
from datetime import date
from PIL import Image as img

def get_Data(filename):
    data = pd.read_csv(filename)
    return data

def input_Data(filename, data):
    df = pd.DataFrame(data)
    df.to_csv(filename, mode='a', index=False, header=False)

dataset = get_Data('posts.csv')
all_Titles = list(dataset.iloc[:,0])
all_Contents = list(dataset.iloc[:,1])

pages = st.selectbox("Select a page", ['Homepage', 'Create a Post', 'Edit a Post', 'All Posts'])

def homepage():

    st.title("Welcome to my blog!")
    st.markdown('   My name si **_Juani Gomez_**, founder of _pynet_ and I am glad to present my blog, here you will be able to follow my journey on building a succesful software company.')
    logo = img.open('pynet_logo_complete.png')
    st.image(logo)

    index = 0
    count =  int(len(all_Titles) - 1)

    for post in all_Titles:
        st.subheader(all_Titles[index])
        st.write(all_Contents[index])
        if index == count:
            break
        else:
            index += 1

def create_Post():

    st.header("Create a new post")

    post_Title = st.text_input("Post title: ")
    post_Content = st.text_area("Post content: ")
    post_Date = st.date_input("Post date: ")
    submit_Btn = st.button("Submit")

    post = [[post_Title, post_Content, post_Date]]
    if submit_Btn:
        input_Data('posts.csv', post)

def edit_Post():

    st.header("Edit a Post")

    title = st.selectbox("Select a post: ", all_Titles)
    index = 0
    count = int(len(all_Titles) - 1)
                    
    if title != all_Titles[index]:
        for post in all_Titles:
            while title != all_Titles[index]:
                if index == count:
                    break
                else:
                    index += 1

    update_Title = st.text_input("Enter new title")
    update_Content = st.text_area("Enter new content")

    update_Btn = st.button("Update")

    if update_Btn:

        dataset.loc[index, '    TITLE   '] = update_Title
        dataset.loc[index, '           CONTENT           '] = update_Content
        
        dataset.to_csv('posts.csv',index=False)

def all_Posts():

    st.header("See all posts on the following table:")

    st.table(dataset)

if pages == 'Homepage':
    homepage()
elif pages == 'Create a Post':
    create_Post()
elif pages =='Edit a Post':
    edit_Post()
elif pages == 'All Posts':
    all_Posts()
