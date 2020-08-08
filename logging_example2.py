import logging


def diff_file_no_obj():
    logging.debug("This is debug, in a different function and file, no obj.")
    logging.info("This is info, in a different function and file, no obj.")
    logging.warning("This is warning, in a different function and file, no obj.")
    logging.error("This is error, in a different function and file, no obj.")
    logging.critical("This is critical, in a different function and file, no obj.")


def diff_file_yes_obj(my_logger):
    my_logger.debug("This is debug, in a different function and file, yes obj.")
    my_logger.info("This is info, in a different function and file, yes obj.")
    my_logger.warning("This is warning, in a different function and file, yes obj.")
    my_logger.error("This is error, in a different function and file, yes obj.")
    my_logger.critical("This is critical, in a different function and file, yes obj.")
