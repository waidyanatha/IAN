# GRAB Analytics - IO (Input / Output) 
#
# purpose of this code is to import and from varoius data sources and then
# output them as a file or stream in the desired formats
#
# contributors: nuwan@sahanafoundation.org
#
# ------------------------------------------------------------------
#
# import libraries
import sys, os, csv
import datetime as dt
import config as conf
import log as log
#
def clean_str(string):
#    string = re.sub(r"\\", "", string)    
#    string = re.sub(r"\'", "", string)    
#    string = re.sub(r"\"", "", string)    
    return string.strip().lower()
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
def load_data():
    error_count = 0
    log.append(error_count, "fetching data files.")
    if not os.path.exists("../data/"+str(conf.alerts_file)):
        error += 1
        log.append(error_count, "../data/"+conf.alerts_file+" does not exist. error count: " + str(error))
    else:
        log.append(error_count, "loading data from: ../data/"+conf.alerts_file)
 
        with open("../data/"+str(conf.alerts_file)) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            alert_list = []
            text_file = open("../data/"+conf.cleaned_alert_data, "w")
            for row in csv_reader:
                #skip the header
                if line_count == 0:
                    log.append(error_count, "number of attributes: "+str(len(row)))
                    log.append(error_count, ', '.join(row))
                else:
                    tmp_str = row[0]+" "+row[1]+" "+row[2]+" "+row[3]+" "+row[4]+" "+row[5]+" "+row[6]+" "+row[7]+" "
                    tmp_str += " "+row[8]+" "+row[9]+" "+row[10]+" "+row[11]+" "+row[12]+" "+row[13]+" "+row[14]+" "+row[15]+" "
                    # clean up the string
                    tmp_str = clean_str(tmp_str)
                    alert_list[line_count:0] = tmp_str
                    text_file.write('"%s"\n' % tmp_str)
                line_count += 1
    
            log.append(error_count, "Processed " + str(line_count)+" rows "+" (1 header row and "+str(line_count-1)+" data rows).")
            text_file.close()
            log.append(error_count, "finished writing alert data to a file ../data/"+conf.cleaned_alert_data)
    return error_count, conf.cleaned_alert_data
