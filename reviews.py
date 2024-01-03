import pandas as pd

#Read the CSV file
wine_reviews = pd.read_csv("./data/winemag-data-130k-v2.csv.zip")

#Group the data by country and calculate mean column
reviews_data = wine_reviews.groupby('country').agg({'points': ['count', 'mean']})

#Name the columns
reviews_data.columns = ['count', 'points']

# Sort by the number of reviews in descending order
reviews_data = reviews_data.sort_values(by='count', ascending=False)

#Round the points to one decimal point
reviews_data['points'] = reviews_data['points'].round(1)

# Write the summary data to a new CSV file
reviews_data.to_csv('data/reviews-per-country.csv')