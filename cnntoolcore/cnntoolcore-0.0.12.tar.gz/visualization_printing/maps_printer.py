from torchvision import transforms

import matplotlib.pyplot as plt
import numpy as np
from skimage import transform

def plot_tensor(tensor):
    results = transforms.ToPILImage()(tensor)
    print(type(results))
    results.show()

def save_tensor_as_image(tensor, filepath):
    results = transforms.ToPILImage()(tensor)
    results.save(filepath)

def plot_tensor_with_heatmap(pil_img, pixel_weight_array):
    add_heatmap(np.asarray(pil_img), pixel_weight_array, display=True)


def save_tensor_with_heatmap(pil_img, pixel_weight_array, filepath):
    add_heatmap(np.asarray(pil_img), pixel_weight_array, display=False, axis='off', save=filepath)



def add_heatmap(image, heat_map, alpha=0.6, display=False, save=None, cmap='viridis', axis='on', verbose=False):

    height = image.shape[0]
    width = image.shape[1]

    # resize heat map
    heat_map_resized = transform.resize(heat_map, (height, width))

    # normalize heat map
    max_value = np.max(heat_map_resized)
    min_value = np.min(heat_map_resized)
    normalized_heat_map = (heat_map_resized - min_value) / (max_value - min_value)

    # display
    plt.axis(axis)
    fig = plt.imshow(image, interpolation = 'nearest')
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    plt.imshow(255 * normalized_heat_map, alpha=alpha, cmap=cmap)


    if display:
        plt.show()

    if save is not None:
        if verbose:
            print('save image: ' + save)
        plt.savefig(save, bbox_inches='tight', pad_inches=0)

