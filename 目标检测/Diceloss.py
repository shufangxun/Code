import torch 
import torch.functional as F
class DiceLoss(nn.Module):
    
    def __init__(self, smooth=0, eps=1e-7):
        super(DiceLoss, self).__init__()
        self.smooth = smooth
        self.eps = eps

    def forward(self, output, target):
        inter = 2 * (torch.sum(output * target) + self.smooth) 
        union = torch.sum(output) + torch.sum(target) + self.smooth + self.eps
        return 1 - inter / union 

class WeightedBCELoss(nn.Module):
    def __init__(self, size_average=True):
        super(WeightedBCELoss, self).__init__()
        self.size_average = size_average


    def forward(self, input, target):
        # _assert_no_grad(target)
        target = target.float()
        # input = input[0][0]
        beta = 1 - torch.mean(target)
        # input = F.softmax(input, dim=1)
        input = input[:, 0, :, :]
        # target pixel = 1 -> weight beta
        # target pixel = 0 -> weight 1-beta
        weights = 1 - beta + (2 * beta - 1) * target
        return F.binary_cross_entropy(input, target, weights, reduction='mean')

def mixed_dice_bce_loss(output, target, dice_weight=0.2, dice_loss=None,
                bce_weight=0.9, bce_loss=None, smooth=0, dice_activation='sigmoid'):

    num_classes = output.size(1)
    target = target[:, :num_classes, :, :].long()
    if bce_loss is None:
        bce_loss = nn.BCEWithLogitsLoss()
    if dice_loss is None:
        dice_loss = multiclass_dice_loss
    return dice_weight * dice_loss(output, target, smooth, dice_activation) + bce_weight *                                                             bce_loss(output, target)