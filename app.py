from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

cols_to_keep = [0,1,2,3,5,6,7,10,13,14,19,20,21,22]
df = pd.read_csv('/home/cem/Hentet/TMDB_movie_dataset_v11.csv', nrows=1000, usecols=cols_to_keep)

# set the max columns to none
pd.set_option('display.max_columns', None)

df.release_date = pd.to_datetime(df.release_date)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/data')
def index():
    # Group by year and calculate average rating
    ratings = df.groupby(df['release_date'].dt.year)['vote_average'].mean().reset_index()
    ratings = ratings.rename(columns={'release_date': 'Year', 'vote_average': 'Rating'})
    return render_template('index.html', avg_ratings=ratings)



