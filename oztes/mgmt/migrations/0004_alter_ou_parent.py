# Generated by Django 4.1.5 on 2023-01-20 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mgmt', '0003_alter_emp_email_alter_emp_phone_alter_ou_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ou',
            name='parent',
            field=models.ForeignKey(blank=True, db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='subortinate', to='mgmt.ou'),
        ),
    ]
