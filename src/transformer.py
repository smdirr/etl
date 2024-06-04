import logging
from src.exceptions import TransformationException
from src.etl import Transformer


logger = logging.getLogger(__name__)


class UppercaseTransformer(Transformer):
    def transform(self, data):
        if data:
            try:
                transformed_data = data.upper()
                logger.info("Data transformed successfully to uppercase")
                return transformed_data
            except Exception as e:
                logger.error(f"Error transforming data: {e}")
                raise TransformationException(f"Error transforming data: {e}")
        else:
            logger.error(f"No data to transform")
            raise TransformationException("No data to transform")
