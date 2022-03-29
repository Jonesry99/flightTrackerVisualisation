# flightTrackerVisualisation
Live flight data from around the world is collected into a CSV file which I load into my program via. pandas.
I created two visualisations representing the data, a latitude and longitude based scatter graph that plots
all the flights currently over Europe, and a bar chart + scatter graph to show the number of airlines currently
active from the top 5 countries with the highest air traffic in the world.

To create the air traffic visualisation, I searched through the whole data set to find the quantity of planes
that had the same flight_icao as the 5 nations I selected. Once a grand total has been found, I plot both graphs
using matplotlib to present the data to the user and added relevant X & Y labels.

To create the scatter map across Europe, I created a subplot using matplotlib, and set a bounding box with the
minimum and maximum longitudes from one side of Europe to the other to find all the aircrafts within that catchment
region. This data would then be pasted over a map of Europe using matplotlib.imread and .scatter.
I defined the size of the plot with .imshow to set the zorder as 0 the extent of the plot as the bounding box data
and the aspect to equal. I then used matplotlib.show along with relevant X & Y labels to make it presentable to the user.
