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
import classify as clfy
import plot as plt
import datetime as dt
import log as log
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
    from tensorflow.python.client import device_lib
    print device_lib.list_local_devices()
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
#######################################################
# Initialize & prerequisits
#######################################################
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
#######################################################
# Load data from source(s)
#######################################################
# load data from file defined in config "alerts_file"
if error_count == 0:
    log.append(error_count, "Starting function call load_data_from_source() from main.py.")
    load_error, filename = dafi.load_data_from_source()
    if load_error > 0 or not filename :
        error_count += load_error
        log.append(error_count, "Function call load_data_from_source() completed. Error count: " + str(error_count) + " file name: " + str(filename))
    # else log.append the same message in previous row
else:
    log.append(error_count, "Skipped function call load_data_from_source() from main.py. Error count: " + str(error_count) + " > 0.")
#
#######################################################
# Call TF function "Sentence Encoding"
#######################################################
if error_count == 0:
    #
    # retrieve data file
    if not os.path.exists("../data/"+conf.cleaned_alert_data):
        log.append(error_count, "File not found ../data/"+conf.cleaned_alert_data+".")
        error_count +=1
    else:
        log.append(error_count, "Fetching data file ../data/"+conf.cleaned_alert_data+".")
        with open("../data/"+conf.cleaned_alert_data) as f:
            messages = f.read().splitlines()
        if len(messages) == 0:
            error_count += 1
            log.append(error_count, "messages list is empty. Cannot run sentence_encoder().")
        else:
            # call sentence encoder
            log.append(error_count, 'Finished loading ' + str(len(messages)) + ' rows from ' + \
                                    str(conf.cleaned_alert_data + ' into a list of messages[]'))
            log.append(error_count, "Starting function call sentence_encoder() from main.py and in classify.py.")
            error_count += clfy.sentence_encoder(messages);
            if error_count > 0:
                log.append(error_count, "Incomplete function call sentence_encoder() from main.py and in classify.py. " \
                                        + "Error count: " + str(error_count))
            else:
                log.append(error_count, "Finished function call sentence_encoder() from main.py and in classify.py. " \
                                        + "Error count: " + str(error_count))
                # create a new file to store the encodings
                if not os.path.exists("../data/"+conf.encoded_alert_msg):
                    csv_file = open("../data/"+conf.encoded_alert_msg, 'w').close()
                    log.append(error_count, "File was not found. Created a new data file, ../data/"+conf.encoded_alert_msg+".")
                else:
                    log.append(error_count, "Found file, ../data/"+conf.encoded_alert_msg+" exist!")
                    # write list to file
                    #
else:
    log.append(error_count, "Skipped function call sentence_encoder() from main.py and in classify.py. " \
                            + "Error count: " + str(error_count) + " > 0.")
#
#######################################################
# 3D scatter plot of "sentence encoding"
#######################################################
if error_count == 0:
    log.append(error_count, "Fetching for data file ../data/"+conf.encoded_alert_msg)
    if not os.path.exists("../data/"+conf.encoded_alert_msg):
        error_count +=1
        log.append(error_count, "No file found, ../data/"+conf.encoded_alert_msg+" does not exist!. Error count: " + str(error_count))
    else:
        log.append(error_count, "Found file, ../data/"+conf.encoded_alert_msg+" exist!")
        log.append(error_count, "Starting function call scatter_3D_plot() from main.py and in plot.py.")
        with open('../data/'+conf.encoded_alert_msg) as csv_file:
            messages = csv.reader(csv_file, delimiter=',')
            plt.scatter_3D_plot(list(messages), title = "Cartesian 2D plot of Universal Sentence Encoding", \
                    fname="scatter_alert_encoding_3D.png")
        log.append(error_count, "Finished function call scatter_3D_plot() from main.py and in plot.py.")
else:
    log.append(error_count,"Skipped function call scatter_3D_plot() from main.py and in plot.py. Error count: " + str(error_count) + " > 0.")
#
#######################################################
# 2D incidence plot od "semantic textual similarity"
#######################################################
if error_count == 0:
    #
    # retrieve data file
    if not os.path.exists("../data/"+conf.cleaned_alert_data):
        log.append(error_count, "File not found ../data/"+conf.cleaned_alert_data+".")
        error_count +=1
    else:
        log.append(error_count, "Fetching data file ../data/"+conf.cleaned_alert_data+".")
        with open("../data/"+conf.cleaned_alert_data) as f:
            messages = f.read().splitlines()
        if len(messages) == 0:
            error_count += 1
            log.append(error_count, "messages list is empty. Cannot run semantic_textual_similarity().")
        else:
            # call sentence encoder
            log.append(error_count, 'Finished loading ' + str(len(messages)) + ' rows from ' + \
                                    str(conf.cleaned_alert_data + ' into a list of messages[]'))
            log.append(error_count, "Starting function call semantic_textual_similarity() from main.py and in classify.py.")
            error_count += clfy.semantic_textual_similarity(messages);
            if error_count > 0:
                log.append(error_count, "Incomplete function call semantic_textual_similarity() from main.py and in classify.py. " \
                                        + "Error count: " + str(error_count))
            else:
                log.append(error_count, "Finished function call semantic_textual_similarity() from main.py and in classify.py. " \
                                        + "Error count: " + str(error_count))
else:
    log.append(error_count, "Skipped function call sentence_encoder() from main.py and in classify.py. " \
                            + "Error count: " + str(error_count) + " > 0.")
#
if error_count == 0:
    log.append(error_count, "Starting function call semantic_textual_similarty () from main.py and in similarityTF.py.")
    error_count += clfy.semantic_textual_similarity();
    if error_count > 0:
        log.append(error_count, "Incomplete function call semantic_textual_similarty () from main.py and in similarityTF.py. Error count: " + str(error_count))
    else:
        log.append(error_count, "Completed function call semantic_textual_similarty () from main.py and in similarityTF.py. Error count: " + str(error_count))
else:
    log.append(error_count, "Skipped function call semantic_textual_similarty () from main.py and in similarityTF.py because of error count: " + str(error_count) + " > 0.")

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
