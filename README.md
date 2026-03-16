👥 HR Analytics Pipeline - Gestion du Personnel

Ce projet est un pipeline de traitement de données RH conçu pour transformer des registres bruts d'employés en tableaux de bord analytiques. Il permet de suivre des indicateurs clés (KPI) comme la répartition par département, l'ancienneté, et les structures salariales.

🏢 Pourquoi ce projet ?

Dans le cadre de ma montée en compétence en Data Engineering, ce projet simule la gestion de données sensibles et stratégiques. L'objectif est de fournir aux départements RH une vision claire de la masse salariale et de la démographie de l'entreprise.

🛠️ Organisation & Centralisation

Le projet utilise une architecture modulaire pour une maintenance facilitée :

config.py : Centralisation des variables globales (chemins d'accès, paramètres de logging).

main.py : Orchestrateur principal qui appelle les modules de nettoyage et d'analyse.

Logging Professionnel : Utilisation de Loguru pour un suivi précis de chaque étape du pipeline.

📊 Analyses & Visualisations

Le rapport final généré automatiquement inclut :

Répartition par Département : Analyse des effectifs via graphiques en secteurs.

Analyse Salariale : Comparaison des revenus par grade et ancienneté.

Indicateurs de Performance : Suivi des statuts des employés (Actif, Congé, etc.).

📂 Structure du Dépôt

├── src/
│   ├── analysis/           # 5 analyses complètes
│   ├── __init__.py
│   ├── adding_features.py  # Enrichissement des données
│   ├── cleaning.py         # Nettoyage robuste
│   ├── excel_generator.py   # Génération Excel avec graphiques
│   └── extracting.py       # Extraction avec retry
├── Output_excel/           # Rapports générés
├── config.py               # Configuration centralisée
├── main.py                 # Orchestration parfaite
├── requirements.txt        # Dépendances complètes
└── README.md               # Documentation pro

Perspectives : Ce projet sera prochainement migré vers une architecture PostgreSQL pour permettre des requêtes SQL complexes sur les historiques de carrière.

🚀 Installation & Lancement

Bash

# 1. Cloner
git clone https://github.com/SopeTaha92/Projet_vente_e-commerce.git

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Exécuter
python main.py

Développé par Mahmoud At-Tidiane - Passionné par l'ingénierie des données et l'analyse décisionnelle.