"""
Logging tester.

Licensed under MIT
Copyright (c) 2016 Brad Brookes <mnp9mm@gmail.com>
"""
import sys
import logging


logger = logging.getLogger(__name__)
logging.error('Test error output.')



#========================================================================================
#========================================================================================
def main():
#========================================================================================
#========================================================================================
    logger.error("Error - In main()")

#----------------------------------------------------------------------------------------
if __name__ == "__main__":
    sys.exit(main())
#----------------------------------------------------------------------------------------

