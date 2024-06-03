from src.exceptions import TransformationException
from src.etl import Transformer


class UppercaseTransformer(Transformer):
    def transform(self, data):
        if data:
            try:
                transformed_data = data.upper()
                print("Data transformed successfully to uppercase")
                return transformed_data
            except Exception as e:
                raise TransformationException(f"Error transforming data: {e}")
        else:
            raise TransformationException("No data to transform")
