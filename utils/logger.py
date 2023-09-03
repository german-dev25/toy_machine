import logging
import datetime


def setup_logger():
    log_format = '%(message)s'
    log_file_name = f'log_{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.txt'

    logging.basicConfig(filename=log_file_name, level=logging.INFO,
                        format=log_format)


if __name__ == "__main__":
    setup_logger()
