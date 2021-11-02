from django.db import models
import random
import uuid


DIFF_CHOICES = (
    ('easy', '簡単'),
    ('medium', 'ふつう'),
    ('hard', '難しい'),
)


class Quiz(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="duration of the quiz in minutes")
    required_score_to_pass = models.IntegerField(
        help_text="required score in %")
    difficulty = models.CharField(max_length=6, choices=DIFF_CHOICES)
    created_at = models.DateTimeField('登録日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    class Meta:
        ordering = ['-created_at', ]
        verbose_name_plural = 'Quizes'

    def __str__(self):
        return f"{self.name}-{self.topic}"

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions
        # return questions[:self.number_of_questions]
