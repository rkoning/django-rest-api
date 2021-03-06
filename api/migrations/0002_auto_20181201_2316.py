# Generated by Django 2.1.3 on 2018-12-02 06:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='account_id',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='campaign_id',
        ),
        migrations.AddField(
            model_name='account',
            name='ext_account_id',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='account',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='campaign',
            name='ext_campaign_id',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='campaign',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='campaign',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
