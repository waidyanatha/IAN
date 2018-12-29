# GRAB - MAIN 
#
# ------------------------------------------------------------------------------
#
#
# contributors: nuwan@sahanafoundation.org
#
# ------------------------------------------------------------------------------
#
# import libraries
import sys, os
import numpy as np
#import pandas as pd
import config as conf
import datafilter as dafi
import similarityTF as stf
import plot as plt
import datetime as dt
from sklearn.cluster import KMeans
from pandas.core.series import Series
import math
import csv
import tensorflow as tf
from tensorflow import keras
#from tensorflow.keras import layers
#
######################################################################################
#
# INITIALIZE: set auxiliary directories and paths
#
######################################################################################
def initiatlize():
    error = 0
    print(str(dt.datetime.now()) + ": system version "+str(sys.version))
    print(str(dt.datetime.now()) + ": tesnorflow verion "+str(tf.VERSION))
    print(str(dt.datetime.now()) + ": keras version"+str(tf.keras.__version__))
    #
    # plots directory
    dir_path = "../plots/"
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    # data directory
    dir_path = "../data/"
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    #
    # check parameters and echo call functionaX
    logstr = "Data filtering parameters  (Initialize): \n"
    print (logstr)
    return error, logstr 
#
######################################################################################
#
#    MAIN CALLS 
#
######################################################################################
error = 0
tstart = dt.datetime.now()
print(str(dt.datetime.now()) + " begin cap.sahana.io message filtering ")
#
#####################
# Initialize algorithm
#####################
print ("\n")
print(str(dt.datetime.now()) + " starting process initializing algorithms. ")
if error == 0:
    init_err, init_str = initiatlize()
    if init_err > 0:
        error += init_err
        print(str(dt.datetime.now()) + " initialization failed with error count: " + str(error) + " value : " + str(init_str))
    else:
        print(str(dt.datetime.now()) + " initializing completed with error count: " + str(error) + " value : " + str(init_str))
else:
    print(str(dt.datetime.now()) + ": unknown error with error count: " + str(error) + " value : " + str(init_str))
#
#####################
# Load data
#####################
# load data from file defined in config "alerts_file"
print ("\n")
print (str(dt.datetime.now()) + " starting process load data.")
if error == 0:
    error, filename = dafi.load_data()
    print (str(dt.datetime.now()) + " load data completed with error count: " + str(error) + " file name: " + str(filename))
else:
    print (str(dt.datetime.now()) + " skip load data because of error count: " + str(error) + " > 0.")
#
#####################
# sentence encoding
#####################
print ("\n")
print (str(dt.datetime.now()) + " starting process TF sentence encoder.")
if error == 0:
    stf.sentence_encoder();
    print (str(dt.datetime.now()) + " sentence encoding completed with error count: " + str(error))
else:
    print (str(dt.datetime.now()) + " skip sentece encoding because of error count: " + str(error) + " > 0.")
#
#####################
#3D scatter plot sentence encoding
#####################
print ("\n")
print (str(dt.datetime.now()) + " starting to plot sentence encoding data.")
if error == 0:
    if not os.path.exists("../data/"+conf.encoded_alert_msg):
        print(str(dt.datetime.now()) + " file ../data/"+conf.encoded_alert_msg+" does not exist!")
    else:
        print (str(dt.datetime.now()) + " plotting universal sentence encodings")
        with open('../data/'+conf.encoded_alert_msg) as csv_file:
            #messages = f.read().splitlines()
            csv_reader = csv.reader(csv_file, delimiter=',')
            plt.scatter_3D_plot(csv_reader, title = "cartesian 3D plot - universal sentence encodings", \
                    fname="scatter_alert_encoding_3D.png")
        print (str(dt.datetime.now()) + " 3D scatter plot completed with error count: " + str(error))
else:
    print (str(dt.datetime.now()) + " skip plot sentece encoding because of error count: " + str(error) + " > 0.")
#
#####################
# semantic textual similarity
#####################
print ("\n")
print (str(dt.datetime.now()) + " starting TF semantic textual similarity.")
if error == 0:
    ##stf.semantic_textual_similarity();
    print (str(dt.datetime.now()) + " textual similarity completed with error count: " + str(error))
else:
    print (str(dt.datetime.now()) + " skip textual similarity because of error count: " + str(error) + " > 0.")

#####################
# close program
#####################
print ("\n")
tfinish = dt.datetime.now()
print(str(dt.datetime.now()) + " ending with a total time of "+str(tfinish - tstart))
#
