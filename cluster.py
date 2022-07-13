import numpy as np
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster import hierarchy
import pandas as pd
import seaborn as sns
import csv

def Cluster_Algothrim_By_Distance_icnb3py(directory_to_csv_file, index_column_name, linkage_algorithm):

    """
    Cluster_Algothrim_By_Distance_icnb3py creates a dendrogram of the distances taken
    from the distance matrix between all pairs of nodes and links in the
    icnb3py distanace. This will create a dendrogram of the distances. 

    This denogram is important for understanding the protein function and different 
    conformations. One of the main ideas is if protein interact with each other, in
    general, if binding is binding to another protein does it assume a general shape. 
    This has to do with sort of trying to charaterizing a protein, what relationshp
    has to its function. 

    This function depends on the following packages: numpy, pyplot, scipy,
    pandas, seaborn, and csv. 
    
    We hope this function will be useful to looking large steps of structures.

    :directory_to_csv_file: directory to csv file. It should include csv at the end
    :index_column_name: name of the index column in the csv file
    :linkage_algorithm: linkage algorithm to used for the hierarchy.linkage.
    To view what linkage algorithm are available, pleaes read the
    scipy documentation. 

    https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html


    :return: the output of this function is a dendrogram of the distances
    """ 

    linkage_algorithm = str(linkage_algorithm)
    index_column_name = str(index_column_name)
    directory_to_csv_file = str(directory_to_csv_file)

    data = pd.read_csv(directory_to_csv_file)
    data = data.set_index(index_column_name)

    Hier_Link = hierarchy.linkage(data, method=linkage_algorithm)

    dendrogram(Hier_Link,leaf_rotation=90, leaf_font_size=12, labels = data.index)
    plt.figure(figsize=(20, 20))
    plt.show()

Cluster_Algothrim_By_Distance_icnb3py('C:\\Users\\eanda\\OneDrive\\Documents\\Python_Files\\dist_table.csv', 'ID', 'complete')
