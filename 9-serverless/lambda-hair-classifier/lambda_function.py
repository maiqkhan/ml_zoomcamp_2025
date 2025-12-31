from io import BytesIO
from urllib import request
import numpy as np
from PIL import Image
import onnxruntime as ort

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img

def prepare_image_for_model(img): 

    img = prepare_image(img, target_size=(200, 200))
    img_array = np.array(img)
    img_array = img_array.astype(np.float32) / 255.0
    img_array = np.transpose(img_array, (2, 0, 1))
    
    mean = np.array([0.485, 0.456, 0.406]).reshape(3, 1, 1)
    std = np.array([0.229, 0.224, 0.225]).reshape(3, 1, 1)
    img_array = (img_array - mean) / std
    
    img_tensor = np.expand_dims(img_array, axis=0).astype(np.float32)

    # transform_pipeline = transforms.Compose([
    #     transforms.ToTensor(),
    #     transforms.Normalize(mean=[0.485, 0.456, 0.406],
    #                          std=[0.229, 0.224, 0.225])
    # ])

    # img_tensor = transform_pipeline(img)
    # img_tensor = img_tensor.unsqueeze(0).numpy()  # Add batch dimension
    
    return img_tensor


def lambda_handler(event, context):
    url = event['url']
    img = download_image(url)
    img_tensor = prepare_image_for_model(img)

    session = ort.InferenceSession("hair_classifier_empty.onnx")
    
    outputs = session.run(None, {session.get_inputs()[0].name: img_tensor})

    predictions = outputs[0].tolist()

    return {
        'statusCode': 200,
        'body': {
            'predictions': predictions
        }
    }