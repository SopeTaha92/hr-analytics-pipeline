


from loguru import logger


def logging_file(file : str):
    logger.remove()
    logger.add(
        file,
        rotation="10 MB",
        retention="30 days",
        compression='zip',
        level='INFO',
        format="{time} | {level} | {name}:{line} | {message}"
    )