# import streamlit as st
# import pickle
# import pandas as pd
# import requests
#
#
# def fetch_poster(movie_id):
#     url=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=2da49761260afcf59aa0b7f7f91c7884".format(movie_id))
#     data= requests.get(url)
#     data=data.json()
#     return "https://image.tmdb.org/t/p/w500/"+data["poster_path"]
#
#
#
# def recommend(movie):
#     movie_index = movies[movies["title"] == movie].index[0]
#     distances = similarity[movie_index]
#     movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#
#     recommended_movies = []
#     recommended_movies_posters = []
#     for i in movie_list:
#         movie_id = movies.iloc[i[0]].movie_id
#         recommended_movies.append(movies.iloc[i[0]].title)
#         # fetch poster from API
#         recommended_movies_posters.append(fetch_poster(movie_id))
#     return recommended_movies, recommended_movies_posters
#
#
# movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
# similarity = pickle.load(open("similariry.plk", "rb"))
# movies = pd.DataFrame(movies_dict)
#
# st.title("Movie Recommender System")
#
# selected_movie_name= st.selectbox("How would you like to be contacted?", movies["title"].values)
#
# if st.button("Recommend"):
#     names, posters = recommend(selected_movie_name)
#     col1, col2, col3, col4, col5 = st.columns(5)
#
#     with col1:
#         st.text(names[0])
#         st.image(posters[0])
#     with col2:
#         st.text(names[1])
#         st.image(posters[1])
#     with col3:
#         st.text(names[2])
#         st.image(posters[2])
#     with col4:
#         st.text(names[3])
#         st.image(posters[3])
#     with col5:
#         st.text(names[4])
#         st.image(posters[4])
#

import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=2da49761260afcf59aa0b7f7f91c7884&language=en-US".format(
        movie_id
    )
    data = requests.get(url).json()
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]


def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[
        1:21
    ]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # Fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


# Load the movies and similarity data
movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))  # Ensure the correct file name

movies = pd.DataFrame(movies_dict)

# Streamlit UI
st.title("Movie Recommender System")

# Dropdown for movie selection
selected_movie_name = st.selectbox("Choose a movie:", movies["title"].values)

# Recommendation button
if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    # Display recommendations
    col1, col2, col3, col4, col5 = st.columns(5)

    # with col1:
    #     st.text(names[0])
    #     st.image(posters[0])
    # with col2:
    #     st.text(names[1])
    #     st.image(posters[1])
    # with col3:
    #     st.text(names[2])
    #     st.image(posters[2])
    # with col4:
    #     st.text(names[3])
    #     st.image(posters[3])
    # with col5:
    #     st.text(names[4])
    #     st.image(posters[4])

    # Display recommendations
    cols = st.columns(5)  # Create 5 columns

    for i in range(20):  # Loop through the first 20 recommended movies
        with cols[i % 5]:  # Cycle through the columns
            # st.text(names[i])  # Display the movie name
            # st.image(posters[i])  # Display the movie poster
            st.markdown(
                f"[![{names[i]}]({posters[i]})](https://www.google.com/search?q={names[i]})",
                unsafe_allow_html=True,
            )

# Footer
st.markdown(
    """
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            text-align: center;
            font-size: 12px;
            color: grey;
        }
    </style>
    <div class="footer">
        &copy; 2024 Kuldeep Sahoo. All rights reserved.
    </div>
""",
    unsafe_allow_html=True,
)
