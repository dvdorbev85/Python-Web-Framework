# Generated by Django 4.0.3 on 2022-03-17 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('image', models.URLField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
