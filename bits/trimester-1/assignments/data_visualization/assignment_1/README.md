# Voter Turnout Dashboard

Interactive dashboard for visualizing voter turnout data from the last three General Elections (2014, 2019, 2024) for 10 selected constituencies.

## Project Structure

```
data_visualization/
├── data/                          # Data files
│   ├── 2014-PC wise Voters Turn Out.csv
│   ├── 2019-PC Wise Voters Turn Out.csv
│   ├── 2024-PC-Wise-Voters-Turn-Out.csv
│   └── voter_turnout_dataset.csv  # Generated dataset
├── src/                           # Source code modules
│   ├── data_loader.py             # Data loading functions
│   ├── data_processor.py          # Data processing and transformation
│   ├── create_dataset.py          # Dataset creation
│   ├── visualizations.py          # Visualization functions
│   ├── interactivity.py           # Interactive widgets
│   ├── styling.py                # Common styling
│   └── color_scheme.py            # Color definitions
├── dashboard.ipynb                # Main dashboard notebook
├── variable_types.md              # Variable type documentation
├── PLAN.md                        # Project plan
└── requirements.txt              # Python dependencies
```

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Ensure data files are in the `data/` directory:
   - 2014-PC wise Voters Turn Out.csv
   - 2019-PC Wise Voters Turn Out.csv
   - 2024-PC-Wise-Voters-Turn-Out.csv

## Usage

### Running the Dashboard

1. Open `dashboard.ipynb` in Jupyter Notebook or JupyterLab
2. Run all cells sequentially
3. The dashboard will be displayed in the notebook with interactive visualizations

### Creating the Dataset

If the dataset doesn't exist, the notebook will automatically create it. Alternatively, you can run:

```python
from src.create_dataset import create_dataset
dataset, selected = create_dataset()
```

## Dashboard Features

The dashboard includes four visualizations:

1. **Visualization A**: Change in voter turnout ratio over time (aggregate)
2. **Visualization B**: Change in voter turnout ratio across genders (aggregate)
3. **Visualization C**: Distribution of voter turnout across constituencies and time
4. **Visualization D**: Distribution of voter turnout across constituencies and genders

### Interactive Features

- Constituency selector: Filter by one or more constituencies
- Year filter: Filter by election year
- Hover tooltips: View detailed information on hover
- Cross-filtering: Visualizations update based on selections

## Data Source

Election Commission of India: https://www.eci.gov.in/statistical-reports

## Requirements

- Python 3.8+
- pandas
- bokeh
- numpy
- openpyxl (for Excel export)
- jupyter

## Submission Files

- `dashboard.ipynb` - Main interactive dashboard
- `data/voter_turnout_dataset.csv` - Curated dataset (CSV)
- `data/voter_turnout_dataset.xlsx` - Curated dataset (Excel)
- `variable_types.md` - Variable type documentation
