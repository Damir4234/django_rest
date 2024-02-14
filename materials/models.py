from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100)
    preview = models.ImageField(upload_to='course_previews/', blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    preview = models.ImageField(upload_to=None, blank=True)
    video_link = models.URLField(blank=True)
    course = models.ForeignKey(
        Course, related_name='lessons', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
