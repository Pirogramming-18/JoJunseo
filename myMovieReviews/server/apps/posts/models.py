from django.db import models

GENRE = {
    ('action','액션'),('SF','SF'),('comedy','코미디'),('romance','로맨스'),('thriller','스릴러'),('fantasy','판타지'),('music','음악')
}

class Post(models.Model):
    title = models.CharField(max_length=20)
    year = models.IntegerField()
    genre = models.CharField(max_length=20, choices=GENRE, null=True)
    rating = models.FloatField()
    time = models.IntegerField()
    minute = models.IntegerField()
    hour = models.IntegerField( )
    review = models.TextField()
    producer = models.CharField(max_length=30)
    actor = models.CharField(max_length=50)
    poster = models.CharField(max_length=1000, null=True, blank=True)
