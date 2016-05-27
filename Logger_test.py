"""
Logging tester.

Licensed under MIT
Copyright (c) 2015 Brad Brookes <mnp9mm@gmail.com>
"""
import argparse
import sys
#import the logging setup class text_logger:
try:
    from PyLib.Debug.text_logger import *
except ImportError:
    sys.path.extend( ['.', '..'])
from PyLib.Debug.text_logger import *

import Sub2
#----------------------------------------------------------------
def Excp1():
    x = XmlError('This is a test.',6,'Another message')
    raise x

#----------------------------------------------------------------
def Sub1():
    a = 8
    logging.error("Unit one's in trouble and it scared out of its wits!")

#----------------------------------------------------------------
def Test1():
    Sub1()
    #Excp1()

#----------------------------------------------------------------
def Main():
    """ This test main uses argparse to allow setting of the loglevel
    from the command line.
    """
    parser = argparse.ArgumentParser(prog='Logger_test')
    parser.add_argument('--loglevel',  action='store', default='WARNING',     help=argparse.SUPPRESS)
    args = parser.parse_args()
    loglevel = getattr(logging, args.loglevel.upper())
    print 'loglevel=', loglevel
    #-----------------------------------------------------------

    # This the line needed in the main() of any text/command line program.
    logger = TextLogger(loglevel,'LogTester.log')
    log = logger.getLogger()
    #logger = logging.getLogger()   # This works too!
    #log.setLevel('INFO')   # This can only set the level higher than the parent above, never lower!


    sc = Sub2.SomeClass()
    sc.doSomething()
    log.debug('A debug message from Main().L2')
    log.info('An info message from Main().')
    log.warning('A warning from Main().L2')
    log.error('An error msg from Main().')
    log.critical('A critical msg from Main().')
    logging.critical('logging:A critical msg from Main().')
    try:
        #Test1()
        a = 5 / 0
        #a = 5 / 3
    except Exception as e:
        logging.exception('An exception message from Main()')
    #else:
        #pass
        #print 'Try else line in Main()'
    #finally:
    #    print 'Finally in Main()'

Main()

