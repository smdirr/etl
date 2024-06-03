import argparse
from src.file import FileExtractor, FileLoader
from src.transformer import UppercaseTransformer
from src.etl import ETL


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run ETL process.")
    parser.add_argument("source", type=str, help="Source file path")
    parser.add_argument("destination", type=str, help="Destination file path")
    args = parser.parse_args()

    file_extractor = FileExtractor(args.source)
    file_loader = FileLoader(args.destination)

    uppercase_transformer = UppercaseTransformer()

    etl = ETL(file_extractor, uppercase_transformer, file_loader)
    etl.execute()
