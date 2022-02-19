# Comparison of Air Source Heat Pumps and Natural Gas Furnaces on Utility Costs and C02 Emissions in the US

# Introduction

This analysis compares the emissions and operating costs of a typical air source heat pump (ASHP) relative to a high efficient natural gas (NG) furnace in a typical US single-family home in various US cities in mild and cold climates. The inspiration to perform this analysis was due in part to the supposed debate regarding the change in CO2 emissions introduced by replacing internal combustion engine vehicles with electric cars. Recent research has clearly shown that electric cars would reduce C02 emissions in any location in the US. Other motivations for performing this research were to provide an overview of which regions of the US would benefit from replacing NG furnaces with ASHPs on a financial and environmental level, and to determine and quantify the obstacles preventing the electrification of homes in the US. There is little in-depth research comparing NG furnaces and ASHPs, and the goal of this analysis is to ultimately determine the impact of location, climate, electricity mix, and natural gas and electricity prices on the cost and CO2 emissions of replacing NG furnaces with ASHPs.

# Method

To perform this analysis, a software program with the following abilities was required.

* A single-family home with ASHP and NG furnaces could be modeled and its heating system specifications edited.
* The amount of energy consumed and delivered by each heating system could be calculated.
* Weather files of different cities could be used to adjust the climate.

The Building Energy Optimization (BEopt) software provided by the National Renewable Energy Laboratory (NREL) was selected since it can perform the required functions for a thorough and accurate analysis. The BEopt software can also calculate C02 emissions and yearly utility bill costs, but calculations using electricity grid emissions, and electricity and natural gas prices were ultimately done separately because of the uncertainty in the BEopt methodology.

During implementation of the software, it was observed that the auxiliary electric resistance heat system would turn on when the ASHP would be unable to meet the home's heating load. This was particularly problematic for the simulation in extremely cold environments, since electric resistance heating is much less efficient than ASHPs, and would negatively impact the performance of the ASHP. The auxiliary heating system was a requirement for the ASHP, and to reduce the impact of this quirk in the software on the ASHP performance and to provide a fairer comparison between ASHPs and NG furnaces, the home was built with excessive insulation, no windows, and no mechanical ventilation. This is a reasonable adjustment in the simulation since it is known that ASHPs can perform well in extremely cold environments, such as Minneapolis. Below are the efficiencies of the heating systems and some of the important house specifications used in this analysis.


* 95 AFUE NG furnace with a low temperature of -20 degrees F. 
* 10 HSPF ASHP
* 



In order to quickly and accurately calculate the required heat loads of a single-family home using 

compared 95 AFUE natural gas furance (95% efficient) to a 10 HSPF air source heat pump

ducts located in the finished living space were used for both heating systems to eliminate duct heating losses. 

one issue with modeling the heat pump was that the auxiliary electric strip 

used , ran simulations for different locations

weather data files - TMY3

used same house for all locations

house specifics



Results


![i1](/png/final_data_alphabetical.png)
![i1](/png/ranked_cost.png)
![i1](/png/ranked_emissions.png)
