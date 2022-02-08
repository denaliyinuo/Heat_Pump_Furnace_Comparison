print(df_cost)
print(df_emissions)

df_cost.sort_values(
    by=['heating_cost_comparison'], ascending=True, inplace=True, axis=1)

df_emissions.sort_values(
    by=['heating_emissions_comparison'], ascending=True, inplace=True, axis=1)


df_cost_order = df_cost.loc['heating_cost_comparison', :]
df_emissions_order = df_emissions.loc['heating_emissions_comparison', :]

print(df_emissions_order)
print(df_cost_order)
