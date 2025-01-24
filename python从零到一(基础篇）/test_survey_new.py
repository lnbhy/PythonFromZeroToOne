import pytest
from survey import AnonymousSurvey as AS
@pytest.fixture
def language_survey():
    # 定义调查问卷的问题
    question = "What language did you first learn to speak?"
    # 创建一个调查问卷对象，使用问题作为参数
    language_survey = AS(question)
    # 返回调查问卷对象
    return language_survey
def test_store_response(language_survey):
    # 定义一个包含语言名称的列表
    responses = ['English', 'Spanish', 'Mandarin']
    # 遍历responses列表中的每个元素
    for response in responses:
        # 调用language_survey返回的AnonymousSurvey对象的store_response方法，将每个语言名称存储起来
        language_survey.store_response(response)
    # 再次遍历responses列表中的每个元素
    for response in responses:
        # 使用断言语句检查每个语言名称是否存在于language_survey对象的responses属性中
        assert response in language_survey.responses