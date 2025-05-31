import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")

# Load the scraped data
df = pd.read_csv("premier_league_standard_stats.csv", skiprows=1)

# Rename column
df.rename(columns={"Playing Time.2" : "Min", "Unnamed: 1" : "Player", "Unnamed: 3" : "Pos", "Unnamed: 4" : "Squad", "Progression" : "PrgC", "Progression.1" : "PrgP", "Progression.2" : "PrgP"}, inplace=True)

# Select the column needed
columns_to_keep = ["Player", "Pos", "Squad", "Min", "PrgC", "PrgP", "PrgR"]
df = df[columns_to_keep]

# Create SQLAlchemy engine
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Load into table (auto-creates table if not exists)
df.to_sql("player_minutes", engine, if_exists="replace", index=False)

print("Data loaded successfully.")
