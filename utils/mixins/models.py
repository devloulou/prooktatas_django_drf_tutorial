from django.db import models
from django.utils.timezone import now

class AddDefaultDateColsMixin(models.Model):
    created_date = models.DateTimeField(default=now, editable=False)
    modified_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.modified_date = now()
        super(AddDefaultDateColsMixin, self).save(*args, **kwargs)

    class Meta:
        abstract = True
