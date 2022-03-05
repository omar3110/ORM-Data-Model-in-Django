from django.db import models
from datetime import datetime


class SearchHistory(models.Model):
    user = models.CharField(max_length=70)
    # search_time = models.DateTimeField(editable=True, blank=True, null=True)
    search_time = models.DateTimeField(default=datetime.now())
    # search_time = datetime.datetime.now().timestamp()
    keywords = models.CharField(max_length=200)
    result_list = models.TextField()
