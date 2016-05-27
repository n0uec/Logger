"""
Logging tester.

Licensed under MIT
Copyright (c) 2015 Brad Brookes <mnp9mm@gmail.com>
"""
import logging
log = logging.getLogger()

class SomeClass(object):
    #----------------------------------------------------------------
    def __init__(self):
        """
        """
        self.value = 24

    #----------------------------------------------------------------
    def doSomething(self):
        """
        """
        #log.setLevel(logging.INFO)
        if log.isEnabledFor(logging.DEBUG): # if message of this level would be processed...
            log.debug('Used for an expensive to compute message.')
        #if logger.isEnabledFor(logging.WARNING):
        #    logger.warning('Used for an expensive to compute message.')
        log.info('Asked to do something...')
        log.warning('We did something wrong!')
        log.error('We did something that should be punished!')

