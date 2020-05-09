from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Group



from django.db import models
from django.contrib.auth.models import User

manger_choices = (
    ('manager', 'manager'),
    ('normal', 'normal'),

)

# Create your models here.
class UserProfileInfo(models.Model):
      user = models.OneToOneField(User,on_delete=models.CASCADE)
      email = models.EmailField(max_length=255, unique=True)
      position = models.CharField(max_length=18, choices=manger_choices ,default='normal')
      def __str__(self):
          return self.user.username

      class Meta:
        managed = False
        db_table = 'DJANGOUSER'


class Alias(models.Model):
    resourceId = models.CharField(max_length=25, null=False, db_column="RESOURCEID")
    alias = models.CharField(max_length=25, db_column="ALIAS")
    lastSavedDate = models.DateField(blank=True, null=True, db_column="LASTSAVEDDATE")
    updateOrigin = models.IntegerField(blank=True, null=True, db_column="UPDATEORIGIN")

    def __str__(self):
        return [self.alias, self.resourceId, self.lastSavedDate, self.updateOrigin]

    class Meta:
        managed = False
        db_table = 'RIDALIAS'



class Computer(models.Model):
    resourceId = models.CharField(max_length=25, null=False, db_column="RESOURCEID")
    ciClass = models.CharField(max_length=25, blank=True, null=True, db_column="CICLASS")
    osRunning = models.CharField(max_length=25, blank=True, null=True, db_column="OSRUNNING")
    fqdn = models.CharField(max_length=25, db_column="FQDN")
    supportOrg = models.CharField(max_length=25, blank=True, null=True, db_column="SUPPORTORG")
    subAccount = models.CharField(max_length=25, db_column="SUBACCOUNT")
    customerCode = models.CharField(max_length=10, db_column="CUSTOMERCODE")
    countryCode = models.CharField(max_length=10, blank=True, db_column="COUNTRYCODE")
    updateOrigin = models.IntegerField(blank=True, null=True, db_column="UPDATEORIGIN")
    lastSavedDate = models.DateField(blank=True, null=True, db_column="LASTSAVEDDATE")
    resourceType = models.IntegerField(blank=True, null=True, db_column="RESOURCETYPE")#COMP_CUST_FK
    resourceUsage = models.CharField(max_length=10, blank=True, null=True, db_column="RESOURCEUSAGE")
    #locaTion = models.CharField(max_length=10, blank=True, null=True, db_column="LOCATION")
    #compCustFk = models.CharField(max_length=10, blank=True, null=True, db_column="COMP_CUST_FK")
    #ibmmanaGed = models.IntegerField(blank=True, null=True, db_column="IBMMANAGED")

    def __str__(self):
        return self.resourceId

    class Meta:
        managed = False
        db_table = 'COMPUTERSYSTEM'


class Filter(models.Model):
    #resourceId = models.CharField(max_length=25, null=False, db_column="RESOURCEID")
    customerCode = models.CharField(max_length=25, null=False, db_column="CUSTOMERCODE")
    filterName = models.CharField(max_length=25, db_column="FILTERNAME")
    filterDesc = models.CharField(max_length=25, db_column="FILTERDESC")
    filterState = models.IntegerField(blank=True, null=True, db_column="FILTERSTATE")
    filterWeight = models.IntegerField(blank=True, null=True, db_column="FILTERWEIGHT")
    subAccount = models.CharField(max_length=25, db_column="SUBACCOUNT")
    ticketGroup = models.CharField(max_length=25, db_column="TICKETGROUP")
    ticketActionId = models.IntegerField(blank=True, null=True, db_column="TICKETACTIONID")
    #IBMMANAGED = models.IntegerField(blank=True, null=True, db_column="IBMMANAGED")

    def __str__(self):
        return [self.customerCode, self.filterName, self.filterDesc, self.filterState,
                self.subAccount, self.ticketGroup]

    class Meta:
        managed = False
        db_table = 'AUTOMATIONFILTERS'

