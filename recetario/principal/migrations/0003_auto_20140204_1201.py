# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [
        ('principal', '0002_receta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='imagen',
            field=models.ImageField(upload_to='recetas', verbose_name='Im\xc3\xa1gen'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='preparacion',
            field=models.TextField(verbose_name='Preparaci\xc3\xb3n'),
        ),
    ]
