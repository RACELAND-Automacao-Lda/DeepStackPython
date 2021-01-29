from deepstack import SceneRecognition,ServerConfig,pilToBytes
import os
import cv2 
from PIL import Image

DEEPSTACK_URL = os.getenv("TEST_DEEPSTACK_URL")
IMAGES_DIR = os.getenv("TEST_IMAGES_DIR")
config = ServerConfig(DEEPSTACK_URL)

def test_scene_file():
    
    scene = SceneRecognition(config)

    res = scene.processImage(os.path.join(IMAGES_DIR,"scene.jpg"))
    
    assert res.label == "yard"
    assert isinstance(res.confidence,float)

def test_scene_callback():
    
    scene = SceneRecognition(config)

    label = None

    def call(image_data,results):
        label = results.label

    res = scene.processImage(os.path.join(IMAGES_DIR,"scene.jpg"),callback=call)
    
    assert label == "yard"
    
def test_scene_url():
   
    scene = SceneRecognition(config)

    res = scene.processImage("https://flowergardengirl.co.uk/wp-content/uploads/2017/07/Garden-Design-chelsea-screen-raised-beds-wonderful-planting-artificial-grass-olives-trees.jpg")

    assert res.label == "yard"
    assert isinstance(res.confidence,float)

def test_scene_cv2():

    scene = SceneRecognition(config)

    img = cv2.imread(os.path.join(IMAGES_DIR,"scene.jpg"))

    res = scene.processImage(img)

    assert res.label == "yard"
    assert isinstance(res.confidence,float)

def test_scene_pil():

    scene = SceneRecognition(config)

    img = Image.open(os.path.join(IMAGES_DIR,"scene.jpg"))

    res = scene.processImage(img)

    assert res.label == "yard"
    assert isinstance(res.confidence,float)

def test_scene_bytes():

    scene = SceneRecognition(config)

    img = Image.open(os.path.join(IMAGES_DIR,"scene.jpg"))

    img_data = pilToBytes(img)

    res = scene.processImage(img_data)

    assert res.label == "yard"
    assert isinstance(res.confidence,float)

def test_scene_video():

    scene = SceneRecognition(config)

    video = os.path.join(IMAGES_DIR,"video.mp4")

    res = scene.processVideo(video,output="vid.mp4")

    savedVid = cv2.VideoCapture("vid.mp4")

    totalframecount= int(savedVid.get(cv2.CAP_PROP_FRAME_COUNT))

    assert totalframecount == 1193