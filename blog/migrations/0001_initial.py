# Generated by Django 4.1.3 on 2022-12-11 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
