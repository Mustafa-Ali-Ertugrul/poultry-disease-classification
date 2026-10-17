"""
Dataset'i Hugging Face Hub'dan repo kokune indirir:
  final_dataset_10_classes/, prepared_duck_3class*/, prepared_goose_2class*/

Dataset private'tir; once `hf auth login` ile giris yapin.

Kullanim:
    python scripts/download_dataset.py
"""

from pathlib import Path

from huggingface_hub import snapshot_download

REPO_ID = "MustafaAlii/poultry-disease-histopathology"
ROOT = Path(__file__).resolve().parent.parent

if __name__ == "__main__":
    snapshot_download(
        repo_id=REPO_ID,
        repo_type="dataset",
        local_dir=ROOT,
        allow_patterns=["final_dataset_10_classes/**", "prepared_*/**"],
    )
    print(f"Dataset indirildi: {ROOT}")
