# Anime Data Analysis and Visualization Project

[Check out the live app here!](https://navdeeps-eda-app.streamlit.app/)

## Abstract
In this project, I've developed a web application using Streamlit, focusing on the analysis and visualization of a comprehensive anime dataset. My goal is to offer insights into various facets of anime, such as genres, ratings, and airing patterns. This application is designed to be an engaging tool for both anime enthusiasts and data analysts, providing interactive and in-depth exploration of anime data. I've created two tools as well: an Anime Recommendation Tool, designed to provide anime recommendations tailored to user input, and an Anime Rating Predictor, which attempts to forecast the rating of anime titles.

## Data Description
The dataset used in this project includes 17,558 anime titles, encompassing a wide range of genres, types (TV, Movie, OVA), viewer scores, and airing dates. The data was cleaned and preprocessed for analysis, including handling missing values, normalizing text fields, and converting data types for analysis readiness. Specifically, the 'Score' column of the dataset is converted to numeric, handling any errors with coercion. Finally, the function returns the data, dropping any rows where 'Score' or 'Type' is missing. Key attributes include anime name, genre, type, number of episodes, and viewer ratings, which were pivotal in conducting the diverse analyses presented in the web app.

1. **MAL_ID**: A unique identifier for each anime.
2. **Name**: The title of the anime.
3. **Score**: The overall rating score of the anime.
4. **Genres**: Genres that the anime falls under.
5. **English name**: The English title of the anime.
6. **Japanese name**: The Japanese title of the anime.
7. **Type**: Indicates whether the anime is a TV series, movie, OVA, etc.
8. **Episodes**: The number of episodes in the series.
9. **Aired**: Original airing dates.
10. **Premiered**: The season and year of premiere.
11. **Producers**, **Licensors**, **Studios**: Companies involved in the production.
12. **Source**: The source material of the anime (e.g., manga, novel).
13. **Duration**: The duration of each episode.
14. **Rating**: Age suitability rating.
15. **Ranked**: The rank of the anime based on the score.
16. **Popularity**: The popularity rank of the anime.
17. **Members**: The number of community members that are aware of the anime.
18. **Favorites**: The number of times the anime has been favorited.
19. **Watching**, **Completed**, **On-Hold**, **Dropped**, **Plan to Watch**: The number of users in each viewing status category.
20. **Score-10** to **Score-1**: The number of users that have given each score from 10 to 1.

## Algorithm Description
In developing this application, I have utilized various data processing algorithms to organize and analyze the anime data effectively. These include:
- Data filtering and sorting based on different attributes like genre, score, and type.
- Predictive modeling, using RandomForestRegressor, to forecast trends.
- Data visualization techniques to present the data in an accessible and engaging manner.

## Tools Used
For this project, I have employed several tools:
- **Streamlit**: To create the user interface of the web application.
- **Pandas**: For data manipulation and cleaning.
- **Matplotlib & Seaborn**: To generate static visualizations.
- **Plotly**: For interactive and dynamic visualizations.
- **Scikit-learn**: For implementing machine learning algorithms
- **NumPy**: For handling numerical operations.
- I've also used additional libraries such as **streamlit_lottie** for animations and **requests** for fetching external data.

