Customer Segmentation Using RFM and KMeans Clustering

Description

This repository showcases an end-to-end Unsupervised Machine Learning project focused on customer segmentation using RFM (Recency, Frequency, Monetary) analysis and KMeans clustering. 
The goal is to gain actionable business insights by identifying different groups of customers based on their purchasing behaviors.

I utilize the Online Retail dataset, conduct exploratory data analysis, engineer features, apply PCA for dimensionality reduction, and evaluate clustering results using metrics and visualization tools. This project is structured for clarity, reproducibility, and real-world applicability—ideal for my data science portfolio.

Directory Structure

CustomerSegmentation/
│
├── README.md                  <- Project description and instructions
├── main.ipynb                 <- Main Jupyter Notebook with EDA, modeling, and insights
├── requirements.txt           <- List of dependencies
│
├── data/
│   └── OnlineRetail.csv       <- Input dataset
│
├── output/
│   ├── elbow_method.png       <- Elbow method graph to determine optimal K
│   ├── cluster_visualization.html <- Plotly interactive cluster visualization
│   └── cluster_summary.csv    <- Summary statistics for each cluster
│
└── src/
    └── utils.py               <- Helper functions for preprocessing and modeling

How to Run

Clone this repository:

git clone https://github.com/yourusername/CustomerSegmentation.git
cd CustomerSegmentation

Create a virtual environment and install dependencies:

pip install -r requirements.txt

Launch the notebook:

jupyter notebook main.ipynb

Key Techniques Used

Data Cleaning & Exploratory Data Analysis

Feature Engineering (RFM)

KMeans Clustering with Elbow Method

Dimensionality Reduction with PCA

Evaluation using Silhouette Score & Visualizations

Insights

The elbow method identified 3 optimal clusters.

Cluster 0: Core customers with moderate activity and spending.

Cluster 1: Dormant customers with infrequent and low-value purchases.

Cluster 2: VIP customers with frequent purchases and high monetary value.

Conclusion

Through this project, we demonstrate how unsupervised learning can be applied to solve real-world business problems. Segmenting customers allows for:

Personalized marketing strategies

Improved resource allocation

Enhanced customer relationship management

Author

Francis Carl Sumile 
Machine Learning Practitioner | Data Scientist
GitHub: github.com/francisuml

License

MIT License

