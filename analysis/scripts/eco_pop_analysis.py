import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

file_path = 'clean_data/eco_pop_data/population_economic_data.csv'

eco_pop_data = pd.read_csv(file_path)

print(eco_pop_data.head(4))