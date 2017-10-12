import os

PY_SCRIPT="/home/marsdenlab/projects/DeepVessel/python/segment_volume.py"
IMAGES="/home/marsdenlab/projects/DeepLofting/python/images.txt"
VOLUMES="/home/marsdenlab/projects/DeepLofting/python/ct_test.txt"
OUTPUT_DIR="/media/marsdenlab/Data2/datasets/DeepLofting/i2i3d/"
MODEL_DIR="/home/marsdenlab/projects/DeepVessel/python/models/i2i_ct/i2i"

#get images
images_file = open(IMAGES).readlines()
images_file = [s.replace('\n','') for s in images_file]

volumes_file = open(VOLUMES).readlines()
volumes_file = [s.replace('\n','') for s in volumes_file]

for v in volumes_file:
    #get image file
    im = [i for i in images_file if v in i][0]
    print im

    #make output filename
    o_fn = "{}{}_i2i3d.mha".format(OUTPUT_DIR,v)

    #execute segment script with required parameters
    #volume, output, model_dir, --modality
    status = os.system("python {} {} {} {} --modality ct".format(
        PY_SCRIPT,im, o_fn, MODEL_DIR
    ))

    if not status == 0:
        raise RuntimeError('executing script failed at {}'.format(v))
