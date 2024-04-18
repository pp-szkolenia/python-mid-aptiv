import logging


logger = logging.getLogger("my_loger")

logger_1 = logging.getLogger("logger1")
logger_2 = logging.getLogger("logger2")

file_handler = logging.FileHandler("logs/logfile.log", mode="w")
stream_handler = logging.StreamHandler()

formatter = logging.Formatter("%(asctime)s - %(pathname)s - %(name)s - %(levelname)s - %(message)s",
                              datefmt="%H:%M:%S")
file_handler.setFormatter(formatter)


logger_1.addHandler(file_handler)
logger_2.addHandler(file_handler)
logger_1.addHandler(stream_handler)
logger_2.addHandler(stream_handler)

logger_1.setLevel(logging.INFO)


def divide(x, y):
    if y == 0:
        logger_2.error("Division by 0! None returned")
        return None

    return x / y


x = 1
logger_1.info("x created")

y = 0
logger_1.info("y created")

z = divide(x, y)
logger_1.info(f"z value: {z}")

# logger_1.debug("Informacja typu debug")
# logger_1.info("Informacja typu info")
# logger_1.warning("Informacja typu warning")
# logger_1.error("Informacja typu error")
# logger_1.critical("Informacja typu critical")
