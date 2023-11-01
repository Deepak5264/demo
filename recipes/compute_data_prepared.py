# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
#import time

# Read recipe inputs
data1 = dataiku.Dataset("data1")
data1_df = data1.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

data_prepared_df = data1_df # For this sample code, simply copy input to output
#data_prepared_df['newtime'] = data_prepared_df['timestamp'].strftime('%Y-%m-%d %H:%M')
#time.sleep(10)

# Write recipe outputs
data_prepared = dataiku.Dataset("data_prepared")
data_prepared.write_with_schema(data_prepared_df)
