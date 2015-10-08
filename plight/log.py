import logging
from logging.handlers import RotatingFileHandler


def start_logging(config):
    app_logger = logging.getLogger('plight')
    app_logger.setLevel(getattr(logging, config['log_level']))
    if app_logger.handlers == []:
        app_logger.addHandler(
            RotatingFileHandler(
                config['log_file'],
                mode='a',
                maxBytes=config['log_filesize'],
                backupCount=config['log_rotation_count']
            )
        )

    web_logger = logging.getLogger('plight_httpd')
    web_logger.setLevel(getattr(logging, config['log_level']))
    if web_logger.handlers == []:
        web_logger.addHandler(
            RotatingFileHandler(
                config['web_log_file'],
                mode='a',
                maxBytes=config['web_log_filesize'],
                backupCount=config['web_log_rotation_count']
            )
        )
