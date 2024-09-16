from django.db import models

# Create your models here.

from django.db import models

class ITTeam(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=255)
    expertise_areas = models.TextField()

    def __str__(self):
        return self.team_name
    
class RequestService(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.service_name
    
class UserRequest(models.Model):
    request_id = models.AutoField(primary_key=True)
    service = models.ForeignKey(RequestService, on_delete=models.CASCADE)
    request_description = models.TextField()
    team = models.ForeignKey(ITTeam, on_delete=models.CASCADE)
    #request_status = models.CharField(max_length=100)

    def __str__(self):
        return f'Request {self.request_id}: {self.request_status}'


