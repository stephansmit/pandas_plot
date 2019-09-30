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
                        figpath, figname,fontsize=12,fontsizetitle=14):

    fig, ax = plt.subplots(figsize=(12,6))

    ax1 = ax.twinx(); ax2 = ax.twinx()    
    ax2.spines['right'].set_position(("outward",90)) 
    lstyles = ['-','-.','--',':']
    mstyles = ['o','v','+','*']
   
    grouped = df.sort_values([groupvariable,xvariable],ascending=True) \
        .groupby(groupvariable)

    # y
    i=0
    for name,  group in grouped:
        grouped.get_group(name).plot(x=xvariable,
              y=yvariable,
              ax= ax,
              color='red',
              linestyle=lstyles[i],
              marker=mstyles[i])
        i+=1
    ax.set_xlabel(" ".join([xname,'['+xunits+']']), fontsize=fontsize)
    ax.set_ylabel(" ".join([yname,'['+yunits+']']), fontsize=fontsize)
    ax.yaxis.label.set_color('red')
    ax.tick_params(axis='y', colors='red')
    ax.spines['left'].set_color('red')
    
    #y2
    i=0
    for name,  group in grouped:
        grouped.get_group(name).plot(x=xvariable,
              y=y2variable,
              ax= ax1,
              color='blue',
              linestyle=lstyles[i],
              marker=mstyles[i])
        i+=1

    ax1.set_xlabel(" ".join([xname,'['+xunits+']']), fontsize=fontsize)
    ax1.set_ylabel(" ".join([y2name,'['+y2units+']']), fontsize=fontsize)
    ax1.yaxis.label.set_color('blue')
    ax1.tick_params(axis='y', colors='blue')
    ax1.spines['right'].set_color('blue') 
    
    #y3
    i=0
    for name,  group in grouped:
        grouped.get_group(name).plot(x=xvariable,
              y=y3variable,
              ax= ax2,
              color='green',
              linestyle=lstyles[i],
              marker=mstyles[i])
        i+=1
    ax2.set_xlabel(" ".join([xname,'['+xunits+']']), fontsize=fontsize)
    ax2.set_ylabel(" ".join([y3name,'['+y3units+']']), fontsize=fontsize)
    ax2.yaxis.label.set_color('green')
    ax2.tick_params(axis='y', colors='green');ax2.spines['left'].set_color('green')
    ax2.spines['left'].set_color('green')

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
                         linestyle=lstyles[index],
                         marker=mstyles[index],
                         markersize=10, 
                         label=label) 
           for index, label in enumerate(labels)]
              
    ax.legend(handles=handles, fontsize=fontsize);

    ax1.legend_.remove()
    ax2.legend_.remove()
    #ax.xaxis.set_major_formatter(FormatStrFormatter(xformat))
    #ax.yaxis.set_major_formatter(FormatStrFormatter(yformat))
    #ax1.yaxis.set_major_formatter(FormatStrFormatter(y2format))
    #ax2.yaxis.set_major_formatter(FormatStrFormatter(y3format))
    ax.tick_params(labelsize=fontsize);ax1.tick_params(labelsize=fontsize);ax2.tick_params(labelsize=fontsize)
    
    plt.tight_layout();plt.savefig(os.path.join(figpath,figname+'.png'))
    plt.close(fig)



    
    
