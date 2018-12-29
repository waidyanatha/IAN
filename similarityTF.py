import os
import config as conf
import datetime as dt
import numpy as np
#import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
import seaborn as sns
import zipfile
from sklearn import model_selection

def embed_tfhub():
    module_url = conf.tf_hub_module_url
    print (str(dt.datetime.now()) + " Tensorflow Hub URL: " + str(module_url))
    # Import the TF Hub module
    print (str(dt.datetime.now()) + " Embedding: " + str(hub.Module(module_url)))
    #embed = hub.Module(module_url)
    return hub.Module(module_url)

def sentence_encoder():
    embed = embed_tfhub()
    #load data from file
    print (str(dt.datetime.now()) + " Loading data from : " + str(conf.cleaned_alert_data))
    with open("../data/"+conf.cleaned_alert_data) as f:
        messages = f.read().splitlines()
    print (str(dt.datetime.now()) + " Loading complete. ")

    # Reduce logging output.
    tf.logging.set_verbosity(tf.logging.ERROR)

    with tf.Session() as session:
        session.run([tf.global_variables_initializer(), tf.tables_initializer()])
        message_embeddings = session.run(embed(messages))
        text_file = open("../data/"+conf.encoded_alert_msg, 'w').close()
        text_file = open("../data/"+conf.encoded_alert_msg, "a")
        print (str(dt.datetime.now()) + " Writing message and encoding data to text file : " + str(conf.encoded_alert_msg))
        for i, message_embedding in enumerate(np.array(message_embeddings).tolist()):
#d            print("Message: {}".format(messages[i]))
#d            print("Embedding size: {}".format(len(message_embedding)))
            message_embedding_snippet = ", ".join(
                (str(x) for x in message_embedding[:3]))
#d            print("Embedding: [{}, ...]\n".format(message_embedding_snippet))
#d          text_file.write(format(messages[i])[0:13] + ", " + format(messages[i]) + ", " + format(message_embedding_snippet) + "\n")
            text_file.write(format(messages[i])[0:13] + ", " + format(message_embedding_snippet) + "\n")
        text_file.close()
        print (str(dt.datetime.now()) + " Writing complete. ")
        
def semantic_textual_similarity():
    embed = embed_tfhub()
    #load data from file
    with open("../data/"+conf.cleaned_alert_data) as f:
        messages = f.read().splitlines()

    import plot as plt
    similarity_input_placeholder = tf.placeholder(tf.string, shape=(None))
    similarity_message_encodings = embed(similarity_input_placeholder)
    with tf.Session() as session:
        session.run(tf.global_variables_initializer())
        session.run(tf.tables_initializer())
        plt.run_and_plot(session, similarity_input_placeholder, messages, similarity_message_encodings)

