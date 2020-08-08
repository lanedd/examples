import logging

from logging_example2 import diff_file_no_obj, diff_file_yes_obj


def same_file_no_obj():
    logging.debug("This is debug, in a different function, no obj.")
    logging.info("This is info, in a different function, no obj.")
    logging.warning("This is warning, in a different function, no obj.")
    logging.error("This is error, in a different function, no obj.")
    logging.critical("This is critical, in a different function, no obj.")


def same_file_yes_obj(my_logger):
    my_logger.debug("This is debug, in a different function, yes obj.")
    my_logger.info("This is info, in a different function, yes obj.")
    my_logger.warning("This is warning, in a different function, yes obj.")
    my_logger.error("This is error, in a different function, yes obj.")
    my_logger.critical("This is critical, in a different function, yes obj.")


no_obj_logger = True
yes_obj_logger = False

if yes_obj_logger:
    # Setting the default logger that will be used across methods and files (no object passing needed)
    fh_d = logging.FileHandler("pipeline_debug_log_HH_MM_SS_no_obj.log")
    fh_d.setLevel(logging.DEBUG)
    # fh_d.name = "FileHandlerDebug"  # Not needed
    fh_w = logging.FileHandler("pipeline_error_log_HH_MM_SS_no_obj.log")
    fh_w.setLevel(logging.WARNING)
    st = logging.StreamHandler()
    st.setLevel(logging.INFO)
    # st.name = "StreamHandler"  # Not needed
    formatter_fh = logging.Formatter("%(levelname)s - %(asctime)s - %(filename)s - %(funcName)s - \n\t%(message)s")
    formatter_st = logging.Formatter("%(levelname)s - %(asctime)s - %(filename)s - %(funcName)s - \n\t%(message)s", datefmt="%H:%M:%S")
    fh_d.setFormatter(formatter_fh)
    fh_w.setFormatter(formatter_fh)
    st.setFormatter(formatter_st)
    # IMPORTANT: SET THE OBJECT LEVEL AT LOWEST OR IT CAN BLOCK A HANDLER LEVEL!
    logging.basicConfig(level=logging.DEBUG, handlers=[fh_d, fh_w, st])
    logging.debug("This is debug, no object")
    logging.info("This is info, no object")
    logging.warning("This is warning, no object")
    logging.error("This is error, no object")
    logging.critical("This is critical, no object")
    # No need to pass object when calling a function, even in a different .py file.
    same_file_no_obj()
    diff_file_no_obj()

if no_obj_logger:
    # create logger object (gives you more control like ability to set different levels for the handlers
    # but you have to pass object)
    # Create a logger object
    logger = logging.getLogger("pipeline_logger_yes_obj")
    logger.setLevel(logging.DEBUG)  # IMPORTANT: SET THE OBJECT LEVEL AT LOWEST OR IT CAN BLOCK A HANDLER LEVEL!
    # create file handler which logs even debug messages
    fh_d = logging.FileHandler("pipeline_debug_log_HH_MM_SS_yes_obj.log")
    fh_d.setLevel(logging.DEBUG)
    # Create file handler which logs warnings and higher
    fh_w = logging.FileHandler("pipeline_error_log_HH_MM_SS_yes_obj.log")
    fh_w.setLevel(logging.WARNING)
    # create console handler which prints out info and higher.
    st = logging.StreamHandler()
    st.setLevel(logging.INFO)
    # create formatter and add it to the handlers
    formatter_fh = logging.Formatter("%(levelname)s - %(asctime)s - %(filename)s - %(funcName)s - \n\t%(message)s")
    formatter_st = logging.Formatter("%(levelname)s - %(asctime)s - %(filename)s - %(funcName)s - \n\t%(message)s", datefmt="%H:%M:%S")
    fh_d.setFormatter(formatter_fh)
    fh_w.setFormatter(formatter_fh)
    st.setFormatter(formatter_st)
    # add the handlers to the logger
    logger.addHandler(fh_d)
    logger.addHandler(fh_w)
    logger.addHandler(st)
    logger.info("Logging level is linear, if handler level is set to warning then warning, error and critical "
                "are logged while debug and info are ignored")
    logger.info("Setting handle level to debug makes it so all levels are logged (I think).")
    # Demo the different level types of logging messages.
    logger.debug("This is debug, yes object")
    logger.info("This is info, yes object")
    logger.warning("This is warning, yes object")
    logger.error("This is error, yes object")
    logger.critical("This is critical, yes object")
    # Not as sure how log works?  Probably more complicated then its worth?
    logger.log(30, "Not as sure how log works?")

    # Need to pass logging object for logging object
    same_file_yes_obj(logger)
    diff_file_yes_obj(logger)



