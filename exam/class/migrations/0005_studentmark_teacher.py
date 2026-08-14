from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('class', '0004_alter_group_created_at_alter_group_mentor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmark',
            name='teacher',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='marks',
                to='class.teacher',
                verbose_name='Учитель',
            ),
        ),
    ]
