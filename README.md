# Molecular Solubility Prediction

This project develops predictive models for aqueous solubility of organic molecules using RDKit molecular descriptors and machine learning.

---

## Background

- Aqueous solubility is a fundamental molecular property in drug discovery, which influences how well a compound is absorbed, distributed, and ultimately bioavailable in our body. 
- Poorly soluble compounds often fail during the development stages despite showing promising biological activity, which makes early computational assessment of solubility necessary for investigating/screening drug candidates before moving on to more cost-heavy experimental synthesis.

- Since solubility prediction is a commonly studied problem in the area of molecular property modeling, it serves as a good benchmark for building and assessing a reproducible cheminformatics workflow. The main goal of this project is not just to create a model that makes good predictions, but to understand why the model works and whether it makes chemical sense.

---

## Project Goals

- Develop and evaluate linear regression (LR) and machine learning (ML) models capable of predicting aqueous solubility for unseen organic molecules
- Identify the molecular features that govern solubility behavior and assess their chemical interpretability
- This workflow combines steps like descriptor generation, exploratory data analysis, feature selection, ML, model training and model interpretation. A strong emphasis is placed  on connecting model behavior to chemical reasoning throughout this project as we want to build a model that a chemist can easily understand, trust and learn from, not just a black box that predicts numbers.

---

## Scientific Questions

- Which molecular descriptors are most strongly associated with aqueous solubility?
- Can ML models accurately predict solubility for unseen molecules?
- Which modeling approaches provide the best balance between predictive performance and chemical interpretability?
- Do the features in the most important model align well with established chemical understanding of solubility?

---

## Cheminformatics Workflow

1. Convert SMILES strings into molecular representations
2. Generate RDKit molecular descriptors
3. Perform data cleaning and preprocessing
4. Explore inter-descriptor correlations and descriptor-target relationships
5. Identify relevant descriptors through feature selection
6. Train and compare LR and ML predictive models
7. Interpret model behavior using feature importance and SHAP analysis
8. Rebuild interpretable LR model using SHAP-selected descriptors and validate against ML baseline
9. Univariate analysis of SHAP-selected descriptors
10. Nonlinearity characterization using SHAP dependence plots, partial dependence plots, polynomial regression
11. Provide a simple easy-to-use linear equation with chemical interpretation of model features 
12. Validate predictive performance using cross-validation
13. Predict solubility for unseen molecules

---

## Computational Methods

**Descriptor generation & representation**
- RDKit, SMILES-based molecular representations

**Feature selection & dimensionality reduction**
- Pearson correlation, Variance Inflation Factor (VIF), SHAP-based feature importance

**Model selection & training**
- LR Models, regularized LR models (Ridge, Lasso, Elastic Net), tree-based models (Random Forest, Gradient Boosting, ExtraTrees), kernel-based models (Support Vector, Kernel Ridge, K-Nearest Neighbors) approaches to identify the best fit for the data before hyperparameter optimization
- Hyperparameter tuning via GridSearchCV, LR model reconstruction using SHAP-selected descriptors, k-fold cross-validation

**Model interpretation**
- Feature importance, SHAP (SHapley Additive exPlanations)
- SHAP dependence plots and partial dependence plots
- Polynomial Regression models 

---

##  Interpretability Significance

- Predictive performance alone is often not enough when models are used to guide real decisions. A ML model that performs well on a benchmark might behave in a way that contradicts chemical intuition, making it difficult to rely on.

- In this project, feature importance and SHAP analysis are used to identify which molecular properties are driving predictions and to determine whether the observed model behavior agrees with already established chemical understanding of solubility (e.g., how physicochemical properties like hydrophobicity, molecular size, charge distribution, hydrogen bonding capabilities relate to aqueous solubility).

- The "notebooks" folder contains markdowns in each notebook that put modeling decisions within a chemical context, including detailed discussions on how descriptor trends relate to aqueous solubility, which can be relevant to early-stage compound assessment in drug discovery contexts.

### The main goal is not just to build an accurate model, but to create a clear picture of what the model has learned and whether that picture makes chemical sense.
---

## Results Overview

- ML models (ExtraTrees, SVR, Random Forest) outperformed initial LR baseline, with ExtraTrees model being the best compromise between accuracy and interpretability (Test R² = 0.86 and MAE = 0.50 log units). The prediction uncertainty was well within the < 1 log unit threshold considered acceptable for early-stage drug candidate screening.
- <img width="1132" height="846" alt="04_Initial_multivariate_LRmodel_18descriptors" src="https://github.com/user-attachments/assets/dd5513ac-dd5d-4c3b-84f0-9300585b57b1" />

- <img width="1273" height="623" alt="05_ML_models_comparison" src="https://github.com/user-attachments/assets/50669ee9-8c2e-435f-8359-d13bdbb22563" />

- Feature importance and SHAPley analysis on the ExtraTrees model suggested that only 5 molecular descriptors were driving the majority of predictions: FilterItLogS (a fragment-based solubility feature), ZMIC1 (molecular size/complexity), Lipinski rule (drug-likeness), RNCG (charge distribution), and PEOE_VSA6 (electronegative Vander Walls surface area). These 5 descriptors showed 1.3 to 2 times stronger correlation with solubility than any descriptor that survived the initial VIF-based filtering, confirming that aggressive feature reduction had discarded  important predictive signal while building the initial multivariate LR models.
- <img width="812" height="912" alt="06_SHAP_beeswarmplot_ExtraTrees_Model" src="https://github.com/user-attachments/assets/72d26180-b64b-4ec7-bfd7-2569bd54356e" />

- A final multivariate LR model was rebuilt using only SHAP-selected descriptors that resulted in a strong predictive performance (Test R² = 0.77 and MAE = 0.70 log units). This model was then assessed using a 10-fold cross-validation on both a held-out test set (R² = 0.81 ± 0.05) and an external set consisting of previously unseen molecules (R² = 0.81, MAE = 0.66). These validations showed only a modest reduction in predictive performance when compared to the full ML model, while producing a simple linear equation a medicinal chemist can easily apply, critique, and trust.
- <img width="1082" height="845" alt="07_Multivariate_LR_model_with_SHAP_features" src="https://github.com/user-attachments/assets/88cedab8-ed2b-4844-a2d5-94fa7a780a82" />
<img width="953" height="48" alt="13_Final_linear_equation" src="https://github.com/user-attachments/assets/4e12d809-5ba3-4a96-8de6-448fa1baa1ba" />

- All the descriptor-solubility trends are chemically interpretable: molecules with higher polarity, negative charge distribution, and drug-like properties are more soluble (FilterItLogS, RNCG, Lipinski) while the  molecules with larger size, more structural complexity and more hydrophobic nature are less soluble (ZMIC1, PEOE_VSA6). The SHAP-dependence, partial dependence and polynomial regression plots confirmed that these descriptor-solubility relationships are predominantly linear and additive, thus explaining why a simple LR model recovered most of the ML model's predictive power.


---

## Repository Structure

```
Molecular-Solubility-Prediction/
├── data/
├── notebooks/
├── Results/
├── Figures/
├── README.md
└── requirements.txt
```
