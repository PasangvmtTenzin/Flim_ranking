import pandas as pd 

basics_path = 'data/movie/title.basics.tsv'

def basic_cleaning(basice_path):
    basics_df = pd.read_csv(basics_path, delimiter='\t', low_memory=False)
    basics_df['genres'] = basics_df['genres'].apply(lambda x: str(x).split(',')[0] if isinstance(x, str) else x)
    df = basics_df.rename(columns={'startYear': 'Year', 'primaryTitle': 'Title'})
    basic_clean = df.drop(columns=['endYear', 'originalTitle', 'isAdult', 'runtimeMinutes', 'titleType'])
    return basic_clean

basics = basic_cleaning(basics_path)
# print(basics.info())
# print(basics.head(5))
# saving the data
basics.to_csv('data/movie/cleaned_genre.csv')

rating_path = 'data/movie/title.ratings.tsv'

def ratings_cleaning(rating_path):
    rating_df = pd.read_csv(rating_path, delimiter='\t', low_memory=False)

    return rating_df
rating = ratings_cleaning(rating_path)

# print(rating.info())
# print(rating.head(10))
# rating.to_csv('data/movie/ratings.csv')

rate_path = 'data/movie/ratings.csv'
genre_path = 'data/movie/cleaned_genre.csv'

output_path = 'data/cleaned_data/cleaned_movie.csv'

def load_mege_data(rate_path, genre_path, output_path):
    rating = pd.read_csv(rate_path)
    genre = pd.read_csv(genre_path)

    merge_data = pd.merge(rating, genre, on=['tconst'])
    df = merge_data.drop(columns=['Unnamed: 0_x', 'Unnamed: 0_y'])
    movie_data = df.to_csv(output_path, index=False)

    return movie_data

merged_data = load_mege_data(rate_path, genre_path, output_path)

print(merged_data)