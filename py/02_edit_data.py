import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)


def call_file(path):
    data = pd.read_csv(path)
    return pd.DataFrame(data)


# call file

path_cost = '/Users/nathanoliver/Desktop/Python/Heat_Pump_Furnace_Comparison_BEOPT/csv/final_data/cost.csv'
path_emissions = '/Users/nathanoliver/Desktop/Python/Heat_Pump_Furnace_Comparison_BEOPT/csv/final_data/emissions.csv'

df_cost = call_file(path_cost)
df_emissions = call_file(path_emissions)


print(df_cost)
print(df_emissions)


df_cost = df_cost.set_index('category')
df_emissions = df_emissions.set_index('category')

# compare cost of furnace and heat pump (heating)

df_cost.loc['heating_cost_comparison', :] = (
    df_cost.loc['hp_heating', :] - df_cost.loc['furnace_heating', :]) / df_cost.loc['furnace_heating', :]


# compare emissions of furnace and heat pump (heating)

df_emissions.loc['heating_emissions_comparison', :] = (
    df_emissions.loc['hp_heating', :] - df_emissions.loc['furnace_heating', :]) / df_emissions.loc['furnace_heating', :]


path_emissions = '/Users/nathanoliver/Desktop/Python/Heat_Pump_Furnace_Comparison_BEOPT/csv/final_data/emissions.csv'
path_cost = '/Users/nathanoliver/Desktop/Python/Heat_Pump_Furnace_Comparison_BEOPT/csv/final_data/cost.csv'


df_emissions.to_csv(path_emissions)
df_cost.to_csv(path_cost)
