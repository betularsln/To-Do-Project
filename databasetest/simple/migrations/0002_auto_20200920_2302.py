# Generated by Django 3.1.1 on 2020-09-20 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('islem_baslik', models.CharField(max_length=255)),
                ('islem_aciklama', models.SlugField(max_length=255, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('finished_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='MySimpleModel',
        ),
    ]