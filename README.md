# Molecular Solubility Prediction

This project develops predictive models for aqueous solubility of organic molecules using RDKit molecular descriptors and machine learning.

---

## Background

- Aqueous solubility is a fundamental molecular property in drug discovery — it influences how well a compound is absorbed, distributed, and ultimately bioavailable when administered orally. 
- Poorly soluble compounds frequently fail in development despite showing promising biological activity, which makes early computational assessment of solubility a practical tool for testing candidate molecules before committing to cost-intensive experimental synthesis.

- Solubility prediction is one of the most studied problems in molecular property modeling, which makes it a well-suited benchmark for building and evaluating a reproducible cheminformatics workflow. The goal here is not just to produce a model that scores well, but to understand *why* it works — and whether its behavior makes chemical sense.

---

## Project Goal

Develop and evaluate descriptor-based machine learning models capable of predicting aqueous solubility for unseen organic molecules, while identifying the molecular features that govern solubility behavior.

The workflow combines descriptor generation, exploratory data analysis, feature selection, machine learning, and model interpretation. The emphasis throughout is on connecting model behavior to chemical reasoning — building something a chemist can trust and learn from, not just a black box that predicts numbers.

---

## Scientific Questions

- Which molecular descriptors are most strongly associated with aqueous solubility?
- Can machine learning models accurately predict solubility for molecules outside the training set?
- Which modeling approaches provide the best balance between predictive performance and interpretability?
- Do the most influential model features align with established chemical understanding of solubility?

---

## Cheminformatics Workflow

1. Convert SMILES strings into molecular representations
2. Generate RDKit molecular descriptors
3. Perform data cleaning and preprocessing
4. Explore descriptor distributions and target-property relationships
5. Identify relevant descriptors through feature selection
6. Train and compare linear regression and machine learning predictive models
7. Interpret model behavior using feature importance and SHAP analysis
8. Reconstruct interpretable LR model using SHAP-selected descriptors and validate against ML baseline
9. Univariate analysis of SHAP-selected descriptors
10. Nonlinearity characterization using SHAP dependence plots, partial dependence plots, polynomial regression
11. Provide a simple easy-to-use linear equation with chemical interpretation of features used to build the LR model
12. Validate performance using cross-validation
13. Predict solubility for unseen molecules

---

## Computational Methods

**Descriptor generation & representation**
- RDKit, SMILES-based molecular representations

**Feature selection & dimensionality reduction**
- Pearson correlation, Variance Inflation Factor, SHAP-based feature importance

**Model selection & training**
- Linear Regression Models, Tree-based models (Random Forest, Gradient Boosting), kernel-based models (Support Vector Regression) approaches to identify the best fit for the data before commimitting to hyperparameter optimization
- Hyperparameter tuning via GridSearchCV, LR model reconstruction using SHAP-selected descriptors, k-fold cross-validation, external validation

**Model interpretation**
- Feature importance, SHAP (SHapley Additive exPlanations), SHAP dependence plots and partial dependence plots for nonlinearity characterization, 

---

## Emphasis on Interpretability

Predictive performance alone is often insufficient when models are used to guide real decisions. A model that scores well on a benchmark but behaves in ways that contradict chemical intuition is difficult to trust or act on.

Throughout this project, feature importance and SHAP analysis are used to identify which molecular properties are driving predictions — and to check whether that behavior holds up against established chemical understanding of solubility (for example, how hydrophobicity, molecular size, and hydrogen bonding capacity relate to aqueous solubility trends).

The notebook markdown throughout connects modeling decisions to chemical context, including discussion of how descriptor trends relate to molecular properties, which can be relevant to early-stage compound assessment.

The aim is not just to build accurate models, but to develop a clear picture of *what the model has learned* — and whether that picture is chemically meaningful.

---

## Results Overview

- Machine learning models (ExtraTrees, SVR, Random Forest) outperformed linear regression on this dataset, with ExtraTrees model being the best compromise between accuracy and interpretability (Test R² = 0.86 and MAE = 0.50 log units). The prediction uncertainty was well within the < 1 log unit threshold considered acceptable for early-stage drug candidate screening
- <img width="1273" height="623" alt="05_ML_models_comparison" src="https://github.com/user-attachments/assets/50669ee9-8c2e-435f-8359-d13bdbb22563" />

- Feature importance and SHAPley analysis on the ExtraTrees model suggested that only 5 molecular descriptors were driving the majority of predictions: FilterItLogS (a fragment-based solubility estimate), ZMIC1 (molecular size/complexity), Lipinski rule compliance (drug-likeness), RNCG (charge distribution), and PEOE_VSA6 (electronegative surface area). These 5 descriptors showed 1.3–2× stronger correlation with solubility than any descriptor surviving the initial VIF-based filtering step, confirming that aggressive feature reduction had discarded  important predictive signal while building the initial multivariate linear regression models
- <img width="812" height="912" alt="06_SHAP_beeswarmplot_ExtraTrees_Model" src="https://github.com/user-attachments/assets/72d26180-b64b-4ec7-bfd7-2569bd54356e" />

- A final multivariate linear regression model was built using only these 5 descriptors that resulted in a strong model performance (Test R² = 0.77 and MAE = 0.70 log units). This model was then assessed using a 10-fold cross-validation on both a held-out test set (R² = 0.81 ± 0.05) and an external set of previously unseen molecules (R² = 0.81, MAE = 0.66). These validations showed only a modest reduction in predictive performance when compared to the full ML model, while producing a simple linear equation a medicinal chemist can easily apply, critique, and trust.
- <img width="1082" height="845" alt="07_Multivariate_LR_model_with_SHAP_features" src="https://github.com/user-attachments/assets/88cedab8-ed2b-4844-a2d5-94fa7a780a82" />
<img width="953" height="48" alt="13_Final_linear_equation" src="https://github.com/user-attachments/assets/4e12d809-5ba3-4a96-8de6-448fa1baa1ba" />

- All 5 descriptor–solubility relationships are chemically interpretable: larger, more complex, and more hydrophobic molecules are less soluble (ZMIC1, PEOE_VSA6), while molecules with greater polarity, charge distribution, and drug-like physicochemical properties are more soluble (RNCG, Lipinski, FilterItLogS). Partial dependence and polynomial regression analyses confirmed that these relationships are predominantly linear and additive, explaining why a simple linear model recovers most of the ML model's predictive power.


---

## Repository Structure

```
Molecular-Solubility-Prediction/
├── data/
├── notebooks/
├── results/
├── figures/
├── README.md
└── requirements.txt
```
