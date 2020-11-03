# Generated by Django 3.1.2 on 2020-11-03 11:39

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0052_pagelogentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostDetailPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.core.fields.RichTextField(help_text='Content body', verbose_name='Body')),
            ],
            options={
                'verbose_name': 'Post page',
                'verbose_name_plural': 'Post pages',
                'permissions': (('save_post_as_pdf', 'Can export post as pdf'),),
            },
            bases=('wagtailcore.page',),
        ),
    ]
