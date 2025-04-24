import pandas as pd

# a) Date time object for Jan 15, 2012
date_time_1 = pd.to_datetime("2012-01-15")
print("a) Date time object for Jan 15, 2012:")
print(date_time_1)

# b) Specific date and time of 9:20 pm
date_time_2 = pd.to_datetime("2012-01-15 21:20")
print("\nb) Specific date and time of 9:20 pm:")
print(date_time_2)

# c) Local date and time
local_datetime = pd.to_datetime("now")
print("\nc) Local date and time:")
print(local_datetime)

# d) A date without time
date_without_time = local_datetime.date()
print("\nd) A date without time:")
print(date_without_time)

# e) Current date
current_date = pd.to_datetime("today").date()
print("\ne) Current date:")
print(current_date)

# f) Time from a date time
time_from_datetime = local_datetime.time()
print("\nf) Time from a date time:")
print(time_from_datetime)

# g) Current local time
current_local_time = pd.to_datetime("now").strftime("%H:%M:%S")
print("\ng) Current local time:")
print(current_local_time)
