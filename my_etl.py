import argparse
import logging
from src.file import FileExtractor, FileLoader
from src.transformer import UppercaseTransformer
from src.etl import ETL


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run ETL process.")
    parser.add_argument("source", type=str, help="Source file path")
    parser.add_argument("destination", type=str, help="Destination file path")
    args = parser.parse_args()

    file_extractor = FileExtractor(args.source)
    file_loader = FileLoader(args.destination)
    logger.debug("executing ETL with params {file_extractor} {file_loader}")

    uppercase_transformer = UppercaseTransformer()

    etl = ETL(file_extractor, uppercase_transformer, file_loader)
    etl.execute()
    logger.debug("ETL ends sucessfully")
