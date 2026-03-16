


from loguru import logger


def logging_file(file : str):
    """Cette fonction se charge de génération des fichiers de logs"""
    logger.info('Fichier de logs crée avec succée début du traitement du pipeline')
    logger.remove()
    logger.add(
        file,
        rotation="10 MB",
        retention="30 days",
        compression='zip',
        level='INFO',
        format="{time} | {level} | {name}:{line} | {message}"
    )