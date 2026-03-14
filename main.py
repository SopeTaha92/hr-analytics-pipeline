



from config import LOG_FILE, BRUTE_DATA_FILE, BRUTE_DATA_CLEAN_FILE, EXCEL_FILE, MAX_RETRIES, DELAY

from src import logging_file
from src import extracting_data, cleaning_data, add_features, repporting_excel
from src import analysis_by_department


logging_file(LOG_FILE)
brute_data = extracting_data(BRUTE_DATA_FILE, MAX_RETRIES, DELAY)
clean_data = cleaning_data(brute_data, BRUTE_DATA_CLEAN_FILE)
complet_data = add_features(clean_data)
analyse_departement = analysis_by_department(complet_data)




print(f"\n{brute_data}")
print(f"\n{complet_data}")

onglets = {
    'Données Brutes' : brute_data,
    'Données Néttoyées au Complet' : complet_data,
    'Données Salaires Par Catégories' : analyse_departement
}


repporting_excel(EXCEL_FILE, onglets)









