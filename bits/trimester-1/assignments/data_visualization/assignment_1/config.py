"""
Configuration file for the voter turnout dashboard project.
"""

# Data file paths
DATA_DIR = 'data'
DATA_2014 = 'data/2014-PC wise Voters Turn Out.csv'
DATA_2019 = 'data/2019-PC Wise Voters Turn Out.csv'
DATA_2024 = 'data/2024-PC-Wise-Voters-Turn-Out.csv'

# Output file paths
OUTPUT_DATASET_CSV = 'data/voter_turnout_dataset.csv'
OUTPUT_DATASET_XLSX = 'data/voter_turnout_dataset.xlsx'
OUTPUT_SELECTED_CONSTITUENCIES = 'data/selected_constituencies.csv'

# Dashboard configuration
DASHBOARD_WIDTH = 1200
DASHBOARD_HEIGHT = 800
VIZ_WIDTH = 500
VIZ_HEIGHT = 350

# Number of constituencies to select
NUM_CONSTITUENCIES = 10

# Years to analyze
ELECTION_YEARS = [2014, 2019, 2024]

