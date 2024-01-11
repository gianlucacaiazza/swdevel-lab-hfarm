
def top_wines_by_rating(df_wines, limit=10):
    top_wines = df_wines.sort_values(by="Rating", ascending=False)
    return top_wines.head(limit)
