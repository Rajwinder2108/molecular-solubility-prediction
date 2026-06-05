## Molecular-solubility-prediction
This project develops predictive models for aqueous solubility of organic molecules using RDKit molecular descriptors and machine learning.

## Background

Aqueous solubility is a key molecular property in drug discovery because it influences absorption, distribution, and oral bioavailability. Poorly soluble compounds often fail despite possessing desirable biological activity, making early assessment of solubility an important part of molecular property optimization. 


## Project Goal
Develop and evaluate descriptor-based machine learning models capable of predicting aqueous solubility for unseen organic molecules while identifying the molecular properties that govern solubility.
The workflow combines descriptor generation, exploratory data analysis, feature selection, machine learning, and model interpretation to identify molecular characteristics associated with aqueous solubility. Model performance is evaluated using cross-validation, while feature importance and SHAP analysis are used to assess chemical interpretability.

## Scientific Questions
- Which molecular descriptors are most strongly associated with aqueous solubility?
- Can machine learning models accurately predict solubility for unseen molecules?
- Which modeling approaches provide the best balance between predictive performance and interpretability?
- Do the most influential model features align with established chemical understanding of solubility?

## Cheminformatics workflow
1. Convert SMILES strings into molecular representations
2. Generate RDKit molecular descriptors
3. Perform data cleaning and preprocessing
4. Explore descriptor distributions and target-property relationships
5. Identify relevant descriptors through feature selection and dimensionality reduction
6. Train and compare predictive models
7. Interpret model behavior using feature importance and SHAP analysis
8. Optimize model hyperparameters
9. Validate performance using cross-validation
10. Predict solubility for unseen molecules

## Computational Methods 
- RDKit
- Scikit-learn
- Pearson correlation
- PCA
- Model screening (Lazypredict)
 - t-SNE
- Feature importance
- Permutation importance
- SHapley
- Linear Regression
- Random Forest
- Extra Trees
- Hyperparameter tuning
- K-fold cross validation
- GridSearch cross validation

## Emphasis on Interpretability

Predictive performance alone is often insufficient when computational models are used to guide scientific decision-making. Throughout this workflow, feature importance, permutation importance, and SHAP analysis are used to identify the molecular properties driving model predictions and assess whether model behavior remains chemically meaningful.

The goal is not only to build accurate predictive models, but also to develop an understanding of the molecular factors governing aqueous solubility and ensure that model predictions can be easily interpreted within an established chemical framework.

## Results Overview

Placeholder

## Repository Structure

Molecular-Solubility-Prediction/

├── data/
├── notebooks/
├── src/
├── results/
├── figures/
├── README.md
└── requirements.txt
