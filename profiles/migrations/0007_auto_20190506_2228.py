# Generated by Django 2.2 on 2019-05-06 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20190430_1728'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100, null=True)),
                ('postcode', models.CharField(max_length=7, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='profile',
        ),
    ]