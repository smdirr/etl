## ETL
### Explanation:
-Extractor, Transformer, Loader Interfaces:

Defines abstract methods extract, transform, and load.
Concrete Classes:

FileExtractor: Implements the extract method to read data from a file.
FileLoader: Implements the load method to write data to a file.
UppercaseTransformer: Implements the transform method to convert data to uppercase.

### ETL Class:

Initialized with instances of Extractor, Transformer, and Loader.
The execute method coordinates the extraction, transformation, and loading flow.

#### Advantages:
- Decoupling: Each component (extraction, transformation, loading) is decoupled, allowing independent modification.
- Flexibility: You can add new extractors, transformers, and loaders without changing the existing code.
- Reusability: You can reuse components in different ETL processes.

Example of use:

`python3 my_etl.py ./data/source.csv ./data/upper.csv`