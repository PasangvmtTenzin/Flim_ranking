import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter
import numpy as np

# Load the dataset
file_path = 'clean_data/movie/movie_data.csv'
movie_data = pd.read_csv(file_path)

# A function to format the y-axis labels
def thousands_formatter(x, pos):
    return f'{int(x/1000)}K'

# Set the style for the plots
sns.set(style='whitegrid')

def plot_distribution_of_average_ratings(data):
    plt.figure(figsize=(10, 6))
    ax = sns.histplot(data['averageRating'], bins=20, kde=True)
    plt.title('Distribution of Average Ratings')
    plt.xlabel('Average Rating')
    plt.ylabel('Frequency')
    ax.yaxis.set_major_formatter(FuncFormatter(thousands_formatter))
    ax.format_coord = lambda x, y: f'x={x:.2f}, y={y:.0f}'
    plt.savefig('analysis/plots/movie/distribution_of_average_ratings.png', dpi=300)
    plt.show()

def plot_number_of_votes_per_year(data):
    plt.figure(figsize=(14, 8))
    ax = sns.lineplot(x='Year', y='numVotes', data=data)
    plt.title('Number of Votes Per Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Votes')
    ax.yaxis.set_major_formatter(FuncFormatter(thousands_formatter))
    plt.savefig('analysis/plots/movie/number_of_votes_per_year.png', dpi=300)
    plt.show()

def plot_average_rating_per_genre(data):
    # Explode the genres
    data_exploded = data.assign(genres=data['genres'].str.split(',')).explode('genres')
    
    # Order genres by median rating
    order = data_exploded.groupby('genres')['averageRating'].median().sort_values(ascending=False).index
    
    plt.figure(figsize=(16, 10))
    sns.set(style="whitegrid")
    
    # Create the box plot
    ax = sns.boxplot(x='genres', y='averageRating', data=data_exploded, order=order, palette='Set3')
    
    # Setting the title and labels with larger font sizes
    plt.title('Average Rating per Genre', fontsize=20)
    plt.xlabel('Genre', fontsize=16)
    plt.ylabel('Average Rating', fontsize=16)
    
    # Rotate x-ticks for better readability and increase their font size
    plt.xticks(rotation=90, fontsize=12)
    plt.yticks(fontsize=12)
    
    # Add annotations for median values
    medians = data_exploded.groupby('genres')['averageRating'].median().loc[order]
    for i, median in enumerate(medians):
        ax.text(i, median + 0.05, f'{median:.2f}', ha='center', fontsize=10, color='black')
    
    plt.tight_layout()  # Adjust layout to prevent clipping of tick-labels
    plt.savefig('analysis/plots/movie/average_rating_per_genre.png', dpi=300)
    plt.show()


def plot_correlation_between_votes_and_ratings(data):
    plt.figure(figsize=(12, 8))
    sns.set(style="whitegrid")

    # Create scatter plot with smaller and semi-transparent markers
    sns.scatterplot(x='numVotes', y='averageRating', data=data, alpha=0.5, s=10, color='blue')

    # Setting the title and labels
    plt.title('Correlation Between Number of Votes and Average Rating', fontsize=20, fontweight='bold')
    plt.xlabel('Number of Votes', fontsize=14, fontweight='bold')
    plt.ylabel('Average Rating', fontsize=14, fontweight='bold')
    
    # Setting the x-axis to logarithmic scale
    plt.xscale('log')
    
    # Add a trend line (using linear regression)
    sns.regplot(x='numVotes', y='averageRating', data=data, scatter=False, color='red', line_kws={"lw": 2})

    # Add gridlines and adjust tick parameters
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.minorticks_on()
    
    # Adjusting the layout to prevent clipping
    plt.tight_layout()

    # Save and show the plot
    plt.savefig('analysis/plots/movie/correlation_between_votes_and_ratings.png', dpi=300)
    plt.show()

def correlation_matrix(data):
    # Select only numerical columns
    numerical_data = data.select_dtypes(include=[np.number])

    # Calculate the correlation matrix
    correlation_matrix = numerical_data.corr()

    # Set up the matplotlib figure
    plt.figure(figsize=(12, 10))

    # Draw the heatmap
    sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', linewidths=0.5, square=True)

    # Add title and adjust layout
    plt.title('Correlation Matrix of the Dataset', fontsize=20, fontweight='bold')
    plt.tight_layout()

    # Save and show the plot
    plt.savefig('analysis/plots/movie/correlation_matrix.png', dpi=300)
    plt.show()

# Calling the functions
# plot_distribution_of_average_ratings(movie_data)
# plot_number_of_votes_per_year(movie_data)
# plot_average_rating_per_genre(movie_data)
# plot_correlation_between_votes_and_ratings(movie_data)
# correlation_matrix(movie_data)