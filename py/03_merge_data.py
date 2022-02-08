import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# city = 'minneapolis'
# state = 'Minnesota'
# region = 'MROW'


pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)


def call_file(path):
    data = pd.read_csv(path)
    return pd.DataFrame(data)


# call file

path_emissions = '/Users/nathanoliver/Desktop/Python/Heat_Pump_Furnace_Comparison_BEOPT/csv/final_data/emissions.csv'
path_cost = '/Users/nathanoliver/Desktop/Python/Heat_Pump_Furnace_Comparison_BEOPT/csv/final_data/cost.csv'
path_data = '/Users/nathanoliver/Desktop/Python/Heat_Pump_Furnace_Comparison_BEOPT/csv/final_data/other_data.csv'

df_emissions = call_file(path_emissions)
df_cost = call_file(path_cost)
df_data = call_file(path_data)

drop_rows = ['heat_pump_electricity_heating',
             'heat_pump_electricity_cooling',
             'furnace_aircon_electricity_heating',
             'furnace_aircon_natural_gas_heating',
             'furnace_aircon_electricity_cooling',
             'hp_heating',
             'furnace_heating',
             'ac_cooling',
             'hp',
             'furnace_ac']

df_emissions = df_emissions.set_index('category')
df_cost = df_cost.set_index('category')
df_data = df_data.set_index('category')

df_cost = df_cost.drop(drop_rows, axis=0)

df = pd.concat([df_emissions, df_cost], axis=0)
df = pd.concat([df, df_data], axis=0)
print(df)


path = '/Users/nathanoliver/Desktop/Python/Heat_Pump_Furnace_Comparison_BEOPT/csv/final_data/merged_data.csv'

df.to_csv(path)
