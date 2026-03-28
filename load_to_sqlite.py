import pandas as pd
import sqlite3
import os

# 1. Get the current folder path automatically
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, 'data', 'raw_file.csv')
db_path = os.path.join(current_dir, 'customer.db')

# 2. Read the CSV
df = pd.read_csv(csv_path)

# 3. Clean column names (Remove spaces/special chars for easier SQL)
df.columns = [c.replace(' ', '_').replace('(', '').replace(')', '').lower() for c in df.columns]

# 4. Create the fresh Database
# Using 'with' ensures the connection closes properly, preventing corruption
with sqlite3.connect(db_path) as conn:
    df.to_sql('customer_shopping_data', conn, if_exists='replace', index=False)

print(f"Success! Fresh database created at: {db_path}")

