# GRAB Analytics - log activities (function status & errors)
#
# ------------------------------------------------------------------------------
#
# contributors: nuwan@sahanafoundation.org
#
# ------------------------------------------------------------------------------
#
# import libraries
import sys, os
import config as conf
import datetime as dt
#
######################################################################################
#
# LOG: sequence of function status and errors
#
######################################################################################
def append(log_code=0, log_str=""):
    log_file = open("./"+conf.log_file, "a")
    log_dt = str(dt.datetime.now())
    log_rec = log_dt + " [" + str(log_code) + "] " + log_str
    log_file.write('%s\n' % log_rec)
    log_file.close()
#
