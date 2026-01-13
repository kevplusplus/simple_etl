import dlt
import requests
import json
if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


def product_generator(url, params):
    response = requests.get(url,stream=True, params=params)
    response.raise_for_status()

    for line in response.iter_lines():
        if line:
            yield json.loads(line)


@custom
def load_and_export(*args, **kwargs):
    """
    args: The output from any upstream parent blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """

    

    # Specify your custom logic here
    url = 'https://fakestoreapi.com/products'
    params = ''

    pipeline = dlt.pipeline(pipeline_name="product_ingestion", \
                            destination='bigquery', \
                            staging='filesystem', \
                            dataset_name='product_data')

    info = pipeline.run(product_generator(url, params), \
                        table_name="product_data", \
                        write_disposition={"disposition": "merge","strategy": "scd2"}, \
                        credentials = dlt.secrets["destination.bigquery.credentials"])

    print(info)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
