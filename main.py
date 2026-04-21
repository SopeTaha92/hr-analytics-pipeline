



from config import LOG_FILE,  BRUTE_DATA_CLEAN_FILE, EXCEL_FILE,  TOP_SALAIRE_DEPARTEMENT

from src import logging_file
from src import extracting_data, cleaning_data, add_features, repporting_excel
from src import analysis_by_department, analysis_by_level, analysis_by_anciennete, analysis_by_performance_rating, analysis_by_top_salaries_par_departement


logging_file(LOG_FILE)
brute_data = extracting_data()
clean_data = cleaning_data(brute_data, BRUTE_DATA_CLEAN_FILE)
complet_data = add_features(clean_data)
analyse_departement = analysis_by_department(complet_data)
analyse_level = analysis_by_level(complet_data)
analyse_anciennete = analysis_by_anciennete(complet_data)
analyse_perf_rating = analysis_by_performance_rating(complet_data)
analyse_top_sal_dep = analysis_by_top_salaries_par_departement(complet_data, TOP_SALAIRE_DEPARTEMENT)



onglets = {
    'Données Brutes' : brute_data,
    'Données Néttoyées au Complet' : complet_data,
    'Données Par Département' : analyse_departement,
    'Données Par Level' : analyse_level,
    'Données Par ancienneté' : analyse_anciennete,
    'Données Par performance_rating' : analyse_perf_rating,
    'Données Top_Salaire_Département' : analyse_top_sal_dep
}


repporting_excel(EXCEL_FILE, onglets)









