from django.db import models
from auth_app.models import User
from common.models import TimeStampMixin
import uuid

# Create your models here.
class Questions(TimeStampMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='questions/')
    visable = models.BooleanField(default=True)

class Answers(TimeStampMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField()
    question = models.ForeignKey(Questions, 
        on_delete=models.CASCADE, 
        related_name="answers"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    visable = models.BooleanField(default=True)

    class Meta:
        unique_together = ("author", "question")


class Likes(TimeStampMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    answer = models.ForeignKey(Answers, 
        on_delete=models.CASCADE, 
        related_name="likes"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("author", "answer")



