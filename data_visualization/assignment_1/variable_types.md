# Variable Types Documentation

This document identifies and categorizes all variables in the voter turnout dataset.

## Dataset Variables

### Categorical/Nominal Variables

**Constituency Name (PC_NAME)**
- Type: Categorical/Nominal
- Description: Name of the parliamentary constituency
- Values: Text strings (e.g., "Araku", "Srikakulam", "Vizianagaram")
- Unique values: 10 (one for each selected constituency)

**State**
- Type: Categorical/Nominal
- Description: Name of the state where the constituency is located
- Values: Text strings (e.g., "Andhra Pradesh", "Tamil Nadu")
- Unique values: Varies based on selected constituencies

### Ordinal Variables

**Election Year (Year)**
- Type: Ordinal
- Description: Year of the general election
- Values: 2014, 2019, 2024
- Order: 2014 < 2019 < 2024 (temporal ordering)

**PC Number (PC_NO)**
- Type: Ordinal (can also be considered discrete numerical)
- Description: Parliamentary constituency number within the state
- Values: Integer numbers
- Order: Numerical ordering (though may not have meaningful ordinal relationship)

### Numerical/Continuous Variables

**Total Electors (Total_Electors)**
- Type: Numerical/Continuous (Count)
- Description: Total number of eligible voters in the constituency
- Range: Positive integers (count data)
- Unit: Number of voters

**Male Electors (Male_Electors)**
- Type: Numerical/Continuous (Count)
- Description: Total number of eligible male voters
- Range: Positive integers
- Unit: Number of voters

**Female Electors (Female_Electors)**
- Type: Numerical/Continuous (Count)
- Description: Total number of eligible female voters
- Range: Positive integers
- Unit: Number of voters

**Others Electors (Others_Electors)**
- Type: Numerical/Continuous (Count)
- Description: Total number of eligible voters in other/third gender category
- Range: Non-negative integers
- Unit: Number of voters

**Total Votes (Total_Votes)**
- Type: Numerical/Continuous (Count)
- Description: Total number of votes polled in the constituency
- Range: Positive integers
- Unit: Number of votes

**Male Votes (Male_Votes)**
- Type: Numerical/Continuous (Count)
- Description: Total number of votes polled by male voters
- Range: Positive integers
- Unit: Number of votes

**Female Votes (Female_Votes)**
- Type: Numerical/Continuous (Count)
- Description: Total number of votes polled by female voters
- Range: Positive integers
- Unit: Number of votes

**Postal Votes (Postal_Votes)**
- Type: Numerical/Continuous (Count)
- Description: Total number of postal votes
- Range: Non-negative integers
- Unit: Number of votes

**Overall Turnout (Overall_Turnout)**
- Type: Numerical/Continuous (Percentage)
- Description: Overall voter turnout ratio as a percentage
- Range: 0 to 100 (typically 50-90 in practice)
- Unit: Percentage (%)

**Male Turnout (Male_Turnout)**
- Type: Numerical/Continuous (Percentage)
- Description: Male voter turnout ratio as a percentage
- Range: 0 to 100
- Unit: Percentage (%)

**Female Turnout (Female_Turnout)**
- Type: Numerical/Continuous (Percentage)
- Description: Female voter turnout ratio as a percentage
- Range: 0 to 100
- Unit: Percentage (%)

**Others Turnout (Others_Turnout)**
- Type: Numerical/Continuous (Percentage)
- Description: Other/third gender voter turnout ratio as a percentage
- Range: 0 to 100
- Unit: Percentage (%)

**Postal Turnout (Postal_Turnout)**
- Type: Numerical/Continuous (Percentage)
- Description: Postal votes as percentage of total electors
- Range: 0 to 100 (typically very small)
- Unit: Percentage (%)

## Summary

- **Categorical/Nominal**: 2 variables (PC_NAME, State)
- **Ordinal**: 2 variables (Year, PC_NO)
- **Numerical/Continuous (Counts)**: 8 variables (all elector and vote counts)
- **Numerical/Continuous (Percentages)**: 5 variables (all turnout ratios)

**Total Variables**: 17 variables in the final dataset

