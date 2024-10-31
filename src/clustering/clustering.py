import pandas as pd
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import MinMaxScaler
from omegaconf import OmegaConf
import hydra
import os
import warnings
import logging

warnings.filterwarnings("ignore", category=UserWarning)

# Set up logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def load_data(filepath):
    """Load the cocktail data from a JSON file."""
    return pd.read_json(filepath)

def ensure_numeric_format(tags_series):
    """Convert one-hot tags from series to a proper numeric array."""
    return pd.DataFrame(tags_series.tolist())

def normalize_tags(tags_df):
    """Normalize the one-hot encoded tags to a [0, 1] range."""
    scaler = MinMaxScaler()
    return pd.DataFrame(scaler.fit_transform(tags_df), columns=tags_df.columns)

def apply_weights(tags_df, weights):
    """Apply weights to the tags to emphasize certain features."""
    return tags_df * weights

def perform_clustering(tags_df, n_clusters):
    """Perform K-means, Agglomerative and DBSCAN clustering."""
    # K-means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=0, n_init=10)
    kmeans_labels = kmeans.fit_predict(tags_df)

    # Agglomerative clustering
    agg_cluster = AgglomerativeClustering(n_clusters=n_clusters)
    agg_labels = agg_cluster.fit_predict(tags_df)

    return kmeans_labels, agg_labels

def evaluate_clustering(tags_df, kmeans_labels, agg_labels):
    """Evaluate clustering using silhouette score."""
    kmeans_silhouette = silhouette_score(tags_df, kmeans_labels)
    logger.info(f"K-means Silhouette Score: {kmeans_silhouette:.4f}")

    agg_silhouette = silhouette_score(tags_df, agg_labels)
    logger.info(f"Agglomerative Clustering Silhouette Score: {agg_silhouette:.4f}")


def log_cluster_counts(cocktail_data):
    """Log the number of cocktails in each cluster."""
    kmeans_counts = cocktail_data['kmeans_cluster'].value_counts()
    agg_counts = cocktail_data['agg_cluster'].value_counts()

    logger.info("Number of cocktails in each K-means cluster:")
    for cluster, count in kmeans_counts.items():
        logger.info(f"Cluster {cluster}: {count} cocktails")

    logger.info("Number of cocktails in each Agglomerative cluster:")
    for cluster, count in agg_counts.items():
        logger.info(f"Cluster {cluster}: {count} cocktails")


def find_optimal_clusters(tags_df, max_clusters=10):
    """Find the optimal number of clusters based on silhouette score."""
    best_score = -1
    best_n = 2
    scores = []

    for n_clusters in range(2, max_clusters + 1):
        kmeans = KMeans(n_clusters=n_clusters, random_state=0, n_init=10)
        kmeans_labels = kmeans.fit_predict(tags_df)

        score = silhouette_score(tags_df, kmeans_labels)
        scores.append(score)
        logger.info(f"Silhouette Score for {n_clusters} clusters: {score:.4f}")

        if score > best_score:
            best_score = score
            best_n = n_clusters

    logger.info(f"Optimal number of clusters: {best_n} with a Silhouette Score of {best_score:.4f}")
    return best_n

@hydra.main(version_base=None, config_path="../../configs/clustering_configs", config_name="clustering_config")
def main(cfg):
    # Load the cocktail data
    cocktail_data = load_data('data/processed/one_hot_encoded_cocktail_dataset.json')

    # Extract the one-hot encoded tags
    tags_df = cocktail_data['one_hot_tags']

    # Ensure tags_df is properly formatted
    tags_df = ensure_numeric_format(tags_df)

    # Normalize the one-hot encoded tags
    #tags_df = normalize_tags(tags_df)

    # Optionally apply weights to certain tags (define weights as per your analysis)
    weights = [1 if count > 5 else 0.5 for count in tags_df.sum()]  # Example weights
    tags_df = apply_weights(tags_df, weights)

    # Find the optimal number of clusters
    optimal_clusters = find_optimal_clusters(tags_df, max_clusters=cfg.clustering.n_clusters)

    # Perform clustering with optimal clusters
    kmeans_labels, agg_labels = perform_clustering(tags_df, optimal_clusters)

    # Evaluate clustering
    evaluate_clustering(tags_df, kmeans_labels, agg_labels)

    # Add cluster labels to the original data for further analysis
    cocktail_data['kmeans_cluster'] = kmeans_labels
    cocktail_data['agg_cluster'] = agg_labels

    # Log the number of cocktails in each cluster
    log_cluster_counts(cocktail_data)

if __name__ == "__main__":
    main()
