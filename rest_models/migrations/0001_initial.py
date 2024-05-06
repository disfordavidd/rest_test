# Generated by Django 5.0.4 on 2024-04-28 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item_rest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('new', models.BooleanField(default=False)),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['added'],
            },
        ),
    ]
