from django.test import TestCase
from .models import Comment

class CommentModelTest(TestCase):
    def test_create_comment(self):
        comment = Comment.objects.create(username="John", content="Test comment")
        self.assertEqual(comment.username, "John")
