#%%
import pandas as pd
import geopandas as gpd



#%%
#
# Bounding Box herausfinden
# dazu hier ein Polygon zeichnen: http://bboxfinder.com/#53.334973,9.639130,53.758454,10.430145
# Links unter dem Menü das KBS eintragen: 3035
# Ganz unten steht "Hide Coordinates / Show Coordinates" - da muss man den Reiter für EPSG 3035 auswählen
# Darunter dann bei Box die Koordinaten kopieren und hier einfügen:
bounding_box = (4314020.5556,3381507.9313,4317415.0462,3385180.7703)


#%%
# Hier evtl Dateiname anpassen
# Filtern und als Geodataframe laden
# Das kann evtl sehr lange dauern

gdf_grid = gpd.read_file('DE_Grid_ETRS89-LAEA_100m.gpkg', bbox=bounding_box)

#%%
# Koordinatenbezugssystem checken
gdf_grid.crs

#%%
# Koordinatenbezugssystem auf 4326 ändern
gdf_grid4326 =  gdf_grid.to_crs('4326')


#%%
# Checken, ob es geklappt hat
gdf_grid4326.crs

#%%
# Mal testweise plotten
gdf_grid4326.plot()


#%%
# Als GeoJSON exportieren
gdf_grid4326.to_file('gdf_grid4326.geojson', index=False, driver='GeoJSON')

