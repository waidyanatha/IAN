# GRAB Analytics - CONFIGURATION
#
# Instructions - file allows for setting parameters values for controlling the
#                   input and output
#
# contributors: nuwan@sahanafoundation.org
#
# ------------------------------------------------------------------
#
# import libraries
import sys, os
#
#dsource = "cap.sahana.io"       # available
# TF HUB @param ["https://tfhub.dev/google/universal-sentence-encoder/2", 
#   "https://tfhub.dev/google/universal-sentence-encoder-large/3"]
# recommended for cloud instances
tf_hub_module_url = "https://tfhub.dev/google/universal-sentence-encoder/2"
# recommended for localhost
##tf_hub_module_url = "./tfhub/"
#
##################################################################################
#
# FILES for storing processed data at various stages
# @instructions:
#     you may change the files names but the file extensions must be preserved
#     all data files will be stored in the directory folder: ./data/
#
##################################################################################
#
alerts_file = "100_test_alerts.csv"
##alerts_file = "alerts_from_cap_server.csv"
cleaned_alert_data = "100_cleaned_alerts.json"
##cleaned_alert_data = "cleaned_alerts.json"
encoded_alert_msg = "100_encoded_alert_messages.csv"
##encoded_alert_msg = "encoded_alert_messages.csv"
#
# Log file name can be specified
log_file = "grab.log"
#
