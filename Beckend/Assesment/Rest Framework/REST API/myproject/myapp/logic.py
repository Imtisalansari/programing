from comments.models import Comment
from django.core.exceptions import ObjectDoesNotExist

def get_all_comments():
    return Comment.objects.all()

def create_comment(data):
    return Comment.objects.create(**data)

def delete_comment(comment_id):
    try:
        comment = Comment.objects.get(pk=comment_id)
        comment.delete()
        return True
    except ObjectDoesNotExist:
        return False
