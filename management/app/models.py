from django.db import models

# Create your models here.
class Post(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=100)
    lesson = models.TextField()
    post_to_facebook = models.BooleanField(
        default=False,
        verbose_name="Facebook"
    )
    post_to_instagram = models.BooleanField(
        default=False,
        verbose_name="Instagram"
    )
    post_to_linkedin = models.BooleanField(
        default=False,
        verbose_name="LinkedIn"
    )
    post_to_tiktok = models.BooleanField(
        default=False,
        verbose_name="TikTok"
    )
    image = models.ImageField(upload_to="images", blank=True, null=True)
    request_image = models.BooleanField(
        default=False,
        verbose_name='Request Image With Post'
    )

    generated_content = models.JSONField(
        default=dict,
        blank=True
    )

    generation_status = models.CharField(
        max_length=20,
        default= "pending",
    )

    generation_error = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.name
