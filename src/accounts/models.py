from django.db import models
from django.contrib.auth.models import User


class TeachingAssistantProfile(models.Model):
    # Choices
    PROGRAMS = (
        ('1', 'M.Tech'),
        ('2', 'Ph.D MHRD'),
        ('3', 'Ph.D VSS'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=9, blank=True)
    program = models.CharField(max_length=1, choices=PROGRAMS)
    phone = models.CharField(max_length=10)
    alternate_phone = models.CharField(max_length=10, blank=True)
    research_area = models.CharField(max_length=256, blank=True)
    btech_specialization = models.CharField(max_length=64)
    mtech_specialization = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.roll_no


class TeachingAssistantSupervisorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_full_name()


class TeachingAssistantCoordinatorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_full_name()


class OfficeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_full_name()
