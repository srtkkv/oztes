# Generated by Django 4.1.5 on 2023-01-20 18:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=20, verbose_name='Employee name')),
                ('LastName', models.CharField(max_length=20, verbose_name='Last name')),
                ('SureName', models.CharField(max_length=20, null=True, verbose_name='Employee sure name')),
                ('Email', models.CharField(max_length=50, verbose_name='Employee email')),
                ('phone', models.CharField(max_length=20, verbose_name='Employee phone')),
            ],
        ),
        migrations.CreateModel(
            name='OU',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=200)),
                ('Description', models.TextField()),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='subortinate', to='mgmt.ou')),
            ],
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Policy Name')),
                ('xml', models.TextField()),
                ('status', models.CharField(choices=[('dr', 'Draft'), ('en', 'Enabled'), ('di', 'Disabled')], max_length=3, verbose_name='LifeCycle Status')),
            ],
        ),
        migrations.CreateModel(
            name='Policy_applied_to_OU',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('OU', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mgmt.ou')),
                ('policy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mgmt.policy')),
            ],
        ),
        migrations.CreateModel(
            name='Policy_appied_to_Emp',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mgmt.emp')),
                ('policy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mgmt.policy')),
            ],
        ),
        migrations.AddField(
            model_name='emp',
            name='OU',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member', to='mgmt.ou'),
        ),
    ]
