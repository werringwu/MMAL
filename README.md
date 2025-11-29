&nbsp;

## 1. Create Environment

### 1.1 Install the environment with Pytorch 1.11

- Make Conda Environment
```
conda create -n Retinexformer python=3.7
conda activate Retinexformer
```

- Install Dependencies
```
conda install pytorch=1.11 torchvision cudatoolkit=11.3 -c pytorch

pip install matplotlib scikit-learn scikit-image opencv-python yacs joblib natsort h5py tqdm tensorboard

pip install einops gdown addict future lmdb numpy pyyaml requests scipy yapf lpips
```

- Install BasicSR
```
python setup.py develop --no_cuda_ext
```

### 1.2 Install the environment with Pytorch 2

- Make Conda Environment
```
conda create -n torch2 python=3.9 -y
conda activate torch2
```

- Install Dependencies
```
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia

pip install matplotlib scikit-learn scikit-image opencv-python yacs joblib natsort h5py tqdm tensorboard

pip install einops gdown addict future lmdb numpy pyyaml requests scipy yapf lpips thop timm
```

- Install BasicSR
```
python setup.py develop --no_cuda_ext
```

## 2. Testing


```shell
# activate the environment
conda activate Retinexformer

# LOL-v1
python3 Enhancement/test_from_dataset.py --opt Options/RetinexFormer_LOL_v1-MMAL.yml --weights pretrained_weights/LOL_v1.pth --dataset LOL_v1

# LOL-v2-real
python3 Enhancement/test_from_dataset.py --opt Options/RetinexFormer_LOL_v2_real-MMAL.yml --weights pretrained_weights/LOL_v2_real.pth --dataset LOL_v2_real

# LOL-v2-synthetic
python3 Enhancement/test_from_dataset.py --opt Options/RetinexFormer_LOL_v2_synthetic-MMAL.yml --weights pretrained_weights/LOL_v2_synthetic.pth --dataset LOL_v2_synthetic

# SID
python3 Enhancement/test_from_dataset.py --opt Options/RetinexFormer_SID-MMAL.yml --weights pretrained_weights/SID.pth --dataset SID

# SMID
python3 Enhancement/test_from_dataset.py --opt Options/RetinexFormer_SMID-MMAL.yml --weights pretrained_weights/SMID.pth --dataset SMID

# FiveK
python3 Enhancement/test_from_dataset.py --opt Options/RetinexFormer_FiveK-MMAL.yml --weights pretrained_weights/FiveK.pth --dataset FiveK

```

- #### Self-ensemble testing strategy
We add the self-ensemble strategy in the testing code to derive better results. Just add a `--self_ensemble` action at the end of the above test command to use it.


- #### The same test setting as LLFlow, KinD, and recent diffusion models
We provide the same test setting as LLFlow, KinD, and recent diffusion models. Please note that we do not suggest this test setting because it uses the mean of ground truth to enhance the output of the model. But if you want to follow this test setting, just add a `--GT_mean` action at the end of the above test command as

```shell
# LOL-v1
python3 Enhancement/test_from_dataset.py --opt Options/RetinexFormer_LOL_v1-MMAL.yml --weights pretrained_weights/LOL_v1.pth --dataset LOL_v1 --GT_mean

# LOL-v2-real
python3 Enhancement/test_from_dataset.py --opt Options/RetinexFormer_LOL_v2_real-MMAL.yml --weights pretrained_weights/LOL_v2_real.pth --dataset LOL_v2_real --GT_mean

# LOL-v2-synthetic
python3 Enhancement/test_from_dataset.py --opt Options/RetinexFormer_LOL_v2_synthetic-MMAL.yml --weights pretrained_weights/LOL_v2_synthetic.pth --dataset LOL_v2_synthetic --GT_mean
```


- #### Evaluating the Params and FLOPS of models
We have provided a function `my_summary()` in `Enhancement/utils.py`, please use this function to evaluate the parameters and computational complexity of the models, especially the Transformers as

```shell
from utils import my_summary
my_summary(RetinexFormer(), 256, 256, 3, 1)
```


