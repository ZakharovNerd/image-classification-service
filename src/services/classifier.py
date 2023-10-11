from typing import Dict, List

import cv2
import numpy as np
import torch
from PIL import Image

from src.services.preprocess_utils import data_transforms


class ImageClassifier:
    def __init__(self, config: Dict):
        self._model_path = config['model_path']
        self._device = config['device']
        self._model = torch.load(self._model_path, map_location=self._device)
        self._threshold = config['threshold']
        self._class_num2class = dict(enumerate(config['classes']))

    def predict(self, image_bytes: np.ndarray) -> List[str]:
        image = cv2.cvtColor(image_bytes, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = data_transforms['predict_transform'](image).unsqueeze(
            0,
        )  # Add batch dimension

        self._model.eval()

        self._model.to(self._device)
        image = image.to(self._device)

        with torch.no_grad():
            outputs = self._model(image)[0]

        return [
            self._class_num2class[class_num]
            for class_num, prob in enumerate(outputs)
            if prob > self._threshold
        ]
