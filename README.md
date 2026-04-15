![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Loguru](https://img.shields.io/badge/Loguru-000000?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![XlsxWriter](https://img.shields.io/badge/XlsxWriter-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![psycopg2](https://img.shields.io/badge/psycopg2-336791?style=for-the-badge&logo=postgresql&logoColor=white)

# 👥 HR Analytics Pipeline - Big Data Edition (1 000+ lignes)

Ce projet implémente un pipeline **ETL (Extract, Transform, Load)** robuste et modulaire pour l'analyse des ressources humaines. Il transforme des données brutes hétérogènes (employés, présences, salaires) en un outil d'aide à la décision automatisé pour les Directions des Ressources Humaines.

**Fonctionnalité clé** : Extraction des données depuis **PostgreSQL** (via `psycopg2`) avec mécanisme de retry, nettoyage avancé, enrichissement des données (calcul du turnover, taux d'absentéisme, ancienneté) et génération automatisée de rapports Excel professionnels.

---

## 🏢 Enjeux du Projet

Passer d'un échantillon de 10 lignes à un dataset de **1 000 collaborateurs** permet de simuler les besoins d'une grande entreprise ou d'une organisation internationale (type ONG). L'objectif est de fournir une vision macro (statistiques globales) et micro (détails par employé) de la structure sociale.

---

## 🌟 Points Forts du Projet

| Fonctionnalité                           | Description                                                                                   |
|------------------------------------------|-----------------------------------------------------------------------------------------------|
| **Connectivité PostgreSQL**              | Extraction robuste avec `psycopg2` et mécanisme de retry                                      |
| **Scalabilité**                          | Traitement fluide de milliers de lignes sans perte de performance                             |
| **Configuration Centralisée**            | Gestion des chemins, paramètres métiers et connexion DB via `config.py`                       |
| **Architecture Modulaire**               | Séparation claire : extraction → nettoyage → calculs → analyses → reporting                   |
| **Nettoyage Avancé**                     | Normalisation des noms, conversion des devises (€), gestion des dates et des formats de bonus |
| **Enrichissement (Feature Engineering)** | Calcul automatique de l'ancienneté, des tranches salariales et des taux de bonus réels        |
| **Métriques RH avancées**                | Calcul du turnover, taux d'absentéisme, ancienneté moyenne, etc.                              |
| **Visualisation Avancée**                | Tableaux de bord Excel automatisés avec formatage conditionnel                                |

---

## 🛠️ Architecture Modulaire & Centralisée

Le projet suit les meilleures pratiques de développement avec une séparation stricte des responsabilités :
├── images/ # 📸 Captures d'écran du rapport et diagramme
│ ├── output_excel/ # 4 images du rapport généré
│ └── architecture/ # Diagramme d'architecture
├── src/
│ ├── analysis/ # 🔍 5 axes d'analyses métiers
│ ├── adding_features.py # ✨ Création de nouveaux indicateurs
│ ├── cleaning.py # 🧹 Nettoyage et normalisation
│ ├── excel_generator.py # 📊 Moteur de rendu XlsxWriter (Graphiques)
│ └── extracting.py # 📥 Extraction résiliente (Retry logic)
├── Output_excel/ # 📂 Rapports générés (Ignorés par Git)
├── config.py # ⚙️ Configuration centralisée (Paths, Logs, DB)
├── main.py # 🚀 Chef d'orchestre du pipeline
├── requirements.txt # 📋 Liste des dépendances
└── README.md # 📖 Documentation professionnelle


---

## ⚙️ Configuration Centralisée (`config.py`)

```python
# Chemins
BRUTE_DATA_DIR = Path('data/raw')
BRUTE_DATA_FILE = BRUTE_DATA_DIR / "hr_data.csv"

# PostgreSQL (optionnel - à activer)
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

📊 Tableau de Bord Excel Automatisé
Le pipeline génère un rapport .xlsx multi-onglets incluant :

Onglet	                                    Contenu
Données Brutes	                Données extraites de PostgreSQL (avant nettoyage)
Données Nettoyées	            Données après typage et correction
Présences	                    Analyse des présences par employé et par mois
Turnover	                    Taux de rotation du personnel par département
Salaires	                    Distribution des salaires, écarts, moyennes
Top Salaire par Département	    Classement des plus hauts salaires

📸 Aperçu du rapport généré 
![Rapport Excel](images/output_excel/brutes.png)
![Rapport Excel](images/output_excel/clean_complet.png)
![Rapport Excel](images/output_excel/departement.png)
![Rapport Excel](images/output_excel/top_salaire_dep.png)

🏗️ Diagramme d'Architecture
![Rapport Excel](images/architecture/Gemini_Generated_Image_vgzdw0vgzdw0vgzd.png)

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
# source venv/bin/activate  # Linux/Mac

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Configurer PostgreSQL (optionnel - pour utiliser la base de données)
#    - Créer une base 'hr_db'
#    - Importer les données dans une table 'rh_table'
#    - Adapter DB_CONFIG dans config.py

# 5. Exécuter le pipeline
python main.py


📈 Prochaines Étapes

Nettoyage avancé et enrichissement des données

Dashboard Interactif : Connexion des sorties vers Power BI ou Streamlit

Index et optimisation : Ajout d'index sur employe_id et date_embauche

Prédiction du turnover : Modèle simple avec scikit-learn

Tests unitaires : Mise en place de pytest

🔗 Autres projets

Pipeline E-commerce - Intégration PostgreSQL complète avec double connectivité (psycopg2 + pg8000)

📝 License
Ce projet est open source et disponible sous la licence MIT.

👨‍💻 Auteur

Mahmoud At-Tidiane - Passionné par l'ingénierie des données, l'analyse décisionnelle et l'intégration PostgreSQL.

GitHub : @SopeTaha92

Projet : hr-analytics-pipeline



