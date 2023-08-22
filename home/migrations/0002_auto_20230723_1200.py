# Generated by Django 3.2.20 on 2023-07-23 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jenis_skill',
            options={'verbose_name_plural': 'Jenis Skill'},
        ),
        migrations.AlterModelOptions(
            name='kejuaraanpelatih',
            options={'verbose_name_plural': 'Kejuaraan'},
        ),
        migrations.AlterModelOptions(
            name='pelatih',
            options={'verbose_name_plural': 'Pelatih'},
        ),
        migrations.AlterModelOptions(
            name='pengalaman',
            options={'verbose_name_plural': 'Pengalaman'},
        ),
        migrations.AlterModelOptions(
            name='sertifikatpelatih',
            options={'verbose_name_plural': 'Sertifikat'},
        ),
        migrations.AddField(
            model_name='jenis_skill',
            name='pelatih',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.pelatih'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jenis_skill',
            name='skill',
            field=models.CharField(choices=[('1', 'Berenang'), ('2', 'Senam'), ('3', 'Atletik'), ('4', 'Fitness'), ('5', 'Game Team')], default=1, max_length=1),
        ),
        migrations.DeleteModel(
            name='skill',
        ),
    ]
