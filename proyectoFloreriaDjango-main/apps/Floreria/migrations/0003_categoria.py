# Generated by Django 5.0.6 on 2024-06-12 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Floreria', '0002_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('categoria_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
    ]
