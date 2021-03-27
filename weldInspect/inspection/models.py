from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class project(models.Model):
    project_number=models.IntegerField(primary_key=True)
    report_number=models.IntegerField(unique=True)
    data_perform=models.DateTimeField(default=timezone.now)
    project_user_name=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.project_number)

    # def get_absolute_url(self):
    #     return reverse('project-detail', kwargs={'pk': self.pk})
    def get_absolute_url(self):
        return reverse('inspection-new')

class location_discipline(models.Model):
    location_name=models.CharField(max_length=200)
    discipline_name=models.CharField(max_length=200)
    location_discipline_id=models.ForeignKey(project,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.location_name)

    # def get_absolute_url(self):
    #     return reverse('loc-detail', kwargs={'pk': self.pk})
    
    def get_absolute_url(self):
        return reverse('inspection-new')

class weld_action(models.Model):
    during_welding=models.BooleanField(default=False)
    before_welding=models.BooleanField(default=False)
    after_welding=models.BooleanField(default=False)
    weld_action_project_id=models.ForeignKey(project,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.weld_action_project_id)

    # def get_absolute_url(self):
    #     return reverse('weldaction-detail', kwargs={'pk': self.pk})
    def get_absolute_url(self):
        return reverse('inspection-new')

class heat_calc(models.Model):
    current_A=models.IntegerField(default=0,blank=True)
    voltage_V=models.IntegerField(default=0,blank=True)
    time_SS=models.IntegerField(default=0,blank=True)
    length_MM=models.IntegerField(default=0,blank=True)
    heat_input=models.IntegerField(default=0,blank=True)
    heat_calc_id=models.ForeignKey(project,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.heat_calc_id)
    
    def get_absolute_url(self):
        return reverse('inspection-new')

    # def get_absolute_url(self):
    #     return reverse('heat-detail', kwargs={'pk': self.pk})
    def calculation_of_heat(self,c,v,t,l):
        self.heat_input=int((c*v*t)//l*1000)
        return self.heat_input
    @property
    def activate_calculation(self):
        return self.calculation_of_heat(self.current_A,self.voltage_V,self.time_SS,self.length_MM)

class drawing(models.Model):
    drawing_number=models.CharField(max_length=200)
    drawing_id=models.ForeignKey(project,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.drawing_number)

    # def get_absolute_url(self):
    #     return reverse('drawing-detail', kwargs={'pk': self.pk})
    def get_absolute_url(self):
        return reverse('inspection-new')

class weld(models.Model):
    weld_number=models.IntegerField()
    weld_id=models.ForeignKey(drawing,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.weld_number)

    # def get_absolute_url(self):
    #     return reverse('weld-detail', kwargs={'pk': self.pk})
    def get_absolute_url(self):
        return reverse('inspection-new')

class gallery(models.Model):
    photo=models.ImageField(upload_to='photo_pics',default='default.jpg')
    photo_report_id=models.ForeignKey(project,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.photo_report_id)
    
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    
    def get_absolute_url(self):
        return reverse('inspection-new')

    # def get_absolute_url(self):
    #     return reverse('photo-detail', kwargs={'pk': self.pk})

class activity_description(models.Model):
    act_descp=models.CharField(max_length=200,blank=True,primary_key=True) # If a field has blank=True, form validation will allow entry of an empty value.
    act_descp_source=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.act_descp)

    def get_absolute_url(self):
        return reverse('act_descp', kwargs={'pk': self.pk})

class activity_inspection_action(models.Model):
    according=models.BooleanField(default=False)
    not_according=models.BooleanField(default=False)
    correction_action=models.BooleanField(default=False)
    comment=models.CharField(max_length=100,blank=True)
    inspection_id=models.ForeignKey(project,on_delete=models.CASCADE)
    act_desp_action_descp=models.ForeignKey(activity_description,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.inspection_id)

    # def get_absolute_url(self):
    #     return reverse('act_inspection_action', kwargs={'pk': self.pk})
    def get_absolute_url(self):
        return reverse('inspection-detail', kwargs={'pk': self.pk})
