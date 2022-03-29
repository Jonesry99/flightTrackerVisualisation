import matplotlib.pyplot as plt
import pandas as pd


def ryanNumOfFlightsVis():
    df = load_cached_data()
    aircraftCountry = ["US", "CN", "IE", "UK", "IN"]
    values = [0, 0, 0, 0, 0]
    for x in df["flag"]:
        if x == "US":
            values[0] += 1
        elif x == "CN":
            values[1] += 1
        elif x == "IE":
            values[2] += 1
        elif x == "UK":
            values[3] += 1
        elif x == "IN":
            values[4] += 1
        else:
            None
    fig, axs = plt.subplots(1, 2, sharey=True)
    axs[0].set_title("Scatter Graph\nTop 5 Air Traffic Countries")
    axs[0].scatter(aircraftCountry, values)
    axs[0].set_xlabel("Country Codes")
    axs[0].set_ylabel("Number of Active Flights")
    axs[1].set_title("Bar Chart\nTop 5 Air Traffic Countries")
    axs[1].bar(aircraftCountry, values)
    axs[1].set_xlabel("Country Codes")
    axs[1].set_ylabel("Number of Active Flights")
    plt.show()


def ryanScatterMapEU():
    df = load_cached_data()
    figure, mapCreate = plt.subplots(figsize=(10, 10))
    boundingBox = (-25.12, 48.20, 35.99, 67.39)
    mapEU = plt.imread('mapEurope.png')
    mapCreate.scatter(df.lng, df.lat, alpha=0.2, c='#ff03cd')
    mapCreate.set_xlim(boundingBox[0], boundingBox[1])
    mapCreate.set_ylim(boundingBox[2], boundingBox[3])
    mapCreate.imshow(mapEU, zorder=0, extent=boundingBox, aspect='equal')
    mapCreate.set_xlabel("Longitude")
    mapCreate.set_ylabel("Latitude")
    plt.show()


def load_cached_data():
    return pd.read_csv('cachedFlightData.csv')


if __name__ == "__main__":
    flight_api_key = "018ec34c-8a03-4cd6-aa66-026d1a0385cf"
    ryanNumOfFlightsVis()
    ryanScatterMapEU()