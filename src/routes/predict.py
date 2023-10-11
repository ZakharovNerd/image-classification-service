import cv2
import numpy as np
from dependency_injector.wiring import Provide, inject
from fastapi import Depends, File

from src.containers.containers import AppContainer
from src.routes.routers import router
from src.services.classifier import ImageClassifier


@router.post('/predict')
@inject
def classify_image(
    input_data: bytes = File(),
    service: ImageClassifier = Depends(Provide[AppContainer.image_classifier]),
):
    image_bytes = cv2.imdecode(
        np.frombuffer(input_data, dtype=np.uint8), cv2.IMREAD_COLOR,
    )
    predictions = service.predict(image_bytes)
    return {'result': predictions}
