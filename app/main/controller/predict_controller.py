from flask import request

from flask_restx import Resource    
from ..util.dto import PredictionDto
from ..service.prediction_service import make_prediction
from ..util.image_processing import process_image


api = PredictionDto.api
_prediction = PredictionDto.prediction

@api.route('/')
class Prediction(Resource):
    @api.doc('Predict if image is cat or dog')
    @api.expect(_prediction, validate=True)
    def post(self):
        """Predict if the image is a cat or a dog"""
        data = request.json
        return make_prediction(data)