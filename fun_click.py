import pylab as plt
import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np
import seaborn

fig, ax = plt.subplots(1, 1)
ax = fig.add_subplot(111, projection = '3d')

#data= np.loadtxt('1000M_thined.obj')*-1
data= X =np.random.random((50,6))
scale=1000 #size objective multiplier  

#Plotting 5 objectives:
im= ax.scatter(data[:,0], data[:,1],data[:,2], c=data[:,3], s= data[:,4]*scale, alpha=1, cmap=plt.cm.spectral, picker=True)

#Setting the  main axis labels:
ax.set_xlabel('OBJECTIVE 1')
ax.set_ylabel('OBJECTIVE 2')
ax.set_zlabel('OBJECTIVE 3')

#Setting colorbar and its label vertically:
cbar= fig.colorbar(im)
cbar.ax.set_ylabel('OBJECTIVE 4')

#Setting size legend:
objs=data[:,4]
   
max_size=np.amax(objs)*scale/32.0
min_size=np.amin(objs)*scale*-200
handles, labels = ax.get_legend_handles_labels()
display = (0,1,2)

size_max = plt.Line2D((0,1),(0,0), color='k', markersize=max_size,linestyle='')
size_min = plt.Line2D((0,1),(0,0), color='k', markersize=min_size,linestyle='')
legend1= ax.legend([handle for i,handle in enumerate(handles) if i in display]+[size_max,size_min],
       [label for i,label in enumerate(labels) if i in display]+["%.2f"%(np.amax(objs)), "%.2f"%(np.amin(objs))], labelspacing=1.5, title='OBJECTIVE 5', loc=1, frameon=True, numpoints=1, markerscale=1)


#Setting the picker function:
def onpick(event):
   ind = event.ind
   print ('index: %d\nobjective 1: %0.2f\nobjective 2: %0.2f\nobjective 3: %0.2f\nobjective 4: %0.2f\nobjective 5: %0.2f\nobjective 6: %0.2f' % (event.ind[0],data[ind,0],data[ind,1],data[ind,2],data[ind,3],data[ind,4],data[ind,5]))


fig.canvas.mpl_connect('pick_event', onpick)


plt.show()