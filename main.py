from bokeh.plotting import curdoc
from bokeh.layouts import layout

import earth_energy


# Initialize Star and Planet
# terrasol_ux = terrasol.TerraSol()

# # Initialize Climate Model
# energy_in = terrasol_ux
# climate_ux = climate.PlanetClimateEBM(terrasol_ux)
# print(climate_ux.climate_result)

# Initialize Simpler Climate Model
# simple_climate_ux = climate.SimpleClimate(terrasol_ux)

# Initializ Earth Energy balance
earth = earth_energy.EarthEnergy(simple_albedo=True)

# TerraSol Layout
# plot_layout = layout([[terrasol_ux.plot],
#                       terrasol_ux.div_row,
#                       terrasol_ux.sliders,
#                       [simple_climate_ux.plot],
#                       simple_climate_ux.model_wx],
#                      sizing_mode='fixed')

plot_layout = layout([[earth.plot],
                      [earth.solar_title_div, earth.planet_title_div, earth.info_title_div],
                      [earth.solar_wx, earth.albedo_wx, earth.info_div]])

# show(plot_layout)
curdoc().add_root(plot_layout)
curdoc().title = 'PlanetaryIO'


