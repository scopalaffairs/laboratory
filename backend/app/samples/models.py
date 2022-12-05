import uuid
from django.db import models


class Patient(models.Model):
    """Usually we want to reference reading.patient_uuid per ForeignKey,
    for this poc, we keep it as a standalone field
    """
    patient_uuid = models.UUIDField()


class Reading(models.Model):
    reading_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_uuid = models.UUIDField(default=uuid.uuid4, editable=True)
    value = models.DecimalField(decimal_places=1, max_digits=2)
    unit = models.TextField()
    recorded_at = models.DateTimeField()
