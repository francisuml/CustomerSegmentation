# Customer Segmentation Using RFM and KMeans Clustering

## Description

This repository showcases an end-to-end Unsupervised Machine Learning project focused on customer segmentation using RFM (Recency, Frequency, Monetary) analysis and KMeans clustering. 
The goal is to gain actionable business insights by identifying different groups of customers based on their purchasing behaviors.

I utilize the Online Retail dataset, conduct exploratory data analysis, engineer features, apply PCA for dimensionality reduction, and evaluate clustering results using metrics and visualization tools. This project is structured for clarity, reproducibility, and real-world applicability—ideal for my data science portfolio.

### Directory Structure

CustomerSegmentation/
│
├── README.md                  
├── main.ipynb                
├── requirements.txt           
│
├── data/
│   └── OnlineRetail.csv       
│
├── output/
│   ├── elbow_method.png       
│   ├── cluster_visualization.html 
│   └── cluster_summary.csv    
│
└── src/
    └── utils.py               

How to Run

Clone this repository:

git clone https://github.com/francisu.ML/CustomerSegmentation.git
cd CustomerSegmentation

Create a virtual environment and install dependencies:

pip install -r requirements.txt

Launch the notebook:

jupyter notebook CustomerSegmentation.ipynb

Key Techniques Used

Data Cleaning & Exploratory Data Analysis

Feature Engineering (RFM)

KMeans Clustering with Elbow Method

Dimensionality Reduction with PCA

Evaluation using Silhouette Score & Visualizations

## Insights

The elbow method identified 3 optimal clusters.

Cluster 0: Core customers with moderate activity and spending.

Cluster 1: Dormant customers with infrequent and low-value purchases.

Cluster 2: VIP customers with frequent purchases and high monetary value.

## Conclusion

Through this project, I demonstrate how unsupervised learning can be applied to solve real-world business problems. Segmenting customers allows for:

* Personalized marketing strategies

* Improved resource allocation

* Enhanced customer relationship management

Author

Francis Carl Sumile  
Machine Learning Practitioner | Data Scientist
GitHub: github.com/francisu.ml

License

MIT License

