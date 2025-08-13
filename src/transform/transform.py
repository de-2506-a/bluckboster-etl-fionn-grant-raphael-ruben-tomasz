import pandas as pd
import os

print(os.getcwd())

tables = [
    'actor', 
    'address',
    'category',
    'city',
    'country',
    'customer',
    'film',
    'film_actor',
    'film_category',
    'inventory',
    'payment',
    'rental'
]

df_dict = dict()

# check tables one by one
for this_table in tables:
    # read particular data frame from relevant csv file  
    df_dict[this_table] = \
        pd.read_csv(f'../../data/raw/uncleaned_{this_table}.csv')

this_table = 'actor'
# depending on tool used an Unnamed: 0 might appear:
try:
    df_dict[this_table].drop(columns=['Unnamed: 0', 'last_update'], inplace=True)
except BaseException:
    df_dict[this_table].drop(columns=['last_update'], inplace=True)

this_table = 'address'
# depending on tool used an Unnamed: 0 might appear:
try:
    df_dict[this_table].drop(columns=['Unnamed: 0', 'last_update', 'address2', 'district', 'postal_code', 'phone'], inplace=True)
except BaseException:
    df_dict[this_table].drop(columns=['last_update', 'address2', 'district', 'postal_code', 'phone'], inplace=True)

this_table = 'category'
# depending on tool used an Unnamed: 0 might appear:
try:
    df_dict[this_table].drop(columns=['Unnamed: 0', 'last_update'], inplace=True)
except BaseException:
    df_dict[this_table].drop(columns=['last_update'], inplace=True)

this_table = 'city'
# depending on tool used an Unnamed: 0 might appear:
try:
    df_dict[this_table].drop(columns=['Unnamed: 0', 'last_update'], inplace=True)
except BaseException:
    df_dict[this_table].drop(columns=['last_update'], inplace=True)

this_table = 'country'
# depending on tool used an Unnamed: 0 might appear:
try:
    df_dict[this_table].drop(columns=['Unnamed: 0', 'last_update'], inplace=True)
except BaseException:
    df_dict[this_table].drop(columns=['last_update'], inplace=True)

this_table = 'customer'
# depending on tool used an Unnamed: 0 might appear:
try:
    df_dict[this_table].drop(columns=['Unnamed: 0', 'last_update', 'create_date'], inplace=True)
except BaseException:
    df_dict[this_table].drop(columns=['last_update', 'create_date'], inplace=True)
df_dict[this_table] = df_dict[this_table].dropna(subset=['address_id'])
df_dict[this_table]['address_id'] = df_dict[this_table]['address_id'].astype(int)

this_table = 'film'
# depending on tool used an Unnamed: 0 might appear:
try:
    df_dict[this_table].drop(columns=['Unnamed: 0', 'last_update'], inplace=True)
except BaseException:
    df_dict[this_table].drop(columns=['last_update'], inplace=True)

this_table = 'film_actor'
# depending on tool used an Unnamed: 0 might appear:
try:
    df_dict[this_table].drop(columns=['Unnamed: 0', 'last_update'], inplace=True)
except BaseException:
    df_dict[this_table].drop(columns=['last_update'], inplace=True)

this_table = 'film_category'
# depending on tool used an Unnamed: 0 might appear:
try:
    df_dict[this_table].drop(columns=['Unnamed: 0', 'last_update'], inplace=True)
except BaseException:
    df_dict[this_table].drop(columns=['last_update'], inplace=True)

this_table = 'inventory'
# depending on tool used an Unnamed: 0 might appear:
try:
    df_dict[this_table].drop(columns=['Unnamed: 0', 'last_update'], inplace=True)
except BaseException:
    df_dict[this_table].drop(columns=['last_update'], inplace=True)

this_table = 'payment'
# depending on tool used an Unnamed: 0 might appear:
try:
    df_dict[this_table].drop(columns=['Unnamed: 0'], inplace=True)
except BaseException:
    pass

this_table = 'rental'
# depending on tool used an Unnamed: 0 might appear:
try:
    df_dict[this_table].drop(columns=['Unnamed: 0', 'last_update','return_date'], inplace=True)
except BaseException:
    df_dict[this_table].drop(columns=['last_update','return_date'], inplace=True)
df_dict[this_table]['rental_date'] = pd.to_datetime(df_dict[this_table]['rental_date'])

for this_table in tables:
    # write particular data frame to relevant csv file  
    df_dict[this_table].to_csv(f'../../data/clean/{this_table}.csv')
