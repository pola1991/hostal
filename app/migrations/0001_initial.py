# Generated by Django 4.2.1 on 2023-10-14 20:45

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('es_cliente', models.BooleanField(default=False)),
                ('es_empleado', models.BooleanField(default=False)),
                ('nombre_empresa', models.CharField(blank=True, max_length=100, null=True)),
                ('rut_empresa', models.CharField(max_length=15)),
                ('cargo', models.CharField(blank=True, max_length=100, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'ordering': ['-id'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Comedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_plato', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Comedor',
                'verbose_name_plural': 'Comedores',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('cargo', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
            },
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_habitacion', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
                ('n_camas', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('estado_habitacion', models.CharField(choices=[('Disponible', 'Disponible'), ('No disponible por estar asignada a empresa', 'No disponible por estar asignada a empresa'), ('No disponible por estar en mantenimiento', 'No disponible por estar en mantenimiento')], max_length=50)),
            ],
            options={
                'verbose_name': 'Habitacion',
                'verbose_name_plural': 'Habitaciones',
            },
        ),
        migrations.CreateModel(
            name='Huesped',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_huesped', models.CharField(max_length=80)),
                ('habitacion_asignada', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.habitacion')),
                ('nombre_empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Huesped',
                'verbose_name_plural': 'Huespedes',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('rubro', models.CharField(max_length=30)),
                ('contacto', models.IntegerField()),
                ('otro', models.TextField()),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
        migrations.CreateModel(
            name='ServicioComedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Tipo_servicio',
                'verbose_name_plural': 'Tipo_servicios',
            },
        ),
        migrations.CreateModel(
            name='OrdenCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_orden', models.CharField(max_length=10, unique=True)),
                ('fecha_check_in', models.DateField()),
                ('fecha_check_out', models.DateField()),
                ('detalle_reserva', models.TextField(blank=True, null=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('habitaciones_asociadas', models.ManyToManyField(to='app.habitacion')),
                ('huesped', models.ManyToManyField(to='app.huesped')),
                ('servicios_adicionales', models.ManyToManyField(to='app.comedor')),
            ],
            options={
                'verbose_name': 'Orden_compra',
                'verbose_name_plural': 'Ordenes_compra',
            },
        ),
        migrations.AddField(
            model_name='comedor',
            name='servicio_comedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.serviciocomedor'),
        ),
    ]
