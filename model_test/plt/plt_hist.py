import numpy as np  
import matplotlib.mlab as mlab  
import matplotlib.pyplot as plt  

def draw_hist(data,batch_size=10,title="batch_hist",file=''):
    plt.clf()
    plt.hist(data, bins=batch_size, normed=0,histtype='bar',facecolor="blue", edgecolor="black",alpha=0.7)  
    plt.savefig('chart/'+file+'/'+title+'.png')
