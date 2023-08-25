## User guide for Large-Selective-Kernel-Network
### Installation
```bash
conda create -n LSKN python=3.8 -y
conda activate LSKN
conda install pytorch==1.8.0 torchvision==0.9.0 cudatoolkit=10.2 -c pytorch -y
pip install -U openmim
mim install mmcv
mim install mmcv-full
mim install mmdet
# For using notebooks through VSCode
conda install ipykernel -y

git clone https://github.com/zcablii/Large-Selective-Kernel-Network.git
cd Large-Selective-Kernel-Network
pip install -v -e .
# Needs to be reinstalled in order to work
pip install pillow==9.0.0
pip install timm
```


### Download pretrained model and config from [LSKN github]
For the detection on barges I took the **LSKNet_S\*** model.
Use inference_bateau_propre.ipynb if you want to replicate the results for the ships in Ile de France.
In order to isolate barge, I kept results with a score > 0.4 and width > 9 

Or you can use other options in the demo folder.

[LSKN github]: https://github.com/zcablii/Large-Selective-Kernel-Network
