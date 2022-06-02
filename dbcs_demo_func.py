''' Created by Raymond Lui, 27 September 2021'''

import numpy as np # v1.19.2
import pandas as pd # v1.1.5
import matplotlib.pyplot as plt # v3.3.4
from scipy.spatial.distance import pdist, squareform, euclidean # v1.5.2



def loadExampleData():
    d = ["D$_{" + str(x + 1) + "}$" for x in range(0, 40)]
    y = [10.36, 13.80, 16.59, 18.03, 20.29, 23.47, 24.93, 25.41, 27.70, 28.76, 29.41, 33.12, 34.45, 35.63, 36.70, 38.02, 38.29, 42.12, 44.37, 46.36, 46.74, 47.32, 47.94, 51.37, 54.29, 56.14, 56.28, 58.13, 59.45, 60.77, 61.83, 65.14, 66.07, 66.60, 71.76, 72.95, 78.37, 84.19, 86.44, 88.66]
    x = [40.57, 76.48, 20.82, 55.70, 33.64, 87.32, 68.41, 11.46, 54.52, 43.07, 26.12, 69.27, 79.49, 48.09, 56.46, 14.89, 39.50, 30.12, 61.99, 70.58, 45.93, 38.19, 53.83, 26.53, 35.56, 56.30, 64.77, 48.12, 78.53, 9.07, 28.46, 57.10, 37.42, 21.37, 49.58, 73.37, 31.30, 53.67, 17.54, 83.75]
    dataset = pd.DataFrame((d, y, x)).T
    dataset.columns = ["id", "y", "x"]

    subset = pd.DataFrame({"id": [], "y": [], "x": []})

    return dataset, subset

def plotChemicalSpace(dataset, subset, filename, distances=False, **kwargs):
    '''
    dataset         DataFrame with three columns: "id", "y", and "x"
    subset          DataFrame with three columns: "id", "y", and "x"
    filename        filename of plot to be saved
    distances       boolean value; if True, then will save a second plot with distances included
    **filename2     filename of second distances plot to be saved
    '''

    '''
    Z-order:
    3   Dataset/subset text
    2   Dataset/subset datapoints
    1   Distance lines
    '''

    if distances:
        filename2 = kwargs.get("filename2")
        if filename2 == None:
                raise ValueError("<filename2> argument required if <distances> is True")

    # Set figure space
    plt.figure(figsize=(4.7, 4.7), dpi=200, tight_layout={"pad":0.1})
    ax = plt.gca()
    ax.tick_params(length=0)

    # Set axis borders
    for side in ax.spines.keys():
        ax.spines[side].set_linewidth(4)
        ax.spines[side].set_color("#1f4e79")

    plt.axis("square")
    plt.xlim(0, 95.51)
    plt.ylim(95.51, 0)
    plt.xticks([])
    plt.yticks([])

    # Plot dataset
    plt.scatter(
        x=dataset["x"], y=dataset["y"],
        s=300, edgecolors="#9dc3e6", facecolors="#bdd7ee", linewidths=1,
        zorder=2
    )

    for _, row in dataset.iterrows():
        plt.text(
            x=row["x"], y=row["y"],
            s=row["id"],
            ha="center", va="center",
            fontfamily="serif", fontsize=8,
            color="#5b9bd5",
            zorder=3
        )

    # Plot subset
    plt.scatter(
        x=subset["x"], y=subset["y"],
        s=300, edgecolors="#1f4e79", facecolors="#1f4e79", linewidths=1,
        zorder=2
    )

    for _, row in subset.iterrows():
        plt.text(
            x=row["x"], y=row["y"],
            s=row["id"],
            ha="center", va="center",
            fontfamily="serif", fontsize=8,
            color="#ffffff",
            zorder=3
        )

    plt.savefig(filename)

    if distances:
        for d_m in dataset.values:
            for s_n in subset.values:
                distance_y = np.array((d_m[1], s_n[1]))
                distance_x = np.array((d_m[2], s_n[2]))
                
                if np.array_equal(s_n, subset.values[-1]):
                    linecolor = "#5b9bd5"
                else:
                    linecolor = "#9dc3e6"

                plt.plot(
                    distance_x, distance_y,
                    linewidth=0.66, linestyle="--",
                    color=linecolor,
                    zorder=1
                )
        
        plt.savefig(filename2)
    
def initialiseSubset(dataset, subset, method="most_dissimilar", plot=False, **kwargs):
    '''
    dataset     DataFrame with three columns: "id", "y", and "x"
    subset      DataFrame with three columns: "id", "y", and "x"; must have zero entries so it can be initialised
    method      >> "most_dissimilar": calculate pairwise distances in dataset and find candidate with greatest summed distance to all other datapoints
                *note only "most_dissimilar" supported in current version to visualise differences in MaxSum and MaxMin selection for DBCS demo
    plot        boolean value
    **filename  filename of plot to be saved
    '''

    if len(subset) == 0:
        if plot:
            '''
            Z-order:
            3   Dataset/subset text
            2   Dataset/subset datapoints
            1   Distance lines
            '''

            filename = kwargs.get("filename")
            if filename == None:
                    raise ValueError("<filename> argument required if <plot> is True")
            else:
                # Set figure space
                plt.figure(figsize=(4.7, 4.7), dpi=200, tight_layout={"pad":0.1})
                ax = plt.gca()
                ax.tick_params(length=0)

                # Set axis borders
                for side in ax.spines.keys():
                    ax.spines[side].set_linewidth(4)
                    ax.spines[side].set_color("#1f4e79")

                plt.axis("square")
                plt.xlim(0, 95.51)
                plt.ylim(95.51, 0)
                plt.xticks([])
                plt.yticks([])

        if method == "most_dissimilar":
            # Calculate all pairwise distances and find index of datapoint with the largest sum of distances to the other datapoints
            distances = pdist(dataset[["y", "x"]].values, metric='euclidean')
            dist_matrix = squareform(distances)
            maxsum_idx = np.argmax(np.sum(dist_matrix, axis=0))
            
            # Extract the subset candidate from the dataset
            subset_candidate = dataset.iloc[maxsum_idx]
            dataset_updated = dataset.drop([maxsum_idx])

            # Plot dataset
            if plot:
                plt.scatter(
                    x=dataset_updated["x"], y=dataset_updated["y"],
                    s=300, edgecolors="#9dc3e6", facecolors="#bdd7ee", linewidths=1,
                    zorder=2
                )

                for _, row in dataset_updated.iterrows():
                    plt.text(
                        x=row["x"], y=row["y"],
                        s=row["id"],
                        ha="center", va="center",
                        fontfamily="serif", fontsize=8,
                        color="#5b9bd5",
                        zorder=3
                    )

                # Plot subset
                plt.scatter(
                    x=subset_candidate["x"], y=subset_candidate["y"],
                    s=300, edgecolors="#ed7c31", facecolors="#ed7c31", linewidths=1,
                    zorder=2
                )

                plt.text(
                    x=subset_candidate["x"], y=subset_candidate["y"],
                    s=subset_candidate["id"],
                    ha="center", va="center",
                    fontfamily="serif", fontsize=8,
                    color="#ffffff",
                    zorder=3
                )
                
                plt.text(
                    x=subset_candidate["x"] + 0.5, y=subset_candidate["y"] - 0.5,
                    s="*",
                    ha="center", va="center",
                    fontfamily="serif", fontsize=8,
                    color="#ffffff",
                    zorder=3
                )
                
                for d_m in dataset_updated.values:
                    distance_y = np.array((d_m[1], subset_candidate.values[1]))
                    distance_x = np.array((d_m[2], subset_candidate.values[2]))
                    
                    plt.plot(
                        distance_x, distance_y,
                        linewidth=0.66, linestyle="--",
                        color="#ed7c31",
                        zorder=1
                    )
                
                # Save plot
                plt.savefig(filename)

            # Reidentify candidate and add to subset
            subset_candidate["id"] = "S$_{" + str(len(subset) + 1) + "}$"
            subset_updated = subset.append(subset_candidate)

            return dataset_updated, subset_updated
        else:
            raise ValueError("<%s> is not a supported initialisation method" % method)
    else:
        raise ValueError("Subset has already been intialised")

def selectCompound(dataset, subset, method, plot=False, **kwargs):
    '''
    dataset     DataFrame with three columns: "id", "y", and "x"
    subset      DataFrame with three columns: "id", "y", and "x"
    method      "maxsum": select dataset instance based on the largest sum of distances to all subset instances
                "maxmin": select dataset instance based on the furthest subset nearest neighbour
    plot        boolean value
    **filename  filename of plot to be saved
    '''

    if len(subset) >= 1:
        # Prepare plot
        if plot:
            '''
            Z-order:
            4   Dataset/subset text
            3   Dataset/subset datapoints
            2   Highlighted distance lines
            1   Distance lines
            '''

            filename = kwargs.get("filename")
            if filename == None:
                    raise ValueError("<filename> argument required if <plot> is True")
            else:
                # Set figure space
                plt.figure(figsize=(4.7, 4.7), dpi=200, tight_layout={"pad":0.1})
                ax = plt.gca()
                ax.tick_params(length=0)

                # Set axis borders
                for side in ax.spines.keys():
                    ax.spines[side].set_linewidth(4)
                    ax.spines[side].set_color("#1f4e79")

                plt.axis("square")
                plt.xlim(0, 95.51)
                plt.ylim(95.51, 0)
                plt.xticks([])
                plt.yticks([])

                # Plot subset first since it does not require any modification related to compound selection (unlike dataset which requires the removal of the datapoint of the new subset candidate)
                plt.scatter(
                    x=subset["x"], y=subset["y"],
                    s=300, edgecolors="#1f4e79", facecolors="#1f4e79", linewidths=1,
                    zorder=3
                )

                for _, row in subset.iterrows():
                    plt.text(
                        x=row["x"], y=row["y"],
                        s=row["id"],
                        ha="center", va="center",
                        fontfamily="serif", fontsize=8,
                        color="#ffffff",
                        zorder=4
                    )

        # Calculate pairwise distances between each datapoint in dataset and each datapoint in subset
        all_distances = []
        for d_m in dataset[["y", "x"]].values:
            dm_distances = []
            for s_n in subset[["y", "x"]].values:
                distance = euclidean(d_m, s_n)
                dm_distances.append(distance)
            all_distances.append(dm_distances)
        
        # MaxSum: sum together dm_distances and find the largest value in all_distances
        if method.lower() == "maxsum":
            for idx, d_m in enumerate(all_distances):
                dm_sum = np.sum(d_m)
                all_distances[idx] = dm_sum

        # MaxMin: find smallest dm_distance and find the largest value in all_distances
        elif method.lower() == "maxmin":
            plot_distances = np.array(all_distances)

            for idx, d_m in enumerate(all_distances):
                dm_min = np.min(d_m)
                all_distances[idx] = dm_min

        else:
            raise ValueError("<%s> is not a supported selection method" % method)
            
        # Extract the subset candidate from dataset
        candidate_idx = np.argmax(all_distances)
        subset_candidate = dataset.iloc[candidate_idx]
        dataset_updated = dataset.drop([candidate_idx]).reset_index(drop=True)

        # Plot highlighted distances, updated dataset, and subset candidate, then save plot
        if plot:
            # MaxSum highlighted distances
            if method.lower() == "maxsum":
                for _, s_n in subset.iterrows():
                    for idx, d_m in dataset.iterrows():
                        distance_y = np.array((d_m["y"], s_n["y"]))
                        distance_x = np.array((d_m["x"], s_n["x"]))

                        if idx == candidate_idx:
                            linewidth=2
                            linestyle="-"
                            linecolor="#ed7c31"
                            zorder=2
                        else:
                            linewidth=0.5
                            linestyle="--"
                            linecolor="#9dc3e6"
                            zorder=1

                        plt.plot(
                            distance_x, distance_y,
                            linewidth=linewidth, linestyle=linestyle,
                            color=linecolor,
                            zorder=zorder
                        )
            
            if method.lower() == "maxmin":
                for subset_idx, s_n in enumerate(subset.values):
                    for d_m in zip(dataset.values, plot_distances):
                        if (subset_idx == np.argmin(d_m[1])) and (np.min(d_m[1]) == np.max(all_distances)): # must go before the next elif so np.min==np.max overrides hierarchy
                            linewidth=2
                            linestyle="-"
                            linecolor="#ed7c31"
                            zorder=2
                        elif subset_idx == np.argmin(d_m[1]):
                            linewidth=1
                            linestyle="--"
                            linecolor="#ed7c31"
                            zorder=2
                        else:
                            linewidth=0.5
                            linestyle="--"
                            linecolor="#9dc3e6"
                            zorder=1
                        
                        distance_y = np.array((d_m[0][1], s_n[1]))
                        distance_x = np.array((d_m[0][2], s_n[2]))

                        plt.plot(
                            distance_x, distance_y,
                            linewidth=linewidth, linestyle=linestyle,
                            color=linecolor,
                            zorder=zorder
                        )


            # Updated dataset
            plt.scatter(
                x=dataset_updated["x"], y=dataset_updated["y"],
                s=300, edgecolors="#9dc3e6", facecolors="#bdd7ee", linewidths=1,
                zorder=3
            )

            for _, row in dataset_updated.iterrows():
                plt.text(
                    x=row["x"], y=row["y"],
                    s=row["id"],
                    ha="center", va="center",
                    fontfamily="serif", fontsize=8,
                    color="#5b9bd5",
                    zorder=4
                )
            
            # Subset candidate
            plt.scatter(
                x=subset_candidate["x"], y=subset_candidate["y"],
                s=300, edgecolors="#ed7c31", facecolors="#ed7c31", linewidths=1,
                zorder=3
            )

            plt.text(
                x=subset_candidate["x"], y=subset_candidate["y"] + 0.25,
                s=subset_candidate["id"],
                ha="center", va="center",
                fontfamily="serif", fontsize=8,
                color="#ffffff",
                zorder=4
            )

            plt.text(
                x=subset_candidate["x"] + 0.75, y=subset_candidate["y"] - 0.5,
                s="*",
                ha="center", va="center",
                fontfamily="serif", fontsize=8,
                color="#ffffff",
                zorder=4
            )
            
            # Save plot
            plt.savefig(filename)
        
        # Reidentify the subset candidate and add to subset
        subset_candidate["id"] = "S$_{" + str(len(subset) + 1) + "}$"
        subset_updated = subset.append(subset_candidate)

        return dataset_updated, subset_updated
    else:
        raise ValueError("Subset needs to be initialised first")