# Loading the dataset using pandas
import pandas as pd
import sqlite3
df = pd.read_csv('data/raw_file.csv')

# Create SQLite DB file
conn = sqlite3.connect("customer.db")

# Save table
df.to_sql("customer_shopping", conn, if_exists="replace", index=False)

conn.close()

print("CSV imported into customer.db successfully!")


df.head()

df.info()
# Summary statistics using .describe()
df.describe(include= 'all')

# Checking if missing data or null values are present in the dataset
df.isnull().sum()

# Imputing missing values in Review Rating column with the median rating of the product category

df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))

# Renaming columns according to snake casing for better readability and documentation

df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')
df = df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})

df.columns

# create a new column age_group
labels = ['Young Adult', 'Adult', 'Middle-aged', 'Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels = labels)

df[['age','age_group']].head(10)

# create new column purchase_frequency_days

frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
}

df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)

df[['purchase_frequency_days','frequency_of_purchases']].head(10) 

(df['discount_applied'] == df['promo_code_used']).all()
# Dropping promo code used column

df = df.drop('promo_code_used', axis=1)

df.columns