import os
import pandas as pd
from flask import current_app

class DashboardService:
    def get_book_ratings():

        root_path = current_app.root_path
        csv_path = os.path.join(root_path, 'archive/books.csv')
        
        books_df = pd.read_csv(csv_path, engine='python', on_bad_lines='skip')
        books_df['ratings_count'] = pd.to_numeric(books_df['ratings_count'], errors='coerce')
        df_sorted = books_df.sort_values(by='ratings_count', ascending=False).head(100)
        df_filtered = df_sorted[['bookID', 'title', 'average_rating', 'ratings_count', 'authors', 'language_code']]
        json_result = df_filtered.to_json(orient='records', lines=False, indent=4)
        
        return json_result