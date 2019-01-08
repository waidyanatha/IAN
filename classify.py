import os, csv
import config as conf
import log as log
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
import seaborn as sns
import zipfile
from sklearn import model_selection

def embed_tfhub():
    error_count = 0
    module_url = conf.tf_hub_module_url
    log.append(error_count, "Tensorflow Hub URL: " + str(module_url))
    log.append(error_count, "Embedding: " + str(hub.Module(module_url)))
    return error_count, hub.Module(module_url)

def sentence_encoder(messages=[]):
    error_count = 0
    error_count, embed = embed_tfhub()

    # Reduce logging output.
    tf.logging.set_verbosity(tf.logging.ERROR)

    with tf.Session() as session:
        session.run([tf.global_variables_initializer(), tf.tables_initializer()])
        log.append(error_count, "Loading data from : " + str(conf.cleaned_alert_data))
        message_embeddings = session.run(embed(messages))
        text_file = open("./data/"+conf.encoded_alert_msg, 'w').close()
        text_file = open("./data/"+conf.encoded_alert_msg, "a")
        log.append(error_count, "Writing message and encoding data to text file : " + str(conf.encoded_alert_msg))
        for i, message_embedding in enumerate(np.array(message_embeddings).tolist()):
            message_embedding_snippet = ", ".join(
                (str(x) for x in message_embedding[:3]))
            text_file.write(format(messages[i])[0:13] + ", " + format(message_embedding_snippet) + "\n")
        text_file.close()
        log.append(error_count, "Writing complete to text file : " + str(conf.encoded_alert_msg))
    return error_count
        
def semantic_textual_similarity(messages=[]):
    error_count = 0
    error_count, embed = embed_tfhub()

    import plot as plt
    similarity_input_placeholder = tf.placeholder(tf.string, shape=(None))
    similarity_message_encodings = embed(similarity_input_placeholder)
    with tf.Session() as session:
        session.run(tf.global_variables_initializer())
        session.run(tf.tables_initializer())
        plt.run_and_plot(session, similarity_input_placeholder, messages, similarity_message_encodings)
    return error_count

