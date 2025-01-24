from survey import AnonymousSurvey as AS
def test_store_response():
    question = "What language did you first learn to speak?"
    my_survey = AS(question)
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        my_survey.store_response(response)
    for response in responses:
        assert response in my_survey.responses