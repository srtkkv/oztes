from django.db import models
import uuid
from .Core.policy import Policy

class OU(models.Model): # organiztion units
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    parent = models.ForeignKey('self',related_name='subortinate', on_delete=models.DO_NOTHING,db_constraint=False)#,blank=True, null=True)
    Name = models.CharField(max_length=200)
    Description = models.TextField(blank=True, null=True)

    def __str__(self):
        p = Policy()
        return self.Name

    def get_list_of_parents(self):
        result=[self,]
        item = self.parent
        while item != item.parent:
            result.append(item)
            item = item.parent
        if item==item.parent:
            result.append(item)
        return result

class Emp(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    OU = models.ForeignKey(OU, on_delete=models.CASCADE, related_name='member')
    Name = models.CharField('Employee name', null=False, max_length=20)
    LastName = models.CharField('Last name', null=False, max_length=20)
    SureName = models.CharField('Employee sure name', null=True, max_length=20)
    Email = models.CharField('Employee email',max_length=50,blank=True)
    phone = models.CharField('Employee phone',max_length=20,blank=True)

    def __str__(self):
        return f'{self.Name} {self.LastName}'

    def aplied_policies(self):
        result = []
        for pol in Policy_appied_to_Emp.objects.filter(Emp=self).filter(policy__status='en'):
            result.append(pol)
        for pol in Policy_applied_to_OU.objects.filter(OU__in=self.OU.get_list_of_parents()).filter(policy__status='en'):
            result.append(pol)
        return result
    def comple_policy(self):
        '''
        Combine all policies in a single document
        :return:
        xml document contains all applied poliecies for the employee.
        '''
        pass


class Policy(models.Model):
    CHOICES = (
        ('dr', 'Draft'),
        ('en', 'Enabled'),
        ('di', 'Disabled'),
    )

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField('Policy Name',max_length=100)
    xml = models.TextField()
    status = models.CharField('LifeCycle Status', choices=CHOICES, max_length=3)

    def __str__(self):
        return f'{self.name} - {self.status}'

class Policy_applied_to_OU(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    policy = models.ForeignKey('Policy' , on_delete=models.CASCADE)
    OU = models.ForeignKey('OU', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.policy} appliend on: {self.OU}'

class Policy_appied_to_Emp(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    policy = models.ForeignKey('Policy', on_delete=models.CASCADE)
    Emp =models.ForeignKey('Emp', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.policy} appliend on: {self.Emp}'

class Agent(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    Emp = models.ForeignKey('Emp', on_delete=models.CASCADE, null=False, help_text='Agents owner', related_name='owned')
    OS = models.CharField('Host OS', max_length=200)
    def __str__(self):
        return f'{self.Emp} - {self.id}'

class Cartificate(models.Model):
    TYPE = (
        ('CA', 'CA Certificate'),
        ('srv', 'Server Certificate'),
        ('agnt', 'Agent Certificate'),
        ('csr', 'Agent\'s CSR' ),
    )
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    type = models.CharField('Certificte', max_length=4, choices=TYPE)
    agent = models.ForeignKey('Agent', blank=True, null=True, on_delete=models.DO_NOTHING)
    countryName = models.CharField(max_length=100, blank=True, null=True)
    C = models.CharField(max_length=100, blank=True, null=True)
    stateOrProvinceName = models.CharField(max_length=100, blank=True, null=True)
    ST = models.CharField(max_length=100, blank=True, null=True)
    localityName = models.CharField(max_length=100, blank=True, null=True)
    L = models.CharField(max_length=100, blank=True, null=True)
    organizationName = models.CharField(max_length=100, blank=True, null=True)
    O = models.CharField(max_length=100, blank=True, null=True)
    organizationalUnitName = models.CharField(max_length=100, blank=True, null=True)
    OU = models.CharField(max_length=100, blank=True, null=True)
    commonName = models.CharField(max_length=100, blank=True, null=True)
    CN = models.CharField(max_length=100, blank=True, null=True)
    emailAddress = models.CharField(max_length=100, blank=True, null=True)
    public_key_txt = models.TextField(blank=True, null=True)
    serial_number = models.IntegerField(blank=True, null=True)
    notAfter = models.DateTimeField(blank=True, null=True)
    notBefore = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.agent} - {self.commonName}'

