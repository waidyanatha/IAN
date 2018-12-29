# GRAB - PLOT (plot data) 
#
# Instructions: 
#     - import (include) this library in main
#
# Reporting Patterns (RePat) for determining telecom availability during crises
# ------------------------------------------------------------------------------
#
# purpose of this code is to plot the clustered and other generated data for
# visualization in various forms
#
# contributors: nuwan@lirneasia.net and ilihdian@gmail.com
#
# ------------------------------------------------------------------
#
# import libraries
import sys, os, csv
import config as conf
import seaborn as sns
#import pyquery
#import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.cm as cm
#import matplotlib as mpl
from pandas.core.series import Series
from __builtin__ import str
#from IPython.core.application import base_aliases pylab inline
style.use('ggplot')
from shapely.geometry import Polygon     #necessary for plotting the L0 data
#
# 3D plot 
def scatter_3D_plot(messages, title = "cartesian 3D plot", fname="plot_cartesian_plane.png"):

    # open from file
    
    from mpl_toolkits.mplot3d import Axes3D

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    label = []
    xs = []
    ys = []
    zs = []
    c = ['r','b']
    m = 'o'
    
    for row in messages:
        l=''.join(map(str,row[0:1]))
        x=''.join(map(str,row[1:2]))
        y=''.join(map(str,row[2:3]))
        z=''.join(map(str,row[3:4]))

        #keep flaot() else throws an error
        xs.append(float(x))
        ys.append(float(y))
        zs.append(float(z))
    
    ax.scatter(xs, ys, zs, c=c, marker=m)
    
    ax.set_xlim3d(min(xs), max(xs))
    ax.set_ylim3d(min(ys), max(ys))
    ax.set_zlim3d(min(zs), max(zs))
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.set_title("CAP message sentence encoding plot")

    plt.savefig("../plots/"+fname, dpi=300, bbox_inces='tight')
    #plt.show()
    return 0
#

def plot_similarity(labels, features, rotation):
    fname = "plot_similarity.png"
    corr = np.inner(features, features)
    sns.set(font_scale=1.2)
    g = sns.heatmap(
        corr,
        xticklabels=labels,
        yticklabels=labels,
        vmin=0,
        vmax=1,
        cmap="YlOrRd")
    g.set_xticklabels(labels, rotation=rotation)
    g.set_title("Semantic Textual Similarity")
    fig = g.get_figure()
    fig.savefig("../plots/plot_similarity.png")

def run_and_plot(session_, input_tensor_, messages_, encoding_tensor):
  message_embeddings_ = session_.run(
      encoding_tensor, feed_dict={input_tensor_: messages_})
  plot_similarity(messages_, message_embeddings_, 90)
