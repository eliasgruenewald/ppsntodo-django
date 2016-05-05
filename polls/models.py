from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class ToDo(models.Model):
    title = models.CharField(max_length=200)

    priority = models.IntegerField(validators=[MinValueValidator(0),
                                            MaxValueValidator(5)])

    progress = models.IntegerField(validators=[MinValueValidator(0),
                                            MaxValueValidator(100)])

    description = models.CharField(max_length=200)

    name = models.CharField(max_length=200)

    deadline_day = models.IntegerField(validators=[MinValueValidator(0),
                                                MaxValueValidator(31)])

    deadline_month = models.IntegerField(validators=[MinValueValidator(0),
                                                 MaxValueValidator(12)])

    deadline_year = models.IntegerField(validators=[MinValueValidator(2016),
                                               MaxValueValidator(2019)])

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.title