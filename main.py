import pandas as pd
import logging
from datetime import datetime
import sys
import get_devices as gd

pd.set_option('display.max_columns', None)


def initialize_logger():
    logger = logging.getLogger()
    logging.basicConfig(level=logging.INFO,
                        filename=f'2w-devices_{datetime.now().strftime("%Y-%m-%d_%H%M%S")}.log',
                        filemode='a')
    console = logging.StreamHandler(sys.stdout)
    console.setLevel(logging.INFO)
    logger.addHandler(console)

    return logger


def main():
    logger = initialize_logger()
    logger.info('Starting device discovery process...')
    devices_df = gd.create_dataframe(logger)


main()
