# Generated by Django 2.2 on 2020-11-19 21:37

from django.db import migrations, models
import form_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, validators=[form_app.models.validate_length])),
                ('last_name', models.CharField(max_length=255, validators=[form_app.models.validate_length])),
                ('email', models.CharField(max_length=255, validators=[form_app.models.validate_email])),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField()),
            ],
        ),
    ]
