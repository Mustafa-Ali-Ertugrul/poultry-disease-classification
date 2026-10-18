"""
Dataset'i Hugging Face Hub'dan repo kokune indirir:
  final_dataset_10_classes/, prepared_duck_3class*/, prepared_goose_2class*/

Her dataset Hub'da tek bir zip olarak durur (istek limitine takilmamak icin).
Dataset private'tir; once `hf auth login` ile giris yapin.

Kullanim:
    python scripts/download_dataset.py
"""

import zipfile
from pathlib import Path

from huggingface_hub import hf_hub_download

REPO_ID = "MustafaAlii/poultry-disease-histopathology"
ROOT = Path(__file__).resolve().parent.parent
ARCHIVES = [
    "final_dataset_10_classes.zip",
    "prepared_duck_3class.zip",
    "prepared_duck_3class_cleaned.zip",
    "prepared_goose_2class.zip",
    "prepared_goose_2class_cleaned.zip",
]

if __name__ == "__main__":
    for name in ARCHIVES:
        path = hf_hub_download(repo_id=REPO_ID, filename=name, repo_type="dataset")
        with zipfile.ZipFile(path) as z:
            z.extractall(ROOT)
        print(f"{name} -> {ROOT / name.removesuffix('.zip')}")
