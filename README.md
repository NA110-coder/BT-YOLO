# BT-YOLO
# BT-YOLO: An Attention-Enhanced Framework for Monitoring Bioluminescent Algal Blooms in Coastal Tourism Zones

This repository is the official implementation for our paper:
> [cite_start]**Title:** BT-YOLO: An Attention-Enhanced Framework for Monitoring Bioluminescent Algal Blooms in Coastal Tourism Zones [cite: 1]
> **Authors:** [Apna Naam aur Co-authors ka Naam Yahan Likhein]
> **Status:** Submitted to *Ecological Informatics* (Under Review)

## ⚠️ Repository Status

**Note:** This repository is provided to ensure the reproducibility of our study, as requested by the Associate Editor and reviewers. We are currently in the process of cleaning the code and adding comprehensive documentation. A fully documented version, along with pre-trained models, will be made publicly available upon the paper's final acceptance.

## 1. Data Availability

[cite_start]Our study introduces the **BT3.8k dataset**[cite: 5]. As per the journal's policy, the complete dataset (images, annotations, and documentation) has been permanently archived and is publicly available on **Zenodo**:

* **Zenodo (BT3.8k Dataset):** `[YAHAN APNA ZENODO LINK DAALEIN]`

## 2. Installation

1.  Clone this repository:
    ```bash
    git clone [YAHAN APNA GITHUB REPO LINK DAALEIN]
    cd [REPOSITORY-FOLDER-KA-NAAM]
    ```
2.  Install the required dependencies. We recommend using a virtual environment.
    ```bash
    pip install -r requirements.txt
    ```

## 3. Basic Usage

These are the basic commands to run the model as described in the paper.

### Train
To train the BT-YOLO model on the BT3.8k dataset:
```bash
# Apni asal training command yahan likhein
# Example:
python train.py --data config/bt3.8k.yaml --cfg models/bt-yolo.yaml --weights 'yolov11m.pt' --batch-size 20
