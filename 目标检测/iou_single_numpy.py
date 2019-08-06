
import numpy as np

def iou(box1, box2):
	'''
	box [x1,y1,x2,y2]
	'''
	xx1 = max(box1[0], box2[0])
	yy1 = max(box1[1], box2[1])
	xx2 = min(box1[2], box2[2])
	yy2 = min(box1[3], box2[3])
	
	box1Area = (box1[2] - box1[0] + 1) * (box1[3] - box1[1] + 1)
	box2Area = (box2[2] - box2[0] + 1) * (box2[3] - box2[1] + 1)
	
	inter = max(xx2 - xx1 + 1, 0.0) * max(yy2 - yy1 + 1, 0.0) 
	union = box1Area + box2Area - inter 
	 
	iou = inter / union
	
	return iou 
	