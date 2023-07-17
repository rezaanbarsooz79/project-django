# Generated by Django 4.2.2 on 2023-07-02 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.TextField()),
                ('area', models.FloatField()),
                ('blooming_time', models.CharField(choices=[('early', 'زودگل'), ('medium', 'متوسط گل'), ('late', 'دیر گل')], max_length=10)),
                ('male_tree_density', models.IntegerField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('last_modified_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='WinterWater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumption', models.FloatField()),
                ('date', models.DateField()),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Component_table.component')),
            ],
        ),
        migrations.CreateModel(
            name='WaterConsumption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumption', models.FloatField()),
                ('date', models.DateField()),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Component_table.component')),
            ],
        ),
        migrations.CreateModel(
            name='SoilAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Component_table.component')),
            ],
        ),
        migrations.CreateModel(
            name='Pest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('pest_type', models.CharField(choices=[('sen', 'سن'), ('psil', 'پسیل'), ('sank', 'سنک'), ('kermania', 'کرمانیا')], max_length=10)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Component_table.component')),
            ],
        ),
        migrations.CreateModel(
            name='Orchard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Component_table.component')),
            ],
        ),
        migrations.CreateModel(
            name='Harvest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('harvest_amount', models.FloatField()),
                ('cluster_defect_percentage', models.FloatField()),
                ('cluster_yield', models.FloatField()),
                ('annual_yield', models.FloatField()),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Component_table.component')),
            ],
        ),
        migrations.CreateModel(
            name='Fertilizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumption', models.FloatField()),
                ('date', models.DateField()),
                ('fertilizer_type', models.CharField(max_length=50)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Component_table.component')),
            ],
        ),
    ]
