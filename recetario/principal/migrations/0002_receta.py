# encoding: utf8
from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receta',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(unique=True, max_length=100)),
                ('ingredientes', models.TextField(help_text='Redacta los ingredientes')),
                ('preparacion', models.TextField(verbose_name='Preparaci\xef\xbf\xbdn')),
                ('imagen', models.ImageField(upload_to='recetas', verbose_name='Im\xef\xbf\xbdgen')),
                ('tiempoRegistro', models.DateTimeField(auto_now=True)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field=u'id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
