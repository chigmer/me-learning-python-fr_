import logging
import sys

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout   # force output to stdout instead of stderr
)

logging.debug("debug hey")
logging.info("info hey")
logging.warning("warning hey")
logging.error("error hey")
logging.critical("critical hey")