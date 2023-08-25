# Change detection using Open-CD
## Install
Download Open-cd official repository.
```bash
git clone https://github.com/likyoo/open-cd
```
Create Anaconda environnement
```bash
conda env create -f environment.yml
```
Download [Weights Changer] if you want to use the changer model (same model that I used)
Then in the open-cd folder you just created :
```bash
mkdir changer_ckpt
```
And put the weights of the model you just downloaded in this folder
## Usage
### In order to run the inference :
1. Setting up the dataset (images names must be the same between each folder)
```
test/
......A/
.........image_1.png
.........image_2.png
......B/
.........image_1.png
.........image_2.png
......label/
.........image_1.png
.........image_2.png
```
Note : If you don't have label image for your dataset a temporary fix is to copy a black/empty image instead with the correct filename.

2. You need to change the path to your data in
```
openlab\open-cd\configs\common\standard_256x256_40k_levircd.py
```
3. When everything is in place :
```bash
conda activate opencd
cd Path/to/where/you/cloned/the/repo
mkdir temp_infer
# It's where the mask results will be stored
python tools/test.py configs/changer/changer_ex_s101_512x512_40k_levircd.py  changer_ckpt/ChangerEx_s101-512x512_40k_levircd_20220710-082722.pth --show-dir temp_infer
```
## Tools
Furthermore,  there is a notebook template named *cut1021.ipynb* for extracting images from a raster in order to create your own dataset.

Also, for some reasons the default test script is trying to load the training dataset, in order to tackle this, a temporary fix is to copy the train folder provided next to the test folder. This contains 3 images just to pass this step in the test script.


[Open-cd]: https://github.com/likyoo/open-cd
[Weights Changer]: https://drive.google.com/file/d/128FVQL-93oN5lUMGuqDcmPU-80RiXBhn/view
