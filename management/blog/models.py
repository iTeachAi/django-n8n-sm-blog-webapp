from django.db import models

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=100)
    lesson_description = models.TextField()
    suggested_topics = models.JSONField(blank=True, null=True, editable=False)
    generation_error = models.TextField(blank=True, editable=False)

    def __str__(self):
        return self.name
    
class BlogQuestions(models.Model):
    topic_request = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name='blog_questions',
    )

    generated_topic = models.CharField(max_length=300)
    principle = models.TextField(blank=True)
    question1 = models.CharField(max_length=300, editable=False)
    answer1 = models.TextField()

    question2 = models.CharField(max_length=300, editable=False)
    answer2 = models.TextField()

    question3 = models.CharField(max_length=300, editable=False)
    answer3 = models.TextField()

    question4 = models.CharField(max_length=300, editable=False)
    answer4 = models.TextField()

    question5 = models.CharField(max_length=300, editable=False)
    answer5 = models.TextField()

    def __str__(self):
        return self.generated_topic


class Blog(models.Model):
    blog_questions = models.OneToOneField(
        BlogQuestions,
        on_delete=models.CASCADE,
        related_name='blog',
    )
    name = models.CharField(max_length=150)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    category = models.CharField(max_length=50)
    summary = models.TextField()
    content = models.TextField()
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    


