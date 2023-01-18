from django.db import models

class Tool(models.Model):
    name = models.CharField(max_length=30)
    kind = models.CharField(max_length=50)
    content = models.TextField()


class Idea(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='posts/%Y%m%d')
    content = models.TextField()
    interest = models.IntegerField()
    devtool = models.ForeignKey(Tool, on_delete=models.CASCADE, related_name="idea_tool")


