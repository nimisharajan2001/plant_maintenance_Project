from django.db import models

# Create your models here.

class designation(models.Model):
    designation = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.designation

class register(models.Model):
	designation = models.ForeignKey(designation, on_delete=models.DO_NOTHING,
		related_name='registerdesignation', null=True, blank=True)
	firstname = models.CharField(max_length=200)
	lastname = models.CharField(max_length=200)
	username = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
	password = models.CharField(max_length=200)
	cpassword = models.CharField(max_length=200)

	def __str__(self):
		return self.firstname
	

class addrequest(models.Model):
	name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	Date_Time = models.CharField(max_length=255)
	phone = models.CharField(max_length=255)
	req_details = models.CharField(max_length=255)
	location = models.CharField(max_length=255)
	category = models.CharField(max_length=255)
	completion_date = models.CharField(max_length=255)
	urgency = models.CharField(max_length=255)

class givework(models.Model):
	user= models.ForeignKey(register, on_delete=models.DO_NOTHING,null=True, blank=True)
	work = models.CharField(max_length=255)
	startdate = models.DateField(max_length=255)
	enddate = models.DateField(max_length=255)
	status = models.CharField(max_length=255 ,null=True, blank=True)

	# def __str__(self):
    #     	return self.firstname

class addperson(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	phone = models.CharField(max_length=255)
	address = models.CharField(max_length=255)

class addvendors(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	phone = models.CharField(max_length=255)
	product = models.CharField(max_length=255)
	address = models.CharField(max_length=255)

class payment(models.Model):
	name = models.CharField(max_length=255)
	date = models.DateField(max_length=255)
	product = models.CharField(max_length=255)
	quantity = models.CharField(max_length=255)
	accountno = models.CharField(max_length=255)
	paymethod = models.CharField(max_length=255)
	amount = models.CharField(max_length=255)

class stockdetails(models.Model):
	product = models.CharField(max_length=255)
	quantity = models.CharField(max_length=255)

class workstatus(models.Model):
	user = models.ForeignKey(register, on_delete=models.DO_NOTHING,null=True, blank=True)
	date = models.DateField(max_length=255)
	status = models.CharField(max_length=255)


class packing(models.Model):
	product = models.CharField(max_length=255)
	quantity = models.CharField(max_length=255)

class repairing(models.Model):
	product = models.CharField(max_length=255)
	quantity = models.CharField(max_length=255)
	amount = models.CharField(max_length=255)

class sales(models.Model):
	name = models.CharField(max_length=255)
	date = models.DateField(max_length=255)
	product = models.CharField(max_length=255)
	amount = models.CharField(max_length=255)