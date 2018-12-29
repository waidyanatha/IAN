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
import pandas as pd
import config as conf
import datafilter as dafi
import similarityTF as stf
##import tfuniven as tf
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
    print(str(dt.datetime.now()) + "system version "+str(sys.version))
    print(str(dt.datetime.now()) + "tesnorflow verion "+str(tf.VERSION))
    print(str(dt.datetime.now()) + "keras version"+str(tf.keras.__version__))
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
#
######################################################################################
#
#    MAIN CALLS 
#
######################################################################################
tstart = dt.datetime.now()
print(str(dt.datetime.now()) + "begin cap.sahana.io message filtering ")
#
print(str(dt.datetime.now()) + ": initializing for analysis. ")
initiatlize()
print(str(dt.datetime.now()) + ": initializing complete. ")
# retrieve the data from defined source
print(str(dt.datetime.now()) + ": looking for data files.")
if not os.path.exists(str(dt.datetime.now()) + ": ../data/"+conf.alerts_file):
    print(str(dt.datetime.now()) + ": ../data/"+conf.alerts_file+" does not exist!")
else:
    print(str(dt.datetime.now()) + ": loading data from: ../data/"+conf.alerts_file)
 
    with open(str(dt.datetime.now()) + ": ../data/"+conf.alerts_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        alert_list = []
        text_file = open("../data/"+conf.cleaned_alert_data, "w")
        for row in csv_reader:
            #skip the header
            if line_count == 0:
                print row
                print (str(dt.datetime.now()) + ": number of attributes: "+str(len(row)))
            else:
                tmp_str = row[0]+" "+row[1]+" "+row[2]+" "+row[3]+" "+row[4]+" "+row[5]+" "+row[6]+" "+row[7]+" "
                tmp_str += " "+row[8]+" "+row[9]+" "+row[10]+" "+row[11]+" "+row[12]+" "+row[13]+" "+row[14]+" "+row[15]+" "
                alert_list[line_count:0] = tmp_str
                text_file.write('"%s"\n' % tmp_str)
            line_count += 1
        
        print(str(dt.datetime.now()) + ": Processed " + str(line_count)+" rows from "+str(conf.source)+" (1 header row and "+str(line_count-1)+" data rows).")
        text_file.close()
        print(str(dt.datetime.now()) + ": finished writing alert data to a file ../data/"+conf.cleaned_alert_data)

#sentence encoding
print (str(dt.datetime.now()) + "starting TF sentence encoder.")
##stf.sentence_encoder();
print (str(dt.datetime.now()) + "sentence encoding complete.")

#sentence encoding
print (str(dt.datetime.now()) + "starting TF semantic textual similarity.")
stf.semantic_textual_similarity();
print (str(dt.datetime.now()) + "semantic textual similarity complete.")

#plot the outputs
if not os.path.exists("../data/"+conf.encoded_alert_msg):
    print(str(dt.datetime.now()) + "../data/"+conf.encoded_alert_msg+" does not exist!")
else:
    print (str(dt.datetime.now()) + "plotting universal sentence encodings")
    with open('../data/'+conf.encoded_alert_msg) as csv_file:
        #messages = f.read().splitlines()
        csv_reader = csv.reader(csv_file, delimiter=',')
        plt.scatter_3D_plot(csv_reader, title = "cartesian 3D plot - universal sentence encodings", fname="scatter_alert_encoding_3D.png")

# close program
tfinish = dt.datetime.now()
print(str(dt.datetime.now()) + "ending with a total time of "+str(tfinish - tstart))
#
