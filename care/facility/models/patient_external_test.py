from django.db import models

from care.facility.models import FacilityBaseModel, PatientRegistration
from care.users.models import User, Ward, LocalBody, District


class PatientExternalTest(FacilityBaseModel):
    srf_id = models.CharField(max_length=255)
    name = models.CharField(max_length=1000)
    age = models.IntegerField()
    age_in = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    address = models.TextField()
    mobile_number = models.CharField(max_length=15)
    is_repeat = models.BooleanField()
    patient_status = models.CharField(max_length=15)
    ward = models.ForeignKey(Ward, on_delete=models.PROTECT, null=True, blank=True)
    local_body = models.ForeignKey(LocalBody, on_delete=models.PROTECT, null=False, blank=False)
    district = models.ForeignKey(District, on_delete=models.PROTECT, null=False, blank=False)
    source = models.CharField(max_length=255)
    patient_category = models.CharField(max_length=255)
    lab_name = models.CharField(max_length=255)
    test_type = models.CharField(max_length=255)
    sample_type = models.CharField(max_length=255)
    result = models.CharField(max_length=255)
    sample_collection_date = models.DateField()
    result_date = models.DateField()

    HEADER_CSV_MAPPING = {
        "srf_id": "SRF-ID",
        "name": "Patient Name",
        "age": "Age",
        "age_in": "Age In",
        "gender": "Gender",
        "address": "Patient Address",
        "mobile_number": "Contact Number",
        "is_repeat": "Is Repeat",
        "patient_status": "Patient Status",
        "ward": "Ward",
        "local_body": "LSGD",
        "lab_name": "LabName",
        "test_type": "Testing Kit Used",
        "sample_type": "Sample Type",
        "result": "Final Result",
        "sample_collection_date": "Sample Collection Date",
        # "result_date": "",
    }
