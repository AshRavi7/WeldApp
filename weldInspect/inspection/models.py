from django.db import models
from datetime import datetime 
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class project(models.Model):
    project_number=models.IntegerField(primary_key=True)
    report_number=models.IntegerField(unique=True)
    data_perform=models.DateTimeField(default=datetime.now())
    project_user_name=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.project_number)

    # def get_absolute_url(self):
    #     return reverse('project-detail', kwargs={'pk': self.project_number})
    # def get_absolute_url(self):
    #     return reverse('inspection-new')

class location_discipline(models.Model):
    location_name=models.CharField(max_length=200)
    discipline_name=models.CharField(max_length=200)
    location_discipline_id=models.OneToOneField(project,on_delete=models.CASCADE,primary_key=True)
    
    def __str__(self):
        return f'Location: {self.location_name} Discipline: {self.discipline_name}'

    # def get_absolute_url(self):
    #     return reverse('location-detail', kwargs={'pk': self.pk})
    
    # def get_absolute_url(self):
    #     return reverse('inspection-new')

class weld_action(models.Model):
    during_welding=models.BooleanField(default=False)
    before_welding=models.BooleanField(default=False)
    after_welding=models.BooleanField(default=False)
    weld_action_project_id=models.OneToOneField(project,on_delete=models.CASCADE,primary_key=True)
    
    def __str__(self):
        return  f' during_welding: {self.during_welding} before_welding: {self.before_welding} after_welding: {self.after_welding}'

    # def get_absolute_url(self):
    #     return reverse('weldAction-detail', kwargs={'pk': self.pk})
    # def get_absolute_url(self):
    #     return reverse('inspection-new')

class heat_calc(models.Model):
    current_A=models.IntegerField(default=0,blank=True)
    voltage_V=models.IntegerField(default=0,blank=True)
    time_SS=models.IntegerField(default=0,blank=True)
    length_MM=models.IntegerField(default=0,blank=True)
    heat_input=models.IntegerField(default=0,blank=True)
    heat_calc_id=models.OneToOneField(project,on_delete=models.CASCADE,primary_key=True)
    
    def __str__(self):
        return  f' current_A: {self.current_A} voltage_V: {self.voltage_V}  time_SS: {self. time_SS} length_MM: {self.length_MM} heat_input:{self.heat_input}'
    
    @staticmethod
    def activate_calculation(a,v,t,l):
        return int((a*v*t)//(l*1000))

class drawing(models.Model):
    drawing_number=models.CharField(max_length=200)
    drawing_id=models.OneToOneField(project,on_delete=models.CASCADE,primary_key=True)
    
    def __str__(self):
        return f'drawing_number: {self.drawing_number}'

    # def get_absolute_url(self):
    #     return reverse('drawing-detail', kwargs={'pk': self.pk})

class weld(models.Model):
    weld_number=models.IntegerField(primary_key=True)
    weld_id=models.ForeignKey(drawing,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'weld:{self.weld_number}'

    # def get_absolute_url(self):
    #     return reverse('weld-detail', kwargs={'pk': self.pk})
    # def get_absolute_url(self):
    #     return reverse('inspection-new')

class gallery(models.Model):
    photo=models.ImageField(upload_to='photo_pics',default='weld.png')
    photo_report_id=models.OneToOneField(project,on_delete=models.CASCADE,primary_key=True)
    
    def __str__(self):
        return f'Photo: {self.photo}'
    
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

        img = Image.open(self.photo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)

    
    # def get_absolute_url(self):
    #     return reverse('inspection-new')

    # def get_absolute_url(self):
    #     return reverse('gallery-detail', kwargs={'pk': self.pk})

class activity_description(models.Model):
    act_descp=models.CharField(max_length=200,blank=True,primary_key=True) # If a field has blank=True, form validation will allow entry of an empty value.
    act_descp_source=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.act_descp)

    # def get_absolute_url(self):
    #     return reverse('act_descp', kwargs={'pk': self.pk})

class activity_inspection_action(models.Model):
    according=models.BooleanField(default=False)
    not_according=models.BooleanField(default=False)
    correction_action=models.BooleanField(default=False)
    comment=models.CharField(max_length=100,blank=True)
    inspection_id=models.ForeignKey(project,on_delete=models.CASCADE)
    act_desp_action_descp=models.ForeignKey(activity_description,on_delete=models.CASCADE)

    def __str__(self):
        return f' according: {self.according} not_according: {self.not_according} correction_action: {self.correction_action} comment: {self.comment} description: {self.act_desp_action_descp}'

    # def get_absolute_url(self):
    #     return reverse('act_inspection_action', kwargs={'pk': self.pk})
    # def get_absolute_url(self):
    #     return reverse('inspection-detail', kwargs={'pk': self.pk})
