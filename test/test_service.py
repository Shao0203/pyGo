import pytest
import unittest.mock as mock
import module.service as service
import requests


@mock.patch('module.service.get_user_from_db')
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = 'Mocked Alice'
    user_name = service.get_user_from_db(1)

    assert user_name == 'Mocked Alice'


@mock.patch('requests.get')
def test_get_users(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "John Doe"}
    mock_get.return_value = mock_response
    user_data = service.get_users()

    assert user_data == {"id": 1, "name": "John Doe"}


@mock.patch('requests.get')
def test_get_users_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response
    with pytest.raises(requests.HTTPError):
        service.get_users()
