""" Helper functions """
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def get_sample_images(classes, img_ids, directory):
    sample_imgs = []
    for classnum, cls in enumerate(classes):
        img_id = img_ids[classnum]
        cls_path = os.path.join(directory, cls)
        imgs_cls = [f for f in os.listdir(cls_path) if not f.startswith('.')]
        s_img_path = os.path.join(cls_path, imgs_cls[img_id])
        sample_imgs.append(s_img_path)
    return sample_imgs

def plot_images(num_classes, imgs):
    # Plot images on a grid
    plt.figure(figsize=(20,4))
    for i, img in enumerate(imgs):
        image = mpimg.imread(img)
        plt.subplot(1,num_classes,i+1); plt.title(img.split('/')[-1][:-4]); plt.imshow(image); plt.axis('off')
        plt.xlabel(img.split('/')[-1][:-4])

