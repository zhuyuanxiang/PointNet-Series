"""
=================================================
@path   : PointNet-Series -> pointnet_utils.py
@IDE    : PyCharm
@Author : zYx.Tom, 526614962@qq.com
@Date   : 2022-01-20 11:02
@Version: v0.1
@License: (C)Copyright 2020-2022, zYx.Tom
@Reference:
@Desc   :
==================================================
"""
from datetime import datetime
import torch


def feature_transform_regularize(trans):
    #
    d = trans.size()[1]
    I = torch.eye(d)[None, :, :]
    I = I.cuda() if trans.is_cuda else I
    loss = torch.mean(torch.norm(torch.bmm(trans, trans.transpose(2, 1)) - I, dim=(1, 2)))
    return loss


def main(name):
    print(f'Hi, {name}', datetime.now())
    pass


if __name__ == "__main__":
    __author__ = 'zYx.Tom'
    main(__author__)
