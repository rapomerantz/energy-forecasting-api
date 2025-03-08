import os
import kaggle

# Paths
DATASET = "mrsimple07/energy-consumption-prediction"
DATA_DIR = "data"

def download_kaggle_dataset():
    """Downloads the dataset from Kaggle."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    kaggle.api.dataset_download_files(DATASET, path=DATA_DIR, unzip=True)

if __name__ == "__main__":
    download_kaggle_dataset()