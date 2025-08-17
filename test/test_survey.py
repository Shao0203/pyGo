from module.survey import AnonymousSurvey
import pytest


@pytest.fixture
def language_survey():
    return AnonymousSurvey('what is your mother language?')


def test_store_single_response(language_survey):
    language_survey.store_response('English')
    assert 'English' in language_survey.responses


def test_store_three_responses(language_survey):
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses
