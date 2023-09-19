from django.db import models

# Create your models here.


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField()
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.project_name