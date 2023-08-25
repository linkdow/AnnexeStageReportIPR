# Comment utiliser YOLOv6
# Installation

Le plus simple est de faire un nouvel environnement [Conda].
```bash
conda create --prefix H:/Anaconda/Yolo python=3.8
conda activate H:/Anaconda/Yolo
conda install git
```
Ensuite à l'endroit de votre choix :
```bash
git clone https://github.com/meituan/YOLOv6
cd YOLOv6
pip install -r requirements.txt
```
Pour les piscines j'ai utilisé ce [dataset] et j'avais déjà converti auparavant les annotations au format csv.
Dans le [dataset] que j'ai pris il y environ 2400 images dont seulement la moitié avec des piscines dessus. Dans la documentation YOLO il est recommandé d'avoir entre 0-10% d'images "background" (sans éléments à reconnaître dessus). Donc j'ai pris 100 images background pour un peu plus de 1200 images labellisées.

# Entraînement
## Préparation des données
Les plus simple est de suivre l'explication de la documentation [Yolov6].
Dans le cas ou les labels sont dans un csv voici un code exemple pour formater les annotations au bon format :
```python
import pandas as pd
# Pour importer les données
df = pd.read_csv("swimming_pools_labels_512x512.csv")
# Calcul des valeurs
col = ["image_id","class_id","center_x","center_y","bbox_width","bbox_height"]
df["bbox_width"] = df['xmax'] - df['xmin']
df['bbox_height'] = df['ymax'] - df['ymin']
df['center_x'] = df['xmin'] + df['bbox_width'] / 2
df['center_y'] = df['ymin'] + df['bbox_height'] / 2
df.drop(columns=["image_path","bbox_area"],inplace=True)
df["class_id"] = 0
size_img = 512
df["bbox_width"] = df["bbox_width"] / size_img
df['bbox_height'] = df['bbox_height'] / size_img
df['center_x'] = df['center_x'] / size_img
df['center_y'] = df['center_y'] / size_img

# Sauvegarde au bon format
import  shutil
# specify the source and destination directories
src_dir = r'H:\Datasets\dataset_piscines\CANNES_TILES_512x512_PNG\CANNES_TILES_512x512_PNG'
dst_dir = r'H:\Datasets\dataset_piscines\yolo_pool\images\train'
label_path = "H:/Datasets/dataset_piscines/yolo_pool/labels/train/"
for  i  in  range(0,856):
	## Copy images
	# specify the file name to be copied
	file_name = names[i]
	# use shutil.copy() to copy the file from source to destination
	shutil.copy(src_dir + '/' + file_name+".png", dst_dir + '/' + file_name + ".png")
	## Create label for image
	with  open(label_path+file_name+".txt", 'w') as  file:
		# write some text to the file
		rows = df[df["image_id"] == names[i]]
		yolo_string = rows[["class_id","center_x","center_y","bbox_width","bbox_height"]].to_string(header=False,index=False)
		file.write(yolo_string)
		if  i%100 == 0:
			print(i)
```
## Lancement de l'entraînement
Une fois le tutoriel suivi, on peut lancer le training avec la commande suivante :
Si possible essayer de maximiser le batch size.
```bash
python tools/train.py --batch 16 --conf configs/yolov6s_finetune.py --data data/dataset.yaml --fuse_ab --device 0 --img-size 512
```

# Inférence
Pour tester l'inférence sur une ou deux images, il est préférable d'utiliser le notebook ***inference.ipynb*** dans le répertoire YOLOv6. En pensant à changer le path des images et du model.
## Par batch
Sous windows seulement, il y a un problème avec le calcul du chemin relatif dans pour trouver les images pour l'inférence.
Dans le cas où une erreur ressemblerait à ça **ValueError: path is on drive C:, start on drive d:** lors du lancement de l'inférence voici un fix :
Dans inferer.py se trouvant ici : **/YOLOv6/yolov6/core/inferer.py** enlever toutes les mentions de la variable ***rel_path*** se trouvant à partir de la ligne 86.
Le nouveau code devrait ressembler à ça :
```python
save_path = osp.join(save_dir, osp.basename(img_path)) # im.jpg
txt_path = osp.join(save_dir, 'labels', osp.splitext(osp.basename(img_path))[0])
print(txt_path)
os.makedirs(osp.join(save_dir), exist_ok=True)
```
## Lancement de l'inférence
```bash
python tools/infer.py --weights output_dir/name/weights/best_ckpt_pool.pt --yaml data/dataset.yaml --source data/images/ --device 0 --save-txt --not-save-img
```
Les labels prédit sont enregistré dans le chemin suivant : **\YOLOv6\runs\inference\exp\labels**

Voici un exemple de code pour transformer les labels au format csv :
```python
import pandas as pd
import os
data = []

image_size = 512

# Loop through all text files in the 'labels' folder
for  filename  in  os.listdir('labels'):
	if  filename.endswith('.txt'):
		# Extract the image ID from the filename
		img_id = filename.split('.')[0]
		# Read the label information from the text file
		with  open(os.path.join('labels', filename), 'r') as  f:
			for  line  in  f:
				# Parse the label information
				class_id, center_x, center_y, bbox_width, bbox_height, confidence = line.strip().split(' ')
				# Calculate the coordinates of the bounding box
				xmin = (float(center_x) - float(bbox_width) / 2) * image_size
				ymin = (float(center_y) - float(bbox_height) / 2) * image_size
				xmax = (float(center_x) + float(bbox_width) / 2) * image_size
				ymax = (float(center_y) + float(bbox_height) / 2) * image_size
				# Append the label information to the list
				data.append([img_id, xmin, ymin, xmax, ymax, confidence])
# Create a Pandas DataFrame from the list of label information
df = pd.DataFrame(data, columns=['Id', 'xmin', 'ymin', 'xmax', 'ymax', 'confidence'])
df.to_csv("labels.csv",index=False)
```


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen.)

   [Conda]: https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
   [Yolov6]: https://github.com/meituan/YOLOv6/blob/main/docs/Train_custom_data.md
   [dataset]: https://www.kaggle.com/datasets/alexj21/swimming-pool-512x512
