from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

def apply_kmeans(data, n_clusters=3):
    model = KMeans(n_clusters=n_clusters, random_state=42)
    data['Cluster'] = model.fit_predict(data[['Recency','Frequency', 'Monetary']])
    return data, model

def reduce_dimensionality(data, n_components=2):
    pca = PCA(n_components=n_components)
    components = pca.fit_transform(data[['Recency', 'Frequency', 'Monetary']])
    data['PC1'], data['PC2'] = components[:, 0], components[:, 1]
    return data
