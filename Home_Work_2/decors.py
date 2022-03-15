"""Декораторы"""

import sys
import logging
import logs.server_log_config
import logs.client_log_config
import datetime

if sys.argv[0].find('client') == -1:
    LOGGER = logging.getLogger('server')
else:
    LOGGER = logging.getLogger('client')


def log(func_to_log):
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def log_saver(*args, **kwargs):
        ret = func_to_log(*args, **kwargs)
        LOGGER.debug(f'{date}. Была вызвана функция {func_to_log.__name__} c параметрами {args}, {kwargs}. '
                     f'Вызов из модуля {func_to_log.__module__}')
        return ret
    return log_saver
