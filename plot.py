import matplotlib.pyplot as plt
import numpy as np
import matplotlib.lines as mlines
from matplotlib.ticker import FormatStrFormatter
import os

def plot3Yaxis(df,      groupvariable, groupname, groupunits, groupformat,
                        xvariable, xname, xunits, xformat,
                        yvariable, yname, yunits, yformat,
                        y2variable, y2name, y2units, y2format, 
                        y3variable, y3name, y3units, y3format,
                        figpath, figname,fontsize=12,fontsizetitle=14, color=True):

    fig, ax = plt.subplots(figsize=(12,6))

    ax1 = ax.twinx(); ax2 = ax.twinx()    
    ax2.spines['right'].set_position(("outward",90)) 
    lstyles = ['-','-.','--']
    mstyles = ['o','v','+','*']
    if color:
       colors = ['red', 'blue', 'green']
    else:
       colors = ['k', 'k', 'k']
   
    grouped = df.sort_values([groupvariable,xvariable],ascending=True) \
        .groupby(groupvariable)

    # y
    i=0
    for name,  group in grouped:
        grouped.get_group(name).plot(x=xvariable,
              y=yvariable,
              ax= ax,
              color=colors[0],
              linestyle=lstyles[0],
              marker=mstyles[i])
        i+=1
    ax.set_xlabel(" ".join([xname,'['+xunits+']']), fontsize=fontsize)
    ax.set_ylabel(" ".join([yname,'['+yunits+']']), fontsize=fontsize)
    ax.yaxis.label.set_color(colors[0])
    ax.tick_params(axis='y', colors=colors[0])
    ax.spines['left'].set_color(colors[0])
    
    #y2
    i=0
    for name,  group in grouped:
        grouped.get_group(name).plot(x=xvariable,
              y=y2variable,
              ax= ax1,
              color=colors[1],
              linestyle=lstyles[1],
              marker=mstyles[i])
        i+=1

    ax1.set_xlabel(" ".join([xname,'['+xunits+']']), fontsize=fontsize)
    ax1.set_ylabel(" ".join([y2name,'['+y2units+']']), fontsize=fontsize)
    ax1.yaxis.label.set_color(colors[1])
    ax1.tick_params(axis='y', colors=colors[1])
    ax1.spines['right'].set_color(colors[1]) 
    
    #y3
    i=0
    for name,  group in grouped:
        grouped.get_group(name).plot(x=xvariable,
              y=y3variable,
              ax= ax2,
              color=colors[2],
              linestyle=lstyles[2],
              marker=mstyles[i])
        i+=1
    ax2.set_xlabel(" ".join([xname,'['+xunits+']']), fontsize=fontsize)
    ax2.set_ylabel(" ".join([y3name,'['+y3units+']']), fontsize=fontsize)
    ax2.yaxis.label.set_color(colors[2])
    ax2.tick_params(axis='y', colors=colors[2])
    ax2.spines['left'].set_color(colors[2])

    #legend     
    labels = map(lambda x: " ".join([groupname,'=',
                                      groupformat.format(x),
                                      groupunits]) if isinstance(x, (np.floating, np.int)) else
			   " ".join([groupname,'=',x,
                                     groupunits]),
                  df.sort_values(groupvariable,ascending=True)[groupvariable] 
                  .unique())
    handles = [mlines.Line2D([], 
                         [], 
                         color='k',  
                         linestyle='None',
                         marker=mstyles[index],
                         markersize=10, 
                         label=label) 
           for index, label in enumerate(labels)]
              
    ax.legend(handles=handles, fontsize=fontsize);

    #legend    
    labels = [yname, y2name, y3name]

    handles = [mlines.Line2D([],
                         [], 
                         color=color,  
                         linestyle=lstyles[index],
                         markersize=10, 
                         label=labels[index]) 
           for index, color in enumerate(colors)]
              
    ax1.legend(handles=handles, fontsize=fontsize, loc='upper left')
    ax2.legend_.remove()
    ax.xaxis.set_major_formatter(FormatStrFormatter(xformat))
    ax.yaxis.set_major_formatter(FormatStrFormatter(yformat))
    ax1.yaxis.set_major_formatter(FormatStrFormatter(y2format))
    ax2.yaxis.set_major_formatter(FormatStrFormatter(y3format))
    ax.tick_params(labelsize=fontsize);ax1.tick_params(labelsize=fontsize);ax2.tick_params(labelsize=fontsize)
    
    plt.tight_layout();plt.savefig(os.path.join(figpath,figname+'.png'))
    plt.close(fig)
    
    
