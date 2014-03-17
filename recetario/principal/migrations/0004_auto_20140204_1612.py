# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [
        ('principal', '0003_auto_20140204_1201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('receta', models.ForeignKey(to=u'principal.Receta', to_field=u'id')),
                ('texto', models.TextField(help_text='Tu comentario', verbose_name='comentario')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Bebida',
        ),
    ]
