import logging
from src.exceptions import ExtractionException, LoadingException
from src.etl import Extractor, Loader


logger = logging.getLogger(__name__)


class FileExtractor(Extractor):
    def __init__(self, filepath):
        self.filepath = filepath

    def extract(self):
        try:
            with open(self.filepath, "r") as file:
                data = file.read()
            logger.info("Data extracted successfully from file")
            return data
        except Exception as e:
            raise ExtractionException(f"Error extracting data from file: {e}")


class FileLoader(Loader):
    def __init__(self, filepath):
        self.filepath = filepath

    def load(self, data):
        try:
            with open(self.filepath, "w") as file:
                file.write(data)
            logger.info("Data loaded successfully to file")
        except Exception as e:
            raise LoadingException(f"Error loading data to file: {e}")
