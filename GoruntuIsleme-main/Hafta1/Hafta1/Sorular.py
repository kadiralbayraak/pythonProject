import numpy as np
from PIL import Image

def getMedian(li):
    # median helper function
    li.sort()
    return li[len(li)/2]

def medianFilterImage(image, kernel_size):
    """ Get a image ndarray and a kernel """
    ret = image.copy()
    size_y = image.shape[0]
    size_x = image.shape[1]
    ofs = kernel_size/2
    for i in range(int(ofs), size_y-int(ofs)):
        for j in range(int(ofs), size_x -int(ofs)):
            vals = []
            for k in range(kernel_size * kernel_size):
                im_val = image[i + k/kernel_size - ofs][j+ k%kernel_size-ofs]
                vals.append(im_val)
            ret[i][j] = getMedian(vals)
    return ret


a = np.array([[2,2,0,0,3],[5,2,1,7,7],[3,5,6,0,2],[2,1,7,3,1],[1,6,4,3,8]])
arr = np.array(a)
removed_noise = medianFilterImage(arr, 3)
print(removed_noise)


