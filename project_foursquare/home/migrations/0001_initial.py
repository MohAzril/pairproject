from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('nama_mall', models.CharField(max_length=255)),
                ('lokasi_mall', models.CharField(max_length=255)),
                ('deskripsi_mall', models.TextField()),
                ('map_mall', models.TextField()),
                ('fasilitas_1', models.CharField(max_length=50)),
                ('fasilitas_2', models.CharField(max_length=50)),
                ('fasilitas_3', models.CharField(max_length=50)),
                ('fasilitas_4', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('lokasi', models.CharField(max_length=255)),
                ('gambar', models.ImageField(upload_to='images')),
                ('deskripsi', models.TextField(max_length=500)),
                ('map_park', models.CharField(max_length=1000)),
                ('fasilitas_1', models.CharField(max_length=255)),
                ('fasilitas_2', models.CharField(max_length=255)),
                ('fasilitas_3', models.CharField(max_length=255)),
                ('fasilitas_4', models.CharField(max_length=255)),
            ],
        ),
    ]
