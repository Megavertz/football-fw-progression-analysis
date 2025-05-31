# Football Data Analysis: Progressive Actions per 90 Minutes

In this project, the performance of football players playing in the Premier League during the 2024-2025 season were analyzed with a focus on progressive carries and passes per 90 minutes for forwards. Data has been scraped from [FBref](https://fbref.com), stored in a PostgreSQL database, and visualized using Python with Matplotlib and Seaborn.

# Project Overview

Comparisons are made between forwards based on:

- **Progressive Carries per 90 minutes**
- **Progressive Passes per 90 minutes**

By normalizing for playing time, a fair comparison between players with varying minutes played is ensured.

# Tech Stack

- Python 3.12
- Libraries: `pandas`, `matplotlib`, `seaborn`, `sqlalchemy`, `psycopg2`, `python-dotenv`
- PostgreSQL
- Jupyter Notebook

# Project Structure
```bash
football-data-analysis/
│
├── .env # Environment variables (excluded from GitHub)
├── .gitignore # Used to ignore files like .env and venv/
├── football_analysis.ipynb # Main notebook where analysis is performed
├── README.md # This file
├── requirements.txt # Python dependencies are listed here
└── venv/ # Virtual environment (not committed)
```
# Environment Variables

Database credentials are stored in a `.env` file and are loaded using `python-dotenv`. This ensures that sensitive information is not exposed.

The `.env` file should contain:

```bash
DB_USER=your_db_user
DB_PASS=your_db_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=football_data
```
To load them in code:

```bash
from dotenv import load_dotenv
load_dotenv()
```
# Sample Visualization

A scatter plot has been created to compare players based on their progressive passes and carries per 90 minutes. Each data point has been labeled with the corresponding player's name.

How to Run:

1. The repository should be cloned:

```bash
git clone https://github.com/yourusername/football-data-analysis.git\n",
cd football-data-analysis
```
2. A virtual environment should be created and activated:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```
3. Dependencies should be installed:
```bash
pip install -r requirements.txt\n",
```
4. A .env file should be created and filled with database credentials.

5. The notebook can then be opened:
```bash
jupyter notebook football_analysis.ipynb
```
