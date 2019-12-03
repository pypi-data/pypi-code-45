import keras
from tensorflow.keras.models import load_model
from keras.utils import CustomObjectScope
from keras.initializers import glorot_uniform
import numpy as np
from keras.preprocessing import image
import PIL.Image
from IPython.display import Image
import tensorflow as tf
import os
import glob
from skimage import io
from reinforcement_terminals.detect_age_gender.model.config_eag import get_config

from pathlib import Path

#cfg = get_config()

# gender_path = pkg_resources.resource_filename(__name__, cfg['model']['gender'])
# age_path = pkg_resources.resource_filename(__name__, cfg['model']['age'])
# print("8********************** {} : {}".format(gender_path, age_path))
this_dir, this_filename = os.path.split(__file__)
def inference():
    with tf.compat.v1.Session() as sesse:
        input_img = tf.compat.v1.placeholder(tf.float32, (None,96,96,3), name = 'image')
        sesse.run(tf.compat.v1.global_variables_initializer())
        gender = load_model("model/gender.h5")
        gender_output  = gender("model/age.h5")
        age =load_model(os.path.join(this_dir, 'model', 'age.h5')) 
        age_output  = age(input_img)
        for root, dirnames, files in os.walk("IDB"):
                if files:
                    images = [io.imread(path) for path in glob.glob(root+'/*.jpg') if io.imread(path).shape[0]==96 and io.imread(path).shape[1]==96]
                    images = np.asarray(images)
                   
                    gender_output_val = sesse.run(gender_output, {input_img:images})
                    age_output_val = sesse.run(age_output, {input_img:images})
                    
                    a = np.greater(gender_output_val[:,0], gender_output_val[:,1])
                    counts = np.bincount(a)
                    gender_inference = "Female" if np.argmax(counts) else "Male"
                    age_inference = "27-37" if np.sum(age_output_val[:,0]) < 0.5 * len(age_output_val[:,0]) else "38-53"
                   
                    print("Gender: {}, age_inference: {}".format(gender_inference, age_inference))


    sesse.close()