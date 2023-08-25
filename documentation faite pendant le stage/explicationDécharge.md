# How to use the aerial waste model on a new dataset.
## Installation
### Installing PyTorch
If you already have a working PyTorch environnement you can skip this part.
The easiest way is to create a new conda environnement [Conda] (link for windows).
Once installed you need to create an environnement.
You can do this by opening an Anaconda command prompt and type :
```bash
conda create --prefix H:/Anaconda/pytorchwaste python=3.8
conda activate H:/Anaconda/pytorchwaste
```
If you need more information on how to install PyTorch please refer to the official [PyTorch] website, for windows this command will do :
```bash
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
```
#### Installing necessary packages :
```bash
pip install matplotlib
pip install pytorch-ignite
```
#### Not necessary but useful to have.
```bash
conda install git
```
[Visual Studio Code] to open and edit the notebooks.
To run the code using VS Code you will need to install the ipykernel package.
```bash
conda install ipykernel --update-deps
```
### Cloning the model
```bash
cd H:/your_path/
git clone https://github.com/linkdow/aerialwaste-model
cd aerialwaste
```
## Usage
Using your favorite notebook editor open *execute_model.ipynb* and select your PyTorch environnement.
Under **Defining global variables** change the ```path_dataset``` variable to where your dataset is and the ```path_save``` to where you want to store the predictions and you can run the code.

 [Conda]: https://conda.io/projects/conda/en/latest/user-guide/install/windows.html#installing-on-windows
 [PyTorch]: https://pytorch.org/get-started/locally/
 [Visual Studio Code]: https://code.visualstudio.com/
