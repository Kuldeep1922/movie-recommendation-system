# Movie Recommendation System 🎬
![App Screenshot](https://github.com/Kuldeep-Sahoo/movie-recommendation-system/blob/main/image.png?raw=true)
This is a Movie Recommendation System built with Streamlit, which suggests movies based on a selected movie using content-based filtering. The app utilizes The Movie Database (TMDb) API to fetch movie posters and display them with clickable links that perform a Google search for the movie.

**Deployed at**: [Movie Recommendation System](https://movie-recommendation-system-rler.onrender.com/)

---

## Features 🚀

- **Movie Recommendation**: Suggests movies similar to a selected movie.
- **Poster Fetching**: Fetches movie posters using the TMDb API.
- **Google Search**: Clicking on a movie poster performs a Google search for the movie.
- **User-Friendly Interface**: Simple and clean UI using Streamlit.

---

## How It Works 🛠️

- The system recommends movies using a content-based filtering technique, comparing the selected movie with others based on similarity scores.
- It retrieves movie posters from the TMDb API to display next to the recommended movies.
- Clicking on a movie poster redirects the user to a Google search for the respective movie.

---

## Installation and Setup 🖥️

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Kuldeep-Sahoo/movie-recommendation-system.git/
    ```

2. **Navigate to the project directory:**

    ```bash
    cd movie-recommendation-system
    ```

3. **Install the dependencies:**

    Install the required Python packages using `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

4. **Download required files:**

    You need two files: `movie_dict.pkl` and `similarity.pkl`. These files should be generated using a pre-trained model or loaded from a dataset.

5. **Run the application:**

    Start the Streamlit server:

    ```bash
    streamlit run app.py
    ```

6. **Access the app:**

    Once the server is running, the app will be accessible at:

    ```
    http://localhost:8501/
    ```

---

## Deployment 🌍

The project is deployed on Render. You can access the live version of the app here:

[Movie Recommendation System on Render](https://movie-recommendation-system-rler.onrender.com/)

---

## API Used 🌐

This project uses [The Movie Database (TMDb) API](https://www.themoviedb.org/) to fetch movie details and posters.

To use the API, you will need an API key, which can be obtained from the TMDb website. Replace `your_api_key` in the app code with your actual API key.

---

## File Structure 📂

```plaintext
movie-recommendation-system/
├── app.py                # Main Streamlit app file
├── movie_dict.pkl        # Pickle file containing movie data
├── similarity.pkl        # Pickle file containing similarity data
├── requirements.txt      # Python dependencies
├── README.md             # Project README file
└── .gitignore            # Git ignore file
