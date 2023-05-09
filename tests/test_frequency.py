import pytest

from mootdx.quotes import Quotes
from mootdx.utils import FREQUENCY


@pytest.fixture(scope='function')
def client():
    return Quotes.factory(market='std')


@pytest.mark.skip(reason='暂时不做重复测试')
@pytest.mark.parametrize('i,v', [(i, v) for i, v in enumerate(FREQUENCY)])
def test_to_data_empty(client, i, v):
    assert all(client.bars(symbol='600036', frequency=i) == client.bars(symbol='600036', frequency=v))
