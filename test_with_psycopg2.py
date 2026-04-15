

import pandas as pd
import psycopg2
from config import DB_CONFIG, TABLE_NAME
#file = config.BRUTE_DATA_FILE
#df = pd.read_csv(file)

try:
    conn = psycopg2.connect(**DB_CONFIG)
    print('testing connection !')
    df = pd.read_sql(f"SELECT * FROM {TABLE_NAME};", conn)
    print("✅ Connexion réussie !")
    conn.close()
    print(df.head(10))
except Exception as e:
    print(f"ERREUR : {e}")


"""

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Loguru](https://img.shields.io/badge/Loguru-000000?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![XlsxWriter](https://img.shields.io/badge/XlsxWriter-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)


👥 HR Analytics Pipeline - Big Data Edition (1 000+ lignes)

Ce projet est un pipeline ETL (Extract, Transform, Load) industriel conçu pour traiter des registres RH volumineux. Il transforme des données brutes hétérogènes en un outil d'aide à la décision automatisé pour les Directions des Ressources Humaines.

🏢 Enjeux du Projet

Passer d'un échantillon de 10 lignes à un dataset de 1 000 collaborateurs permet de simuler les besoins d'une grande entreprise ou d'une organisation internationale (type ONG).
L'objectif est de fournir une vision macro (statistiques globales) et micro (détails par employé) de la structure sociale.

🚀 Fonctionnalités Clés

Scalabilité : Traitement fluide de milliers de lignes sans perte de performance.

Nettoyage Avancé : Normalisation des noms, conversion des devises (€), gestion des dates et des formats de bonus.

Enrichissement (Feature Engineering) : Calcul automatique de l'ancienneté, des tranches salariales et des taux de bonus réels.

Résilience : Système d'extraction avec Retry Logic pour garantir la continuité du pipeline.

🛠️ Architecture Modulaire & Centralisée

Le projet suit les meilleures pratiques de développement avec une séparation stricte des responsabilités :

config.py : Unique source de vérité pour les chemins, formats et paramètres métier.

src/extracting.py : Module robuste de récupération des données.

src/cleaning.py : Algorithmes de nettoyage et de typage des données.

src/analysis/ : 5 modules d'analyses distincts pour une clarté maximale.

📊 Tableau de Bord Excel Automatisé

Le pipeline génère un rapport .xlsx multi-onglets incluant :

Répartition par Département : Analyse des effectifs (Pie Charts).

Structure Salariale : Comparaison des revenus par grade et expérience (Bar/Line Charts).

Analyse Géographique : Répartition des employés par ville (Sénégal/International).

Performance & Bonus : Corrélation entre notation et rémunération variable.

## 📸 Aperçu du rapport généré

![Rapport Excel](images/output_excel/brutes.png)
![Rapport Excel](images/output_excel/clean_complet.png)
![Rapport Excel](images/output_excel/departement.png)
![Rapport Excel](images/output_excel/top_salaire_dep.png)


📂 Structure du Dépôt
├── images/           ← Nouveau dossier
│   ├── output_excel/ 4 images du rapport
│   └── architecture/ une image du diagramme d'architecture
├── src/
│   ├── analysis/        # 🔍 5 axes d'analyses métiers
│   ├── adding_features.py # ✨ Création de nouveaux indicateurs
│   ├── cleaning.py      # 🧹 Nettoyage et normalisation
│   ├── excel_generator.py # 📊 Moteur de rendu XlsxWriter (Graphiques)
│   └── extracting.py    # 📥 Extraction résiliente (Retry logic)
├── Output_excel/        # 📂 Rapports générés (Ignorés par Git via .gitignore)
├── config.py            # ⚙️ Configuration centralisée (Paths, Logs)
├── main.py              # 🚀 Chef d'orchestre du pipeline
├── requirements.txt     # 📋 Liste des dépendances (Pandas, XlsxWriter, Loguru)
└── README.md            # 📖 Documentation professionnelle

![Diagramme d'Architecture](images/architecture/Gemini_Generated_Image_vgzdw0vgzdw0vgzd.png)



📈 Prochaines Étapes

[ ] SQL Integration : Migration du stockage CSV vers PostgreSQL.

[ ] Dashboard Interactif : Connexion des sorties vers Power BI ou Streamlit.

[ ] Data SIG : Cartographie des effectifs pour le secteur humanitaire.

💻 Installation & Lancement
Bash

# 1. Cloner le dépôt
git clone https://github.com/SopeTaha92/hr-analytics-pipeline.git

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Exécuter le pipeline
python main.py


Développé par Mahmoud Saleh At-Tidiane - Data Engineer en devenir, spécialisé dans l'automatisation et l'analyse décisionnelle.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Loguru](https://img.shields.io/badge/Loguru-000000?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![XlsxWriter](https://img.shields.io/badge/XlsxWriter-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![psycopg2](https://img.shields.io/badge/psycopg2-336791?style=for-the-badge&logo=postgresql&logoColor=white)

# 📊 Pipeline d'Analyse RH (HR Analytics)

Ce projet implémente un pipeline **ETL (Extract, Transform, Load)** robuste et modulaire pour l'analyse des ressources humaines. Il permet de transformer des données brutes RH (employés, présences, salaires) en un rapport Excel décisionnel avec une gestion centralisée des paramètres.

**Fonctionnalité clé** : Extraction des données depuis **PostgreSQL** (via `psycopg2`) avec mécanisme de retry, nettoyage avancé, enrichissement des données (calcul du turnover, taux d'absentéisme, etc.) et génération automatisée de rapports Excel professionnels.

---

## 🌟 Points Forts du Projet

| Fonctionnalité               | Description                                                                    |
|------------------------------|--------------------------------------------------------------------------------|
| **Connectivité PostgreSQL**  | Extraction robuste avec `psycopg2` et fallback CSV                             |
| **Configuration Centralisée**| Gestion des chemins, paramètres métiers et connexion DB via `config.py`        |
| **Robustesse (Retry Logic)** | Système d'extraction avec tentatives multiples et délai exponentiel            |
| **Architecture Modulaire**   | Séparation claire : extraction → nettoyage → calculs → analyses → reporting    |
| **Métriques RH avancées**    | Calcul du turnover, taux d'absentéisme, ancienneté moyenne, etc.               |
| **Visualisation Avancée**    | Tableaux de bord Excel automatisés avec formatage conditionnel                 |

---

## 🛠️ Architecture du Code
├── config.py # ⚙️ Centre de contrôle (Chemins, Formats, Seuils, DB_CONFIG)
├── main.py # 🚀 Point d'entrée du pipeline
├── src/
│ ├── extract.py # 📥 Extraction depuis PostgreSQL (psycopg2 + retry)
│ ├── clean.py # 🧹 Nettoyage et typage (Pandas)
│ ├── features.py # 📈 Calcul d'indicateurs RH (turnover, absentéisme)
│ ├── analysis/ # 🔍 Analyses spécifiques (présences, salaires, départements)
│ ├── logger.py # 📝 Gestionnaire de logs (Loguru)
│ └── repport_excel.py # 📊 Moteur de rendu XlsxWriter
├── data/ # 💾 Dossier des sources (CSV - optionnel)
├── logs/ # 📜 Historique d'exécution
└── output/ # 📂 Rapports générés


---

## ⚙️ Configuration Centralisée (`config.py`)

```python
# Chemins
BRUTE_DATA_DIR = Path('data/raw')
BRUTE_DATA_FILE = BRUTE_DATA_DIR / "hr_data.csv"

# PostgreSQL
DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'dbname': 'hr_db',
    'user': 'sope',
    'password': 'azerty12'
}
TABLE_NAME = 'rh_table'

# Paramètres de retry
MAX_RETRIES = 3
DELAY = 1

📊 Reporting Automatisé

Le rapport Excel généré contient plusieurs onglets stratégiques :

Onglet	                                 Contenu
Données Brutes	            Données extraites de PostgreSQL (avant nettoyage)
Données Nettoyées	        Données après typage et correction
Présences	                Analyse des présences par employé et par mois
Turnover	                Taux de rotation du personnel par département
Salaires	                Distribution des salaires, écarts, moyennes

🐛 Difficultés rencontrées et solutions

2. Gestion des dates de contrat

Défi : Calculer l'ancienneté et le turnover à partir de dates d'embauche et de départ.

Solution : Utilisation de pd.to_datetime() et calcul de différence en jours/mois.

🔧 Dépendances principales
Bibliothèque	    Version	        Utilité
psycopg2-binary	    2.9.11	    Connexion PostgreSQL
pandas	            2.0.3	    Manipulation et nettoyage
loguru	            0.7.3	    Logging structuré
xlsxwriter	        3.2.9	    Génération de rapports Excel

🚀 Installation & Lancement
bash
# 1. Cloner le dépôt
git clone https://github.com/SopeTaha92/hr-analytics-pipeline.git
cd hr-analytics-pipeline

# 2. Créer l'environnement virtuel
python -m venv venv
venv\Scripts\activate     # Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Configurer PostgreSQL
#    - Créer une base 'hr_db'
#    - Importer les données dans une table 'employes'

# 5. Exécuter le pipeline
python main.py

📈 Évolutions futures
Ajout d'index sur les colonnes employe_id et date_embauche

Dashboard Power BI connecté à PostgreSQL

Prédiction du turnover avec un modèle simple (scikit-learn)

Tests unitaires avec pytest

👨‍💻 Auteur
Mahmoud At-Tidiane - Passionné par l'ingénierie des données, l'analyse décisionnelle et l'intégration PostgreSQL.

GitHub : @SopeTaha92

Projet : hr-analytics-pipeline

📝 License
Ce projet est open source et disponible sous la licence MIT.

text

---

## ✅ Ce que j'ai amélioré

| Section           | Changement                                     |
|-------------------|------------------------------------------------|
| **Badges**        | Ajout des badges PostgreSQL, psycopg2          |
| **Description**   | Adaptée au domaine RH                          |
| **Points Forts**  | Ajout des métriques RH (turnover, absentéisme) |
| **Architecture**  | Clarifiée                                      |
| **Configuration** | Exemple concret                                |
| **Reporting**     | Onglets adaptés aux RH                         |
| **Difficultés**   | Problèmes spécifiques RH                       |
| **Évolutions**    | Ajout d'une idée de prédiction ML              |

---

## 📝 Ce que tu dois adapter

| Point                 | Action                                                             |
|-----------------------|--------------------------------------------------------------------|
| **Noms des colonnes** | Remplace par les vraies colonnes de ton CSV RH                     |
| **Métriques**         | Si tu as d'autres indicateurs (ex: notes d'évaluation), ajoute-les |
| **Capture d'écran**   | Ajoute une image du rapport Excel généré                           |

---


"""