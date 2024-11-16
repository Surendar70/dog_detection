!nvidia-smi


!git clone https://github.com/ultralytics/yolov5.git 


%cd yolov5


!pip install -r requirements.txt

from roboflow import Roboflow
rf = Roboflow(api_key="DDCKAczcbafR3Gkr2GSe")
project = rf.workspace("dog-vvtv0").project("dog-tcgjx")
version = project.version(1)
dataset = version.download("yolov5-obb")
!pip install roboflow



!python train.py --img 640 --batch 3 --epochs 2 --data /content/yolov5/DOG-1/data.yaml --weights yolov5m.pt 


/content/yolov5/best.pt

