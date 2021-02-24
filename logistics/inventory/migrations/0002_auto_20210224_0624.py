# Generated by Django 3.1.7 on 2021-02-23 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='inbound',
            new_name='initial_inventory',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='outbound',
        ),
        migrations.AddField(
            model_name='inventory',
            name='comment',
            field=models.TextField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='inventory',
            name='inventory_status',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.CreateModel(
            name='InAndOutBound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_inventory', models.IntegerField()),
                ('inbound', models.IntegerField(default=0)),
                ('outbound', models.IntegerField(default=0)),
                ('registered', models.DateTimeField(auto_now_add=True)),
                ('product_id', models.ForeignKey(db_column='product_id', on_delete=django.db.models.deletion.CASCADE, to='inventory.inventory')),
            ],
            options={
                'db_table': 'in_and_out_bound',
            },
        ),
    ]