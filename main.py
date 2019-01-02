# GRAB Analytics - main library to execute 
#
# ------------------------------------------------------------------------------
#
# contributors: nuwan@sahanafoundation.org
#
# ------------------------------------------------------------------------------
#
# import libraries
import sys, os
import numpy as np
import config as conf
import datafilter as dafi
import similarityTF as stf
import plot as plt
import datetime as dt
import log as log
#from sklearn.cluster import KMeans
#from pandas.core.series import Series
import math
import csv
import tensorflow as tf
from tensorflow import keras
#
######################################################################################
#
# INITIALIZE: set auxiliary directories and paths
#
######################################################################################
def initiatlize():
    init_err_cnt = 0
    log.append(init_err_cnt, "system version "+str(sys.version))
    log.append(init_err_cnt, "tesnorflow verion "+str(tf.VERSION))
    log.append(init_err_cnt, "keras version"+str(tf.keras.__version__))
    #
    # plots directory
    dir_path = "../plots/"
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        log.append(0, "directory path does not exists, creating new directory " + str(dir_path))
    # data directory
    dir_path = "../data/"
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        log.append(0, "directory path does not exists, creating new directory " + str(dir_path))
    #
    # check parameters and echo call functionaX
    log.append(0, "initialization done returning error count "+str(init_err_cnt))
    return init_err_cnt, "done"
#
######################################################################################
#
#    MAIN CALLS 
#
######################################################################################
error_count = 0
tstart = dt.datetime.now()
print(str(tstart) + ": begin message text classification with TF and NLP ")
log.append(error_count, "begin message text classification with TF and NLP ")
#
###########################
# Initialize & prerequisits
###########################
if error_count == 0:
    log.append(error_count, "starting process initializing algorithms. ")
    init_err, init_str = initiatlize()
    if init_err > 0:
        error_count += init_err
        log.append(error_count, "initialization failed with error count: " + str(error_count) + " value : " + str(init_str))
    else:
        log.append(error_count, "initializing completed with error count: " + str(error_count) + " value : " + str(init_str))
else:
    print(str(dt.datetime.now()) + ": unknown error with error count: " + str(error_count) + " value : " + str(init_str))
#
###########################
# Load data
###########################
# load data from file defined in config "alerts_file"
if error_count == 0:
    log.append(error_count, "starting tp load the data.")
    error_count, filename = dafi.load_data()
    log.append(error_count, "load data completed with error count: " + str(error_count) + " file name: " + str(filename))
else:
    log.append(error_count, "Skipped function call sentence_encoder() from main.py and in library similarityTF.py. Error count: " + str(error_count) + " > 0.")
#
###########################
# sentence encoding
###########################
if error_count == 0:
    log.append(error_count, "Starting function call sentence_encoder() from main.py and in library plot.py.")
##    error_count += stf.sentence_encoder();
    if error_count > 0:
        log.append(error_count, "Incomplete function call sentence_encoder() from main.py and in library similarityTF.py. Error count: " + str(error_count))
    else:
        log.append(error_count, "Finished function call sentence_encoder() from main.py and in library similarityTF.py. Error count: " + str(error_count))
else:
    log.append(error_count, "Skipped function call sentence_encoder() from main.py and in library similarityTF.py. Error count: " + str(error_count) + " > 0.")
#
#####################################
#3D scatter plot of sentence encoding
#####################################
if error_count == 0:
    log.append(error_count, "Fetching data files from directory.")
    if not os.path.exists("../data/"+conf.encoded_alert_msg):
        error_count +=1
        log.append(error_count, "No file found, ../data/"+conf.encoded_alert_msg+" does not exist!. Error count: " + str(error_count))
    else:
        log.append(error_count, "Found file, ../data/"+conf.encoded_alert_msg+" exist!")
        log.append(error_count, "Starting function call scatter_3D_plot() from main.py and in library plot.py.")
        with open('../data/'+conf.encoded_alert_msg) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
##            plt.scatter_3D_plot(csv_reader, title = "cartesian 3D plot - universal sentence encodings", \
##                    fname="scatter_alert_encoding_3D.png")
        log.append(error_count, "Finished function call scatter_3D_plot() from main.py and in library plot.py.")
else:
    log.append(error_count,"Skipped function call scatter_3D_plot() from main.py and in library plot.py. Error count: " + str(error_count) + " > 0.")
#
#####################################
# semantic textual similarity
#####################################
if error_count == 0:
    log.append(error_count, "Starting function call semantic_textual_similarty () from main.py and in library similarityTF.py.")
    error_count += stf.semantic_textual_similarity();
    if error_count > 0:
        log.append(error_count, "Incomplete function call semantic_textual_similarty () from main.py and in library similarityTF.py. Error count: " + str(error_count))
    else:
        log.append(error_count, "Completed function call semantic_textual_similarty () from main.py and in library similarityTF.py. Error count: " + str(error_count))
else:
    log.append(error_count, "Skipped function call semantic_textual_similarty () from main.py and in library similarityTF.py because of error count: " + str(error_count) + " > 0.")

#####################################
# close program
#####################################
tfinish = dt.datetime.now()
print("Ending with a total time of "+str(tfinish - tstart))
#
if error_count > 0:
    print("ERROR encountered, check the log file: " + str(conf.log_file))
    log.append(error_count, "ERROR encountered, check the log file: " + str(conf.log_file))
else:
    print("SUCCESSFULLY finished the program at " + str(tfinish))
    log.append(error_count, "SUCCESSFULLY finished the program")
#
