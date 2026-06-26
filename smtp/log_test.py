import logging

logger = logging.getLogger(__name__)

logging.basicConfig(
    filename = 'log_info.log',
    filemode = 'a',
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s' ,
    datefmt = '%Y-%m-%d %H:%M:%S' ,
    level = logging.DEBUG
)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',)

ch.setFormatter(formatter)

logger.addHandler(ch)


logger = logging.getlogger('simpleExample')


logger.debug('This message should go to the log file')
logger.info('So should this')
logger.warning('And this, too')
logger.error('And non-ASCII stuff, too, like Øresund and Malmö')

