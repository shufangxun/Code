import numpy as np
def resize(src, dst_h, dst_w):
    '''
    邻域插值
    '''
    src_h, src_w, channels = src.shape
    ratio_h = src_h / dst_h
    ratio_w = src_w / dst_h
    dst = np.zeros((dst_h, dst_w), np.int8)
    for i in range(channels):
        for y in range(dst_h):
            for x in range(dst_w):
                x_ori = int(x * ratio_w)
                y_ori = int(y * ratio_h)
                dst[y, x, i] = src[y_ori, x_ori, i]
    return dst