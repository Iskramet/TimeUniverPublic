# Generated by Django 3.0.2 on 2020-02-01 12:57

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('middle_name', models.CharField(max_length=150)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('faculty_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=15)),
                ('decryption', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('group_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=10)),
                ('start_semestr', models.DateField()),
                ('end_semestr', models.DateField()),
                ('faculty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Faculty')),
                ('monitor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('university_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('decryption', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='shedule',
            fields=[
                ('lesson_id', models.AutoField(primary_key=True, serialize=False)),
                ('lesson', models.CharField(max_length=50)),
                ('teacher', models.CharField(blank=True, max_length=100)),
                ('classroom', models.CharField(max_length=10)),
                ('start_time', models.TimeField(default=django.utils.timezone.now)),
                ('end_time', models.TimeField(default=django.utils.timezone.now)),
                ('type_lesson', models.PositiveSmallIntegerField()),
                ('parity_week', models.PositiveSmallIntegerField()),
                ('day_week', models.PositiveSmallIntegerField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('institute_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('decryption', models.CharField(max_length=200)),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.University')),
            ],
        ),
        migrations.CreateModel(
            name='Housing',
            fields=[
                ('housing_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=5)),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.University')),
            ],
        ),
        migrations.AddField(
            model_name='faculty',
            name='institute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Institute'),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('decryption', models.CharField(max_length=200)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Faculty')),
            ],
        ),
    ]
