import numpy as np

def nms(predicts_dict, threshold=0.5):
	for object_name, bbox in predicts_dict.items():
    	#对每一个类别分别进行NMS；一次读取一对键值（即某个类别的所有框）
		bbox_array = np.array(bbox, dtype=np.float)
		
		x1 = bbox_array[:, 0]
		y1 = bbox_array[:, 1]
		x2 = bbox_array[:, 2]
		y2 = bbox_array[:, 3]
		scores = bbox_array[:, 4]
		
		order = scores.argsort()[::-1]
		areas = (x2 - x1 + 1) * (y2 - y1 + 1)
		keep = []
		
		# 按score从高到低遍历bbx，移除所有与该矩形框的IoU值大于threshold的矩形框
		while order.size > 0:
			i = order[0]
			keep.append(i)#保留当前最大confidence对应的bbx索引
			
			# 获取所有与当前bbx的交集对应的左上角和右下角坐标，并计算IoU（注意这里是同时计算一个bbx与其他所有bbx的IoU）
			xx1 = np.maximum(x1[i], x1[order[1:]]) 
			yy1 = np.maximum(y1[i], y1[order[1:]])
			xx2 = np.minimum(x2[i], x2[order[1:]])
			yy2 = np.minimum(y2[i], y2[order[1:]])
			
			inter = np.maximum(0.0, xx2-xx1+1) * np.maximum(0.0, yy2-yy1+1)
			iou = inter / (areas[i] + areas[order[1:]] - inter) # 注意这里都是采用广播机制，同时计算了置信度最高的框与其余框的IoU
			idx = np.where(iou <= threshold)[0]
			order = order[idx + 1]
		bbox = bbox_array[keep]
		predicts_dict[object_name] = bbox.tolist()
		
	return predicts_dict