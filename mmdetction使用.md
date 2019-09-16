### 安装 (基于SJTU)
1. 创建环境并激活
    ```Shell
    module load anaconda3/2019.07
    conda create -n mmdet python=3.6
    source activate mmdet
    ```

2. 换清华源并安装pytorch和依赖库
   ```Shell
   # 修改 .condarc
    channels:
        - defaults
    show_channel_urls: true
    default_channels:
        - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
        - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
    custom_channels:
        conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
        msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
        bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
        menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
        pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud

    # 安装pytorch
    conda install pytorch torchvision cudatoolkit=10.0 -c pytorch

    # 依赖库
    conda install cython
    pip install mmcv
    conda install -c cmusselle gcc
   ```

3. 安装mmdetection
```Shell

```