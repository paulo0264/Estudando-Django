# Generated by Django 4.1.2 on 2022-10-31 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Proposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(blank=True, max_length=14)),
                ('cnpj', models.CharField(blank=True, max_length=18)),
                ('endereco', models.CharField(blank=True, max_length=200)),
                ('bairro', models.CharField(blank=True, max_length=100)),
                ('cidade', models.CharField(blank=True, max_length=100)),
                ('estado', models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2, null=True)),
                ('data', models.DateField(verbose_name='Data de Emissão')),
                ('validade', models.CharField(blank=True, choices=[('Quinze', '15 (Quinze)'), ('Trinta', '30 (Trinta)'), ('Sessenta', '60 (Sessenta)')], max_length=200)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8)),
                ('situacao', models.CharField(choices=[('Atrasado', 'Atrasado'), ('AVencer', 'Á Vencer'), ('Pago', 'Pago')], max_length=200)),
                ('pago', models.BooleanField(default=False)),
                ('dominio', models.CharField(blank=True, help_text='URL - exe: seudominio.com.br', max_length=200)),
                ('dominio_loguin', models.CharField(blank=True, help_text='URL - exe: seudominio.com.br/admin', max_length=200)),
                ('loguin', models.CharField(blank=True, max_length=30)),
                ('senha', models.CharField(blank=True, max_length=30)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proposta.cliente')),
            ],
            options={
                'verbose_name': 'UMA PROPOSTA',
                'verbose_name_plural': 'PROPOSTAS',
                'ordering': ['-data'],
            },
        ),
    ]
