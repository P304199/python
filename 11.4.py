import pandas as pd

data = {
    'day': pd.date_range(start="2025-04-25", periods=10, freq='D'),
    'john_and_judy_visiting': [False, True, False, False, True, False, False, True, False, False]
}

df = pd.DataFrame(data)

def calculate_days_til_party(visits):
    days_til_party = []
    days_until_next_party = float('inf')
    for visit in reversed(visits):
        if visit:
            days_until_next_party = 0
        days_til_party.insert(0, days_until_next_party)
        if days_until_next_party < float('inf'):
            days_until_next_party += 1
    return days_til_party

df['days_til_party'] = calculate_days_til_party(df['john_and_judy_visiting'])

print(df)
