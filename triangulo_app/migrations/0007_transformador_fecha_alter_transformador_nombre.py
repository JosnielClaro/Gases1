# Generated by Django 4.1.7 on 2023-04-04 00:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('triangulo_app', '0006_alter_transformador_t1fallas_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transformador',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transformador',
            name='nombre',
            field=models.CharField(default='', max_length=30),
        ),
    ]
