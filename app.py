import pickle
import streamlit as st
import pandas as pd
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies
movies_list = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_list)
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender system')

Selected_movie_name = st.selectbox('Movie Name',movies['title'].values)
if st.button('Recommend'):
    recommendations = recommend(Selected_movie_name)
    for i in recommendations:
        st.write(i)