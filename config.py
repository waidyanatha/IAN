# REPAT - CONFIGURATION
#
# Instructions - Configure the file to enable/disable parameters
#                and determine which functions to execute to 
#                achieve your desired results
#
# contributors: nuwan@lirneasia.net
#
# ------------------------------------------------------------------
#
# import libraries
import sys, os
#
##################################################################################
#
# Parameters for DATA IMPORT
#
##################################################################################
# uncomment the source to retrieve data from; only one at a time and not all
# we have scripts in rio.py to import data for each of the sources
source = "cap.sahana.io"       # available
#
##################################################################################
#
# FILES for storing processed data at various stages
#
# @instructions:
#     you may change the files names but the file extensions must be preserved
#     all data files will be stored in the directory folder: ./data/
#
# @purpose:
#     to be able to start a process at any point in the main.py without to repeat
#     the previous lengthy process by such as data clustering, extraction, etc 
#     User may simply comment the function in main.py MAIN CALLS to skip the step
##################################################################################
#
alerts_file = "10_test_alerts.csv"
#alerts_file = "alerts_from_cap_server.csv"
cleaned_alert_data = "cleaned_alerts.json"
encoded_alert_msg = "encoded_alert_messages.csv"
#
# other temporary files of the data set at various stages of the processing
#
#file_formatted_data = "nepal.txt"
#file_formatted_data = "tmp_formatted_"+ISO_3166_1_APLPHA_2+"_"+source+".txt"

