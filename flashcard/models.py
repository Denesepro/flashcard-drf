from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()
class Flashcard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if len(self.question) > 10:
            return f"{self.question[0:10]}..."
        else:
            return f"{self.question}"
