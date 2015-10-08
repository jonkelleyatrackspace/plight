import logging
from logging.handlers import RotatingFileHandler
import plight.config as plconfig

CONFIG = plconfig.get_config()

app_logger = logging.getLogger('plight')
app_logger.setLevel(getattr(logging, CONFIG['log_level']))
if app_logger.handlers == []:
    app_logger.addHandler(
        RotatingFileHandler(
            CONFIG['log_file'],
            mode='a',
            maxBytes=CONFIG['log_filesize'],
            backupCount=CONFIG['log_rotation_count']
        )
    )

web_logger = logging.getLogger('plight_httpd')
web_logger.setLevel(getattr(logging, CONFIG['log_level']))
if web_logger.handlers == []:
    web_logger.addHandler(
        RotatingFileHandler(
            CONFIG['web_log_file'],
            mode='a',
            maxBytes=CONFIG['web_log_filesize'],
            backupCount=CONFIG['web_log_rotation_count']
        )
    )
