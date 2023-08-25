# Image classification using Tensorflow
## Installation
The easiest way is to create a new conda or miniconda environnement [Conda] (link for windows).
Once installed you need to create an environnement :
```bash
conda create --prefix H:/Anaconda/tensorflow python=3.8
conda activate H:/Anaconda/tensorflow
```
####  Tensorflow
Next you will need to install [Tensorflow], you can follow the step by step tutorial on their website but here is a quick recap :
```bash
conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0
python -m pip install tensorflow==2.9
```
Anything above 2.10 is not supported on the GPU on Windows Native. Also, there is a bug on TensorFlow version greater than 2.9 preventing the use of EfficientNet as a backbone for transfer learning.
#### Necessary packages
```bash
pip install numpy
pip install matplotlib
```
####  Not necessary but useful to have.
[Visual Studio Code] to open and edit the notebooks.

To clone the repository :
```bash
conda install git
```
To run the code using VS Code you will need to install the ipykernel package.
```bash
conda install ipykernel --update-deps
```
### Cloning the repository
```bash
cd H:/your_path/
git clone https://github.com/linkdow/TF-Image-Classification
cd TF-Image-Classification
```
## Usage
#### Training
Before being able to train on your own dataset you need to do a few things.
- In order to load the dataset, the code uses the function ```tf.keras.utils.image_dataset_from_directory()``` if you want to use the code as is you need to ensure that your dataset follow this directory structure :
(images names are not relevant)
	```
	main_directory/
	...class_a/
	......a_image_1.jpg
	......a_image_2.jpg
	...class_b/
	......b_image_1.jpg
	......b_image_2.jpg
	```
- Next in *Classification_transfer_learning_template.ipynb* you need to change the different variables located under the **Defining global variables** according to your dataset.
- Finally you can change the backbone of your model, by default the *EfficientNetB3* is used. It is located under the **Model Definition** section in the notebook.
A full list of available model can be found here : [Keras Model]

#### Inference
Once you trained your model you can use the *inference_template.ipynb*  notebook to predict classes on unlabelled data.
In order to do that you can open the notebook and you only need to change the variables under **Defining global variables** section according to your needs, and you're good to go.

[Conda]: https://conda.io/projects/conda/en/latest/user-guide/install/windows.html#installing-on-windows
[Tensorflow]: https://www.tensorflow.org/install/pip#windows-native
[Visual Studio Code]: https://code.visualstudio.com/
[Keras Model]: https://keras.io/api/applications/
