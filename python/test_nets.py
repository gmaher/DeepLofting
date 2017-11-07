import tensorflow as tf
import modules.layers as tf_util
import numpy as np
import matplotlib.pyplot as plt
import vtk
import sys
print sys.path
from vtk import vtkImageExport
def VTKSPtoNumpy(vol):
    '''
    Utility function to convert a VTK structured points (SP) object to a numpy array
    the exporting is done via the vtkImageExport object which copies the data
    from the supplied SP object into an empty pointer or array

    C/C++ can interpret a python string as a pointer/array

    This function was shamelessly copied from
    http://public.kitware.com/pipermail/vtkusers/2002-September/013412.html
    args:
    	@a vol: vtk.vtkStructuredPoints object
    '''
    exporter = vtkImageExport()
    exporter.SetInputData(vol)
    dims = exporter.GetDataDimensions()
    if np.sum(dims) == 0:
        return np.zeros((1,64,64))
    if (exporter.GetDataScalarType() == 3):
    	dtype = UnsignedInt8
    if (exporter.GetDataScalarType() == 4):
    	dtype = np.short
    if (exporter.GetDataScalarType() == 5):
    	dtype = np.int16
    if (exporter.GetDataScalarType() == 10):
    	dtype = np.float32
    if (exporter.GetDataScalarType() == 11):
    	dtype = np.float64
    a = np.zeros(reduce(np.multiply,dims),dtype)
    s = a.tostring()
    exporter.SetExportVoidPointer(s)
    exporter.Export()
    a = np.reshape(np.fromstring(s,dtype),(dims[2],dims[0],dims[1]))
    return a[0]

def VTKSPtoNumpyFromFile(fn):
	'''
	reads a .vts file into a numpy array


	args:
		@a fn - string, filename of .sp file to read
	'''
	reader = vtk.vtkStructuredPointsReader()
	reader.SetFileName(fn)
	reader.Update()
	sp = reader.GetOutput()
	return VTKSPtoNumpy(sp)

def crop_center(img,cropx,cropy):
    y,x = img.shape
    startx = x//2-(cropx//2)
    starty = y//2-(cropy//2)
    return img[starty:starty+cropy,startx:startx+cropx]

MODEL_DL = "/home/marsdenlab/projects/DeepLofting/python/models/i2i_CT/i2i_CT"
MODEL_SV = "/home/marsdenlab/projects/SV3/ml_plugin/org.sv.gui.qt.ml/src/python/models/i2i_CT/i2i_CT"
FILE = "/home/marsdenlab/17127.npy"
FILE_2 = "/home/marsdenlab/projects/data_test/tmp/120.vts"

X_VTS_NP = VTKSPtoNumpyFromFile(FILE_2)
X_VTS_NP = crop_center(X_VTS_NP,128,128).reshape((128,128,1))*1.0/3000
print X_VTS_NP.shape
X_IN = np.load(FILE).reshape((1,128,128,1))
######################################################
# Define variables
######################################################
N = 1
W = 128
H = 128
C=1
crop_dims = 128
Nbatch = 16
lr = 1e-4
Nsteps=40000
print_step=200
init = 7e-2
lam = 0.0001
Nfilters = 32

EPS=1e-4
leaky_relu = tf.contrib.keras.layers.LeakyReLU(0.2)
y_index=0
alph = 0.3
beta = 0.7

X_IN = np.concatenate((X_IN,np.zeros((Nbatch-1,crop_dims,crop_dims,1))))
X_IN[1] = X_VTS_NP

def selu(x):
    with ops.name_scope('elu') as scope:
        alpha = 1.6732632423543772848170429916717
        scale = 1.0507009873554804934193349852946
    return scale*tf.where(x>=0.0, x, alpha*tf.nn.elu(x)-alpha)
#########################################################
# Define graph
#########################################################
#lr_tf = tf.placeholder(shape=[],dtype=tf.float32,name='lr')
with tf.device('/cpu:0'):
    x = tf.placeholder(shape=[None,crop_dims,crop_dims,C],dtype=tf.float32)
    y = tf.placeholder(shape=[None,crop_dims,crop_dims,C],dtype=tf.float32)

    ###############
    # I2I
    ###############

    yclass,yhat,o3,o4 = tf_util.I2INet(x,nfilters=Nfilters,activation=leaky_relu,init=init)

    y_vec = tf.reshape(yhat, (Nbatch,crop_dims**2))

    sp = tf_util.fullyConnected(y_vec,crop_dims,leaky_relu, std='xavier', scope='sp1')
    sp = tf_util.fullyConnected(y_vec,crop_dims**2,leaky_relu, std='xavier', scope='sp2')
    sp = tf.reshape(sp, (Nbatch,crop_dims,crop_dims,1))

    y_sp = tf_util.conv2D(sp, nfilters=Nfilters, activation=leaky_relu,init=init, scope='sp3')
    y_sp_1 = tf_util.conv2D(y_sp, nfilters=Nfilters, activation=leaky_relu, init=init,scope='sp4')
    y_sp_2 = tf_util.conv2D(y_sp_1, nfilters=Nfilters, activation=leaky_relu, init=init,scope='sp5')

    yhat = tf_util.conv2D(y_sp_2, nfilters=1, activation=tf.identity, init=init,scope='sp6')

    yclass = tf.sigmoid(yhat)

    # TP = tf.reduce_sum(yclass*y)
    # FP = tf.reduce_sum(yclass*(1-y))
    # FN = tf.reduce_sum((1-yclass)*y)
    # loss = -TP/(TP + alph*FP+beta*FN+EPS)

    loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=yhat,labels=y))

    loss = loss + tf_util.l2_reg(lam)

    opt = tf.train.AdamOptimizer(lr)
    train = opt.minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

print yclass

saver = tf.train.Saver()


#Model 1
saver.restore(sess,MODEL_DL)
y_1 = sess.run(yclass,{x:X_IN})

saver.restore(sess,MODEL_SV)
y_2 = sess.run(yclass,{x:X_IN})

plt.figure()
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True, figsize=(8,2))
im1 = ax1.imshow(X_IN[0,:,:,0],cmap='gray')
im2 = ax2.imshow(y_1[0,:,:,0],cmap='gray')
im3 = ax3.imshow(y_2[0,:,:,0],cmap='gray')
plt.colorbar(im1,ax1)
plt.colorbar(im2,ax2)
plt.colorbar(im3,ax3)
plt.tight_layout
#plt.savefig('transform_{}.pdf'.format(j),dpi=600)
plt.show()

plt.figure()
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True, figsize=(8,2))
im1 = ax1.imshow(X_IN[1,:,:,0],cmap='gray')
im2 = ax2.imshow(y_1[1,:,:,0],cmap='gray')
im3 = ax3.imshow(y_2[1,:,:,0],cmap='gray')
plt.colorbar(im1,ax1)
plt.colorbar(im2,ax2)
plt.colorbar(im3,ax3)
plt.tight_layout
#plt.savefig('transform_{}.pdf'.format(j),dpi=600)
plt.show()

plt.figure()
plt.imshow(X_IN[1,:,:,0],cmap='gray')
plt.colorbar()
plt.show()
