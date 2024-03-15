import base64
from PIL import Image
import io
from flask import request,jsonify

from app.main import ml_model
from ..util.image_processing import process_image
from typing import Dict, Tuple

def make_prediction(data: Dict[str,str])->Tuple[Dict[str,str],int]:
    encoded = data['image'] 
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))
    processed_image = process_image(image,target_size=(224,224))

    prediction=ml_model.predict(processed_image).tolist()

    response = {
        'prediction':{
            'dog':prediction[0][0],
            'cat':prediction[0][1]
        }
    }

    return response,200