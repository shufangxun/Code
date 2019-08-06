import numpy as np

def nms(dets, thr=0.5):
	'''
	dets: (N,5) 
	前四个维度是(x,y),最后一个维度是score
	只对一个类别做NMS
	'''
	xl = dets[:,0]
	yl = dets[:,1]
	xr = dets[:,2]
	yr = dets[:,3]
	score = dets[:,4]
	
	order = score.argsort()[::-1]   # box按socre降序的索引  
	area = (xr - xl + 1) * (yr - yl + 1) # 所有box的面积数组
	keep = [] # 保留的索引
	
	while order.size > 0:
		i = order[0]
		keep.append(i)
		# box的交集
		xxl = np.maximum(xl[i], xl[order[1:]])  # 数组
		yyl = np.maximum(yl[i], yl[order[1:]])
		xxr = np.minimum(xl[i], xl[order[1:]])
		yyr = np.minimum(xl[i], xl[order[1:]])
		
		inter = np.maximum(0.0, xxr - xxl + 1) * np.maximum(0.0, yyr - yyl + 1)
		union = area[i] + area[order[1:]] - inter  # 数组 广播机制
		iou = inter / union # 数组
		
		idx_list = np.where(iou <= thr)[0]
		order = order[idx_list + 1]
		
	return dets[keep]
		
		
		
		
	
	