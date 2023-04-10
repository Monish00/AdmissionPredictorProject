from django.db import models
from django.utils import timezone

class Student_Detail(models.Model):
	student_name = models.CharField('Student Name', max_length=255)
	email_id = models.EmailField('Email Id', max_length=255)
	phone_number = models.CharField('Mobile Number', max_length=50,null=True,blank=True)
	dob =  models.DateField()
	gender = models.CharField('Gender',max_length=20)
	education = models.CharField('Education',max_length=200)
	mark = models.CharField('Score',max_length=200)
	caste = models.CharField('Caste',max_length=200,null=True,blank=True)
	cutoff_mark = models.CharField('Cutoff Mark',max_length=200)
	address = models.TextField('Address',null=True,blank=True)
	Score = models.CharField('Score',max_length=200,null=True)
	country = models.CharField('Country', max_length=100,default='India')
	state = models.CharField('State', max_length=100,default='Tamil Nadu')
	city = models.CharField('City', max_length=100,null=True,blank=True)
	username = models.CharField('Username', max_length=100, unique=True)
	password = models.CharField('Password',max_length=30)
	image = models.FileField('Student Image',upload_to='documents/',null=True)
	def __str__(self):
		return self.student_name
class Engineering_College_Detail(models.Model):
	college_name = models.CharField('College Name', max_length=1000,null=True,blank=True)
	degree = models.CharField('Degree', max_length=1000,null=True,blank=True)
	department = models.CharField('Department', max_length=1000,null=True,blank=True)
	OC = models.CharField('OC',max_length=20,null=True,blank=True)
	BC = models.CharField('BC',max_length=200,null=True,blank=True)
	BCM = models.CharField('BCM',max_length=200,null=True,blank=True)
	MBCV = models.CharField('MBCV',max_length=200,null=True,blank=True)
	MBCDNC = models.TextField('MBCDNC',null=True,blank=True)
	MBA = models.CharField('MBA',max_length=200,null=True)
	SC = models.CharField('SC', max_length=100,null=True,blank=True)
	SCA = models.CharField('SCA', max_length=100,null=True,blank=True)
	ST = models.CharField('ST', max_length=100,null=True,blank=True)
	def __str__(self):
		return self.college_name
class Medical_College_Detail(models.Model):
	college_name = models.CharField('College Name', max_length=1000,null=True,blank=True)
	degree = models.CharField('Degree', max_length=1000,null=True,blank=True)
	department = models.CharField('Department', max_length=1000,null=True,blank=True)
	OC = models.CharField('OC',max_length=20,null=True,blank=True)
	BC = models.CharField('BC',max_length=200,null=True,blank=True)
	BCM = models.CharField('BCM',max_length=200,null=True,blank=True)
	MBCV = models.CharField('MBCV',max_length=200,null=True,blank=True)
	MBCDNC = models.TextField('MBCDNC',null=True,blank=True)
	MBA = models.CharField('MBA',max_length=200,null=True)
	SC = models.CharField('SC', max_length=100,null=True,blank=True)
	SCA = models.CharField('SCA', max_length=100,null=True,blank=True)
	ST = models.CharField('ST', max_length=100,null=True,blank=True)
	def __str__(self):
		return self.college_name
class Agri_College_Detail(models.Model):
	college_name = models.CharField('College Name', max_length=1000,null=True,blank=True)
	degree = models.CharField('Degree', max_length=1000,null=True,blank=True)
	department = models.CharField('Department', max_length=1000,null=True,blank=True)
	OC = models.CharField('OC',max_length=20,null=True,blank=True)
	BC = models.CharField('BC',max_length=200,null=True,blank=True)
	BCM = models.CharField('BCM',max_length=200,null=True,blank=True)
	MBCV = models.CharField('MBCV',max_length=200,null=True,blank=True)
	MBCDNC = models.TextField('MBCDNC',null=True,blank=True)
	MBA = models.CharField('MBA',max_length=200,null=True)
	SC = models.CharField('SC', max_length=100,null=True,blank=True)
	SCA = models.CharField('SCA', max_length=100,null=True,blank=True)
	ST = models.CharField('ST', max_length=100,null=True,blank=True)
	def __str__(self):
		return self.college_name
