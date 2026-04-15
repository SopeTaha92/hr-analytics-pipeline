
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
