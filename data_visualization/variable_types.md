# Variable Type Identification

This document identifies the variable types in the voter turnout dataset.

## Variable Categories

### Categorical Variables

These variables represent categories or groups:

1. **Constituency Name**
   - Type: Categorical (Nominal)
   - Description: Name of the parliamentary constituency
   - Values: Text strings (e.g., "Amethi", "Varanasi", "Bangalore North")

2. **State**
   - Type: Categorical (Nominal)
   - Description: Name of the state where the constituency is located
   - Values: Text strings (e.g., "Uttar Pradesh", "Karnataka", "Tamil Nadu")

3. **Year**
   - Type: Categorical (Ordinal)
   - Description: Year of the general election
   - Values: 2014, 2019, 2024
   - Note: While numeric, this is treated as categorical/ordinal as it represents discrete time periods

### Numerical Variables - Discrete

These variables represent counts (whole numbers):

4. **Total Voters**
   - Type: Numerical (Discrete)
   - Description: Total number of registered voters in the constituency
   - Values: Non-negative integers
   - Units: Number of voters

5. **Male Voters**
   - Type: Numerical (Discrete)
   - Description: Number of registered male voters
   - Values: Non-negative integers
   - Units: Number of voters

6. **Female Voters**
   - Type: Numerical (Discrete)
   - Description: Number of registered female voters
   - Values: Non-negative integers
   - Units: Number of voters

7. **Total Votes Polled**
   - Type: Numerical (Discrete)
   - Description: Total number of votes cast in the election
   - Values: Non-negative integers
   - Units: Number of votes

8. **Male Votes Polled**
   - Type: Numerical (Discrete)
   - Description: Number of votes cast by male voters
   - Values: Non-negative integers
   - Units: Number of votes

9. **Female Votes Polled**
   - Type: Numerical (Discrete)
   - Description: Number of votes cast by female voters
   - Values: Non-negative integers
   - Units: Number of votes

10. **Postal Votes**
    - Type: Numerical (Discrete)
    - Description: Number of postal votes cast
    - Values: Non-negative integers
    - Units: Number of votes

### Numerical Variables - Continuous

These variables represent ratios or percentages (can have decimal values):

11. **Voter Turnout Ratio - Overall**
    - Type: Numerical (Continuous)
    - Description: Overall voter turnout as a percentage
    - Values: 0-100 (percentage)
    - Formula: (Total Votes Polled / Total Voters) × 100
    - Units: Percentage (%)

12. **Voter Turnout Ratio - Male**
    - Type: Numerical (Continuous)
    - Description: Male voter turnout as a percentage
    - Values: 0-100 (percentage)
    - Formula: (Male Votes Polled / Male Voters) × 100
    - Units: Percentage (%)

13. **Voter Turnout Ratio - Female**
    - Type: Numerical (Continuous)
    - Description: Female voter turnout as a percentage
    - Values: 0-100 (percentage)
    - Formula: (Female Votes Polled / Female Voters) × 100
    - Units: Percentage (%)

14. **Voter Turnout Ratio - Postal**
    - Type: Numerical (Continuous)
    - Description: Postal votes as a percentage of total voters
    - Values: 0-100 (percentage)
    - Formula: (Postal Votes / Total Voters) × 100
    - Units: Percentage (%)

## Summary

- **Categorical Variables**: 3 (Constituency Name, State, Year)
- **Numerical Discrete Variables**: 7 (All count-based variables)
- **Numerical Continuous Variables**: 4 (All turnout ratio variables)

**Total Variables**: 14


