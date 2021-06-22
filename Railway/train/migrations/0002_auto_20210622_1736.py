# Generated by Django 3.2.4 on 2021-06-22 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transection',
            name='transaction_for_ticket',
        ),
        migrations.AddField(
            model_name='ticket',
            name='transaction_for_ticket',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='train.transection'),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='p_transaction_id',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='train.transection'),
        ),
        migrations.AlterField(
            model_name='route',
            name='r_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticket_train',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='train.train_info'),
        ),
    ]
