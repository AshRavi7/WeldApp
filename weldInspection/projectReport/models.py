from django.db import models
from django.utils import timezone
from django.db.models.lookups import IsNull

# Create your models here.
# class Post(models.Model):
#     				title = models.CharField(max_length=100)
#     				content = models.TextField()
#     				date_posted = models.DateTimeField(default=timezone.now)

class inspec_user(models.Model):
    user_id=models.AutoField(primary_key=False)
    user_name=models.CharField(max_length=100,primary_key=True,null=False)
    user_pass=models.CharField(max_length=100,null=False)

# CREATE TABLE inspec_user 
#     (
#      user_id NUMERIC (30) IDENTITY, 
#      user_name VARCHAR (100) NOT NULL , 
#      user_pass VARCHAR (100) NOT NULL 
#     )
# GO

# ALTER TABLE inspec_user ADD CONSTRAINT inspec_user_PK PRIMARY KEY CLUSTERED (user_name)
#      WITH (
#      ALLOW_PAGE_LOCKS = ON , 
#      ALLOW_ROW_LOCKS = ON )
# GO

class project_report(models.Model):
    project_number=models.IntegerField(max_length=30,primary_key=True,unique=True,null=False)
    report_number=models.IntegerField(max_length=30,unique=True,null=False)
    data_perform=models.DateTimeField(default=timezone.now)
    project_user_name=models.ForeignKey(inspec_user,on_delete=models.CASCADE)


# CREATE TABLE project_report 
#     (
#      project_number NUMERIC (30) NOT NULL , 
#      report_number NUMERIC (30) NOT NULL , 
#      date_perform DATE NOT NULL , 
#      project_user_name VARCHAR (100) NOT NULL , 
#     )
# GO

# ALTER TABLE project_report ADD CONSTRAINT project_report_PK PRIMARY KEY CLUSTERED (project_number)
#      WITH (
#      ALLOW_PAGE_LOCKS = ON , 
#      ALLOW_ROW_LOCKS = ON )
# GO

# ALTER TABLE project_report 
#     ADD CONSTRAINT project_report_inspec_user_FK FOREIGN KEY 
#     ( 
#      project_user_name
#     ) 
#     REFERENCES inspec_user 
#     ( 
#      user_name 
#     ) 
#     ON DELETE NO ACTION 
#     ON UPDATE NO ACTION 
# GO

class weld_action(models.Model):
    weld_action_id=models.IntegerField(max_length=30,primary_key=False,null=False)
    during_welding=models.BooleanField(null=False)
    before_welding=models.BooleanField(null=False)
    after_welding=models.BooleanField(null=False)
    weld_action_project_id=models.ForeignKey(project_report,primary_key=True,null=False,on_delete=models.CASCADE)



# CREATE TABLE weld_action
#     (
#      weld_action_id NUMERIC (30) NOT NULL , 
#      during_welding BIT NOT NULL , 
#      before_welding BIT NOT NULL , 
#      after_welding BIT NOT NULL , 
#      weld_action_project_id NUMERIC (30) NOT NULL , 
#     )
# GO 


# ALTER TABLE weld_action ADD CONSTRAINT weld_action_PK PRIMARY KEY CLUSTERED (weld_action_project_id)
#      WITH (
#      ALLOW_PAGE_LOCKS = ON , 
#      ALLOW_ROW_LOCKS = ON )
# GO


# ALTER TABLE weld_action 
#     ADD CONSTRAINT weld_action_project_report_FK FOREIGN KEY 
#     ( 
#      weld_action_project_id
#     ) 
#     REFERENCES project_report 
#     ( 
#      project_number 
#     ) 
#     ON DELETE NO ACTION 
#     ON UPDATE NO ACTION 
# GO
class heat_calc(models.Model):
    current_A=models.IntegerField(max_length=30,null=False)
    voltage_V=models.IntegerField(max_length=30,null=False)
    time_SS=models.IntegerField(max_length=30,null=False)
    length_MM=models.IntegerField(max_length=30,null=False)
    heat_input=models.IntegerField(max_length=30,null=False)
    heat_calc_id=models.ForeignKey(project_report,null=False,primary_key=True,on_delete=models.CASCADE)
    
# CREATE TABLE heat_calc 
#     (
#      heat_calc_id NUMERIC (30) NOT NULL , 
#      current_A NUMERIC (30) NOT NULL , 
#      voltage_V NUMERIC (30) NOT NULL , 
#      time_SS NUMERIC (30) NOT NULL , 
#      length_MM NUMERIC (30) NOT NULL , 
#      heat_input NUMERIC (30) NOT NULL , 

#     )
# GO 


# ALTER TABLE heat_calc ADD CONSTRAINT heat_calc_PK PRIMARY KEY CLUSTERED (heat_calc_id)
#      WITH (
#      ALLOW_PAGE_LOCKS = ON , 
#      ALLOW_ROW_LOCKS = ON )
# GO

# ALTER TABLE heat_calc 
#     ADD CONSTRAINT heat_calc_project_report_FK FOREIGN KEY 
#     ( 
#      heat_calc_id 

#     ) 
#     REFERENCES project_report 
#     ( 
#      project_number 
 
#     ) 
#     ON DELETE NO ACTION 
#     ON UPDATE NO ACTION 
# GO

# CREATE TABLE drawing 
#     (
#      drawing_number VARCHAR (200) NOT NULL, 
#      drawing_id NUMERIC (30) NOT NULL , 
#     )
# GO

# ALTER TABLE drawing ADD CONSTRAINT drawing_PK PRIMARY KEY CLUSTERED (drawing_id)
#      WITH (
#      ALLOW_PAGE_LOCKS = ON , 
#      ALLOW_ROW_LOCKS = ON )
# GO


# ALTER TABLE drawing 
#     ADD CONSTRAINT drawing_project_report_FK FOREIGN KEY 
#     ( 
#      drawing_id 
 
#     ) 
#     REFERENCES project_report 
#     ( 
#      project_number 
  
#     ) 
#     ON DELETE NO ACTION 
#     ON UPDATE NO ACTION 
# GO



# CREATE TABLE weld 
#     (
#      weld_number NUMERIC (30) NOT NULL, 
#      weld_id NUMERIC (30) NOT NULL
#     )
# GO

# ALTER TABLE weld ADD CONSTRAINT weld_PK PRIMARY KEY CLUSTERED (weld_id)
#      WITH (
#      ALLOW_PAGE_LOCKS = ON , 
#      ALLOW_ROW_LOCKS = ON )
# GO

# ALTER TABLE weld 
#     ADD CONSTRAINT weld_id_FK FOREIGN KEY 
#     ( 
#      weld_id
#     ) 
#     REFERENCES drawing
#     ( 
#      drawing_id
#     ) 
#     ON DELETE NO ACTION 
#     ON UPDATE NO ACTION 
# GO



# CREATE TABLE gallery 
#     (
#      count_id NUMERIC (30) IDENTITY, 
#      photo IMAGE NOT NULL, 
#      photo_report_id NUMERIC (30) NOT NULL , 

#     )
# GO



# ALTER TABLE gallery ADD CONSTRAINT gallery_PK PRIMARY KEY CLUSTERED (count_id)
#      WITH (
#      ALLOW_PAGE_LOCKS = ON , 
#      ALLOW_ROW_LOCKS = ON )
# GO

# ALTER TABLE gallery 
#     ADD CONSTRAINT photo_report_id_FK FOREIGN KEY 
#     ( 
#      photo_report_id
#     ) 
#     REFERENCES project_report 
#     ( 
#      project_number 
#     ) 
#     ON DELETE NO ACTION 
#     ON UPDATE NO ACTION 
# GO

# CREATE TABLE activity_description 
#     (
#      act_descp VARCHAR (200) NOT NULL , 
#      act_id INT IDENTITY 
#     )
# GO

# ALTER TABLE activity_description ADD CONSTRAINT activity_description_PK PRIMARY KEY CLUSTERED (act_descp)
#      WITH (
#      ALLOW_PAGE_LOCKS = ON , 
#      ALLOW_ROW_LOCKS = ON )


# CREATE TABLE activity_inspection_action 
#     (
#      acction_count INT IDENTITY , 
#      inspection_id NUMERIC (30) NOT NULL , 
#      according BIT NOT NULL , 
#      not_according BIT NOT NULL , 
#      correctin_acction BIT NOT NULL , 
#      comment VARCHAR (200) , 
#      act_descp_action_id VARCHAR (200) NOT NULL, 
     
#     )
# GO

# ALTER TABLE activity_inspection_action ADD CONSTRAINT activity_inspection_action_PK PRIMARY KEY CLUSTERED (acction_count)
#      WITH (
#      ALLOW_PAGE_LOCKS = ON , 
#      ALLOW_ROW_LOCKS = ON )
# GO


# ALTER TABLE activity_inspection_action 
#     ADD CONSTRAINT activity_inspection_FK FOREIGN KEY 
#     ( 
#      act_descp_action_id
#     ) 
#     REFERENCES activity_description 
#     ( 
#      act_descp 
#     ) 
#     ON DELETE NO ACTION 
#     ON UPDATE NO ACTION 
# GO

# ALTER TABLE activity_inspection_action 
#     ADD CONSTRAINT activity_inspection_report_FK FOREIGN KEY 
#     ( 
#      inspection_id
#     ) 
#     REFERENCES project_report 
#     ( 
#      project_number 
#     ) 
#     ON DELETE NO ACTION 
#     ON UPDATE NO ACTION 
# GO



# CREATE TABLE location_discipline 
#     (
#      location_name VARCHAR (200) NOT NULL , 
#      discipline_name VARCHAR (200) NOT NULL, 
#      location_discipline_id NUMERIC (30) NOT NULL , 
  
#     )
# GO 

 

# ALTER TABLE location_discipline ADD CONSTRAINT location_discipline_PK PRIMARY KEY CLUSTERED (location_discipline_id)
#      WITH (
#      ALLOW_PAGE_LOCKS = ON , 
#      ALLOW_ROW_LOCKS = ON )
# GO


# ALTER TABLE location_discipline 
#     ADD CONSTRAINT location_discipline_report_FK FOREIGN KEY 
#     ( 
#      location_discipline_id
#     ) 
#     REFERENCES project_report 
#     ( 
#      project_number
#     ) 
#     ON DELETE NO ACTION 
#     ON UPDATE NO ACTION 
# GO 


