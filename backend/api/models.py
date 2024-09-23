from django.db import models

class ExpertiseArea(models.Model):
    name = models.CharField(max_length=255)

class ITTeam(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=255)
    expertise_areas = models.ManyToManyField(ExpertiseArea)

    def __str__(self):
        return self.team_name

class RequestService(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=255)

    def __str__(self):
        return self.service_name

class UserRequest(models.Model):
    request_id = models.AutoField(primary_key=True)
    service = models.ForeignKey(RequestService, on_delete=models.CASCADE)
    team = models.ForeignKey(ITTeam, on_delete=models.CASCADE)

    def __str__(self):
        return f'Request {self.request_id}'
