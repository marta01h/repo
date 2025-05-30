# Generated by Django 5.1.7 on 2025-03-30 14:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('basics', '💻 Основы программирования'), ('algorithms', '📊 Алгоритмы и структуры данных'), ('web', '🌍 Веб-разработка'), ('mobile', '📱 Мобильная разработка'), ('ai', '🤖 Искусственный интеллект'), ('devops', '🛠 DevOps и администрирование')], default='basics', max_length=50),
        ),
        migrations.CreateModel(
            name='DownloadHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('downloaded_at', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
