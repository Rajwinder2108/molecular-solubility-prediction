# Linear Regression (LR) model building after VIF filtering (Steps 1 & 2)
- A curated dataset is prepared with 18 descriptors and target variable from development set generated after VIF filtering
- A Linear regression model was prioritised at this stage due to its interpretability, allowing direct mapping between molecular descriptors and aqueous solubility.
- This enables chemically meaningful interpretation of models and understanding how individual physicochemical properties contribute to solubility trends
- The dataset was split into training and test sets (80:20 split), resulting in 732 training molecules and 183 test molecules.
- The test set was kept as an internal validation set to assess how well the model generalizes and detect potential overfitting during model development

# Assessing descriptor–target correlation analysis (Step 3)
- Since now we have a manageable number of descriptors remaining, Pearson correlation coefficients is cacluated between descriptors and solubility (logS) to select top descriptors
- The goal is to identify which descriptors are individually relevant to solubility and select top few descriptors
<img width="267" height="588" alt="initial_correlation_coefficients" src="https://github.com/user-attachments/assets/3173aef6-e0dc-4c43-87aa-7d58efded3e5" />

  # Results
- Correlation coefficients fall in the range of 0.1-0.4 and 9 out of 18 descriptors had coefficients > 0.2
- These descriptors were selected for the subsequent univariate predictions step

# Univariate descriptor analysis (Step 4)
- Following descriptor–target correlation analysis, descriptors with |r| > 0.2 were retained for further inspection
- To assess whether individual descriptors carry any independent predictive information, a univariate linear regression approach was applied, where each descriptor was used individually to predict aqueous solubility
- This resulted in 9 LR models while R$^{2}$ values and mean absolute error (MAE) were calculated for each model to evaluate predictive performance
<img width="1128" height="1113" alt="01_univariate_LR_plots_before_ML" src="https://github.com/user-attachments/assets/abcb0c8f-751f-49e5-bbc8-cc5416d499ba" />

# Results
- None of the individual molecular descriptors showed a strong relationship with aqueous solubility
- Univariate regression models could explain only 5–16% of the observed variation in logS values leaving a lot of the variation unexplained
- Although select descriptors such as JGI6, JGI7, and JGI8 showed weak trends with solubility, a substantial scatter can be seen around the regression lines, indicating that these descriptors alone cannot reliably/accurately predict molecular solubility
- Futhrermore, prediction errors were considerably high (MAE = 1.51–1.64 logS units),demonstrating the limited predictive value of individual descriptors

  # Descriptor-descriptor correlation analysis (Step 5)
- Although the 9 selected descriptors had correlation coofficents > 0.2, it is important to ensure that we are not including any redundant descriptors that provide same chemical description of the physicochemical properties
- Therefore, a correlation matrix was built with the training set so that pairwise correlations and correlation coefficient values were easily noticeable
<img width="1118" height="811" alt="02_correlation_matrix_for_features_postVIFfiltering" src="https://github.com/user-attachments/assets/055da123-4501-4779-a05f-d88e32f9d7e5" />

  # Results
- The descriptors from the JGI family show moderate correlation to each other 
- Although 'GHOSEFILTER' descriptor was moderately correlated to JGI6
- 'SMR_VSA9', 'ATSC6Z' were not correlated to the JGI family or 'GHOSEFILTER'
- Although moderate correlation was obeserved between many descriptors, all 9 descriptors were considered for the next step to ensure that no meaninful chemical information was lost

  # Building initial baseline multivariate LR model using 9 descriptors (Step 6)
- Using the descriptors identified from the univariate analysis and descriptor–descriptor correlation matrix, an initial multivariate linear regression (MLR) model was constructed
- The goal was to create an interpretable baseline model with strong predictive performance and minimum redundancy
- The performance was measured using metrics: R2 to assess how much variability in the data can be predicted by MLR model, adjusted R2 to evaluate model complexity, and mean absolute error (MAE) to determine the average prediction error
<img width="1136" height="857" alt="03_Initial_multivariate_LRmodel_9descriptors" src="https://github.com/user-attachments/assets/495aab0b-2871-49de-ae74-99cb0e95a1cd" />

# Results
- The multivariate LR model could describe only 25%-26 of the variability in aqueous solubility, with a relatively high prediction error (MAE=1.42)
- The low R2 performance indicates that simple additive relationships between the selected physico-chemical descriptors explain only a limited proportion of solubility variability
- The relatively high error suggests that there is a noticeable deviation between the predicted and experimentally measured solubility values
- These observations suggest that current descriptor set is not sufficient to fully capture the variability in aqueous solubility
- One possible reason for this limited performance maybe aggressive descriptor filtering, which could have removed descriptors with useful predictive information, indicating a need for model improvement and/or descriptor expansion

#  Expanding the multivariate LR model using 18 descriptors post-VIF filtering (Step 7)
- The goal is to investigate whether the performance loss in nine-descriptor MLR model was a result of description reduction due to excessive filtering
- Therefore, the model obtained after VIF filtering was directly used to make an 18-descriptor MLR model and the performance metrices (R2, adjusted R2, and MAE) were calculated to evaluate the model performance
<img width="1132" height="846" alt="04_Initial_multivariate_LRmodel_18descriptors" src="https://github.com/user-attachments/assets/fe4753bc-c3c3-4766-980b-3fb270422be4" />

# Comparing and interpreting the 9-descriptor vs 18-descriptor MLR model (Step 8)	
- Expanding the descriptor set from 9 to 18 improved model performance suggesting that refining the descriptors might have removed some useful predictive information
- Although descriptor expansion improved the performance, the ability of the MLR model to predict solubility varaibility as well as average prediction error, remained modest (R² = 0.33, adjusted R² = 0.32, and MAE=1.34) indicating that descriptor selection might not be the reason behind limited performance of MLR models

# Final LR Conclusion (Step 9)
- This observation suggests that aqueous solubility may not be adequately described by a linear model and non-linear relationships between molecular descriptors might play an important role
- Therefore, non-linear ML regression models were investigated using the full descriptor set (218 descriptors) obtained before VIF filtering

# Multivariate ML model (Step 10)
- Train Machine Learning (ML) models using 218 descriptors without VIF filtering	Evaluate nonlinear regression models (RF / XGBoost / SVR)	To capture nonlinear structure–property relationships not captured by LR models
- Following the observation that linear regression models exhibited limited explanatory power, a series of progressively more flexible nonlinear machine learning models were evaluated. These included regularized linear models as baseline comparators, kernel-based methods to capture nonlinear transformations, and ensemble tree-based models capable of learning complex feature interactions

 # ML model evaluation and comparison (Step 11)
- To evaluate the best ML model based on performance metrics, trade-off between accuracy and interpretability
- Compare model performace with linear regression baseline to assess model improvement
<img width="1273" height="623" alt="05_ML_models_comparison" src="https://github.com/user-attachments/assets/787f1276-d857-44af-adcb-41171e7783f5" />

  # Results
## Best predicition model: SVR (Train R2=1.00 and Train MAE=0.03, Test R2=0.87 and Test MAE = 0.49)
- SVR turned out to be the best performer with training models slightly overfitting the data, which is expected with highly flexible tree-based models 
- Regardless, model generalization is still good (0.87) which indicates the descriptors do contain a strong predictive signal

## Best balance between predictive power and interpretability: ExtraTrees (Train R2=1.00 and Train MAE=0.008, Test R2=0.86 and Test MAE = 0.50)
- ExtraTrees showed a very strong performance, stable across train:test splits (CV R2=0.91) with reasonable prediction error. 
- For a good trade-off between accuracy and interpretability, ExtraTrees model was carried forward as was carried forward to assess feature contribution using feature importance and SHAP analysis. Furthermore, ExtraTrees captures non-linear relationships well and give reliable feature importance compared to SVR
- Compared to the LR baseline (R² = 0.33 and MAE=1.34), the ML model outperformed it by 164% highlighting that descriptor redundancy determined from pairwise correlation or multicollinearity analys isdoes not necessarily imply redundancy in predictive information. Correlated descriptors might still encode distinct aspects of molecular structure, information that nonlinear ensemble methods can exploit
- To get a closer look at these types of descriptors, feature contribution analysis was performed

# Feature contribution (Step 12)
- Feature contribution was perfomed using feature importance and SHAP to identify and obtain chemical insights regarding the descriptors driving predicitions in ML models
- Feature importance provided information about how often a feature was used across all decision trees, while SHAPley gave the magnitude and direction of how a single feature's value shifted the final prediction of the target variable
<img width="1112" height="1080" alt="06_Feature_importance_ExtraTrees_Model" src="https://github.com/user-attachments/assets/5cf54ab4-1330-4afa-999b-fa2d67822d0e" />
<img width="812" height="912" alt="06_SHAP_beeswarmplot_ExtraTrees_Model" src="https://github.com/user-attachments/assets/f124ee03-6fc5-4a32-8fc6-7071621fc3c8" />

# Results
- Feature Importance: The top 20 descriptors were selected based on SHAP feature importance values. However, only 5 descriptors had importance value > 0.05 indicating prediction model predominantly reiles on few key features
- Shapley was used to extract more detailed information on the contribution from each diescriptor. In these plots, the red points (high feature values) correspond to extrememly negative SHAP values, it generally indicates that higher value of that descriptor would decrease the prediction and vice-versa
- Among the 20 descriptors, nine showed a negative correlation to predicted solubility suggesting that these descriptors might correspond to molecular properties with lower solubility like hydrophobicity or branched structures. The remaining descriptors led to positive contribution towards solubility indicating that they might be associated wih properties with more solubility such as polarity or hydrogen-bonding interactions. Overall, these observations are in line with the well-established solubility range in drug design which requires a compromise between molecular characteristics like polarity and hydrophobicity. The specific chemical interpretation for these desccriptors will be investigated in subsquent analysis sections
- Overall, these observations provided us an insight into the molecular features that drive the model predictions and suggested that only a small number of physicochemical properties are required to explain the varaibility in solubility

  # Building LR models using top SHAP-selected features  (Step 13)
- Based on the deeper understanding of feature contributions to predictions, two multivariate regression models were built using the top 20 and top 5 descriptors identified from SHAP analysis
- The main goal was to investigate whether the ML-guided feature selection would recover the poor performance observed with initial multivariate models (9 and 18 descriptors)
<img width="1082" height="845" alt="07_Multivariate_LR_model_with_SHAP_features" src="https://github.com/user-attachments/assets/c3b341af-007e-479b-91d4-8f1e737217c3" />

# Results
- Using the SHAP-selected features to build the multivariate regression models improved the prediction perfomance by 142%-145%, while the prediction error was reduced by 54%-55%
-  When compared to the 20-descriptor LR model, the 5-descriptor model performed well with only 5% loss in prediction performance and 15% loss in error prediction indicating that the top 5 descriptors could explain the majority of variability in aqueous solubility
- To further investigate if individual predictors carried sufficient independent signal, univariate plots were asssessed

  # Univariate analysis of SHAP-selected descriptors (Step 14)
- The top 5 descriptors were selected from the previous step to build 5 univariate plots, in order to assess whether these descriptors could provide strong predictive performance independently or were the strong predictions in the multivariate plot a result of combined effects of few/several features
- The performance metrices from these univariate plots were compared to initial univariate analysis (Step 4) to check if the low performance could be recovered
<img width="1121" height="607" alt="08_Univariate_LR_plot_top5_SHAP_features" src="https://github.com/user-attachments/assets/c98eacd2-492e-46a3-a774-bb2ad2b0b5ad" />

 # Results
- Four of the five descriptors individually explained 20% or more of the variance in logS, with FilterItLogS being the dominant contributor (Test R² = 0.68, MAE = 0.82), followed by PEOE_VSA6 (R2=0.39 and MAE=1.19)
- When compared to initial univariate models (R2=0.10-0.16 and MAE=1.52), the goodness of fit and prediction error improved substantially. This indicates that SHAP feature selection successfully identified features that captures a large portion of variability in aqueous solubility
- The top-5 SHAP-selected descriptors show 1.3–2× stronger univariate correlation with logS than any descriptor that survived VIF filtering, thus supporting the hypothesis that aggressive filtering discarded useful predictive signal

 # SHAP dependence plots for top descriptors and Correlation Matrix (Step 15)
- SHAP dependence plots were built for top 5 descriptors to visualize how each top descriptor's value impact model predictions, and whether other features (via correlation or interaction) influence the predictive capability of each feature
- Since there was some variability left unexplained from linear regression models, this analysis was performed to identify any non-linear relationships, threshold or saturation behavior
- A correlation matrix was constructed to assess whether multiple feature weres describing overlapping chemical information or structural characteristics. The results from this analysis were combined with SHAP dependence plots to determine whether the SHAP-identified trends were a result of high correlation or non-linearity
<img width="1137" height="588" alt="09_SHAP_dependence_plots_top5_features" src="https://github.com/user-attachments/assets/25c50309-f7e1-4aa8-917f-ea8eeb58e7bf" />
<img width="1121" height="828" alt="10_correlation_matrix_SHAP_selected_features" src="https://github.com/user-attachments/assets/3c61346e-bf4a-47b4-9ecd-0121a7028f21" />

# Results 
- FilterItLogS: the smooth curve, very small vertical spread with SHAP values in the range of -1.5 to 1.5 indicate that this is the major contributor in the prediction model. This makes sense as FilterItLogS is a pre-computed fragment-based logS feature which is essentially using another model's solubility prediction as a feature.Since this feature has prior chemical information on solubility, it naturally leads to high predictive performance for our model. Since the other 4 plots are colored based on FilterItLogS and the correlation coefficients for this feature with respect to remaining features are high, which also makes sense this feature represents solubility. The plot not being a completely straight line with saturation on both sides suggests that the feature has modest non-linear behavior. However, there is no clear distinction between the 2 colors and correlation coefficient with respect to ZMIC1 is high (-0.7). This means that although FilterItLogS and ZMIC1 are strongly negatively correlated (high FilterItLogS values = low ZMIC1 values), the pattern in SDP is coming from feature correlation rather than strong interactions.
- ZMIC1: This plot is the mirror image of the plot above with SHAP values for ZMIC1 lying in a smaller range (0.35 to -0.65) compared to FilterItLogS indicating it is the 2nd most important contributor. Since ZMIC1 encodes molecular size and branching, high values of ZMIC1 correspond to larger size/complex branching in the molecule. Larger molecules tend to have poor aqueous solubility; therefore, a strong negative correlation of ZMIC1 to logS as well as FilterItLogS makes complete sense. This suggests that although the two features are correlated, ZMIC1 is providing supplementary structural information relevant to the molecule
- Lipinski: Since this is a binary descriptor, a linear behavior like before is not expected, simply passing the Lipinski criteria leads to high SHAP values. This makes sense as Lipinski criteria is generally used to assess the "Drug-Likeness" of a molecule, if the molecules meet this criteria, they are more Drug-Like. Since the colors are not clearly separated, a non-linear behavior is not strong. Although correlation between Lipinski and PEOE_VSA6 is moderate (0.5), the plot is dominated by the Lipinski effect than strong interactions
- RNCG (Relative negative charge): With SHAP values ranging from -0.3 to 0.5 and a positive relation to logS indicates that RNCG is an important contributor to prediction. This makes sense as RNCG encodes for charge distribution on the molecule. Molecules with high RNCG would be highly polar and engage in more hydrogen-bonding interactions with water, hence higher solubility. Although RNCG is positively related to solubility, the slope is not very steep and there is a large vertical spread. For eg. at one value of RNCG (0.3), multiple SHAP values are possible (-0.4, -0.1, 0.2, 0.5), which indicates RNCG alone does not determine predictions ans some other features might be influencing its behavior. Indeed, RNCG is moderately/strongly correlated with several descriptors (correlation coefficients with logS:0.65, GhoseFilter:-0.39, PEOE_VSA6:-0.39, FilterItLogS: 0.50, ZMIC1: -0.58) that encode for structural complexity, lipophilicity, polarity etc. for the molecule. Overall, a large vertical spread, mixed colors, less smooth curve suggest that RNCG is a shared-information descriptor with non-linear behavior, rather than being an independent one
- PEOE_VSA6: It encodes for the total Van der Waals surface area of atoms in a molecule whose PEOE (Partial Equalization of Orbital Electronegativities)-calculated partial charges fall within a specific mathematical bin or range. The relation of this feature to target is not as straight-forward. But based on its high correlation to solubility (-0.71) and the shape of the curve (negatively monotonic) and high independent predictive power (R2=0.39) suggest that this feature is providing a meaningful contribution to prediction. One possible reason might be that since this feature encodes for surface area in a sense, hence larger size/lipophilic surface area would lead to poor solubility
- Overall, SPDs gave us valuable insight into how each feature contributes to prediction and how features may influence each other's performance

# Partial Dependence Plots (PDPs) for top descriptors (Step 16)
- While SHAP dependence plots showed instance-level feature contributions, PDPs can characterize the global impact of each feature, wehn averaged across all other features
- The SHAP-identified trends were compared with global PDP-identified trends to indicate that agreement between SHAP and PDP trends confirms that the observed relationships are population-level effects rather than just local artifacts
- PDPs were also unsed to  identify threshold or saturation regions where present and providing an easy visualization/interpretation of descriptor-target relationships
<img width="1126" height="692" alt="11_Partial_dependence_plots_SHAP_selected_features" src="https://github.com/user-attachments/assets/2af73448-e12e-48a3-b9f5-1576faff56d4" />

# Results
-  PDPs show that even on a global scale, the descriptor-target correlation trends observed in SDPs are maintained. The threshold value for each feature are clearly visible on the x-axis of each PDP
- FilterItLogS maintains strong positive monotonic relation with solubility with saturation at extreme end, while the opposite is true for ZMIC1
- Lipinski shows a distinct shift at the threshold (1.0) and a rise in predictions for molecules satisfying the Lipinski criteria
- The RNCG plot shows a sigmoidal curve with threshold at 0.2 and the not so smooth curve indicates complex behavior as seen in SDPs
- PEOE_VSA6 plot shows a negative-monotonic relationship with solubility which is in agreement with the correlation and SDP assessment

# Polynomial regression (Step 17)
- Second- and third-degree polynomial regression models were built using the 5 descriptors to confirm the presence and quantify the extent of nonlinear behavior suggested by the SHAP and PDP analyses
- The performance metrices from linear regression were compared with polynomial metrics to determine whether higher-order terms provide meaningful improvements in predictive performance
<img width="832" height="1045" alt="12_Polynomial_Regression_plots_SHAP_selected_features" src="https://github.com/user-attachments/assets/88da9664-30a1-4948-ba3c-be4581a39e82" />

# Results
- The results from 2nd- and 3rd degree polynomial regression show that the simple monotonic relationships observed in SDPs and PDPs are indeed true as there is hardly any improvement in the predictive performance when the model moves away from linearity
- Only a modest improvement was observed for RNCG (0.04 in predictive performance and 0.03 in MAE), when the model deviated from linearity
- Overall, the results from SHAP, correlation, PDP, and polynomial analyses suggest that aqueous solubility is primarily governed by the additive monotonic effects from 5 chemically interpretable descriptors, with only modest contributions from higher-order nonlinear interactions

# Build chemically interpretable multivariate LR model (Step 18)
- Based on the combined analysis from SHAP, correlation, PDP, and polynomial analyses a final multivariate linear regression was built and a simple easy to use linear equation was provided
- A chemical explanation was provided on how the physicochemical properties encoded by each descriptor govern aqueous solubility
- The final linear equation demonstrated that the model has learnt chemically meaningful relationships and nicely linked the computatinal output to chemical intuition
<img width="953" height="48" alt="13_Final_linear_equation" src="https://github.com/user-attachments/assets/2ab5e03d-ef3d-47b2-825e-b5e9193ad6ae" />

# Results: 
- When compared to the ExtraTrees ML model, the linear model with only 5 descriptors led to a 10% reduction in predictive performance and 27% increase in MAE. On a side note, less than 1 log unit of uncertainty is considered adequate during prescreening drug candidates
- Nonetheless, linear regression gave a chemically interpretable model and an easy to apply linear equation. The positive signs of coefficients for FilterItLogS, Lipinski, and RNCG indicate a positive, monotonic relationship with solubility which is in agreement with the observations from SHAP dependence plots, correlation analysis, partial dependence plots, and polynomial regression analysis. Two features ZMIC1 and PEOE_VSA6 have negative coefficients which correlates with the observations from PDP and correlation matrix indicating a negative, monotonic relationship with solubility
- The model also makes sense in terms of chemical interpretability. Specifically, FilterItLogS is a pre-computed fragment-based descriptor that directly takes solubility into account. Molecules with higher fragment-based solubility will naturally lead to increase in aqueous solubility. ZMIC1 is a feature that encodes for structural complexity which means larger/more branched compounds will have low solubility. Lipinski feature is a criteria used to assess the "Drug'Likeness" of a molecule based on its M.W., lipophilicity, and hydrogen-bonding capabilities. Therefore, if the molecules meet this criteria, they are more Drug-Like. The criteria requires: hydrogen bond donors ≤ 5, hydrogen bond acceptors ≤ 10, the molecules that fall under this criteria have reasonable structure complexity, polarity, and lipophilicity, which would lead to increased aqueous solubility. RNCG (Relative negative charge) is a feature that encodes for charge distribution on a molecule. More charge density on a molecule would lead to increased engagement in more hydrogen-bonding interactions with water, hence higher solubility. PEOE_VSA6 encodes for the total Van der Waals surface area of atoms in a molecule, hence larger size/lipophilic surface area would lead to poor solubility
- Overall, ML helped us identify the most predictive features, while linear regression translated them into an equation a medicinal chemist can apply, critique, and trust.

# Cross-validation and prediction for unseen molecules (Step 19)
- The robustness and reliability of the final LR model was assessed using 10-fold cross-validation to ensure there was no bias in train:test splits while building the model
- The generalizability of the model to previously unseen molecules were demonstrated using an external validation set (which was kept untouched during model development)
<img width="1109" height="823" alt="14_K-fold_Cross_validation" src="https://github.com/user-attachments/assets/9b792669-beef-40a0-9f33-2cfa539c8416" />

<img width="872" height="452" alt="14_K-fold_Cross_validation_summary" src="https://github.com/user-attachments/assets/10e0be5d-4998-4e8e-b73d-1a0c3a01b6ed" />
<img width="746" height="545" alt="15_Prediction_unseen_molecules" src="https://github.com/user-attachments/assets/f76b2657-d744-401b-b857-37f645220e71" />

# Results 
- When the 5-descriptor multivariate LR model was assessed using 10-fold cross-validation, the plots indicate the test R2 = 0.82 ± 0.05 and MAE = 0.66 ± 0.05 which shows that the model is stable and there was no bias in train:test splits while building the model. It also generalizes well to the compounds in test set
- When compared against an external validation set that contained previously unseen molecules, R2 of 0.81 and MAE of 0.66 suggest that the final LR model can be generalized well to unfamiliar compounds and that both interpretability and predictive performance of the model is maintained.
