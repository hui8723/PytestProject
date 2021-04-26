import pytest
import logging

def test_log():
    logging.info("info")
    logging.debug("debug")
    logging.error("error")
    logging.critical("critical")
    logging.warning("warning")