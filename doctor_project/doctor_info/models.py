from django.db import models # type: ignore

def upload_to(instast, filename):
      return'assets/uploads/doctor_info/images/{filename}'.format(filename=filename)

class DoctorInfo(models.Model):
    sl=models.IntegerField(blank=True,null=True)
    dls_id=models.CharField(max_length=200,blank=True,null=True)
    aci_id=models.IntegerField(blank=True,null=True)
    name=models.CharField(max_length=200,blank=True,null=True)
    divisions=models.CharField(max_length=200,blank=True,null=True)
    district=models.CharField(max_length=200,blank=True,null=True)
    upazilla=models.CharField(max_length=200,blank=True,null=True)
    union=models.CharField(max_length=200,blank=True,null=True)
    photo = models.ImageField(upload_to="doctor_info/images/", blank=True, null=True, default="doctor_info/images/default.jpg")

    create_at=models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_at=models.DateTimeField(auto_now=True, blank=True, null=True)

def __str__(self):  # ✅ Corrected
    return self.name

