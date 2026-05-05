import pandas as pd
import numpy as np

# 1. Identifier les colonnes à modifier
# On prend 'loan_status' comme référence et on choisit 11 autres colonnes
target_col = 'loan_status'
cols_to_miss = [c for c in df.columns if c != target_col][:11]

# 2. Injecter les valeurs manquantes directement dans le DataFrame original
for col in cols_to_miss:
    # Pourcentage aléatoire entre 5% et 15%
    missing_percentage = np.random.uniform(0.05, 0.15)
    
    # Création du masque sur la longueur totale du DataFrame
    mask = np.random.rand(len(df)) < missing_percentage
    
    # Application des NaN uniquement sur ces colonnes
    df.loc[mask, col] = np.nan

# 3. Vérification pour les colonnes concernées
print("Pourcentage de valeurs manquantes par colonne :")
print(df[cols_to_miss].isnull().mean() * 100)