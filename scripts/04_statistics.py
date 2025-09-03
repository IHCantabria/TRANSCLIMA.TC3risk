import os
import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns


# ----------------------------
# Utility functions
# ----------------------------
def format_labels(val):
    return f"{int(val)}"


def sumarize_by_regions(df, n):
    """Summarize percentages by region IDs (based on count)."""
    groups = {
        "a": [435, 437, 441, 443, 445, 453, 455, 457],
        "b": [573, 575, 609, 611, 825, 827, 861, 863, 681, 683, 717, 719],
        "c": [573, 575, 609, 611],
        "d": [681, 683, 717, 719],
        "e": [825, 827, 861, 863],
        "f": [623, 633, 635],
        "g": [765, 767, 777, 779],
        "h": [471, 473, 475, 511, 649, 457, 901],
        "i": [471, 473, 475, 511],
        "j": [649, 757, 901],
        "k": [441, 443, 445, 623, 729, 731, 733, 765, 767],
        "m": [453, 455, 457, 633, 635, 741, 743, 777, 779],
    }

    results = []
    for key, values in groups.items():
        subset = df[df["region"].isin(values)]
        results.append(round(100 * len(subset) / n, 2))
    print(results)


def sumarize_by_population(df, n):
    """Summarize percentages by population (popG_2020)."""
    groups = {
        "a": [435, 437, 441, 443, 445, 453, 455, 457],
        "b": [573, 575, 609, 611, 825, 827, 861, 863, 681, 683, 717, 719],
        "c": [573, 575, 609, 611],
        "d": [681, 683, 717, 719],
        "e": [825, 827, 861, 863],
        "f": [623, 633, 635],
        "g": [765, 767, 777, 779],
        "h": [471, 473, 475, 511, 649, 457, 901],
        "i": [471, 473, 475, 511],
        "j": [649, 757, 901],
        "k": [441, 443, 445, 623, 729, 731, 733, 765, 767],
        "m": [453, 455, 457, 633, 635, 741, 743, 777, 779],
    }

    results = []
    for key, values in groups.items():
        subset = df[df["region"].isin(values)]
        results.append(round(100 * np.nansum(subset["popG_2020"]) / n, 2))
    print(results)


def pie_plot_climatic_regions(country, gdf1, climatic_regiones, b_colors, column_name):
    """Pie chart for climatic regions of a given country."""
    gdf2 = gdf1[gdf1["NAME_0"] == country].copy()
    gdf2["number"] = gdf2[column_name] / gdf2[column_name]
    grouped = gdf2.groupby(column_name)
    result = grouped["number"].sum()

    class0 = result.index.astype(int)
    number = result.values.astype(int)

    df = pd.DataFrame({"col1": class0, "col2": number})
    df = df.set_index("col1").reindex(climatic_regiones, fill_value=0).reset_index()

    fig, ax = plt.subplots(figsize=(10, 10))
    size = 0.5
    ax.pie(number, radius=1, colors=b_colors, wedgeprops=dict(width=size, edgecolor="w", linewidth=4))
    ax.text(0, 0, str(int(number.sum())), ha="center", va="center", fontsize=30)
    plt.savefig(f"{country}_adaptation_score_{column_name}.png", dpi=400)


# ----------------------------
# Main execution
# ----------------------------
if __name__ == "__main__":
    path = os.getcwd()

    # Input / output paths
    path_h = os.path.join(path, "1_Hazard", "ENSEMBLE")
    path_h1 = os.path.join(path, "1_Hazard")
    pathOut = os.path.join(path, "4_Risk")
    os.makedirs(pathOut, exist_ok=True)

    # Load data
    df = gpd.read_file(os.path.join(path_h, "climatic_regions_ENSEMBLE_monte_carlo_v1.shp"))
    TC_regions = pd.read_excel(os.path.join(path_h, "TC_regions_list_ENSEMBLE.xlsx"))


    lables = pd.read_excel(path_h+'/TCregions_figure.xlsx')
    colors=lables['list_colors'].tolist()
    colors = [c.strip().strip("'").strip('"') for c in colors]

    lables=lables['type of TC region'].tolist()

    climatic_regiones = TC_regions["class"].tolist()
    b_colors = [c.strip().strip("'").strip('"') for c in TC_regions["list_colors"].tolist()]
    color_map = dict(zip(climatic_regiones, b_colors))

    # Example: Pie plots for each continent
    region_counts = df.groupby(["CONTINENT", "region"]).size().reset_index(name="count")
    continents = df["CONTINENT"].unique()

    for continent in continents[:6]:
        subset = region_counts[region_counts["CONTINENT"] == continent]
        colors = subset["region"].map(color_map)

        fig, ax = plt.subplots(figsize=(6, 6))
        wedges, texts, _ = ax.pie(
            subset["count"],
            radius=1,
            colors=colors,
            wedgeprops=dict(width=0.4, edgecolor="w", linewidth=1),
            autopct="",
            startangle=140,
            labeldistance=1.1,
        )

        for i, t in enumerate(texts):
            angle = (wedges[i].theta2 + wedges[i].theta1) / 2
            t.set_rotation(angle)
            t.set_fontsize(10)

        ax.text(0, 0, str(int(subset["count"].sum())), ha="center", va="center", fontsize=30)
        plt.title(f"TC regions in {continent}")
        plt.savefig(os.path.join(pathOut, f"{continent}_TC_regions.png"), dpi=400)