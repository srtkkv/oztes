# Generated by Django 4.1.5 on 2023-01-21 08:32

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mgmt', '0006_alter_ou_description_alter_ou_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='CA',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('CA', 'CA Certificate'), ('srv', 'Server Certificate'), ('agnt', 'Agent Certificate'), ('csr', "Agent's CSR")], max_length=4, verbose_name='Certificte')),
            ],
        ),
        migrations.CreateModel(
            name='agent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('OS', models.CharField(max_length=200, verbose_name='Host OS')),
                ('Emp', models.ForeignKey(help_text='Agents owner', on_delete=django.db.models.deletion.CASCADE, related_name='owned', to='mgmt.emp')),
            ],
        ),
    ]
