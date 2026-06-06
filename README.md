# Molecular Solubility Prediction

This project develops predictive models for aqueous solubility of organic molecules using RDKit molecular descriptors and machine learning.

---

## Background

- Aqueous solubility is a fundamental molecular property in drug discovery — it influences how well a compound is absorbed, distributed, and ultimately bioavailable when administered orally. 
- Poorly soluble compounds frequently fail in development despite showing promising biological activity, which makes early computational assessment of solubility a practical tool for testing candidate molecules before starting cost-intensive experimental synthesis.

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
5. Identify relevant descriptors through feature selection and dimensionality reduction
6. Train and compare predictive models
7. Interpret model behavior using feature importance and SHAP analysis
8. Optimize model hyperparameters
9. Validate performance using cross-validation
10.Predict solubility for unseen molecules

---

## Computational Methods

**Descriptor generation & representation**
- RDKit, SMILES-based molecular representations

**Feature selection & dimensionality reduction**
- Pearson correlation, Variance Inflation Factor

**Model screening & training**
- Linear Regression Models, Tree-based models (Random Forest, Gradient Boosting), kernel-based models (Support Vector Regression)
- Hyperparameter tuning via GridSearchCV, k-fold cross-validation

**Model interpretation**
- Feature importance, SHAP (SHapley Additive exPlanations)

---

## Emphasis on Interpretability

Predictive performance alone is often insufficient when models are used to guide real decisions. A model that scores well on a benchmark but behaves in ways that contradict chemical intuition is difficult to trust or act on.

Throughout this project, feature importance and SHAP analysis are used to identify which molecular properties are driving predictions — and to check whether that behavior holds up against established chemical understanding of solubility (for example, how hydrophobicity, molecular size, and hydrogen bonding capacity relate to aqueous solubility trends).

The notebook markdown throughout connects modeling decisions to chemical context, including discussion of how descriptor trends relate to molecular properties, which can be relevant to early-stage compound assessment.

The aim is not just to build accurate models, but to develop a clear picture of *what the model has learned* — and whether that picture is chemically meaningful.

---

## Results Overview

*(To be added upon project completion. Key outputs will include cross-validated performance metrics for each model, SHAP summary plots, and a comparison of the most influential descriptors against the published solubility literature.)*

---

## Repository Structure

```
Molecular-Solubility-Prediction/
├── data/
├── notebooks/
├── src/
├── results/
├── figures/
├── README.md
└── requirements.txt
