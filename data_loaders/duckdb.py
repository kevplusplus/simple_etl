import duckdb

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    """
    Template code for loading data from any source.

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your data loading logic here
    conn = duckdb.connect(f"product_ingestion.duckdb")

    # let's see the tables
    conn.sql(f"SET search_path = product_staging")
    print('Loaded tables: ')
    display(conn.sql("show tables"))

    dim_customer = conn.sql("PRAGMA show_tables;").df()
    display(dim_customer)
    conn.close()
    return {}


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
