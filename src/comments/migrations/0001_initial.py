# Generated by Django 2.2.7 on 2019-11-15 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField(max_length=10000000000000000000)),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]