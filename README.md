# Anime Data Analysis and Visualization Project

[Check out the live app here!](https://navdeeps-eda-app.streamlit.app/)

## Abstract
The main purpose of my project was to create an interactive web application for analyzing and visualizing anime data. Using Streamlit, I developed a platform where users can explore various aspects of anime, such as genres, popularity trends, and viewer ratings. The app successfully integrates Python libraries like Pandas, NumPy, and Scikit-learn for processing large datasets and implementing machine learning for features like anime rating prediction.

From this project, I achieved an engaging and user friendly application that offers personalized anime recommendations and insights into viewer behavior.

## Data Description

[Link to the Data Set](https://www.kaggle.com/datasets/hernan4444/anime-recommendation-database-2020?select=anime.csv)

### Data is only till 02/25/2021

The data was sourced from a CSV file containing detailed information about 17,558 anime titles. It included following attributes:

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

**Data Cleaning and Preprocessing:**

   - **Missing Values**: I handled missing data, particularly in fields like `Score`, `Type`, and `Genres`. Rows with missing scores were dropped to maintain analysis integrity.
   - **Type Conversion**: Certain columns like `Score` and `Episodes` were converted to numeric types to facilitate statistical analysis.
   - **Date Handling**: The `Aired` column was processed to extract the year, which was essential for trend analysis over time.
   - **Genre Processing**: The `Genres` column, containing comma separated values, was split and restructured for genre based analysis.

**Data Transformation:**

   - **Binarization**: Used MultiLabelBinarizer for transforming the `Genres` column into a binary format suitable for machine learning models.
   - **Label Encoding**: The `Studios` column was encoded using LabelEncoder to convert studio names into a machine readable numeric format.


## Algorithm Description

I'm using a variety of algorithms and data processing techniques. Let me break down for you how each algorithm works, the way I've applied them, and how they're each contributing something special to this project.

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
For this project, I have used the following tools:
- **Streamlit**: To create the user interface of the web application.
- **Pandas**: For data manipulation and cleaning.
- **Matplotlib & Seaborn**: To generate static visualizations.
- **Plotly**: For interactive and dynamic visualizations.
- **Scikit-learn**: For implementing machine learning algorithms
- **NumPy**: For handling numerical operations.
- I've also used additional libraries such as **streamlit_lottie** for animations and **requests** for fetching external data.

