# Generated by Django 4.1.7 on 2023-03-11 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triangulo_app', '0005_transformador_t4fallas_transformador_t5fallas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transformador',
            name='t1fallas',
            field=models.CharField(default='', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='transformador',
            name='t4fallas',
            field=models.CharField(default='', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='transformador',
            name='t5fallas',
            field=models.CharField(default='', max_length=2, null=True),
        ),
    ]
