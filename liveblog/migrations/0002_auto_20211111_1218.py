# Generated by Django 3.2.8 on 2021-11-11 12:18

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('liveblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='liveblogpage',
            name='hero_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='liveblogpage',
            name='hero_text',
            field=wagtail.core.fields.RichTextField(default='Hero'),
            preserve_default=False,
        ),
    ]
