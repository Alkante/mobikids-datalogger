# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      alkante
#
# Created:     25/09/2015
# Copyright:   (c) alkante 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os.path
from dataFileParser import *
DATA_FILENAME = 'E:/Documents/Olivier/id4car/data/0001_090915_101617.dat'
OUT_BASE = unicode('E:/Documents/Olivier/id4car/data/ééé/0001_090915_101617','utf-8')
def main():

    dataFileParser = DataFileParser(None,"console")
    dataFileParser.convertFile(DATA_FILENAME, OUT_BASE)
    pass

if __name__ == '__main__':
    main()
