import pytest

from app import make_app


@pytest.fixture
def client():
    app = make_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_memory_database_loaded(client):
    from database import database
    assert database['67352'].sale_details
    assert database['67352'].schedule
    assert database['87390'].classification


def test_index_view(client):
    response = client.get('/')
    assert response.status_code == 200


@pytest.mark.parametrize(
    ['test_id', 'test_year'], [('67352', '2007'), ('87964', '2011')]
)
def test_search_view(client, test_id, test_year):
    response = client.post('/search', data={'id': test_id, 'year': test_year})
    assert response.status_code == 200
    if test_id == '67352':
        assert b'Market calculated value: 216384.71025600002' in response.data
        assert b'Auction calculated value: 126089.52642' in response.data
    if test_id == '87964':
        assert b'ID not found on database' in response.data
