from torchvision import transforms

# Just normalization for validation
data_transforms = {
    'predict_transform': transforms.Compose(
        [
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
        ],
    ),
}
