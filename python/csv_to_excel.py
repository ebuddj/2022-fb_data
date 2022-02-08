#!/usr/bin/python
# -*- coding: UTF8 -*-
# @See http://www.python.org/dev/peps/pep-0263/

#######
# ABOUT
#######

# Convert .csv-file to Excel

########
# AUTHOR
########

# Teemo Tebest (teemo.tebest@gmail.com)

#########
# LICENSE
#########

# CC-BY-SA 4.0 EBU / Teemo Tebest

#######
# USAGE
#######

# python csv_to_excel.py [filename]


# Load sys for reading arguments
import sys

# Remove the script name.
sys.argv.pop(0)

if len(sys.argv) > 0:
  import pandas as pd

  filename = sys.argv[0]

  read_file = pd.read_csv(filename + '.csv')
  read_file.to_excel(filename + '.xlsx', index=None, header=True)

  print('\033[1mOutput in: \033[0m' + filename + '.xlsx')
  
else:
  print('\033[1mEnter at least one search term!\033[0m')
  print('Usage: python csv_to_excel.py [filename]')