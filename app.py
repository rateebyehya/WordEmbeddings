import streamlit as st
import os 

#An embedding is a vector of floating point numbers. The distance between two vectors measures their relatedness. 
#Small distances suggest high relatedness and large distances suggest low relatedness 

#As LangChain has been working aggressively on improving the tool
from langchain_openai import OpenAIEmbeddings

#FAISS is an open-source library developed by Facebook AI Research for efficient similarity search and clustering of large-scale datasets, particularly with high-dimensional vectors. 
#It provides optimized indexing structures and algorithms for tasks like nearest neighbor search and recommendation systems.

from langchain_community.vectorstores import FAISS 

#load_dotenv() is a function that loads variables from a .env file into environment variables in a Python script. 
#It allows you to store sensitive information or configuration settings separate from your code
#and access them within your application.
from dotenv import load_dotenv

load_dotenv()

#By using st.set_page_config(), you can customize the appearance of your Streamlit application's web page
st.set_page_config(page_title="Educate Kids", page_icon=":robot:")
st.header("Hey, insert something, and I will give out similar things")

embeddings = OpenAIEmbeddings()

#The below snippet helps us to import CSV file data for our tasks
from langchain.document_loaders.csv_loader import CSVLoader
loader = CSVLoader(file_path='myData.csv', csv_args={
    'delimiter': ',',
    'quotechar': '"',
    'fieldnames': ['Words']
})

#Assigning the data inside the csv to our variable here
data = loader.load()

#Display the data
print(data)

db = FAISS.from_documents(data, embeddings)

#Function to receive input from user and store it in a variable
def get_text():
    input_text = st.text_input("You: ", key= input)
    return input_text

user_input=get_text()
submit = st.button('Find similar things')  

if submit:
    
    #If the button is clicked, the below snippet will fetch us the similar text
    docs = db.similarity_search(user_input)
    st.subheader("Top Matches:")
    st.text(docs[0].page_content)
    st.text(docs[1].page_content)

