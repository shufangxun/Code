import torch
# 假设box1维度为[N,4]   box2维度为[M,4]
def iou(self, box1, box2):
	N = box1.size(0)
	M = box2.size(0)

	lt = torch.max(  # 左上角的点
		box1[:, :2].unsqueeze(1).expand(N, M, 2),   # [N,2]->[N,1,2]->[N,M,2]
		box2[:, :2].unsqueeze(0).expand(N, M, 2),   # [M,2]->[1,M,2]->[N,M,2]
	)

	rb = torch.min( # 右下角的点
		box1[:, 2:].unsqueeze(1).expand(N, M, 2),
		box2[:, 2:].unsqueeze(0).expand(N, M, 2),
	)

	wh = rb - lt  # [N,M,2]
	wh[wh < 0] = 0   # 两个box没有重叠区域
	inter = wh[:,:,0] * wh[:,:,1]   # [N,M]

	area1 = (box1[:,2]-box1[:,0]) * (box1[:,3]-box1[:,1])  # (N,)
	area2 = (box2[:,2]-box2[:,0]) * (box2[:,3]-box2[:,1])  # (M,)
	area1 = area1.unsqueeze(1).expand(N,M)  # (N,M)
	area2 = area2.unsqueeze(0).expand(N,M)  # (N,M)

	iou = inter / (area1+area2-inter)
	return iou