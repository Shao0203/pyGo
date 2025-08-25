import pytest
from module.survey import AnonymousSurvey


@pytest.fixture
def language_survey():
    question = 'What language did you first learn to speak?'
    language_survey = AnonymousSurvey(question)
    return language_survey


def test_store_single_response(language_survey):
    language_survey.store_response('English')
    assert 'English' in language_survey.responses


def test_store_three_responses(language_survey):
    responses = ['English', 'Chinese', 'Spanish']
    for response in responses:
        language_survey.store_response(response)

    for response in language_survey.responses:
        assert response in responses
    # assert len(language_survey.responses) == 3
