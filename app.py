import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import numpy as np 
import plotly.express as px
from streamlit_lottie import st_lottie
from collections import Counter
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer, LabelEncoder

#---------------CSS------------------


def custom_css():
    st.markdown("""
        <style>
        h1 {
            color: #FF4500;
            text-align: center;
        }
        h2 {
            color: #FFA07A;
        }
        footer {
            visibility: hidden;
        }
        </style>
        """, unsafe_allow_html=True)

st.set_page_config(page_title="My Webpage", page_icon=":tada:")

custom_css()


#---------LOTTIE-------------

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/5ae5c403-6777-4ddc-9d4b-69b991f2244e/SrRQPFgsnv.json")

st.title('Anime Analytics Pro')

with st.container():
    st.write("---")
    st_lottie(lottie_coding, height=300, key="coding")
    
    
#---------DATAFRAME-------------

@st.cache_data 
def load_data():
    data = pd.read_csv('anime.csv') 
    data['Score'] = pd.to_numeric(data['Score'], errors='coerce')
    return data.dropna(subset=['Score', 'Type'])

data = load_data()

# Displays subset
st.subheader('Subset of Data')
st.dataframe(data.head()) 



#-----------GENERAL STATISTICS--------------

# def display_stats(data):
#     # Descriptive statistics for numerical columns
#     descriptive_stats = data.describe()

#     # descriptive statistics for the Score column
#     score_stats = data['Score'].describe()

#     return descriptive_stats, score_stats

# def main():
#     st.title("Anime Data Statistics")

#     descriptive_stats, score_stats = display_stats(data)

#     st.subheader("Descriptive Statistics for Numerical Columns")
#     st.write(descriptive_stats)

#     st.subheader("Descriptive Statistics for the Score Column")
#     st.write(score_stats)

# if __name__ == "__main__":
#     main()


st.subheader('General Statistics')

st.write("""
### 
- **MAL_ID**: The IDs range from 1 to 48,492, indicating a large and diverse set of anime titles.
- **Popularity**: Varies widely, indicating a mixed set of well-known and lesser-known anime.
- **Members**: The number of members interested in each anime ranges significantly, with some titles having over 2.5 million members.
- **Favorites**: Some anime are highly favored, with the maximum number of favorites being 183,914.
- **Watching, Completed, On-Hold, Dropped, Plan to Watch**: These columns provide insights into how viewers engage with the anime, showing large variations in viewer behavior.
""")

st.markdown("""
### Score Statistics
- **Mean Score**: The average score is approximately 6.51, on a scale from 1.85 to 9.19.
- **Standard Deviation**: The standard deviation of 0.89 indicates a moderate spread in the scores.
- **Median Score**: The median score is 6.52, very close to the mean, suggesting a relatively symmetric distribution of scores.
""")

#---------DISTRIBUTION OF ANIME SCORES----------

df = load_data() 

# Converting score column to numeric 
df['Score'] = pd.to_numeric(df['Score'], errors='coerce')

st.title('Distribution of Anime Scores')

# Slider for selecting score range
min_score, max_score = st.slider('Select Score Range:', float(df['Score'].min()), float(df['Score'].max()), (1.85, 9.0))
filtered_data = df[df['Score'].between(min_score, max_score)]

# Plotting the distribution of scores
plt.figure(figsize=(10, 4))
sns.histplot(filtered_data['Score'], bins=30, kde=True)
plt.title('Score Distribution')
plt.xlabel('Score')
plt.ylabel('Frequency')
st.pyplot(plt)

st.markdown("""
### Score Distribution Analysis
- **The distribution of anime scores shows a roughly bell-shaped curve, indicating a normal distribution.**
- **Most scores are clustered around the mean of 6.51**, with fewer titles receiving extremely high or low scores.
- **This suggests a general consistency in the scoring of anime titles.**
""")

# TRENDS

def load_data_1():
    df = pd.read_csv('anime.csv')
    df['Score'] = pd.to_numeric(df['Score'], errors='coerce')
    df['Year'] = pd.to_datetime(df['Aired'].str.extract(r'(\d{4})')[0], errors='coerce').dt.year
    df['Genres'] = df['Genres'].fillna('').apply(lambda x: x.split(', '))
    df.dropna(subset=['Score', 'Year'], inplace=True)
    return df

df = load_data_1()

# Average Score Trend Over Years
st.markdown("""
        ### Average Score Trend Over Year
         A line chart showing the average score per year is displayed. This helps in understanding how anime scores have evolved over time.
         """)
avg_score_by_year = df.groupby('Year')['Score'].mean().dropna()
st.line_chart(avg_score_by_year)




#---------GENRE ANALYSIS IN ANIME-------------

st.title('Genre Analysis in Anime')

st.markdown("""
- **Now, let's analyze the genres of the anime in the dataset.**
- **This will involve extracting genres from each title**, counting their occurrences, and visualizing the frequency of each genre.
""")


df = load_data() 

# Extracting genres
df['Genres'] = df['Genres'].fillna('Unknown')
all_genres = df['Genres'].str.split(', ').sum()
genre_counts = Counter(all_genres)

# Selecting a number of top genres to display
top_n = st.slider('Number of Top Genres to Display:', min_value=5, max_value=30, value=10)
top_genres = dict(genre_counts.most_common(top_n))

# Plotting the top genres
plt.figure(figsize=(12, 6))
sns.barplot(x=list(top_genres.values()), y=list(top_genres.keys()))
plt.title(f'Top {top_n} Genres in Anime')
plt.xlabel('Frequency')
plt.ylabel('Genres')
st.pyplot(plt)

st.markdown("""
- **The bar plot illustrates the frequency of different anime genres in the dataset.**
- Certain genres stand out more than others, showing they're either more popular or just appear more often in anime.
""")



#-------ANIME TYPES DISTRIBUTION------------

st.title('Anime Types Distribution')

st.markdown("""
- **Next, we will explore the distribution of various anime formats, including TV series, movies, and more.**
- **This analysis aims to understand the composition of the dataset in terms of anime formats.** It will provide insights into which formats are more commonly represented and potentially indicate trends in anime production.
- **By exploring this aspect, we'll gain a clearer picture of the anime landscape** as captured in the dataset.
""")


df = load_data()  

# Counting the occurrences of each type
type_counts = df['Type'].value_counts()

# Plotting 
plt.figure(figsize=(10, 6))
sns.barplot(x=type_counts.index, y=type_counts.values)
plt.title('Distribution of Different Types of Anime')
plt.xlabel('Type')
plt.ylabel('Frequency')
st.pyplot(plt)

st.markdown("""
- **The bar plot above reveals how different types of anime, like TV series and movies, are distributed.**
- **This visualization is key to understanding the diversity of anime production and consumption.** It highlights not just the popular formats, but also the niche ones that contribute to the rich tapestry of anime culture.
- **By examining these patterns, we gain insight into the evolving trends and preferences in the anime industry.**
""")


#--------EPISODE COUNT ANALYSIS IN ANIME------------

st.title('Episode Count Analysis in Anime')

st.markdown("""
- **Now, let's take a closer look into the range of episode counts across the dataset.**
- This analysis help us figure out how long most anime shows are. We want to know how many episodes are usual for different kinds of anime. By looking at this, we can learn more about how anime stories are told and made.
""")

# Converting 'Episodes' to numeric
df['Episodes'] = pd.to_numeric(df['Episodes'], errors='coerce')


@st.cache_data
def load_data():
    data = pd.read_csv('anime.csv')  
    data['Episodes'] = pd.to_numeric(data['Episodes'], errors='coerce')
    return data

data = load_data()

def display_episode_stats(data):
    # Descriptive statistics for the Episodes column
    episode_stats = data['Episodes'].describe()

    # Count of missing values in the Episodes column
    missing_episodes = data['Episodes'].isna().sum()

    return episode_stats, missing_episodes

def main():
    episode_stats, missing_episodes = display_episode_stats(data)

    st.subheader("Descriptive Statistics for the Episodes Column")

    # Transposing the stats for horizontal display
    episode_stats_df = pd.DataFrame(episode_stats).transpose()

    st.table(episode_stats_df)
    
if __name__ == "__main__":
    main()



st.markdown("""
### Episode Count Distribution in Anime
- **Count**: There are 17,046 anime titles with numeric episode counts in our dataset.
- **Mean**: On average, an anime has about 11.53 episodes, indicating a trend towards shorter series.
- **Standard Deviation**: A high standard deviation (47.35) highlights the wide variance in episode counts, from short to very long series.
- **Minimum**: The minimum episode count is 1, typical for movies or short series.
- **Quartiles**: Intriguingly, 25% of anime have only 1 episode, and 75% have 12 episodes or fewer, underscoring the prevalence of short series or movies.
- **Maximum**: An outlier is the maximum episode count of 3,057, likely representing long-running series like 'Lan Mao'.
- **Histogram Insights**: The histogram, which you can view below, illustrates a heavy concentration of anime with a small number of episodes. This trend sharply declines for longer series, echoing the industry norm where many series are brief, while a few are exceptionally long-running.
""")


# Slider for selecting episode range
min_episodes, max_episodes = st.slider('Select Episode Range:', int(df['Episodes'].min()), int(df['Episodes'].max()), (1, 100))
filtered_episodes = df[df['Episodes'].between(min_episodes, max_episodes)]

# Plotting the distribution of episodes
plt.figure(figsize=(10, 4))
sns.histplot(filtered_episodes['Episodes'], bins=30, kde=False)
plt.title('Episode Distribution')
plt.xlabel('Number of Episodes')
plt.ylabel('Frequency')
st.pyplot(plt)


#------------TRENDS IN ANIME AIRING AND PREMIERING----------------

st.title('Trends in Anime Airing and Premiering')

st.markdown(""" 
- **This involves analysis of the 'Aired' and 'Premiered' columns** in our dataset, which will reveal how anime release patterns have evolved over time.
- **By exploring these trends**, we aim to understand not only the frequency of anime productions but also identify any significant changes or developments in the industry across different periods.
- **This analysis is crucial for grasping the historical context** and the current state of anime production, potentially offering insights into future trends.
""")

# Extracting year from 'Aired' column
df['Aired Year'] = df['Aired'].str.extract(r'(\d{4})')
df['Aired Year'] = pd.to_numeric(df['Aired Year'], errors='coerce')

# Grouping data by aired year and calculating the count
yearly_counts = df['Aired Year'].value_counts().sort_index()

# Plotting
plt.figure(figsize=(15, 6))
sns.lineplot(x=yearly_counts.index, y=yearly_counts.values)
plt.title('Trend of Anime Airing Over Years')
plt.xlabel('Year')
plt.ylabel('Number of Anime')
st.pyplot(plt)

st.markdown("""
### Trend of Anime Premiering Over the Years
- **The line plot above provides a visual journey through the history of anime premieres year by year.**
- There's a noticeable general increase in the number of anime premiering each year, with a significant uptick starting from the early 2000s. This trend mirrors the anime industry's expansion and its escalating popularity across the globe.
- The plot also highlights some fluctuations in certain years. These variations could be reflections of changing industry dynamics, broader economic conditions, or even nuances in how data has been collected over time.
- **Overall**, this visualization offers a compelling narrative of the anime industry's growth and its evolving landscape.
""")


#-----------POPULARITY TRENDS IN ANIME OVER TIME------------

st.title('Popularity Trends in Anime Over Time')

df['Popularity'] = pd.to_numeric(df['Popularity'], errors='coerce')

popularity_trends = df.groupby('Aired Year')['Popularity'].mean().dropna().reset_index()

fig = px.line(popularity_trends, x='Aired Year', y='Popularity', 
              title='Average Anime Popularity Trends Over Years',
              labels={'Popularity': 'Average Popularity', 'Aired Year': 'Year'},
              markers=True)

fig.update_traces(line=dict(color='Turquoise', width=3), 
                  marker=dict(color='DarkSlateBlue', size=6, line=dict(color='MediumPurple', width=2)))

fig.update_traces(hovertemplate='Year: %{x}<br>Popularity: %{y:.2f}')

fig.update_xaxes(title_text='Year', tickangle=-45, gridcolor='LightGrey')

# Inverting y-axis as lower numbers indicate higher popularity
fig.update_yaxes(title_text='Average Popularity', autorange='reversed', gridcolor='LightGrey')

fig.update_layout(autosize=True)

st.plotly_chart(fig, use_container_width=True)


st.markdown("""
The line graph above shows the trend of anime popularity over the years, based on the average number of members per anime title. This visualization represents how the average interest in anime has evolved over time.
- **Insights**:
    - There is a noticeable upward trend in the average number of members interested in anime titles, especially in more recent years.
    - This increase suggests that anime has been growing in popularity, attracting larger audiences over time.
    - The graph also highlights specific years where there was a significant spike in interest, which could correlate with the release of highly popular anime titles or increased global exposure of anime.

- This analysis, therefore, provides a clear indication of the growing appeal of anime across a wider audience, making it a valuable insight for content creators, marketers, and platforms involved in the anime industry. ​​            
""")

# ANIME TYPE POPULARITY TREND


def load_data_2():
    df = pd.read_csv('anime.csv')
    df['Year'] = pd.to_datetime(df['Aired'].str.extract(r'(\d{4})')[0], errors='coerce').dt.year
    return df

df = load_data_2()

st.markdown("""
            ### Anime Type Popularity Trend
            This visualizes how the popularity of different types of anime (TV, Movie, OVA, etc.) has changed over the years. Users can select an anime type from a dropdown menu.
    """)

# User input for selecting anime type
selected_type = st.selectbox('Select Type of Anime', df['Type'].unique(), key='type_select')

# Filtering data based on selected type
type_filtered_df = df[df['Type'] == selected_type].groupby('Year').size()

# Plotting
st.write(f"Popularity Trend for Type: {selected_type}")
st.line_chart(type_filtered_df)


#---------FAVORITE GENRES ANALYSIS--------------
st.title('Favorite Genres Analysis')

def load_data():
    data = pd.read_csv("anime.csv")
    return data

def plot_genres(anime_data, max_genres):
    genre_counts = anime_data['Genres'].str.split(', ').explode().value_counts()

    genre_df = genre_counts.reset_index()
    genre_df.columns = ['Genre', 'Count']

    selected_genres = genre_df.head(max_genres)

    fig = px.bar(selected_genres, x='Count', y='Genre', orientation='h', 
                 title='Favorite Genres in Anime', 
                 labels={'Count': 'Count', 'Genre': 'Genre'},
                 color='Genre',
                 color_continuous_scale=px.colors.sequential.Viridis)
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig)

anime_data = load_data()

max_genres = st.slider('Select the number of genres to display', 10, len(anime_data['Genres'].str.split(', ').explode().unique()), 10)

plot_genres(anime_data, max_genres)



st.markdown("""
In the diverse world of anime, genres play a crucial role in defining the narrative and appeal of each series. This analysis delves into understanding which genres resonate the most with the audience. By examining the prevalence of different genres in anime, we gain insights into viewer preferences and emerging trends in the anime industry.

- **Comedy** is the most common type of anime, with 6029 shows, showing that a lot of anime fans like it. 
- **Action** is the second most common, with 3888 shows, meaning many viewers enjoy exciting and action-packed anime. 
- **Fantasy** and Adventure are also popular, with 3285 and 2957 shows. These kinds usually have creative stories full of adventures. 
- **Anime** for kids and with music are also popular, which means there are many different kinds of fans, including young ones and those who like songs in anime. 
- Other liked types are Drama, Sci-Fi, Shounen (for young boys), and Slice of Life, which range from everyday life stories to futuristic tales. 
- While Comedy, Action, and Fantasy are the top choices, genres like Psychological or Horror are less common but still important, as they appeal to fans who want deeper and more intense stories. This variation highlights the diverse tastes within the anime community.

""")

# TREND

df = load_data_1()

# Genre Popularity Trend
st.header("Genre Popularity Trend")
st.markdown("""
             The user can select a genre from a dropdown menu, and a line chart will display the number of anime produced in that genre each year.
             """)
selected_genre = st.selectbox('Select a Genre', sorted(set(sum(df['Genres'], []))))
genre_popularity = df[df['Genres'].apply(lambda x: selected_genre in x)].groupby('Year').size()
st.line_chart(genre_popularity)




# -------- SCORE VS. POPULARITY ANALYSIS ---------------

st.markdown("""
            # Correlation between an anime's score and its popularity.
            For this analysis, we'll investigate the relationship between the score (which could be interpreted as a measure of quality or viewer appreciation) and the popularity of an anime.
            """)

def load_data():
    data = pd.read_csv("anime.csv")  # Change to your file path
    data['Score'] = pd.to_numeric(data['Score'], errors='coerce')
    return data

anime_data = load_data()

score_popularity_data = anime_data[['Score', 'Members']].dropna()
correlation = score_popularity_data.corr()

# Plotting 
fig = px.scatter(score_popularity_data, x='Score', y='Members', 
                 title='Correlation between Anime Score and Popularity',
                 trendline='ols', trendline_color_override='red', opacity=0.5)
fig.update_layout(xaxis_title='Score', yaxis_title='Number of Members',
                  yaxis_type='log')  # log scale for Members due to wide range

st.plotly_chart(fig)

correlation_display = correlation.iloc[0, 1]
st.write(f"Correlation: {correlation_display:.2f}")

st.markdown("""

The scatter plot visualizes the relationship between anime scores and their popularity, measured by the number of members.

### Correlation Analysis
- The correlation coefficient between the score and the number of members is approximately `0.41`, indicating a moderate positive correlation.
- This suggests that, generally, anime with higher scores tend to be more popular, attracting more members. However, the correlation is not strong enough to imply a direct or consistent relationship.

### Key Observations
- There are many data points clustered at the lower end of the member count, indicating numerous anime with varying scores but lower popularity.
- Anime with very high scores (above 8) also tend to have a large number of members, supporting the idea that high-quality anime attracts more viewers.
- It's important to note that outliers and exceptions exist. Some anime with high scores might not have gained widespread popularity, and conversely, some with lower scores might be surprisingly popular due to factors like niche appeal or cult following.

### Conclusion
- The analysis highlights a general trend where quality, as indicated by scores, is a factor in an anime's popularity. However, this relationship is influenced by various other factors, such as genre, marketing, and audience preferences.
            """)

# Score Distribution by Genre Tool

def load_data_3():
    df = pd.read_csv('anime.csv')
    df['Score'] = pd.to_numeric(df['Score'], errors='coerce')
    df['Genres'] = df['Genres'].fillna('').apply(lambda x: x.split(', '))
    df.dropna(subset=['Score'], inplace=True)
    return df

df = load_data_3()

st.markdown("""
            ## Anime Score Distribution by Genre
            This analyzes and visualizes the distribution of anime scores across different genres, helping to understand which genres tend to have higher ratings. Users can select a genre from the dropdown menu. 
            """)

# User input for selecting a genre
selected_genre = st.selectbox('Select a Genre', sorted(set(sum(df['Genres'], []))), key='genre_select')

# Filtering data based on selected genre
genre_filtered_df = df[df['Genres'].apply(lambda x: selected_genre in x)]

# Plotting
st.write(f"Score Distribution for Genre: {selected_genre}")
plt.figure(figsize=(10, 6))
sns.histplot(genre_filtered_df['Score'], kde=True)
st.pyplot(plt)

# -------- LONGEVITY ANALYSIS ---------------



st.markdown("""
            # Longevity Analysis
            In this analysis, we'll examine how the length of an anime (measured by the number of episodes) correlates with its overall score. This will give us insights into whether longer or shorter series tend to be rated higher by viewers.
            """)


def load_data():
    data = pd.read_csv("anime.csv")  # Change to your file path
    data['Score'] = pd.to_numeric(data['Score'], errors='coerce')
    data['Episodes'] = pd.to_numeric(data['Episodes'], errors='coerce')
    return data

anime_data = load_data()

episodes_score_data = anime_data[['Episodes', 'Score']].dropna()

# Calculating the correlation
episodes_score_correlation = episodes_score_data.corr()

# Plotting using plotly
fig = px.scatter(episodes_score_data, x='Episodes', y='Score', 
                 title='Correlation between Number of Episodes and Anime Score',
                 log_x=True, opacity=0.5)
fig.update_layout(xaxis_title='Number of Episodes (log scale)', yaxis_title='Score')

st.plotly_chart(fig)

# Display the correlation value
episodes_score_correlation_display = episodes_score_correlation.iloc[0, 1]
st.write(f"Correlation: {episodes_score_correlation_display:.2f}")

st.markdown("""

The scatter plot with a logarithmic scale on the x-axis (number of episodes) shows the relationship between the number of episodes and the anime score.

### Correlation Analysis
- **Correlation Coefficient**: Approximately `0.09`.
- This indicates a very weak positive correlation, suggesting that there isn't a strong or consistent relationship between the length of an anime series and its overall score.

### Key Observations
-  A significant number of anime have a low number of episodes, with a wide range of scores. This cluster indicates that short series can vary greatly in quality.
- There are fewer anime with a very high episode count. While some of these longer series have high scores, the correlation is not strong enough to suggest a definitive trend.
- The weak correlation implies that the number of episodes is not a significant factor in determining the quality or appeal of an anime. Other factors like story, character development, and production quality might play more pivotal roles.

### Conclusion
-  The analysis indicates that the length of an anime, in terms of episode count, does not significantly impact its score. Both short and long series can achieve high or low scores, underscoring the importance of content quality over quantity.
 """)

# -------- GENRE AND TYPE CORRELATION ANALYSIS ---------------

st.markdown("""
            # Genre and Type Correlation
             This analysis aims to explore the relationship between genres and the types of anime (such as TV series, movies, OVAs, etc.). We'll examine which genres are commonly associated with different types of anime, providing insights into industry trends and audience preferences.
            """)

@st.cache_data
def load_data():
    anime_data = pd.read_csv('anime.csv')
    return anime_data

# Function to calculate genre type counts
def get_genre_type_counts(anime_data):
    unique_genres = list(set([genre for sublist in anime_data['Genres'].str.split(', ') for genre in sublist]))
    unique_types = anime_data['Type'].unique()

    genre_type_counts = pd.DataFrame(index=unique_genres, columns=unique_types)
    genre_type_counts = genre_type_counts.fillna(0)

    for _, row in anime_data.iterrows():
        genres = row['Genres'].split(', ')
        anime_type = row['Type']
        for genre in genres:
            genre_type_counts.at[genre, anime_type] += 1

    return genre_type_counts

data = load_data()

# Plotting
genre_type_counts = get_genre_type_counts(data)
plt.figure(figsize=(12, 10))
sns.heatmap(genre_type_counts, annot=True, fmt="d", cmap="YlGnBu")
plt.title("Occurrence of Anime Genres Across Different Types")
plt.xlabel("Type of Anime")
plt.ylabel("Genre")
plt.xticks(rotation=45)
plt.yticks(rotation=0)
st.pyplot(plt)

st.markdown("""

This analysis focuses on the distribution of various genres across different types of anime, such as TV series, movies, OVAs, Specials, and ONAs.

### Genre Distribution in Different Anime Formats

#### TV Series
- **Adventure**: 1157 occurrences
- **Mystery**: 314 occurrences
- **Super Power**: 245 occurrences

#### Movies
- **Adventure**: 774 occurrences
- **Mystery**: 122 occurrences
- **Demons**: 71 occurrences

#### OVAs (Original Video Animation)
- **Demons**: 150 occurrences
- **Adventure**: 437 occurrences
- **Super Power**: 114 occurrences

#### Specials and ONAs (Original Net Animation)
- Feature a variety of genres, though in smaller counts compared to TV series and movies.

### Key Insights
- Adventure and Mystery stories are really liked in all types of anime. They seem to be favorites for a lot of people.
- This shows that some types of stories are popular in all kinds of anime, but others are more special and fit better in certain types like movies or TV shows.
- Knowing what stories work best in each type of anime can help people who make and share anime decide what to make next

### Conclusion

- The genre and type correlation analysis provides a comprehensive view of how different anime genres distribute across various formats. This insight is crucial for understanding audience preferences and industry trends in anime production.
           """)



# -------- MEMBER ENGAGEMENT ANALYSIS ---------------

st.markdown("""
            # Member Engagement
            In this analysis, we'll examine how members of the anime community engage with anime across different statuses: watching, completed, on-hold, dropped, and planning to watch. This will provide insights into viewing behaviors and preferences.
            """)

def load_data():
    data = pd.read_csv("anime.csv")  
    return data

anime_data = load_data()

# Selecting relevant columns for member engagement analysis
member_engagement_data = anime_data[['Watching', 'Completed', 'On-Hold', 'Dropped', 'Plan to Watch']]

# Summing up the counts for each category
total_engagement = member_engagement_data.sum().reset_index()
total_engagement.columns = ['Status', 'Number of Members']

# Plotting 
fig = px.bar(total_engagement, x='Status', y='Number of Members', color='Status',
             labels={'Number of Members':'Number of Members'},
             title='Member Engagement Across Different Anime Statuses')
fig.update_layout(xaxis_title='Status', yaxis_title='Number of Members')

st.plotly_chart(fig)

st.markdown("""

The bar plot illustrates the distribution of member engagement across different anime statuses, accompanied by the total counts in each category.

### Member Engagement Distribution

- **Completed (388,042,424 members)**: This category dominates, indicating that most members have completed a significant number of anime series. This suggests high engagement and a strong interest in following series to their conclusion.
- **Plan to Watch (144,005,436 members)**: Also a significant category, showing many members have a substantial list of anime they intend to watch. This reflects ongoing interest and future engagement potential.
- **Watching (39,189,388 members)**: Represents the currently active viewership, indicating ongoing engagement with airing or selected series.
- **Dropped (20,663,441 members)** and **On-Hold (16,772,582 members)**: While lower compared to other categories, these numbers are still notable, suggesting that a considerable number of viewers pause or discontinue series for various reasons.

### Key Insights

- **High Completion Rate**: The high number of completed series underscores a dedicated and engaged anime community.
- **Plans to Watch**: The substantial "Plan to Watch" numbers indicate a continuous interest in exploring new or different anime series.
- **Dropped and On-Hold**: The figures for "Dropped" and "On-Hold" provide an interesting aspect of viewer habits, hinting at factors like time constraints, series appeal, or changing preferences.

### Conclusion

The member engagement analysis reveals significant insights into how viewers interact with anime. The data highlights the commitment of the anime community to their chosen series and their eagerness to explore new content.

            """)



# Anime Recommendation Tool

@st.cache_data  
def load_data():
    df = pd.read_csv('anime.csv')
    df['Score'] = pd.to_numeric(df['Score'], errors='coerce')  # Convert Score to numeric
    df['Year'] = df['Aired'].str.extract(r'(\d{4})').astype(float)  # Extract year
    return df

df = load_data()

st.title('Anime Recommendation Tool')

st.markdown(""" This tool allows users to explore and discover anime based on their personal preferences.   
            
- **Genre Selection**:
    - Users can select one or multiple genres from a dropdown menu.
    - This menu lists all unique genres extracted from the dataset.
- **Minimum Rating Selection**:
    - A slider allows users to choose a minimum rating for anime, ranging from 0.0 to 10.0.
    - The default value of this slider is set at 7.0.
- **Year Range Selection**:
    - Users can select a range of release years for anime.
    - This range is based on the earliest and latest years available in the dataset.

- **Filtering the Dataset**
    - The dataset is dynamically filtered based on the user's selected criteria of genres, minimum rating, and year range.
    - If there are anime that match the user’s criteria, they will be displayed in a table, showing their names, genres, scores, and release years.
             """)

unique_genres = set()
for genres in df['Genres'].dropna().str.split(', '):
    unique_genres.update(genres)
unique_genres = sorted(unique_genres)

# User Inputs
selected_genres = st.multiselect('Select Genre(s)', options=unique_genres)
selected_rating = st.slider('Select Minimum Rating', 0.0, 10.0, 7.0)
year_min, year_max = int(df['Year'].min()), int(df['Year'].max())
selected_year_range = st.slider('Select Year of Release Range', year_min, year_max, (year_min, year_max))

# Filtering the dataset
def filter_anime(df, genres, rating, year_range):
    filtered_df = df[df['Score'] >= rating]
    filtered_df = filtered_df[(filtered_df['Year'] >= year_range[0]) & (filtered_df['Year'] <= year_range[1])]
    if genres:
        mask = filtered_df['Genres'].apply(lambda x: x is not None and any(genre in x for genre in genres))
        filtered_df = filtered_df[mask]
    return filtered_df

recommended_anime = filter_anime(df, selected_genres, selected_rating, selected_year_range)

# Display recommendations
st.write('Recommended Anime:')
if not recommended_anime.empty:
    st.dataframe(recommended_anime[['Name', 'Genres', 'Score', 'Year']].dropna())
else:
    st.write("No anime found matching the criteria. Please adjust your filters.")


        
        
#----------- ANIME RATING PREDICTOR ----------------

@st.cache_data 
def load_data():
    df = pd.read_csv('anime.csv')
    df['Score'] = pd.to_numeric(df['Score'], errors='coerce')
    df['Year'] = pd.to_datetime(df['Aired'].str.extract(r'(\d{4})')[0], errors='coerce').dt.year
    df['Episodes'] = pd.to_numeric(df['Episodes'], errors='coerce')
    df['Genres'] = df['Genres'].fillna('').apply(lambda x: x.split(', '))
    df['Studios'] = df['Studios'].fillna('Unknown')
    df.dropna(subset=['Score', 'Year', 'Episodes', 'Studios'], inplace=True)
    return df

df = load_data()

# Genre encoding
mlb = MultiLabelBinarizer()
genre_encoded = mlb.fit_transform(df['Genres'])
genre_encoded_df = pd.DataFrame(genre_encoded, columns=mlb.classes_, index=df.index)

le = LabelEncoder()
df['Studio_encoded'] = le.fit_transform(df['Studios'])

X = pd.concat([df[['Year', 'Episodes', 'Studio_encoded']], genre_encoded_df], axis=1, join='inner')
y = df['Score']

# Splitting the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Training model
model = RandomForestRegressor()
model.fit(X_train, y_train)

st.title('Anime Rating Predictor')

# User inputs for prediction
st.write("Predict the score of an anime based on its year, number of episodes, genres, and optionally studio")
input_year = st.number_input('Year of Release', min_value=int(X['Year'].min()), max_value=int(X['Year'].max()), value=2020)
input_episodes = st.number_input('Number of Episodes', min_value=1, max_value=1000, value=12)
input_genres = st.multiselect('Select Genres', options=mlb.classes_)
input_studio = st.selectbox('Select Studio (Optional)', options=[''] + list(le.classes_), index=0)

# Predicting the score
if st.button('Predict Score'):
    input_genre_encoded = mlb.transform([input_genres])
    input_studio_encoded = le.transform([input_studio])[0] if input_studio else 0  # Default to 0 if no studio selected
    input_data = np.concatenate(([input_year, input_episodes, input_studio_encoded], input_genre_encoded[0]))
    predicted_score = model.predict([input_data])
    st.write(f'Predicted Anime Score: {predicted_score[0]:.2f}')


lottie_coding = load_lottieurl("https://lottie.host/ea036356-04bf-41cc-8983-7cc9cb4e3083/3hPzbrsPuU.json")

st_lottie(lottie_coding, height = 350, key="anime")











