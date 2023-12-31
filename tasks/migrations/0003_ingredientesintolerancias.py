# Generated by Django 4.2.7 on 2023-12-13 02:06

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_usuario_costomaximo'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngredientesIntolerancias',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ingredientes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.ingredientes')),
                ('intolerancias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.intolerancias')),
            ],
        ),
    ]
