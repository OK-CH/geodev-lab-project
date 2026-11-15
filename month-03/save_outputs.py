import geopandas as gpd

wards = gpd.read_file("week-10/data/processed/wards.gpkg", layer="wards")
wards.to_file("week-10/data/processed/week10_outputs.gpkg", layer="wards_copy")
wards.drop(columns="geometry").to_csv("week-10/wards_table.csv", index=False)
print(gpd.list_layers("week-10/data/processed/week10_outputs.gpkg"))