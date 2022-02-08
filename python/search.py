#!/usr/bin/python
# -*- coding: UTF8 -*-
# @See http://www.python.org/dev/peps/pep-0263/

#######
# ABOUT
#######

# Make keyword searches from .csv-file

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

# python search.py [terms]

#################
# DEFINE THINGS #
#################

# Load the Pandas libraries with alias 'pd'
import pandas as pd
import pandas.io.common
from dotenv import load_dotenv
import os
load_dotenv()

FILENAME = os.getenv('FILENAME')

# Load sys for reading arguments
import sys

# Remove the script name.
sys.argv.pop(0)

if len(sys.argv) > 0:
  with open('./result.csv', 'a', newline ='') as file:
    words = sys.argv
    print('\033[1mSearch terms:\033[0m ', str(words))

    # Import libraries.
    import csv
    import re

    # Create the csv writer.
    writer = csv.writer(file, delimiter=',')

    # Check if file exists and if not add a header.
    if os.stat('./result.csv').st_size == 0:
      header = ['search_terms', 'document_name', 'page', 'raw_text']
      writer.writerow(column for column in header)

    # If we haven't yet collected data for this search.
    try:
      df_existing = pd.read_csv('./result.csv')
      if (len(df_existing[df_existing['search_terms'].str.contains(', '.join(words), flags=re.IGNORECASE, regex=True, na=False)])) == 0:
        df = pd.read_csv('../data/' + FILENAME)
        base = r'{}'
        expr = '(?=.*{}.*)'
        search_term_regexp = base.format(''.join(expr.format(w) for w in words))
        # print(search_term_regexp)
        result = df['raw_text'].str.contains(search_term_regexp, flags=re.IGNORECASE, regex=True, na=False)
        print('\033[1mDocuments count: \033[0m' + str(len(df[result])))

        for index, row in df[result].iterrows():
          writer.writerow([', '.join(words), row['document_name'], row['page'], row['raw_text']])
      else:
        print('\033[1mAlready included!\033[0m')
    except pd.errors.EmptyDataError:
      print('\033[1mOnly initialized the output file, run the script again!\033[0m')

else:
  print('\033[1mEnter at least one search term!\033[0m')
  print('Usage: python search.py [terms]')

print('')