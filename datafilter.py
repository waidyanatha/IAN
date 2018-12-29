# GRAB - IO (Input Output) 
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
import datetime as dt
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
#
def load_data():
    error = 0
    print(str(dt.datetime.now()) + ": looking for data files.")
    if not os.path.exists("../data/"+str(conf.alerts_file)):
        error += 1
        print(str(dt.datetime.now()) + " ../data/"+conf.alerts_file+" does not exist. error count: " + str(error))
    else:
        print(str(dt.datetime.now()) + " loading data from: ../data/"+conf.alerts_file)
 
        with open("../data/"+str(conf.alerts_file)) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            alert_list = []
            text_file = open("../data/"+conf.cleaned_alert_data, "w")
            for row in csv_reader:
                #skip the header
                if line_count == 0:
                    print row
                    print (str(dt.datetime.now()) + " number of attributes: "+str(len(row)))
                else:
                    tmp_str = row[0]+" "+row[1]+" "+row[2]+" "+row[3]+" "+row[4]+" "+row[5]+" "+row[6]+" "+row[7]+" "
                    tmp_str += " "+row[8]+" "+row[9]+" "+row[10]+" "+row[11]+" "+row[12]+" "+row[13]+" "+row[14]+" "+row[15]+" "
                    alert_list[line_count:0] = tmp_str
                    text_file.write('"%s"\n' % tmp_str)
                line_count += 1
    
            print(str(dt.datetime.now()) + " Processed " + str(line_count)+" rows from "+str(conf.source)+" (1 header row and "+str(line_count-1)+" data rows).")
            text_file.close()
            print(str(dt.datetime.now()) + " finished writing alert data to a file ../data/"+conf.cleaned_alert_data)
    return error, conf.cleaned_alert_data
