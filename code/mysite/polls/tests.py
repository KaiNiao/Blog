import datetime

from django.test import TestCase
from django.utils import timezone
from .models import Question


# Create your tests here.
class QuestionMethodTests(TestCase):
    """
    在将来发布的问卷应该返回False，自动化测试
    """
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(time)  # 创建实例用于测试
        self.assertIs(future_question.was_published_recently(), False)