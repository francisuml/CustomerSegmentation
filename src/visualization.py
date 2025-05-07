import matplotlib.pyplot as plt
import plotly.express as px

def plot_elbow(wcss):
    plt.plot(range(2,11), wcss, marker='o')
    plt.title('Elbow Method')
    plt.xlabel('Number of Clusters')
    plt.ylabel('WCSS')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('output/elbow_method.png')
    plt.show()

def plot_clusters_plotly(data):
    fig = px.scatter(data, x='PC1', y='PC2', color=data['Cluster'].astype(str),
                     title='Customer Segmentation (KMeans)', labels={'color':'Cluster'})
    fig.write_html('output/cluster_visualization.html')
    fig.show()