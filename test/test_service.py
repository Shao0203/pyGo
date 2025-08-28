import pytest
import unittest.mock as mock
import module.service as service


def test_get_user_from_fake_db(monkeypatch):
    fake_db = {1: "Mocked Alice", 2: "Mocked Bob"}
    monkeypatch.setattr(service, 'database', fake_db)
    user = service.get_user_from_db(1)
    assert user == 'Mocked Alice'


@mock.patch('module.service.get_user_from_db')
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = 'Mocked Alice'
    user = service.get_user_from_db(1)
    assert user == 'Mocked Alice'


@mock.patch('requests.get')
def test_get_users_success(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "Mocked User"}
    mock_get.return_value = mock_response
    users = service.get_users()
    assert users == {"id": 1, "name": "Mocked User"}
    mock_get.assert_called_once_with(
        "https://jsonplaceholder.typicode.com/users")


@mock.patch('requests.get')
def test_get_users_failure(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response
    with pytest.raises(service.requests.HTTPError):
        service.get_users()
