from abc import ABC, abstractmethod
from src.exceptions import ETLException


class Extractor(ABC):
    @abstractmethod
    def extract(self):
        pass


class Transformer(ABC):
    @abstractmethod
    def transform(self, data):
        pass


class Loader(ABC):
    @abstractmethod
    def load(self, data):
        pass


class ETL:
    def __init__(self, extractor: Extractor, transformer: Transformer, loader: Loader):
        self.extractor = extractor
        self.transformer = transformer
        self.loader = loader

    def execute(self):
        try:
            data = self.extractor.extract()
            transformed_data = self.transformer.transform(data)
            self.loader.load(transformed_data)
        except ETLException as e:
            print(f"{type(e).__name__} {e}")
