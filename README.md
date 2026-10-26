# ensemble-learning
Code for ML model and Flask app
This repository contains the Python code for the machine learning modeling and the Flask-based web tool used in the paper  It is provided to support code review and transparency; it is not intended as a full reproduction package for all analyses.
## File Structure

```text
.
├── README.md
├── LICENSE
├── model_TCGA_gene.ipynb    # Jupyter Notebook for model training, evaluation, and SHAP analysis
├── TCGA_data.xlsx           # Processed data/features used by the model (if applicable)
└── project_gene/            # Flask web application
    ├── model.pkl            # Trained machine learning model
    ├── model_gene.py        # Backend Python script for the web app
    └── templates/
        └── index.html       # Frontend HTML interface
model_TCGA_gene.ipynb: The main Jupyter Notebook containing the Python code for building, training, and evaluating the machine learning models.
project_gene/: The complete Flask application for the web-based prediction tool. It includes the trained model (model.pkl), the backend routing script (model_gene.py), and the frontend HTML template.
Requirements
The code is written in Python. Main dependencies include scikit-learn, pandas, numpy, shap (for the notebook) and flask (for the web app).
You can install the required packages using:
bash
pip install scikit-learn pandas numpy shap flask
￼
￼
Usage
1. Model Code
You can open and run model_TCGA_gene.ipynb using Jupyter Notebook or Jupyter Lab. The input data format is illustrated in TCGA_data.xlsx.
2. Flask Web Tool
To run the web application locally:
bash
cd project_gene
python model_gene.py
After the server starts, open your browser and go to the local address provided in the terminal (usually http://127.0.0.1:5000). The web interface accepts input features and uses model.pkl to return a predicted risk probability.
Data
Raw data are not redistributed here. TCGA-THCA data can be obtained from the GDC Data Portal (https://portal.gdc.cancer.gov/). The TCGA_data.xlsx file provides the processed input format expected by the model.
Citation
If you use this code, please cite:
[Full citation, to be completed after publication]
Contact
[Xiao Chen], [2071430369@qq.com]
GitHub: [CHENXIAO325]
License
[MIT License / GPL-3.0, as appropriate]. See LICENSE for details.