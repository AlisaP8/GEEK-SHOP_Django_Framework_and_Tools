# Generated by Django 3.2.9 on 2022-02-01 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_alter_user_activation_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='langs',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='язык'),
        ),
    ]