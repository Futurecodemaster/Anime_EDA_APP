# Anime Data Analysis and Visualization Project

[Check out the live app here!](https://navdeeps-eda-app.streamlit.app/)

## Abstract
In this project, I've developed a web application using Streamlit, focusing on the analysis and visualization of a comprehensive anime dataset. My goal is to offer insights into various facets of anime, such as genres, ratings, and airing patterns. This application is designed to be an engaging tool for both anime enthusiasts and data analysts, providing interactive and in-depth exploration of anime data. I've created two tools as well: an Anime Recommendation Tool, designed to provide anime recommendations tailored to user input, and an Anime Rating Predictor, which attempts to forecast the rating of anime titles.

## Data Description

[Link to the Data Set](https://www.kaggle.com/datasets/hernan4444/anime-recommendation-database-2020?select=anime.csv)

### Data is only till 02/25/2021

The dataset used in this project includes 17,558 anime titles, encompassing a wide range of genres, types (TV, Movie, OVA), viewer scores, and airing dates. The data was cleaned and preprocessed for analysis, including handling missing values, normalizing text fields, and converting data types for analysis readiness. Specifically, the 'Score' column of the dataset is converted to numeric, handling any errors with coercion. Finally, the function returns the data, dropping any rows where 'Score' or 'Type' is missing. Key attributes include anime name, genre, type, number of episodes, and viewer ratings, which were pivotal in conducting the diverse analyses presented in the web app.

- **MAL_ID**: A unique identifier for each anime.
- **Name**: The title of the anime.
- **Score**: The overall rating score of the anime.
- **Genres**: Genres that the anime falls under.
- **English name**: The English title of the anime.
- **Japanese name**: The Japanese title of the anime.
- **Type**: Indicates whether the anime is a TV series, movie, OVA, etc.
- **Episodes**: The number of episodes in the series.
- **Aired**: Original airing dates.
- **Premiered**: The season and year of premiere.
- **Producers**, **Licensors**, **Studios**: Companies involved in the production.
- **Source**: The source material of the anime (e.g., manga, novel).
- **Duration**: The duration of each episode.
- **Rating**: Age suitability rating.
- **Ranked**: The rank of the anime based on the score.
- **Popularity**: The popularity rank of the anime.
- **Members**: The number of community members that are aware of the anime.
- **Favorites**: The number of times the anime has been favorited.
- **Watching**, **Completed**, **On-Hold**, **Dropped**, **Plan to Watch**: The number of users in each viewing status category.
- **Score-10** to **Score-1**: The number of users that have given each score from 10 to 1.

## Algorithm Description

In this project, I'm using a variety of algorithms and data processing techniques to dive into the fascinating world of anime data. Let me break down for you how each algorithm works, the way I've applied them, and how they're each contributing something special to this project.

### 1. Random Forest Regressor
- **Purpose**: Used for predicting the rating of an anime based on various features.
- **Application**: Implemented in the "Anime Rating Predictor" section.
- **Details**: This machine learning model is adept at handling a mix of categorical and numerical features and is used to estimate anime ratings.

### 2. MultiLabelBinarizer
- **Purpose**: To encode multiple labels per instance in the 'Genres' feature.
- **Application**: Utilized during data preprocessing in the "Anime Rating Predictor" section.
- **Details**: Transforms the genre labels into a binary matrix, preparing them for use in the machine learning model.

### 3. LabelEncoder
- **Purpose**: Encoding categorical data, specifically the 'Studio' feature.
- **Application**: In the "Anime Rating Predictor" for data preprocessing.
- **Details**: Converts studio names into numerical values, enabling their use in the prediction model.

### 4. Train-Test Split (train_test_split)
- **Purpose**: Splitting the dataset into training and testing sets for model validation.
- **Application**: Used in the "Anime Rating Predictor" section for model training and validation.
- **Details**: A critical step in machine learning to evaluate the model's performance on unseen data.

### 5. Correlation Calculation (corr)
- **Purpose**: To calculate the correlation coefficient between pairs of variables.
- **Application**: In sections like "Correlation between Anime Score and Popularity" and "Correlation between Number of Episodes and Anime Score".
- **Details**: Helps in understanding the strength and direction of linear relationships between variables.

### 6. Plotly Express (px)
- **Purpose**: For creating interactive data visualizations.
- **Application**: Used across various sections for enhanced data visualization.
- **Details**: Enables the creation of dynamic, interactive graphs that improve user engagement and data interpretation.

### 7. Seaborn and Matplotlib (sns, plt)
- **Purpose**: For creating static data visualizations.
- **Application**: Throughout the application for plotting various types of graphs.
- **Details**: These libraries are essential for depicting data distributions, trends, and statistical insights in a visually appealing manner.

### 8. Pandas Descriptive Statistics (describe)
- **Purpose**: To generate summary statistics of data distributions.
- **Application**: In "General Statistics" and "Episode Count Analysis".
- **Details**: Provides a quick overview of the dataset, including measures like mean, standard deviation, min/max values, and quantiles.


## Tools Used
For this project, I have employed several tools:
- **Streamlit**: To create the user interface of the web application.
- **Pandas**: For data manipulation and cleaning.
- **Matplotlib & Seaborn**: To generate static visualizations.
- **Plotly**: For interactive and dynamic visualizations.
- **Scikit-learn**: For implementing machine learning algorithms
- **NumPy**: For handling numerical operations.
- I've also used additional libraries such as **streamlit_lottie** for animations and **requests** for fetching external data.

