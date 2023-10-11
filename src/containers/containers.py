from dependency_injector import containers, providers

from src.services.classifier import ImageClassifier


class AppContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    image_classifier = providers.Singleton(
        ImageClassifier,
        config=config.services.image_classifier,
    )
