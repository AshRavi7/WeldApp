from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.utils import timezone
from django.db.models.lookups import IsNull
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    hobby = models.TextField()

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class project(models.Model):
    project_number=models.IntegerField(primary_key=True,unique=True,blank=False)
    report_number=models.IntegerField(unique=True,blank=False)
    data_perform=models.DateTimeField(default=timezone.now,blank=False)
    project_user_name=models.OneToOneField(User,on_delete=models.DO_NOTHING)

class location_discipline(models.Model):
    location_name=models.CharField(max_length=200,blank=True)
    discipline_name=models.CharField(max_length=200,blank=True)
    location_discipline_id=models.OneToOneField(project,unique=True,primary_key=True,on_delete=models.DO_NOTHING)

class weld_action(models.Model):
    during_welding=models.BooleanField(default=False)
    before_welding=models.BooleanField(default=False)
    after_welding=models.BooleanField(default=False)
    weld_action_project_id=models.OneToOneField(project,unique=True,primary_key=True,blank=False,on_delete=models.DO_NOTHING)

class heat_calc(models.Model):
    current_A=models.IntegerField(default=0,blank=True)
    voltage_V=models.IntegerField(default=0,blank=True)
    time_SS=models.IntegerField(default=0,blank=True)
    length_MM=models.IntegerField(default=0,blank=True)
    heat_input=models.IntegerField(default=0,blank=True)
    heat_calc_id=models.OneToOneField(project,unique=True,primary_key=True,on_delete=models.DO_NOTHING)

    def calculation_of_heat(self,c,v,t,l):
        self.heat_input=((c*v*t)//l*1000)

    @property
    def activate_calculation(self):
        return self.calculation_of_heat(self.current_A,self.voltage_V,self.time_SS,self.length_MM)

class drawing(models.Model):
    drawing_number=models.CharField(max_length=200,blank=False)
    drawing_id=models.OneToOneField(project,unique=True,primary_key=True,on_delete=models.DO_NOTHING)

class weld(models.Model):
    weld_number=models.IntegerField(blank=False)
    weld_id=models.OneToOneField(drawing,unique=True,primary_key=True,on_delete=models.DO_NOTHING)

class gallery(models.Model):
    photo=models.ImageField()
    photo_report_id=models.OneToOneField(project,unique=True,on_delete=models.DO_NOTHING)
    

class activity_description(models.Model):
    act_descp=models.CharField(max_length=200,blank=True,primary_key=True) # If a field has blank=True, form validation will allow entry of an empty value.
    act_descp_source=models.OneToOneField(User,on_delete=models.DO_NOTHING) # admin_user creates 10 default questions 


class activity_inspection_action(models.Model):
    according=models.BooleanField(default=False)
    not_according=models.BooleanField(default=False)
    correction_action=models.BooleanField(default=False)
    comment=models.CharField(max_length=100,blank=True)
    inspection_id=models.OneToOneField(project,unique=True,on_delete=models.DO_NOTHING)
    act_desp_action_id=models.OneToOneField(activity_description,on_delete=models.DO_NOTHING)



