import os
import unittest
import tempfile
from unittest.mock import patch, mock_open
from src.file import FileExtractor
from src.exceptions import ExtractionException


class TestFileExtractor(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="test data")
    def test_extract_success(self, mock_file):
        extractor = FileExtractor("dummy_path.txt")
        result = extractor.extract()
        self.assertEqual(result, "test data")
        mock_file.assert_called_once_with("dummy_path.txt", "r")

    @patch("os.path.exists", return_value=False)
    def test_extract_file_not_found(self, mock_exists):
        extractor = FileExtractor("dummy_path.txt")
        with self.assertRaises(ExtractionException) as context:
            extractor.extract()
        self.assertEqual(
            str(context.exception),
            "Error extracting data from file: [Errno 2] No such file or directory: 'dummy_path.txt'",
        )

    @patch("builtins.open", side_effect=IOError("File error"))
    def test_extract_file_read_error(self, mock_file):
        extractor = FileExtractor("dummy_path.txt")
        with self.assertRaises(ExtractionException) as context:
            extractor.extract()
        self.assertTrue(
            "Error extracting data from file: File error" in str(context.exception)
        )

    def test_extract_csv_file(self):
        csv_data = """name,age,country
John Doe,1990-05-20,USA
Maria García,1985-10-30,Spain
Kenji Yamamoto,1978-03-15,Japan
"""
        with tempfile.NamedTemporaryFile(
            delete=False, mode="w", suffix=".csv"
        ) as temp_file:
            temp_file.write(csv_data)
            temp_file_name = temp_file.name

        try:
            extractor = FileExtractor(temp_file_name)
            result = extractor.extract()
            self.assertEqual(result, csv_data)
        finally:
            os.remove(temp_file_name)


if __name__ == "__main__":
    unittest.main()
