import numpy as np
import vtk
import modules.utility as utility
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import tables
import os
from scipy.interpolate import UnivariateSpline


######################################
mhas = open('images.txt').readlines()
mhas = [i.replace('\n','') for i in mhas]
# mhas = [i.split('/')[-1] for i in mhas]
# mhas = ['./data/'+i for i in mhas]

truths = open('truths.txt').readlines()
truths = [i.replace('\n','') for i in truths]

paths = open('paths.txt').readlines()
paths = [i.replace('\n','') for i in paths]

groups = open('groups.txt').readlines()
groups = [i.replace('\n','') for i in groups]

im_mr = open('mr_images.list').readlines()
im_mr = [i.replace('\n','') for i in im_mr]

im_ct = open('ct_images.list').readlines()
im_ct = [i.replace('\n','') for i in im_ct]

ct_val = open('ct_val.txt').readlines()
ct_val = [i.replace('\n','') for i in ct_val]

ct_test = open('ct_test.txt').readlines()
ct_test = [i.replace('\n','') for i in ct_test]

mr_val = open('mr_val.txt').readlines()
mr_val = [i.replace('\n','') for i in mr_val]

mr_test = open('mr_test.txt').readlines()
mr_test = [i.replace('\n','') for i in mr_test]

###########################################

def normalize_grps(grp_dict,path_info):
    norm_grps = []
    for i in sorted(grp_dict.keys()):

            vecs = path_info[i-1]
            p = vecs[:3]
            t = vecs[3:6]
            tx= vecs[6:]
            c = grp_dict[i]['contour']

            contour_norm = utility.normalizeContour(c,p,t,tx)
            norm_grps.append(contour_norm)
    return norm_grps

def reinterp_grps(grps_list, num_pts=20):
    reinterp_list = [
        utility.interpContour(c,num_pts) for c in grps_list
    ]
    return reinterp_list

def loft_path(grps_list, grp_points, num_new_points, k=3):
    """
    Note grp_points and path_points should be sorted
    """
    xsplines = []
    ysplines = []

    gpts = np.asarray(grp_points)
    gpts = 1.0*gpts/np.amax(gpts)

    d = 1.0/num_new_points
    ppts = np.arange(0,1,d)

    num_contour_pts = len(grps_list[0])

    for i in range(num_contour_pts):
        x = [g[i,0] for g in grps_list]
        y = [g[i,1] for g in grps_list]

        x_s = UnivariateSpline(gpts,x,k=k)
        y_s = UnivariateSpline(gpts,y,k=k)

        xsplines.append(x_s)
        ysplines.append(y_s)

    new_grps = []
    for p in ppts:
        cpts = [[xsplines[i](p),ysplines[i](p)]
                 for i in range(num_contour_pts)]
        new_grps.append(np.asarray(cpts))

    return new_grps

def get_all_lofted_segs(path, grp_fn, dims, spacing):

    total_groups = []
    total_segs = []
    processed_grps = []
    for grp_id in path.keys():
        grp = path[grp_id]['name']

        if os.path.exists(grp_fn+'/'+grp):

            path_info = path[grp_id]['points']

            grp_dict = utility.parseGroupFile(grp_fn+'/'+grp)

            norm_grps = normalize_grps(grp_dict,path_info)

            if len(norm_grps) > 3:
                print grp
                processed_grps.append(grp)

                interp_grps = reinterp_grps(norm_grps)

                lofted_grps = loft_path(interp_grps,sorted(grp_dict.keys()),len(path_info))

                total_groups += lofted_grps

                origin = [-spacing[0]*dims[0]/2,-spacing[1]*dims[1]/2]

                segs = [utility.contourToSeg(c,origin,dims,spacing) for c in
                       lofted_grps]

                total_segs += segs

    return total_segs,lofted_grps, processed_grps

output_dir = "/media/marsdenlab/Data2/datasets/DeepLofting/"
ext = [191, 191]
DIMS = [192,192]
NUM_CONTOUR_PTS = 20

#####################################################

def ct_norm(x):
    return (1.0*x+1000)/(2000)

def mr_norm(x):
    x = np.log(1.0*x-np.amin(x)+1)
    m = np.amin(x)
    x = (x-m)/(np.amax(x)-m)
    return x

def image_reader(fn_tup):

    img_fn, truth_fn, path_fn, grp_fn = fn_tup
    reader = vtk.vtkMetaImageReader()
    reader2 = vtk.vtkMetaImageReader()

    img_name = img_fn.split('/')[-2]

    reader.SetFileName(img_fn)
    reader.Update()
    the_image = reader.GetOutput()

    model = truth_fn
    model_name = model.split('/')[-2]

    print img_fn,truth_fn

    reader2.SetFileName(model)
    reader2.Update()
    the_model = reader2.GetOutput()

    path_dict = utility.parsePathFile(path_fn)

    return (the_image,the_model,path_dict,grp_fn)

def process_image(data_tup, f_x, f_y, f_c, normalizer):
    the_image, the_model, path_dict, grp_fn = data_tup

    spacing = the_image.GetSpacing()
    dims = the_image.GetDimensions()
    origin = [-ext[0]*spacing[0]/2,ext[1]*spacing[1]/2]
    minmax = the_image.GetScalarRange()

    #tmpimages = utility.getAllImageSlices(the_image, path_dict, ext, True)
    #tmpsegs = utility.getAllImageSlices(the_model, path_dict, ext, True)

    tmpsegs, lofted_grps, grp_names = get_all_lofted_segs(path_dict,grp_fn,DIMS,spacing)

    tmpimages = []
    for p in path_dict.keys():
        grp = path_dict[p]['name']
        if os.path.exists(grp_fn+'/'+grp) and any([grp == g for g in grp_names]):
            print 'grp {} exists, getting images'.format(grp)
            for v in path_dict[p]['points']:
                i =utility.getImageReslice(the_image,ext,v[:3],v[3:6],v[6:9], True)
                tmpimages.append(i)

    tmpimages = np.asarray(tmpimages)[:,:,:,np.newaxis]
    tmpsegs = np.asarray(tmpsegs)[:,:,:,np.newaxis]
    lofted_grps = np.asarray(lofted_grps)
    print tmpimages.shape, tmpsegs.shape
#     tmpimages = np.transpose(tmpimages,axes=(0,2,3,1))
#     tmpsegs = np.transpose(tmpsegs,axes=(0,2,3,1))

    tmpimages = normalizer(tmpimages)
    tmpsegs = 1.0*tmpsegs/np.amax(tmpsegs)
    inds = [i for i in range(len(tmpimages)) if np.sum(tmpsegs[i])>0]
    print tmpimages.shape
    f_x.append(tmpimages[inds])
    f_y.append(tmpsegs[inds])
    f_c.append(lofted_grps)

def images_to_hdf5(image_list,
                   reader, post_processor, normalizer,shape, label_shape, dtype, label_dtype,
                   output_fn):
    """
    takes a list of images, post processes them and stores result in extendable
    hdf5 table

    inputs:
        - image_list, (list of strings), list of image filenames, readable by reader
        - reader, (function), reader compatible with the file type in image_list
        - post_processor, (function), post processes output of reader, must return list of np arrays with same shape
        - output_fn, (string), ouput filename, must be hdf5 file
    """
    EXPECTED_ROWS = 10000

    #create hdf5 file
    hdf5_file = tables.open_file(output_fn,'w')
    filters = tables.Filters(complevel=5, complib='blosc')

    data_storage = hdf5_file.create_earray(hdf5_file.root,'X',
                                      tables.Atom.from_dtype(dtype),
                                      shape=[0]+list(shape),
                                         filters=filters,
                                         expectedrows=EXPECTED_ROWS)

    label_storage = hdf5_file.create_earray(hdf5_file.root,'Y',
                                      tables.Atom.from_dtype(label_dtype),
                                      shape=[0]+list(label_shape),
                                         filters=filters,
                                         expectedrows=EXPECTED_ROWS)

    contour_shape = [NUM_CONTOUR_PTS,2]
    c_storage = hdf5_file.create_earray(hdf5_file.root,'C',
                                  tables.Atom.from_dtype(label_dtype),
                                  shape=[0]+contour_shape,
                                     filters=filters,
                                     expectedrows=EXPECTED_ROWS)

    for i in range(len(image_list)):
        print 'image {}'.format(i)
        data_tuple = reader(image_list[i])

        post_processor(data_tuple,data_storage,label_storage,c_storage,normalizer)

    hdf5_file.close()

####################################################
train_ct = '/media/marsdenlab/Data2/datasets/DeepLofting/train_192_ct.hdf5'
val_ct = '/media/marsdenlab/Data2/datasets/DeepLofting/val_192_ct.hdf5'
test_ct = '/media/marsdenlab/Data2/datasets/DeepLofting/test_192_ct.hdf5'

train_mr = '/media/marsdenlab/Data2/datasets/DeepLofting/train_192_mr.hdf5'
val_mr = '/media/marsdenlab/Data2/datasets/DeepLofting/val_192_mr.hdf5'
test_mr = '/media/marsdenlab/Data2/datasets/DeepLofting/test_192_mr.hdf5'

ct_inds = [i for i in range(len(mhas)) if any([c in mhas[i] for c in im_ct])]
mr_inds = [i for i in range(len(mhas)) if any([c in mhas[i] for c in im_mr])]
ct_fn_tup = [(mhas[i],truths[i],paths[i],groups[i]) for i in ct_inds]
mr_fn_tup = [(mhas[i],truths[i],paths[i],groups[i]) for i in mr_inds]

print ct_fn_tup
print mr_fn_tup


ct_train_tups = []
ct_val_tups = []
ct_test_tups = []

for i in range(len(ct_fn_tup)):
    t = ct_fn_tup[i]
    fn = t[0]

    if any([c in fn for c in ct_val]):
        ct_val_tups.append(t)
    elif any([c in fn for c in ct_test]):
        ct_test_tups.append(t)
    else:
        ct_train_tups.append(t)

print "train"
print ct_train_tups

print "val"
print ct_val_tups

print "test"
print ct_test_tups


d = np.dtype(np.float16)
images_to_hdf5(ct_train_tups,
                   image_reader,
                   process_image, ct_norm, (ext[0]+1,ext[0]+1,1), (ext[0]+1,ext[1]+1,1), d, d,
                   train_ct)

images_to_hdf5(ct_val_tups,
                   image_reader,
                   process_image, ct_norm, (ext[0]+1,ext[1]+1,1), (ext[0]+1,ext[1]+1,1),d, d,
                   val_ct)

images_to_hdf5(ct_test_tups,
                   image_reader,
                   process_image, ct_norm, (ext[0]+1,ext[1]+1,1), (ext[0]+1,ext[1]+1,1), d, d,
                   test_ct)

##############################################

mr_train_tups = []
mr_val_tups = []
mr_test_tups = []

for i in range(len(mr_fn_tup)):
    t = mr_fn_tup[i]
    fn = t[0]

    if any([c in fn for c in mr_val]):
        mr_val_tups.append(t)
    elif any([c in fn for c in mr_test]):
        mr_test_tups.append(t)
    else:
        mr_train_tups.append(t)

print "train"
print mr_train_tups

print "val"
print mr_val_tups

print "test"
print mr_test_tups

d = np.dtype(np.float16)
images_to_hdf5(mr_train_tups,
                   image_reader,
                   process_image, mr_norm, (ext[0]+1,ext[0]+1,1), (ext[0]+1,ext[1]+1,1), d, d,
                   train_mr)

images_to_hdf5(mr_val_tups,
                   image_reader,
                   process_image, mr_norm, (ext[0]+1,ext[1]+1,1), (ext[0]+1,ext[1]+1,1),d, d,
                   val_mr)

images_to_hdf5(mr_test_tups,
                   image_reader,
                   process_image, mr_norm, (ext[0]+1,ext[1]+1,1), (ext[0]+1,ext[1]+1,1), d, d,
                   test_mr)
