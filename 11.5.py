import pandas as pd

data = {
    'artist': ['A', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B'],
    'venue': ['V1', 'V2', 'V1', 'V2', 'V1', 'V2', 'V1', 'V2', 'V1'],
    'date': pd.to_datetime(['2025-01-01', '2025-01-15', '2025-02-01', '2025-02-20', 
                            '2025-03-05', '2025-03-10', '2025-03-15', '2025-04-01', '2025-04-10'])
}

df = pd.DataFrame(data)

df['year_month'] = df['date'].dt.to_period('M')

artist_venue_pairs = pd.MultiIndex.from_product([df['artist'].unique(), df['venue'].unique()], names=['artist', 'venue'])

concert_counts = df.groupby(['year_month', 'artist', 'venue']).size().unstack(fill_value=0)

concert_counts = concert_counts.reindex(columns=artist_venue_pairs, fill_value=0)

print(concert_counts)
