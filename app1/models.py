from django.db import models

from django_jalali.db import models  as jmodels




class Test(models.Model):
    date = jmodels.jDateField()
