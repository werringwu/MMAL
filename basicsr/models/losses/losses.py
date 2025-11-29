import torch
from torch import nn as nn
from torch.nn import functional as F
import numpy as np

from basicsr.models.losses.loss_util import weighted_loss

_reduction_modes = ['none', 'mean', 'sum']


@weighted_loss   
def l1_loss(pred, target):
    return F.l1_loss(pred, target, reduction='none')


@weighted_loss   
def mse_loss(pred, target):
    return F.mse_loss(pred, target, reduction='none')


# @weighted_loss
# def charbonnier_loss(pred, target, eps=1e-12):
#     return torch.sqrt((pred - target)**2 + eps)


class L1Loss(nn.Module):
    """L1 (mean absolute error, MAE) loss.

    Args:
        loss_weight (float): Loss weight for L1 loss. Default: 1.0.
        reduction (str): Specifies the reduction to apply to the output.
            Supported choices are 'none' | 'mean' | 'sum'. Default: 'mean'.
    """

    def __init__(self, loss_weight=1.0, reduction='mean'):
        super(L1Loss, self).__init__()
        if reduction not in ['none', 'mean', 'sum']:
            raise ValueError(f'Unsupported reduction mode: {reduction}. '
                             f'Supported ones are: {_reduction_modes}')

        self.loss_weight = loss_weight
        self.reduction = reduction

    def forward(self, pred, target, weight=None, **kwargs):
        """
        Args:
            pred (Tensor): of shape (N, C, H, W). Predicted tensor.
            target (Tensor): of shape (N, C, H, W). Ground truth tensor.
            weight (Tensor, optional): of shape (N, C, H, W). Element-wise
                weights. Default: None.
        """
        return self.loss_weight * l1_loss(
            pred, target, weight, reduction=self.reduction)

class MSELoss(nn.Module):
    """MSE (L2) loss.

    Args:
        loss_weight (float): Loss weight for MSE loss. Default: 1.0.
        reduction (str): Specifies the reduction to apply to the output.
            Supported choices are 'none' | 'mean' | 'sum'. Default: 'mean'.
    """

    def __init__(self, loss_weight=1.0, reduction='mean'):
        super(MSELoss, self).__init__()
        if reduction not in ['none', 'mean', 'sum']:
            raise ValueError(f'Unsupported reduction mode: {reduction}. '
                             f'Supported ones are: {_reduction_modes}')

        self.loss_weight = loss_weight
        self.reduction = reduction

    def forward(self, pred, target, weight=None, **kwargs):
        """
        Args:
            pred (Tensor): of shape (N, C, H, W). Predicted tensor.
            target (Tensor): of shape (N, C, H, W). Ground truth tensor.
            weight (Tensor, optional): of shape (N, C, H, W). Element-wise
                weights. Default: None.
        """
        return self.loss_weight * mse_loss(
            pred, target, weight, reduction=self.reduction)

class PSNRLoss(nn.Module):

    def __init__(self, loss_weight=1.0, reduction='mean', toY=False):
        super(PSNRLoss, self).__init__()
        assert reduction == 'mean'
        self.loss_weight = loss_weight
        self.scale = 10 / np.log(10)
        self.toY = toY
        self.coef = torch.tensor([65.481, 128.553, 24.966]).reshape(1, 3, 1, 1)
        self.first = True

    def forward(self, pred, target):
        assert len(pred.size()) == 4
        if self.toY:
            if self.first:
                self.coef = self.coef.to(pred.device)
                self.first = False

            pred = (pred * self.coef).sum(dim=1).unsqueeze(dim=1) + 16.
            target = (target * self.coef).sum(dim=1).unsqueeze(dim=1) + 16.

            pred, target = pred / 255., target / 255.
            pass
        assert len(pred.size()) == 4

        return self.loss_weight * self.scale * torch.log(((pred - target) ** 2).mean(dim=(1, 2, 3)) + 1e-8).mean()

class CharbonnierLoss(nn.Module):
    """Charbonnier Loss (L1)"""

    def __init__(self, loss_weight=1.0, reduction='mean', eps=1e-3):
        super(CharbonnierLoss, self).__init__()
        self.eps = eps

    def forward(self, x, y):
        diff = x - y
        # loss = torch.sum(torch.sqrt(diff * diff + self.eps))
        loss = torch.mean(torch.sqrt((diff * diff) + (self.eps*self.eps)))
        return loss

# def gradient(input_tensor, direction):
#     smooth_kernel_x = torch.reshape(torch.tensor([[0, 0], [-1, 1]], dtype=torch.float32), [2, 2, 1, 1])
#     smooth_kernel_y = torch.transpose(smooth_kernel_x, 0, 1)
#     if direction == "x":
#         kernel = smooth_kernel_x
#     elif direction == "y":
#         kernel = smooth_kernel_y
#     gradient_orig = torch.abs(torch.nn.conv2d(input_tensor, kernel, strides=[1, 1, 1, 1], padding='SAME'))
#     grad_min = torch.min(gradient_orig)
#     grad_max = torch.max(gradient_orig)
#     grad_norm = torch.div((gradient_orig - grad_min), (grad_max - grad_min + 0.0001))
#     return grad_norm

# class SmoothLoss(nn.Moudle):
#     """ illumination smoothness"""

#     def __init__(self, loss_weight=0.15, reduction='mean', eps=1e-2):
#         super(SmoothLoss,self).__init__()
#         self.loss_weight = loss_weight
#         self.eps = eps
#         self.reduction = reduction
    
#     def forward(self, illu, img):
#         # illu: b×c×h×w   illumination map
#         # img:  b×c×h×w   input image
#         illu_gradient_x = gradient(illu, "x")
#         img_gradient_x  = gradient(img, "x")
#         x_loss = torch.abs(torch.div(illu_gradient_x, torch.maximum(img_gradient_x, 0.01)))

#         illu_gradient_y = gradient(illu, "y")
#         img_gradient_y  = gradient(img, "y")
#         y_loss = torch.abs(torch.div(illu_gradient_y, torch.maximum(img_gradient_y, 0.01)))

#         loss = torch.mean(x_loss + y_loss) * self.loss_weight

#         return loss

# class MultualLoss(nn.Moudle):
#     """ Multual Consistency"""

#     def __init__(self, loss_weight=0.20, reduction='mean'):
#         super(MultualLoss,self).__init__()

#         self.loss_weight = loss_weight
#         self.reduction = reduction
    

#     def forward(self, illu):
#         # illu: b x c x h x w
#         gradient_x = gradient(illu,"x")
#         gradient_y = gradient(illu,"y")

#         x_loss = gradient_x * torch.exp(-10*gradient_x)
#         y_loss = gradient_y * torch.exp(-10*gradient_y)

#         loss = torch.mean(x_loss+y_loss) * self.loss_weight
#         return loss

def image_normalization(image):
    min_value = image.min(dim=2, keepdim=True)[0].min(dim=3, keepdim=True)[0]
    max_value = image.max(dim=2,keepdim=True)[0].max(dim=3, keepdim=True)[0]
    image = (image - min_value) / (max_value - min_value)
    return image

def moments_funtion(img_ori_map):
    # return img_ori_map
    # return torch.log(1+torch.abs(img_ori_map))
    # return torch.pow(2,img_ori_map)
    # return torch.sigmoid(img_ori_map)
    return (1+img_ori_map)/(2+img_ori_map)

    # return (2+img_ori_map)/(1+img_ori_map)

def moments_process(image,kernel_size=[11,11],order=3,padding_mode='reflect',isNorm=True,eps=1e-6):
    half_kernel_size = [i // 2 for i in kernel_size]
    padded_image = F.pad(image, (half_kernel_size[0], half_kernel_size[1], half_kernel_size[0], half_kernel_size[1]),
                         mode=padding_mode)
    unfolded_image = F.unfold(padded_image, kernel_size=kernel_size)
    num_windows = unfolded_image.shape[-1]
    unfolded_image = unfolded_image.view(image.shape[0], image.shape[1], -1, num_windows)
    mean_map = unfolded_image.mean(dim=2).view(image.shape[0], image.shape[1], image.shape[2], image.shape[3])
    mean_map_expanded = mean_map.view(image.shape[0], image.shape[1], -1,
                                      num_windows)  
    mean_map_expanded = mean_map_expanded.repeat(1, 1, kernel_size[0] * kernel_size[1], 1)
    moments_map = (unfolded_image - mean_map_expanded).pow(order).mean(dim=2).view(image.shape[0], image.shape[1],
                                                                                image.shape[2], image.shape[3])
    if isNorm:
        moments_map = image_normalization(moments_map)
    return moments_map
@weighted_loss
def moments_amplitude_loss(img_ori,img_dest,kernel_size=[11,11],scale = 1,L_scale=1.0,order=3,padding_mode='reflect',isNorm=True):
    img_ori_map = moments_process(img_ori,kernel_size,order=order,padding_mode=padding_mode,isNorm=isNorm)
    img_dest_map = moments_process(img_dest,kernel_size,order=order,padding_mode=padding_mode,isNorm=isNorm)
    F_recovered = torch.fft.fft2(img_ori*(moments_funtion(img_ori_map.data)*scale))
    F_target = torch.fft.fft2(img_dest*(moments_funtion(img_dest_map.data)*scale))
    amplitude_recovered = torch.abs(F_recovered)
    amplitude_target = torch.abs(F_target)
    amplitude_diff = torch.abs(amplitude_recovered - amplitude_target)
    # amplitude_diff = torch.log(1 + amplitude_diff)
    amplitude_loss_value = torch.mean(L_scale*amplitude_diff, dim=[1, 2, 3])
    loss = torch.mean(amplitude_loss_value)
    return loss

class MMALoss(nn.Module):

    def __init__(self, loss_weight=1.0, reduction='mean'):
        super(MMALoss, self).__init__()
        if reduction not in ['none', 'mean', 'sum']:
            raise ValueError(f'Unsupported reduction mode: {reduction}. '
                             f'Supported ones are: {_reduction_modes}')

        self.loss_weight = loss_weight
        self.reduction = reduction

    def forward(self, pred, target, weight=None, **kwargs):
        return self.loss_weight * moments_amplitude_loss(pred, target, kernel_size=[5,5],
                                                         scale = 1,L_scale=1,order=2,padding_mode='reflect',isNorm=True)
