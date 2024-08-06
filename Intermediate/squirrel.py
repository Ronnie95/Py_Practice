import pandas as pd             

sq = pd.read_csv('./intermediate/squirrel.csv')

# print(sq)

# print(sq.head(10)) prints the first # of  specified rows

# print(sq.tail(5)) prints the last # of specified rows

# print(sq.info())


new_sq = sq.dropna()

print(new_sq)