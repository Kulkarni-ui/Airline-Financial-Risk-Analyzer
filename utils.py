import pandas as pd
import numpy as np

# Cost constants (you can tweak as needed)
COST_PER_MINUTE = 75   # Airline operational cost per min delay in USD
COMPENSATION_PER_PASSENGER = 100  # Passenger compensation per delay

def calculate_costs(df):
    """
    Add financial cost estimates to dataset.
    Assumes df has 'DelayMinutes' and 'Passengers' columns.
    """
    df['Operational_Cost'] = df['DelayMinutes'] * COST_PER_MINUTE
    df['Compensation_Cost'] = df['Passengers'] * COMPENSATION_PER_PASSENGER
    df['Total_Cost'] = df['Operational_Cost'] + df['Compensation_Cost']
    return df

def risk_analysis(df):
    """
    Simple Value-at-Risk style analysis for airline losses.
    """
    airline_losses = df.groupby('Airline')['Total_Cost'].sum().sort_values(ascending=False)
    worst_case = np.percentile(df['Total_Cost'], 95)  # 95% worst-case cost
    return airline_losses, worst_case