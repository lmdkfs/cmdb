# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=256, verbose_name='\u7528\u6237\u540d')),
                ('password', models.CharField(max_length=256, verbose_name='\u5bc6\u7801')),
            ],
            options={
                'verbose_name_plural': '\u7528\u6237\u767b\u5f55\u8d26\u53f7',
            },
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cabinet_num', models.CharField(max_length=30, null=True, verbose_name='\u673a\u67dc\u53f7', blank=True)),
                ('cabinet_order', models.CharField(max_length=30, null=True, verbose_name='\u673a\u67dc\u4e2d\u5e8f\u53f7', blank=True)),
                ('memo', models.TextField(null=True, verbose_name='\u5907\u6ce8', blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('latest_date', models.DateField(null=True, blank=True)),
            ],
            options={
                'verbose_name': '\u8d44\u4ea7\u603b\u8868',
                'verbose_name_plural': '\u8d44\u4ea7\u603b\u8868',
            },
        ),
        migrations.CreateModel(
            name='BusinessUnit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64, verbose_name='\u4e1a\u52a1\u7ebf')),
                ('memo', models.CharField(max_length=64, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'verbose_name': '\u4e1a\u52a1\u7ebf',
                'verbose_name_plural': '\u4e1a\u52a1\u7ebf',
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sn', models.CharField(unique=True, max_length=64, verbose_name='\u5408\u540c\u53f7')),
                ('name', models.CharField(max_length=64, verbose_name='\u5408\u540c\u540d\u79f0')),
                ('cost', models.IntegerField(verbose_name='\u5408\u540c\u91d1\u989d')),
                ('start_date', models.DateTimeField(blank=True)),
                ('end_date', models.DateTimeField(blank=True)),
                ('license_num', models.IntegerField(verbose_name='license\u6570\u91cf', blank=True)),
                ('memo', models.TextField(verbose_name='\u5907\u6ce8', blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u5408\u540c',
                'verbose_name_plural': '\u5408\u540c',
            },
        ),
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('code', models.CharField(max_length=64)),
                ('memo', models.CharField(max_length=256, null=True, blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': '\u8bbe\u5907\u7c7b\u578b',
            },
        ),
        migrations.CreateModel(
            name='Disk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slot', models.CharField(max_length=32, verbose_name='\u63d2\u69fd\u4f4d', blank=True)),
                ('model', models.CharField(max_length=128, verbose_name='\u78c1\u76d8\u578b\u53f7', blank=True)),
                ('capacity', models.FloatField(verbose_name='\u78c1\u76d8\u5bb9\u91cfGB', blank=True)),
                ('pd_type', models.CharField(max_length=64, verbose_name='\u78c1\u76d8\u7c7b\u578b', blank=True)),
                ('memo', models.TextField(verbose_name='\u5907\u6ce8', blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': '\u786c\u76d8',
            },
        ),
        migrations.CreateModel(
            name='ErrorLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='HandleLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(null=True, blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('asset_info', models.ForeignKey(to='web_manage.Asset')),
            ],
            options={
                'verbose_name_plural': '\u8d44\u4ea7\u53d8\u66f4\u65e5\u5fd7',
            },
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('region', models.CharField(max_length=64, verbose_name='\u533a\u57df\u4e2d\u6587')),
                ('name', models.CharField(max_length=32, verbose_name='\u4e2d\u6587\u663e\u793a\u540d')),
                ('floor', models.IntegerField(default=1, verbose_name='\u697c\u5c42')),
                ('display', models.CharField(max_length=128)),
                ('memo', models.CharField(max_length=64, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '\u673a\u623f',
                'verbose_name_plural': '\u673a\u623f',
            },
        ),
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slot', models.CharField(max_length=32, verbose_name='\u63d2\u69fd\u4f4d', blank=True)),
                ('manufactory', models.CharField(max_length=32, null=True, verbose_name='\u5236\u9020\u5546', blank=True)),
                ('model', models.CharField(max_length=64, verbose_name='\u578b\u53f7', blank=True)),
                ('capacity', models.FloatField(verbose_name='\u5bb9\u91cf', blank=True)),
                ('sn', models.CharField(default=b'', max_length=256, null=True, blank=True)),
                ('speed', models.CharField(default=b'', max_length=64, null=True, blank=True)),
                ('memo', models.TextField(verbose_name='\u5907\u6ce8', blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u5185\u5b58\u90e8\u4ef6',
                'verbose_name_plural': '\u5185\u5b58\u90e8\u4ef6',
            },
        ),
        migrations.CreateModel(
            name='NetworkDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sn', models.CharField(unique=True, max_length=64, verbose_name='SN\u53f7')),
                ('asset', models.OneToOneField(to='web_manage.Asset')),
            ],
        ),
        migrations.CreateModel(
            name='NIC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='\u7f51\u5361\u540d\u79f0', blank=True)),
                ('hwaddr', models.CharField(max_length=64, verbose_name='\u7f51\u5361mac\u5730\u5740')),
                ('up', models.BooleanField(default=False)),
                ('netmask', models.CharField(max_length=64, blank=True)),
                ('ipaddrs', models.CharField(max_length=256, null=True, verbose_name='ip\u5730\u5740')),
                ('memo', models.TextField(verbose_name='\u5907\u6ce8', blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u7f51\u5361\u90e8\u4ef6',
                'verbose_name_plural': '\u7f51\u5361\u90e8\u4ef6',
            },
        ),
        migrations.CreateModel(
            name='OsInstall',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(max_length=128)),
                ('ip', models.GenericIPAddressField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(max_length=128, null=True, blank=True)),
                ('service_sn', models.CharField(max_length=128, null=True, verbose_name='\u5feb\u901f\u670d\u52a1\u7f16\u7801', blank=True)),
                ('sn', models.CharField(max_length=64, null=True, verbose_name='SN\u53f7', blank=True)),
                ('manufactory', models.CharField(max_length=128, null=True, verbose_name='\u5236\u9020\u5546', blank=True)),
                ('model', models.CharField(max_length=128, null=True, verbose_name='\u578b\u53f7', blank=True)),
                ('manage_ip', models.GenericIPAddressField(null=True, blank=True)),
                ('business_ip', models.GenericIPAddressField(null=True, blank=True)),
                ('os_platform', models.CharField(max_length=64, null=True, verbose_name='\u7cfb\u7edf', blank=True)),
                ('os_version', models.CharField(max_length=64, null=True, verbose_name='\u7cfb\u7edf\u7248\u672c', blank=True)),
                ('cpu_count', models.IntegerField(null=True, blank=True)),
                ('cpu_physical_count', models.IntegerField(null=True, blank=True)),
                ('cpu_model', models.CharField(max_length=128, null=True, blank=True)),
                ('first_mac', models.CharField(max_length=128, null=True, blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('asset', models.OneToOneField(to='web_manage.Asset')),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u5668',
                'verbose_name_plural': '\u670d\u52a1\u5668',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('code', models.CharField(max_length=64)),
                ('memo', models.TextField(null=True, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'verbose_name_plural': '\u72b6\u6001',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32, verbose_name=b'Tag name')),
                ('memo', models.TextField(verbose_name='\u5907\u6ce8', blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': '\u6807\u7b7e',
            },
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32, db_index=True)),
            ],
            options={
                'verbose_name_plural': '\u7528\u6237\u7ec4',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name='\u540d\u5b57')),
                ('email', models.EmailField(max_length=254, verbose_name='\u90ae\u7bb1')),
                ('phone', models.CharField(max_length=50, verbose_name='\u5ea7\u673a')),
                ('mobile', models.CharField(max_length=32, verbose_name='\u624b\u673a')),
                ('memo', models.TextField(verbose_name='\u5907\u6ce8', blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u7528\u6237\u4fe1\u606f',
                'verbose_name_plural': '\u7528\u6237\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caption', models.CharField(unique=True, max_length=32, db_index=True)),
                ('code', models.CharField(unique=True, max_length=32, db_index=True)),
            ],
            options={
                'verbose_name_plural': '\u7528\u6237\u7c7b\u578b',
            },
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_type',
            field=models.ForeignKey(to='web_manage.UserType'),
        ),
        migrations.AddField(
            model_name='usergroup',
            name='users',
            field=models.ManyToManyField(to='web_manage.UserProfile', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='osinstall',
            name='creator',
            field=models.ForeignKey(to='web_manage.UserProfile'),
        ),
        migrations.AddField(
            model_name='osinstall',
            name='server',
            field=models.ForeignKey(to='web_manage.Server'),
        ),
        migrations.AddField(
            model_name='nic',
            name='server_info',
            field=models.ForeignKey(to='web_manage.Server'),
        ),
        migrations.AddField(
            model_name='memory',
            name='server_info',
            field=models.ForeignKey(to='web_manage.Server'),
        ),
        migrations.AddField(
            model_name='handlelog',
            name='creator',
            field=models.ForeignKey(to='web_manage.UserProfile'),
        ),
        migrations.AddField(
            model_name='disk',
            name='server_info',
            field=models.ForeignKey(to='web_manage.Server'),
        ),
        migrations.AddField(
            model_name='businessunit',
            name='contact',
            field=models.ForeignKey(to='web_manage.UserProfile'),
        ),
        migrations.AddField(
            model_name='businessunit',
            name='user_group',
            field=models.ForeignKey(blank=True, to='web_manage.UserGroup', null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='business_unit',
            field=models.ForeignKey(verbose_name='\u5c5e\u4e8e\u7684\u4e1a\u52a1\u7ebf', blank=True, to='web_manage.BusinessUnit', null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='contract',
            field=models.ForeignKey(verbose_name='\u5408\u540c', blank=True, to='web_manage.Contract', null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='device_status',
            field=models.ForeignKey(to='web_manage.Status'),
        ),
        migrations.AddField(
            model_name='asset',
            name='device_type',
            field=models.ForeignKey(to='web_manage.DeviceType'),
        ),
        migrations.AddField(
            model_name='asset',
            name='idc',
            field=models.ForeignKey(verbose_name='IDC\u673a\u623f', blank=True, to='web_manage.IDC', null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='tag',
            field=models.ManyToManyField(to='web_manage.Tag', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='admininfo',
            name='user_info',
            field=models.OneToOneField(to='web_manage.UserProfile'),
        ),
        migrations.AlterIndexTogether(
            name='server',
            index_together=set([('sn', 'asset')]),
        ),
    ]
