import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# city = 'minneapolis'
# state = 'Minnesota'
# region = 'MROW'


pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)

# call file function

index = ['heat_pump_electricity_heating',
         'heat_pump_electricity_cooling',
         'furnace_aircon_electricity_heating',
         'furnace_aircon_natural_gas_heating',
         'furnace_aircon_electricity_cooling',
         'hp_heating',
         'hp_cooling',
         'furnace_heating',
         'ac_cooling',
         'hp',
         'furnace_ac']


df_emissions_final = pd.DataFrame(columns=['blank'], index=index)
df_costs_final = pd.DataFrame(columns=['blank'], index=index)
df_data_final = pd.DataFrame(columns=['blank'], index=[
                             'cop', 'fuel_cost', 'grid_emissions'])


def call_file(path):
    data = pd.read_csv(path)
    return pd.DataFrame(data)


# call file

path0 = '/Users/nathanoliver/Desktop/Python/Heat_Pump_Furnace_Comparison_BEOPT/csv/US_city_state_region_list.csv'

df_path = call_file(path0)


# df_path = df_path.set_index('city')

n = len(df_path)

print(df_path)

print(df_path.loc[0, 'city'])

# print(df.iloc[])

print(n)

for i in range(n):
    city = df_path.loc[i, 'city']
    state = df_path.loc[i, 'state']
    region = df_path.loc[i, 'region']

    print(city, state, region)

    path1 = '/Users/nathanoliver/Desktop/Python/Heat_Pump_Furnace_Comparison_BEOPT/csv/' + \
        city + '/' + city + '_source_energy.csv'
    path2 = '/Users/nathanoliver/Desktop/Python/Heat_Pump_Furnace_Comparison_BEOPT/csv/' + \
        city + '/' + city + '_site_energy.csv'
    path3 = '/Users/nathanoliver/Desktop/Python/Heat_Pump_Furnace_Comparison_BEOPT/csv/' + \
        city + '/' + city + '_delivered_energy.csv'
    pathe = '/Users/nathanoliver/Desktop/Python/Heat_Pump_Furnace_Comparison_BEOPT/csv/US_Region_Electricity_Emissions_2019.csv'
    pathp = '/Users/nathanoliver/Desktop/Python/Heat_Pump_Furnace_Comparison_BEOPT/csv/US_State_Electricity_NG_Prices.csv'
    # path = '/Users/nathanoliver/Desktop/Python/Anchorage_Water_Heat/csv/2020_ADUs.csv'

    df_1 = call_file(path1)
    df_2 = call_file(path2)
    df_3 = call_file(path3)
    df_e = call_file(pathe)
    df_p = call_file(pathp)

    df_1 = df_1.set_index('Unnamed: 0')
    df_2 = df_2.set_index('Unnamed: 0')
    df_3 = df_3.set_index('Unnamed: 0')
    df_e = df_e.set_index('region')
    df_p = df_p.set_index('State')

    index = ['heat_pump_main_heating',
             'heat_pump_supp_heating',
             'furnace',
             'heat_pump_cooling',
             'air_conditioner',
             'heat_pump_pump_fan_heating',
             'furnace_pump_fan',
             'heat_pump_pump_fan_cooling',
             'air_con_pump_fan',
             'heat_pump_electricity_heating',
             'heat_pump_electricity_cooling',
             'furnace_aircon_electricity_heating',
             'furnace_aircon_natural_gas_heating',
             'furnace_aircon_electricity_cooling']

    df = pd.DataFrame(columns=['delivered', 'site',
                               'source', 'emissions', 'cost'], index=index)

    df_data = pd.DataFrame(columns=['data'], index=[
                           'cop', 'natural_gas_price', 'electricity_price', 'fuel_cost', 'grid_emissions'])

    # delivered energy

    df.loc['heat_pump_main_heating',
           'delivered'] = df_3.loc['Htg Delivered (main)', 'Point 1']
    try:
        df.loc['heat_pump_supp_heating',
               'delivered'] = df_3.loc['Htg Delivered (suppl.)', 'Point 1']
    except:
        df.loc['heat_pump_supp_heating', 'delivered'] = 0
    df.loc['furnace',
           'delivered'] = df_3.loc['Htg Delivered (main)', 'Point 2']
    try:
        df.loc['heat_pump_cooling', 'delivered'] = df_3.loc['Clg Delivered (sensible)',
                                                            'Point 1'] + df_3.loc['Clg Delivered (latent)', 'Point 1']
    except:
        df.loc['air_conditioner', 'delivered'] = 0

    # site energy
    df.loc['heat_pump_main_heating',
           'site'] = df_2.loc['Heating (E)', 'Point 1']
    try:
        df.loc['heat_pump_supp_heating',
               'site'] = df_2.loc['Heating, Suppl. (E)', 'Point 1']
    except:
        df.loc['heat_pump_supp_heating', 'site'] = 0
    df.loc['furnace', 'site'] = df_2.loc['Heating (G)', 'Point 2']
    df.loc['heat_pump_cooling', 'site'] = df_2.loc['Cooling (E)', 'Point 1']
    df.loc['air_conditioner', 'site'] = df_2.loc['Cooling (E)', 'Point 2']

    df.loc['heat_pump_pump_fan_heating',
           'site'] = df_2.loc['Heating Fan/Pump (E)', 'Point 1']
    df.loc['furnace_pump_fan',
           'site'] = df_2.loc['Heating Fan/Pump (E)', 'Point 2']
    df.loc['heat_pump_pump_fan_cooling',
           'site'] = df_2.loc['Heating Fan/Pump (E)', 'Point 1']
    df.loc['air_con_pump_fan',
           'site'] = df_2.loc['Heating Fan/Pump (E)', 'Point 2']

    # source energy
    df.loc['heat_pump_main_heating',
           'source'] = df_1.loc['Heating (E)', 'Point 1']
    try:
        df.loc['heat_pump_supp_heating',
               'source'] = df_1.loc['Heating, Suppl. (E)', 'Point 1']
    except:
        df.loc['heat_pump_supp_heating',
               'source'] = 0
    df.loc['furnace', 'source'] = df_1.loc['Heating (G)', 'Point 2']
    df.loc['heat_pump_cooling', 'source'] = df_1.loc['Cooling (E)', 'Point 1']
    df.loc['air_conditioner', 'source'] = df_1.loc['Cooling (E)', 'Point 2']

    df.loc['heat_pump_pump_fan_heating',
           'source'] = df_1.loc['Heating Fan/Pump (E)', 'Point 1']
    df.loc['furnace_pump_fan',
           'source'] = df_1.loc['Heating Fan/Pump (E)', 'Point 2']
    try:
        df.loc['heat_pump_pump_fan_cooling',
               'source'] = df_1.loc['Cooling Fan/Pump (E)', 'Point 1']
    except:
        df.loc['heat_pump_pump_fan_cooling', 'source'] = 0

    try:
        df.loc['air_con_pump_fan',
               'source'] = df_1.loc['Cooling Fan/Pump (E)', 'Point 2']
    except:
        df.loc['air_con_pump_fan', 'source'] = 0
    # heat pump
    df.loc['heat_pump_electricity_heating', 'delivered'] = df.loc['heat_pump_main_heating', 'delivered'] + \
        df.loc['heat_pump_supp_heating', 'delivered']

    df.loc['heat_pump_electricity_cooling', 'delivered'] = df.loc['heat_pump_cooling',
                                                                  'delivered']

    df.loc['heat_pump_electricity_heating', 'site'] = df.loc['heat_pump_main_heating',
                                                             'site'] + df.loc['heat_pump_supp_heating', 'site'] + df.loc['heat_pump_pump_fan_heating', 'site']
    df.loc['heat_pump_electricity_cooling', 'site'] = df.loc['heat_pump_cooling',
                                                             'site'] + df.loc['heat_pump_pump_fan_cooling', 'site']

    # air con / furnace

    df.loc['furnace_aircon_natural_gas_heating', 'delivered'] = df.loc['furnace',
                                                                       'delivered']
    df.loc['furnace_aircon_electricity_cooling', 'delivered'] = df.loc['air_conditioner',
                                                                       'delivered']

    df.loc['furnace_aircon_electricity_heating',
           'site'] = df.loc['furnace_pump_fan', 'site']
    df.loc['furnace_aircon_natural_gas_heating', 'site'] = df.loc['furnace',
                                                                  'site']
    df.loc['furnace_aircon_electricity_cooling', 'site'] = df.loc['air_conditioner',
                                                                  'site'] + df.loc['air_con_pump_fan', 'site']

    elec_losses = df_e.loc[region, 'elec_loss']

    # source

    df.loc['heat_pump_electricity_heating',
           'source'] = df.loc['heat_pump_electricity_heating', 'site'] / (1 - elec_losses / 100)
    df.loc['heat_pump_electricity_cooling',
           'source'] = df.loc['heat_pump_electricity_cooling', 'site'] / (1 - elec_losses / 100)
    df.loc['furnace_aircon_electricity_heating',
           'source'] = df.loc['furnace_aircon_electricity_heating', 'site'] / (1 - elec_losses / 100)
    df.loc['furnace_aircon_natural_gas_heating',
           'source'] = df.loc['furnace_aircon_natural_gas_heating', 'site']
    df.loc['furnace_aircon_electricity_cooling',
           'source'] = df.loc['furnace_aircon_electricity_cooling', 'site'] / (1 - elec_losses / 100)

    print(df)
    print()
    # emissions

    # emission constants
    elec_emissions = df_e.loc[region, 'co2e (metric tons / MMBtu)']
    ng_emissions = 52.91

    # emission calculations
    df.loc['heat_pump_electricity_heating',
           'emissions'] = df.loc['heat_pump_electricity_heating', 'source'] * elec_emissions * 1000
    df.loc['heat_pump_electricity_cooling',
           'emissions'] = df.loc['heat_pump_electricity_cooling', 'source'] * elec_emissions * 1000

    df.loc['furnace_aircon_electricity_heating',
           'emissions'] = df.loc['furnace_aircon_electricity_heating', 'source'] * elec_emissions * 1000
    df.loc['furnace_aircon_natural_gas_heating',
           'emissions'] = df.loc['furnace_aircon_natural_gas_heating', 'source'] * ng_emissions
    df.loc['furnace_aircon_electricity_cooling',
           'emissions'] = df.loc['furnace_aircon_electricity_cooling', 'source'] * elec_emissions * 1000

    df.loc['hp_heating',
           'emissions'] = df.loc['heat_pump_electricity_heating', 'emissions']
    df.loc['hp_cooling',
           'emissions'] = df.loc['heat_pump_electricity_cooling', 'emissions']
    df.loc['furnace_heating', 'emissions'] = df.loc['furnace_aircon_electricity_heating',
                                                    'emissions'] + df.loc['furnace_aircon_natural_gas_heating', 'emissions']
    df.loc['ac_cooling',
           'emissions'] = df.loc['furnace_aircon_electricity_cooling', 'emissions']

    df.loc['hp', 'emissions'] = df.loc['hp_heating',
                                       'emissions'] + df.loc['hp_cooling', 'emissions']
    df.loc['furnace_ac', 'emissions'] = df.loc['furnace_heating',
                                               'emissions'] + df.loc['ac_cooling', 'emissions']

    price_elec = df_p.loc[state, 'Electricity ($/MMBtu)']
    price_ng = df_p.loc[state, 'Natural Gas ($/MMBtu)']

    # cost

    df.loc['heat_pump_electricity_heating',
           'cost'] = df.loc['heat_pump_electricity_heating', 'site'] * price_elec
    df.loc['heat_pump_electricity_cooling',
           'cost'] = df.loc['heat_pump_electricity_cooling', 'site'] * price_elec
    df.loc['furnace_aircon_electricity_heating',
           'cost'] = df.loc['furnace_aircon_electricity_heating', 'site'] * price_elec
    df.loc['furnace_aircon_natural_gas_heating',
           'cost'] = df.loc['furnace_aircon_natural_gas_heating', 'site'] * price_ng
    df.loc['furnace_aircon_electricity_cooling',
           'cost'] = df.loc['furnace_aircon_electricity_cooling', 'site'] * price_elec

    df.loc['hp_heating', 'cost'] = df.loc['heat_pump_electricity_heating', 'cost']
    df.loc['hp_cooling', 'cost'] = df.loc['heat_pump_electricity_cooling', 'cost']
    df.loc['furnace_heating', 'cost'] = df.loc['furnace_aircon_electricity_heating',
                                               'cost'] + df.loc['furnace_aircon_natural_gas_heating', 'cost']
    df.loc['ac_cooling', 'cost'] = df.loc['furnace_aircon_electricity_cooling', 'cost']

    df.loc['hp', 'cost'] = df.loc['hp_heating',
                                  'cost'] + df.loc['hp_cooling', 'cost']
    df.loc['furnace_ac', 'cost'] = df.loc['furnace_heating',
                                          'cost'] + df.loc['ac_cooling', 'cost']

    # other data (COP, fuel cost, grid emissions)

    df_data_final.loc['cop', city] = df.loc['heat_pump_electricity_heating',
                                            'delivered'] / df.loc['heat_pump_electricity_heating', 'site']

    df_data_final.loc['natural_gas_price', city] = price_ng
    df_data_final.loc['electricity_price', city] = price_elec

    df_data_final.loc['fuel_cost', city] = (price_elec - price_ng) / price_ng

    df_data_final.loc['grid_emissions', city] = elec_emissions * 1000

    # prepare final dataframes for export
    drop_columns = ['delivered', 'site', 'source']
    drop_rows = ['heat_pump_main_heating',
                 'heat_pump_supp_heating',
                 'furnace',
                 'heat_pump_cooling',
                 'air_conditioner',
                 'heat_pump_pump_fan_heating',
                 'furnace_pump_fan',
                 'heat_pump_pump_fan_cooling',
                 'air_con_pump_fan']

    df = df.drop(drop_columns, axis=1)
    df = df.drop(drop_rows, axis=0)

    df_emissions = df
    df_cost = df
    # df_cost = df_data

    df_emissions = df_emissions.drop('cost', axis=1)
    df_cost = df_cost.drop('emissions', axis=1)

    # print(df_cost)

    print(df_data)

    df_emissions_final.loc[:, city] = df_emissions.loc[:, 'emissions']
    df_costs_final.loc[:, city] = df_cost.loc[:, 'cost']


# print(df_emissions_final)
# print()
# print(df_costs_final)
print()

df_emissions_final = df_emissions_final.drop('blank', axis=1)
df_costs_final = df_costs_final.drop('blank', axis=1)
df_data_final = df_data_final.drop('blank', axis=1)

# print(df_emissions_final)
# print()
# print(df_costs_final)

path_emissions = '/Users/nathanoliver/Desktop/Python/Heat_Pump_Furnace_Comparison_BEOPT/csv/final_data/emissions.csv'
path_cost = '/Users/nathanoliver/Desktop/Python/Heat_Pump_Furnace_Comparison_BEOPT/csv/final_data/cost.csv'
path_data = '/Users/nathanoliver/Desktop/Python/Heat_Pump_Furnace_Comparison_BEOPT/csv/final_data/other_data.csv'


df_emissions_final.to_csv(path_emissions)
df_costs_final.to_csv(path_cost)
df_data_final.to_csv(path_data)

print(df_data_final)
