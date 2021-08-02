from django.db import models


# Create your models here.
class ParentModel(models.Model):
    parent_name = models.CharField(max_length=50)


class ChildModel(ParentModel):
    child_name = models.CharField(max_length=50)
