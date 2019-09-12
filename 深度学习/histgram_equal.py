import numpy as np
from PIL import Image

def histgram_equal(img):
    img = np.asarray(img) # 转化为数组
    # 统计灰度级别
    numpix = np.zeros([256])
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            numpix[img[i][j]] += 1
    
    # 归一化累积
    propix = numpix / img.size
    sum_pix = np.zeros([256])
    for i,_ in enumerate(sum_pix):
        sum_pix[i] = sum(propix[:i])
    
    # 重新映射
    new_img = np.empty(img.shape, dtype=np.uint8)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            new_img[i][j] = 255 * sum_pix[img[i][j]]
    
    return new_img
    
'''
https://zh.wikipedia.org/wiki/%E7%9B%B4%E6%96%B9%E5%9B%BE%E5%9D%87%E8%A1%A1%E5%8C%96
def histgram_equal(img):
    img = np.asarray(img) # 转化为数组
    # 统计灰度级别
    numpix = np.zeros([256])
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            numpix[img[i][j]] += 1
    
    # 累积灰度
    sumpix = np.zeros([256])
    for i, _ in enumerate(numpix):
        sumpix[i] = sum(numpix[:i])

    # 映射
    min_pix = min(sumpix)
    new_img = np.empty(img.shape, dtype=np.uint8)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            new_img[i][j] = 255 * (sumpix[img[i][j]] - min_pix) // (img.size - min_pix) 
    
    return new_img
'''

    
if __name__ == "__main__":
    img = Image.open('./Desktop/test.jpg')
    img = img.convert('L') # 转化为灰度图 8bit
    new_img = histgram_equal(img)
    new_img = Image.fromarray(new_img)

