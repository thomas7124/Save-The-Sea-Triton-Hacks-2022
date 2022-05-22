import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import mpld3


df = pd.read_csv("new_coral.csv",
                 usecols=["latitude", "longitude", "ScientificName"])
df.head()

countries = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
countries.head()

# initialize an axis
fig, ax = plt.subplots(figsize=(8,6))

# plot map on axis
countries = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
countries.plot(color="lightgrey", ax=ax)


# plot points
df.plot(x = "longitude", y = "latitude", s = 0.1, kind="scatter", colormap="YlOrRd", title="Locations of Coral Reefs",
        ax=ax)



ax.grid(visible=True, alpha=0.5)

html_str = mpld3.fig_to_html(fig)
Html_file= open("map.html","w")
Html_file.write(html_str)
Html_file.close()
print(fig)

plt.show()



