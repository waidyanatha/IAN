# REPAT - IO (Input Output) 
#
# Instructions: 
#     - edit values for the settings in config.py
#     - import (include) this library in main
#
# Reporting Patterns (RePat) for determining telecom availability during crises
# ------------------------------------------------------------------------------
#
# purpose of this code is to import and from varoius data sources and then
# output them as a file or stream in the desired formats
#
# contributors: nuwan@lirneasia.net and ilihdian@gmail.com
#
# ------------------------------------------------------------------
#
# import libraries
import sys, os, csv
#import pyquery
import pandas as pd
import config as conf
#
# Define a function to remove all symbol characters and replace with a space 
def remove_symbol(str):
    for char in str.punctuation:
        str=str.replace(char,' ')
    return str

# Define a function to remove all symbol characters without replacement
def remove_symbol_nospace(str):
    for char in str.punctuation:
        str=str.replace(char,'')
    return str
#
# cleanup the alerts for processing
def cleanup_alerts(file="../data/"+conf.alerts_file):
    #
    error = 0
    if file.startswith("../data/"):
        file = "../data/"+file
    if not os.path.exists(file):
        print("Cannot find raw data in director ../data/ with name: "+file)
        error += 1
    else:
        # Import csv as pandas object
        dfalerts = pd.read_csv(file,delimiter=',',encoding="ISO-8859-1")
        # not empty then loop through to structure the data
        cols= ['UUID','alert_id','senderName','headline','sent','status','msgType', \
        'info_id','language','category','event','respType','urgency','severity','certainty','effective','onset','expires' \
        'area_id', 'areaDesc']
        clean_df = pd.DataFrame(columns=cols)

    # Print column headers
    return error, clean_df

