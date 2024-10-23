from dataclasses import fields
from email.policy import default

from account import migrations, models


class Migration(migrations.Migration):
    initial = True
    # dependencies = [('auth', '0001_initial'),]

    operations = [
        migrations.CreatModel(
            name ='User',
            fields = [
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password',models.CharField(max_length=128, verbose_name='password')),
                ('email',models.EmailField(max_length=254, unique=True))
            ],
            options={
                'abstract': False,
            },
        )
    ]
