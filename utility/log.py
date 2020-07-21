"""
    logging File to access logs
"""
import logging
from datetime import datetime
from django.conf import settings


class log:
    """
        logging File to access logs
    """
    DEBUG_LOGS = True
    BLOCKED_LOG_TAGS = []

    @classmethod
    def exception(cls, e):
        """

        @param e:
        """
        logger = logging.getLogger(settings.GENERAL_LOGGER)
        logger.exception(e)

    @classmethod
    def info(cls, e):
        """

        @param e:
        """
        logger = logging.getLogger(settings.GENERAL_LOGGER)
        logger.info(e)

    @classmethod
    def error(cls, e):
        """

        @param e:
        """
        logger = logging.getLogger(settings.GENERAL_LOGGER)
        logger.error(e)

    @classmethod
    def warning(cls, e):
        """

        @param e:
        """
        logger = logging.getLogger(settings.GENERAL_LOGGER)
        logger.warning(e)

    '''
    @classmethod
    def e(cls, TAG, logText):
        logger = logging.getLogger(settings.GENERAL_LOGGER)
        if TAG not in cls.BLOCKED_LOG_TAGS:
            logger.error('|E| ' + str(datetime.now()) + ' | ' + str(TAG) + '| ' + logText+ '|')
    '''

    @classmethod
    def v(cls, TAG, logText):
        """

        @param TAG:
        @param logText:
        @return:
        """
        return


    @classmethod
    def d(cls, TAG, logText):
        """

        @param TAG:
        @param logText:
        """
        logger = logging.getLogger(settings.GENERAL_LOGGER)
        if TAG not in cls.BLOCKED_LOG_TAGS and cls.DEBUG_LOGS:
            logger.debug('|D| ' + str(datetime.now()) + ' | ' + str(TAG) + '| ' + logText + '|')

    '''
    @classmethod
    def critical(cls, TAG, logText):
        logger = logging.getLogger(settings.GENERAL_LOGGER)
        if TAG not in cls.BLOCKED_LOG_TAGS:
            logger.critical('|C| ' + str(datetime.now()) + ' | ' + str(TAG) + '| ' +  logText+'|')
            '''
