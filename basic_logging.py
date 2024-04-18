import logging


# print(logging.getLevelName(10))
# print(logging.getLevelName(20))
# print(logging.getLevelName(30))
# print(logging.getLevelName(40))
# print(logging.getLevelName(50))

# print(logging.getLevelName(
#     logging.getLogger().getEffectiveLevel())
# )

# logging.debug("Informacja typu debug")
# logging.info("Informacja typu info")
# logging.warning("Informacja typu warning")
# logging.error("Informacja typu error")
# logging.critical("Informacja typu critical")

# print("hello")

logging.basicConfig(level=logging.DEBUG,
                    format="%(levelname)s - %(asctime)s - %(name)s - %(message)s",
                    datefmt="%H:%M:%S",
                    filename="logfile.log", filemode="w")

x = 4
logging.debug(f"x value: {x}")

my_list = [1, 2, 3]

logging.info("list created")

if len(my_list) < 4:
    logging.warning(f"Length of the list: {len(my_list)}")

