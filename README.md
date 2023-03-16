# Assignment 1

1. Create python environment

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run unit tests

```bash
pytest
```

4. Build the module (will create the \*.whl file in `./dist` directory)

```bash
python setup.py bdist_wheel
```

5. Install the module in your other python project

```bash
pip install /path/to/the/whl/from/previous/step
```

6. Use the library

```python
from record_batcher.functions import record_batcher, record_batcher_cpy

def main():
    # batch your records
    batches = record_batcher(...records here...)

    # or if you rather copy the strings and not use originals of the records
    batches_copied = record_batcher_cpy(...records here...)

if __name__ == "__main__":
    main()

```
