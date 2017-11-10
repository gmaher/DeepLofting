import tables
import numpy as np

shape = [192,192,1]

def create_hdf5(output_fn,dtype=np.dtype(np.float32)):
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
                                      tables.Atom.from_dtype(dtype),
                                      shape=[0]+list(shape),
                                         filters=filters,
                                         expectedrows=EXPECTED_ROWS)

    contour_shape = [NUM_CONTOUR_PTS,2]
    c_storage = hdf5_file.create_earray(hdf5_file.root,'C',
                                  tables.Atom.from_dtype(dtype),
                                  shape=[0]+contour_shape,
                                     filters=filters,
                                     expectedrows=EXPECTED_ROWS)

    meta = hdf5_file.create_earray(hdf5_file.root,'meta',
                                  tables.Atom.from_dtype(dtype),
                                  shape=[0,2],
                                     filters=filters,
                                     expectedrows=EXPECTED_ROWS)
    return hdf5_file

def populate_hdf5(f,f_ct,f_mr):
    f.root.X.append(f_ct.root.X[:])
    f.root.Y.append(f_ct.root.Y[:])
    f.root.C.append(f_ct.root.C[:])
    f.root.meta.append(f_ct.root.meta[:])

    f.root.X.append(f_mr.root.X[:])
    f.root.Y.append(f_mr.root.Y[:])
    f.root.C.append(f_mr.root.C[:])
    f.root.meta.append(f_mr.root.meta[:])

NUM_CONTOUR_PTS = 20

data_path = '/media/marsdenlab/Data2/datasets/DeepLofting/'

train_ct = data_path+'train_192_ct.hdf5'
val_ct   = data_path+'val_192_ct.hdf5'
test_ct  = data_path+'test_192_ct.hdf5'

train_mr = data_path+'train_192_mr.hdf5'
val_mr   = data_path+'val_192_mr.hdf5'
test_mr  = data_path+'test_192_mr.hdf5'

train_combined = data_path+'train_192_combined.hdf5'
val_combined   = data_path+'val_192_combined.hdf5'
test_combined  = data_path+'test_192_combined.hdf5'

f_train_ct = tables.open_file(train_ct)
f_val_ct   = tables.open_file(val_ct)
f_test_ct  = tables.open_file(test_ct)

f_train_mr = tables.open_file(train_mr)
f_val_mr   = tables.open_file(val_mr)
f_test_mr  = tables.open_file(test_mr)

f_train_combined = create_hdf5(train_combined)
f_val_combined = create_hdf5(val_combined)
f_test_combined = create_hdf5(test_combined)


populate_hdf5(f_train_combined,f_train_ct,f_train_mr)
populate_hdf5(f_val_combined,f_val_ct,f_val_mr)
populate_hdf5(f_test_combined,f_test_ct,f_test_mr)

f_train_combined.close()
f_val_combined.close()
f_test_combined.close()
