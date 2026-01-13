import io
import pandas as pd
import requests
import dlt
import json

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
    


def iterable_to_stream(iterable, buffer_size=io.DEFAULT_BUFFER_SIZE):
    """
    Lets you use an iterable (e.g. a generator) that yields bytestrings as a read-only
    input stream.

    The stream implements Python 3's newer I/O API (available in Python 2's io module).
    For efficiency, the stream is buffered.
    """
    class IterStream(io.RawIOBase):
        def __init__(self):
            self.leftover = None
        def readable(self):
            return True
        def readinto(self, b):
            try:
                l = len(b)  # We're supposed to return at most this much
                chunk = self.leftover or next(iterable)
                output, self.leftover = chunk[:l], chunk[l:]
                b[:len(output)] = output
                return len(output)
            except StopIteration:
                return 0    # indicate EOF
    return io.BufferedReader(IterStream(), buffer_size=buffer_size)

@data_loader
def load_data(*args, **kwargs):
    """
    Template code for loading data from any source.
    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your data loading logic here
    dtypes = {
                'id': pd.Int64Dtype(),
                'title': str,
                'price': float,
                'description': str,
                'category': str,
                'image': str,
                'rating': {
                    'count': pd.Int64Dtype(),
                    'rate': float
                }

    }

    url = 'https://fakestoreapi.com/products'

    
    

    

    # df = pd.read_json(iterable_to_stream(response.iter_content(chunk_size=8*128)))
    
    return product_generator(url)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
