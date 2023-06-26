# connecting for the other website in web scripting
from bs4 import BeautifulSoup
import requests
url = BeautifulSoup('https://www.icc-cricket.com/rankings/mens/team-rankings/odi', 'html.parser')
print(url)
soup = requests.get(url)
print (soup)

# show the data in the web scripting code
ranking_data = soup.text
ranking_data = BeautifulSoup(ranking_data, 'lxml')
# print(ranking_data)

# select data
table_ranking = ranking_data.table
# print(len(table_ranking))
thead_rows = table_ranking.thead.find_all('tr')
tbody_rows = table_ranking.tbody.find_all('tr')

# Extract header data
header_data = [col.text.strip() for col in thead_rows[0].find_all('th')]

# Extract body data
body_data = []
for row in tbody_rows:
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    body_data.append(cols)

# Combine header and body data
doc = [header_data] + body_data

# # Write data to a CSV file
# import csv
# file = open('ranking.csv', 'w', newline='')
# a = csv.writer(file)
# a.writerows(doc)
# file.close()


# # # # pandas select data
import pandas as pd
df = pd.read_csv('ranking.csv', encoding= "latin1")


# Assuming df is your DataFrame
import plotly.graph_objects as go
subset_team = df['Team\nT'][0:21]
subset_matches = df['Matches\nM'][0:21]
subset_point = df['Rating\nR'] [0:21]

fig = go.Figure()
fig.add_trace(go.Bar(x=subset_team, y=subset_matches, name='Matches'))
fig.show()





fig = go.Figure(data=[
    go.Bar(name='Matches', x=subset_team, y=subset_matches),
    go.Bar(name='points', x=subset_team, y=subset_point)
])
# Change the bar mode
fig.update_layout(barmode='group')
fig.show()