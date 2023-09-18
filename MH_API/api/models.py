from django.db import models


# Create your models here.
class Monster(models.Model):
    rank_Levels = [
        ('9', 'Hunter Rank 9'),
        ('8', 'Hunter Rank 8'),
        ('7', 'Hunter Rank 7'),
        ('6', 'Hunter Rank 6'),
        ('5', 'Hunter Rank 5'),
        ('4', 'Hunter Rank 4'),
        ('3', 'Hunter Rank 3'),
        ('2', 'Hunter Rank 2'),
        ('1', 'Hunter Rank 1'),
    ]

    elemental_attributes = [
        ('Fire', 'Fire'),
        ('Water', 'Water'),
        ('Thunder', 'Thunder'),
        ('Ice', 'Ice'),
        ('Dragon', 'Dragon'),
    ]

    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    attribute = models.CharField(max_length=15, choices=elemental_attributes)
    weakness = models.CharField(max_length=20)
    rank = models.CharField(max_length=1, choices=rank_Levels)

