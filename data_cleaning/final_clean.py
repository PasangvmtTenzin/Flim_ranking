import pandas as pd 
import numpy as np

movie_path = 'data/cleaned_data/cleaned_movie.csv'

eco_pop_path = 'data/cleaned_data/population_economic_data.csv'

def load_clean_movie(movie_path):
    movie = pd.read_csv(movie_path)
    movie.replace('\\N', np.nan, inplace=True)
    movie['genres'] = movie['genres'].fillna('short')
    clean_df = movie.drop(columns=['tconst'])
    clean_df['Year'] = clean_df['Year'].astype('Int64')
    clean = clean_df[clean_df['Year'] >= 1960]
    cleaned_data = clean.sort_values(by='Year', ascending=True)
    return cleaned_data

clean_movie = load_clean_movie(movie_path)
# print(clean_movie.info())
# print("\n", clean_movie.isnull().sum())
# print("\n", clean_movie.head(5))
# clean_movie.to_csv('data/cleaned_data/movie.csv')

def load_clean_eco_pop(eco_pop_path):
    eco_pop = pd.read_csv(eco_pop_path)
    clean = eco_pop.sort_values(by='Year', ascending=True)
    return clean

gdp = load_clean_eco_pop(eco_pop_path)

# print(gdp.info(),"\n")
# print(gdp.isnull().sum(), "\n")
# print(gdp.head(5))
# gdp.to_csv('data/cleaned_data/gdp_data.csv')

gdp_path = 'data/cleaned_data/gdp_data.csv'
movie_data_path = 'data/cleaned_data/movie.csv'

def load_merge_data(gdp_path, movie_data_path):
    movie_data = pd.read_csv(movie_data_path)
    pop_eco_data = pd.read_csv(gdp_path)
    # Merge the datasets on 'Year' column, while aligning the data
    merged_data = pd.merge(movie_data, pop_eco_data, on='Year', how='left', suffixes=('', '_gdp'))
    
    # Replace the null values in 'Year' column of movie_data with values from pop_eco_data
    movie_data['Year'] = movie_data['Year'].fillna(merged_data['Year'])

    return movie_data

final_merge = load_merge_data(gdp_path, movie_data_path)

print(final_merge.head(5))