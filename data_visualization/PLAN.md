# Project Plan: Voter Turnout Dashboard using Python Bokeh

## Overview
This project aims to create an interactive dashboard using Python Bokeh to visualize voter turnout data from the last three General Elections (2014, 2019, 2024) for 10 selected constituencies, demonstrating effective visualization design principles.

---

## Phase 1: Data Preparation and Dataset Creation [5 Marks]

### 1.1 Data Loading and Exploration
**Tasks:**
- Load CSV files for all three elections (2014, 2019, 2024)
- Explore data structure and identify column name variations across years
- Handle missing values and data inconsistencies
- Identify common constituencies across all three elections

**Files to create:**
- `src/data_loader.py` - Functions to load and parse CSV files
- `src/explore_data.py` - Script to explore data structure and identify available constituencies

**Key considerations:**
- Column names differ across years (e.g., "OTHERS" vs "THIRD GENDER" vs "TG")
- Handle different data formats and encoding issues
- Ensure constituency names are consistent across years

### 1.2 Constituency Selection
**Criteria for selecting 10 constituencies:**
- Must have data available in all three elections (2014, 2019, 2024)
- Geographic diversity (different states/regions)
- Varying voter turnout patterns (high, medium, low turnout constituencies)
- Mix of urban and rural constituencies

**Output:**
- List of 10 selected constituencies with justification

### 1.3 Data Extraction and Transformation
**Tasks:**
- Extract data for selected 10 constituencies from all three elections
- Standardize column names across all years
- Calculate required variables:
  - Total voters (Male, Female, Others/Third Gender)
  - Total votes polled (Male, Female, Postal votes, Others)
  - Voter turnout ratios:
    - Overall turnout = (Total votes polled / Total electors) × 100
    - Male turnout = (Male votes polled / Male electors) × 100
    - Female turnout = (Female votes polled / Female electors) × 100
    - Postal votes turnout = (Postal votes / Total electors) × 100

**Files to create:**
- `src/data_processor.py` - Functions to process and transform data
- `src/create_dataset.py` - Script to create the final curated dataset

**Output:**
- `data/voter_turnout_dataset.csv` - Final curated dataset
- `data/voter_turnout_dataset.xlsx` - Excel version for submission

### 1.4 Variable Type Identification [1 Mark]
**Tasks:**
- Document variable types for all columns in the dataset
- Categorize as:
  - **Categorical/Nominal**: Constituency name, State
  - **Ordinal**: Election year (2014, 2019, 2024)
  - **Numerical/Continuous**:
    - Total voters (counts)
    - Votes polled (counts)
    - Voter turnout ratios (percentages, 0-100)
  - **Numerical/Discrete**: PC Number

**File to create:**
- `variable_types.md` - Documentation of variable types

---

## Phase 2: Visualization Development [10 Marks]

### 2.1 Visualization A: Change in Voter Turnout Ratio Over Time (Aggregate)
**Visualization Type:** Line chart or Area chart
**Data:** Aggregate voter turnout ratio across all 10 constituencies for each election year

**Bokeh Implementation:**
- Use `figure()` with line glyph
- X-axis: Election Year (2014, 2019, 2024)
- Y-axis: Voter Turnout Ratio (%)
- Show overall aggregate turnout trend
- Add markers for each data point
- Include hover tooltips showing exact values

**Design Principles:**
- Clear axis labels and title
- Use color to highlight trend direction
- Add grid lines for easier reading

### 2.2 Visualization B: Change in Voter Turnout Ratio Across Genders (Aggregate)
**Visualization Type:** Grouped bar chart or Multi-line chart
**Data:** Aggregate voter turnout ratio by gender (Male, Female) across election years

**Bokeh Implementation:**
- Use `figure()` with multiple line glyphs or vbar with grouping
- X-axis: Election Year
- Y-axis: Voter Turnout Ratio (%)
- Separate lines/bars for Male and Female
- Use distinct colors for gender differentiation
- Add legend

**Design Principles:**
- Color coding: Use intuitive colors (e.g., blue for Male, pink/red for Female)
- Ensure sufficient contrast between genders
- Clear legend placement

### 2.3 Visualization C: Distribution of Voter Turnout Across Constituencies and Time
**Visualization Type:** Heatmap or Grouped bar chart
**Data:** Voter turnout ratio for each of the 10 constituencies across three election years

**Bokeh Implementation:**
- Option 1: Heatmap using `rect()` glyph
  - X-axis: Constituency names
  - Y-axis: Election Year
  - Color intensity: Voter turnout ratio
- Option 2: Grouped bar chart
  - X-axis: Constituency names (grouped)
  - Y-axis: Voter Turnout Ratio (%)
  - Different colored bars for each election year

**Design Principles:**
- Use color gradient for heatmap (low to high turnout)
- Ensure constituency names are readable (rotation if needed)
- Clear color scale/legend

### 2.4 Visualization D: Distribution of Voter Turnout Across Constituencies and Genders
**Visualization Type:** Grouped bar chart or Stacked bar chart
**Data:** Voter turnout ratio by gender for each constituency (aggregated across years or shown per year)

**Bokeh Implementation:**
- Use `vbar()` with grouping or stacking
- X-axis: Constituency names
- Y-axis: Voter Turnout Ratio (%)
- Separate bars for Male and Female turnout
- Option to show average across years or per year

**Design Principles:**
- Consistent color scheme with Visualization B
- Clear grouping/stacking to show comparison
- Legend for gender identification

**Files to create:**
- `src/visualizations.py` - Functions to create individual visualizations
- `src/styling.py` - Common styling and color scheme definitions

---

## Phase 3: Dashboard Design [5 Marks]

### 3.1 Dashboard Layout
**Bokeh Implementation:**
- Use `gridplot()` or `column()` and `row()` to arrange four visualizations
- Layout structure:
  ```
  [Visualization A - Time Trend]  [Visualization B - Gender Comparison]
  [Visualization C - Constituency & Time]  [Visualization D - Constituency & Gender]
  ```
- Responsive layout that adapts to screen size
- Add title and description at the top

**File to create:**
- `src/dashboard.py` - Main dashboard assembly

### 3.2 Interactivity Features
**Drill-down/Selection Feature:**
- **Constituency Selector:** Dropdown or Multi-select widget
  - Allow users to select one or more constituencies
  - Update all visualizations to show data for selected constituencies
  - Show aggregate when multiple constituencies selected
- **Year Filter:** Toggle buttons or checkbox group
  - Allow filtering by election year
  - Update visualizations accordingly
- **Hover Tooltips:**
  - Show detailed information on hover
  - Include constituency name, year, gender, turnout ratio, etc.
- **Cross-filtering:**
  - Clicking on a bar/point in one visualization highlights related data in others
  - Use Bokeh's `TapTool` and `Selection` callbacks

**Bokeh Widgets to use:**
- `Select` or `MultiSelect` for constituency selection
- `CheckboxGroup` or `Toggle` for year filtering
- `CustomJS` callbacks for interactivity
- `ColumnDataSource` for dynamic data updates

**File to create:**
- `src/interactivity.py` - Functions for interactive features and callbacks

### 3.3 Design Principles Implementation

#### Gestalt Principles:
1. **Proximity:** Group related visualizations together
2. **Similarity:** Use consistent colors, shapes, and styles across visualizations
3. **Closure:** Complete visual boundaries for each chart
4. **Continuity:** Smooth lines and transitions in line charts
5. **Figure/Ground:** Clear distinction between data and background

#### Visualization Best Practices:
1. **Clear Titles and Labels:**
   - Descriptive titles for each visualization
   - Axis labels with units (%)
   - Legend for multi-series data

2. **Appropriate Chart Types:**
   - Line charts for time series
   - Bar charts for categorical comparisons
   - Heatmaps for two-dimensional distributions

3. **Color Accessibility:**
   - Use colorblind-friendly palette
   - Sufficient contrast ratios
   - Don't rely solely on color (use patterns/textures if needed)

4. **Data-Ink Ratio:**
   - Remove unnecessary grid lines
   - Minimize chart junk
   - Focus on data representation

5. **Consistent Scales:**
   - Use consistent Y-axis scales where appropriate for comparison
   - Clear scale breaks if needed

#### Color Schema:
- **Primary Colors:**
  - Overall/General: Deep Blue (#1f77b4) or Teal (#2ca02c)
  - Male: Blue shades (#3498db, #2980b9)
  - Female: Pink/Red shades (#e74c3c, #c0392b)
  - Postal votes: Orange (#f39c12)

- **Time-based Colors:**
  - 2014: Lighter shade
  - 2019: Medium shade
  - 2024: Darker shade (most recent)

- **Heatmap Colors:**
  - Low turnout: Light yellow/beige
  - Medium turnout: Orange
  - High turnout: Dark red/brown

- **Background:**
  - Light gray or white for clean appearance
  - Subtle grid lines in light gray

**File to create:**
- `src/color_scheme.py` - Color palette definitions

---

## Phase 4: Implementation Structure

### 4.1 Project Structure
```
data_visualization/
├── data/
│   ├── 2014-PC wise Voters Turn Out.csv
│   ├── 2019-PC Wise Voters Turn Out.csv
│   ├── 2024-PC-Wise-Voters-Turn-Out.csv
│   ├── voter_turnout_dataset.csv
│   └── voter_turnout_dataset.xlsx
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── data_processor.py
│   ├── create_dataset.py
│   ├── explore_data.py
│   ├── visualizations.py
│   ├── dashboard.py
│   ├── interactivity.py
│   ├── styling.py
│   └── color_scheme.py
├── output/
│   └── voter_turnout_dashboard.html
├── notebooks/
│   └── dashboard.ipynb (optional, for development)
├── ASSIGNMENT.md
├── PLAN.md
├── variable_types.md
├── requirements.txt
└── README.md
```

### 4.2 Main Execution Script
**File to create:**
- `run.py` or `main.py` - Main script to:
  1. Load and process data
  2. Create dataset (if not exists)
  3. Generate visualizations
  4. Assemble dashboard
  5. Save as HTML file

### 4.3 Configuration
**File to create:**
- `config.py` - Configuration file for:
  - Selected constituencies list
  - File paths
  - Color schemes
  - Dashboard dimensions

---

## Phase 5: Testing and Refinement

### 5.1 Data Validation
- Verify calculations for voter turnout ratios
- Check data consistency across years
- Validate selected constituencies have complete data

### 5.2 Visualization Testing
- Test all four visualizations render correctly
- Verify interactivity works as expected
- Check responsiveness on different screen sizes
- Validate color accessibility

### 5.3 User Experience Testing
- Test drill-down functionality
- Verify tooltips show correct information
- Check filter interactions
- Ensure smooth transitions

---

## Phase 6: Documentation and Submission

### 6.1 Documentation
- Update `README.md` with:
  - Project description
  - Setup instructions
  - How to run the dashboard
  - Data source information
  - Selected constituencies justification

### 6.2 Submission Files
1. **Jupyter Notebook or Python Script:**
   - `dashboard.ipynb` or `run.py` - Executable code
   - Well-commented and organized

2. **Curated Dataset:**
   - `data/voter_turnout_dataset.csv`
   - `data/voter_turnout_dataset.xlsx`

3. **Variable Types Documentation:**
   - `variable_types.md`

4. **Dashboard Output:**
   - `output/voter_turnout_dashboard.html` - Standalone HTML file

5. **Documentation:**
   - `README.md` - Project documentation
   - `PLAN.md` - This planning document

---

## Technical Implementation Details

### Bokeh-Specific Considerations

1. **Data Sources:**
   - Use `ColumnDataSource` for efficient data handling
   - Update sources dynamically for interactivity

2. **Output Format:**
   - Generate standalone HTML using `output_file()` or `save()`
   - Ensure all dependencies are embedded

3. **Performance:**
   - Use `CDSView` for filtering large datasets
   - Implement efficient callbacks using `CustomJS` where possible

4. **Styling:**
   - Use Bokeh themes or custom styling
   - Apply consistent fonts and sizes
   - Set appropriate figure dimensions

5. **Interactivity:**
   - Use `js_on_change()` for widget callbacks
   - Implement `CustomJS` for client-side filtering
   - Use `TapTool` and `HoverTool` for enhanced interaction

---

## Timeline and Milestones

1. **Week 1:** Data loading, exploration, and dataset creation
2. **Week 2:** Individual visualization development
3. **Week 3:** Dashboard assembly and interactivity implementation
4. **Week 4:** Testing, refinement, and documentation

---

## Success Criteria

- ✅ Complete dataset with 10 constituencies across 3 elections
- ✅ All required variables calculated correctly
- ✅ Variable types documented
- ✅ Four visualizations implemented as specified
- ✅ Interactive dashboard with drill-down/selection features
- ✅ Demonstrates Gestalt principles and visualization best practices
- ✅ Consistent and accessible color schema
- ✅ Standalone HTML file that can be shared publicly
- ✅ All submission files ready

---

## References and Resources

- Bokeh Documentation: https://docs.bokeh.org/
- Storytelling with Data: https://www.storytellingwithdata.com/
- Election Commission of India: https://www.eci.gov.in/statistical-reports
- Color Accessibility: https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html

