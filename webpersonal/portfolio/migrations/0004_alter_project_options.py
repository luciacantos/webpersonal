# Generated by Django 5.1.3 on 2024-11-24 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_project_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-created'], 'verbose_name': 'Proyecto', 'verbose_name_plural': 'Proyectos'},
        ),
    ]
