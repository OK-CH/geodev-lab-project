# %%
import pandas as pd

pop = pd.read_csv("week-10/data/raw/ward_population.csv")

print(pop.head())
print("Shape:", pop.shape)
print("Columns:", list(pop.columns))
print(pop.dtypes)
print(pop["population_2024"].describe())

# %%
import geopandas as gpd

print(gpd.list_layers("week-10/data/processed/wards.gpkg"))

wards = gpd.read_file("week-10/data/processed/wards.gpkg", layer="wards")

print(wards.head())
print("Rows and columns:", wards.shape)
print(wards.geom_type.value_counts())
print("CRS:", wards.crs)
print("Bounds:", wards.total_bounds)