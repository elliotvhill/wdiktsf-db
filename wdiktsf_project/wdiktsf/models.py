from django.db import models
    
class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Album(models.Model):
    title = models.CharField(max_length=100)
    releaseYear = models.DateField()
    artist = models.ManyToManyField(
        Artist, help_text='Select an artist(s) for this album', related_name='albums')

    def __str__(self):
        return self.title

class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.RESTRICT, related_name='songs', null=True)
    title = models.CharField(max_length=100)
    albums = models.ManyToManyField(
        Album, help_text='Select an album for this song'
    )

    def __str__(self):
        return self.title