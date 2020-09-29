from django.db import models

# Articles:
#   title
#   content
#   author
#   date
#   image1
#   image2
#
# Papers:
#   title
#   date
#   file
#

auth = [
    ('P1', 'Person 1'),
    ('P2', 'Person 2'),
    ('P3', 'Person 3')
]

category = [
    ('LOC', 'Local'),
    ('NAT', 'National'),
    ('INT', 'International')
]

class Article(models.Model):
    title = models.CharField(max_length=64)
    content = models.CharField(max_length=400)
    cate = models.CharField(max_length=3, choices=category)
    author = models.CharField(max_length=2, choices=auth)
    date = models.DateTimeField()
    img1 = models.ImageField()
    img2 = models.ImageField()

    def __str__(self):
        return self.title

#class NewsPapers(models.Model):
#    name = models.CharField(max_length=50)
#    date = models.DateTimeField(default=timezone.now())
#    paper = models.FileField()