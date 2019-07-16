# Generated by Django 2.1 on 2019-07-16 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=45)),
                ('pincode', models.CharField(blank=True, max_length=45, null=True)),
                ('contact', models.IntegerField()),
                ('country', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='Assesment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ass_id', models.CharField(max_length=45, unique=True)),
                ('type', models.CharField(max_length=45)),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'assesment',
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'attendance',
            },
        ),
        migrations.CreateModel(
            name='BookIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateField()),
            ],
            options={
                'db_table': 'book_issue',
            },
        ),
        migrations.CreateModel(
            name='BookReturn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('return_date', models.DateField()),
            ],
            options={
                'db_table': 'book_return',
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.CharField(max_length=45, unique=True)),
                ('book_name', models.CharField(max_length=45)),
                ('author', models.CharField(max_length=45)),
                ('publication', models.CharField(max_length=45)),
                ('purchase_date', models.DateField()),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
            options={
                'db_table': 'books',
            },
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_total', models.IntegerField()),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'deposit',
            },
        ),
        migrations.CreateModel(
            name='DepositRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('deposit_date', models.DateField()),
            ],
            options={
                'db_table': 'deposit_record',
            },
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField()),
                ('ass', models.ForeignKey(default='01', on_delete=django.db.models.deletion.DO_NOTHING, to='rfid.Assesment')),
            ],
            options={
                'db_table': 'marks',
            },
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_id', models.CharField(max_length=45, unique=True)),
                ('f_name', models.CharField(max_length=45)),
                ('l_name', models.CharField(max_length=45)),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=45)),
                ('photo', models.CharField(blank=True, max_length=45, null=True)),
                ('profession', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'parent',
            },
        ),
        migrations.CreateModel(
            name='PaymentAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('psw', models.CharField(max_length=60)),
                ('created_date', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'payment_account',
            },
        ),
        migrations.CreateModel(
            name='PaymentRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'payment_record',
            },
        ),
        migrations.CreateModel(
            name='RfReader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reader_id', models.CharField(max_length=45, unique=True)),
                ('purpose', models.CharField(max_length=45)),
                ('install_date', models.DateField()),
            ],
            options={
                'db_table': 'rf_reader',
            },
        ),
        migrations.CreateModel(
            name='StdSubs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_grade', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'std_subs',
            },
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_roll', models.CharField(max_length=45, unique=True)),
                ('rftag', models.CharField(max_length=45)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('grade', models.CharField(max_length=45)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('enroll_date', models.DateField()),
                ('photo', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.ForeignKey(default='01', on_delete=django.db.models.deletion.DO_NOTHING, to='rfid.Address')),
                ('parent', models.ForeignKey(default='01', on_delete=django.db.models.deletion.DO_NOTHING, to='rfid.Parent')),
            ],
            options={
                'db_table': 'student_info',
            },
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_id', models.CharField(max_length=45, unique=True)),
                ('sub_name', models.CharField(max_length=45)),
                ('grade', models.CharField(max_length=45)),
                ('type', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'subjects',
            },
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tea_id', models.CharField(max_length=45, unique=True)),
                ('f_name', models.CharField(max_length=45)),
                ('l_name', models.CharField(max_length=45)),
                ('rftag', models.CharField(max_length=45)),
                ('gender', models.CharField(max_length=45)),
                ('dob', models.DateField()),
                ('roll_type', models.CharField(max_length=45)),
                ('address', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('photo', models.CharField(blank=True, max_length=45, null=True)),
                ('address_0', models.ForeignKey(db_column='address_id', default='01', on_delete=django.db.models.deletion.DO_NOTHING, to='rfid.Address')),
            ],
            options={
                'db_table': 'teachers',
            },
        ),
        migrations.CreateModel(
            name='TeaSub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub', models.ForeignKey(default='01', on_delete=django.db.models.deletion.DO_NOTHING, to='rfid.Subjects')),
                ('tea', models.ForeignKey(default='01', on_delete=django.db.models.deletion.DO_NOTHING, to='rfid.Teachers')),
            ],
            options={
                'db_table': 'tea_sub',
            },
        ),
        migrations.AlterUniqueTogether(
            name='subjects',
            unique_together={('id', 'sub_id')},
        ),
        migrations.AddField(
            model_name='stdsubs',
            name='std_roll',
            field=models.ForeignKey(db_column='std_roll', default='01', on_delete=django.db.models.deletion.DO_NOTHING, to='rfid.StudentInfo'),
        ),
        migrations.AlterUniqueTogether(
            name='rfreader',
            unique_together={('id', 'reader_id')},
        ),
        migrations.AddField(
            model_name='paymentrecord',
            name='reader',
            field=models.ForeignKey(default='01', on_delete=django.db.models.deletion.DO_NOTHING, to='rfid.RfReader'),
        ),
        migrations.AddField(
            model_name='paymentrecord',
            name='user',
            field=models.ForeignKey(default='01', on_delete=django.db.models.deletion.DO_NOTHING, to='rfid.PaymentAccount'),
        ),
        migrations.AddField(
            model_name='paymentaccount',
            name='user',
            field=models.ForeignKey(default='01', on_delete=django.db.models.deletion.DO_NOTHING, to='rfid.Teachers'),
        ),
        migrations.AlterUniqueTogether(
            name='parent',
            unique_together={('id', 'parent_id')},
        ),
        migrations.AddField(
            model_name='marks',
            name='std_roll',
            field=models.ForeignKey(db_column='std_roll', default='01', on_delete=django.db.models.deletion.DO_NOTHING, to='rfid.StudentInfo'),
        ),
        migrations.AddField(
            model_name='marks',
            name='sub',
            field=models.ForeignKey(default='01', on_delete=django.db.models.deletion.DO_NOTHING, to='rfid.Subjects'),
        ),
        migrations.AddField(
            model_name='marks',
            name='tea',
            field=models.ForeignKey(default='01', on_delete=django.db.models.deletion.DO_NOTHING, to='rfid.Teachers'),
        ),
        migrations.AddField(
            model_name='depositrecord',
            name='user',
            field=models.ForeignKey(default='01', on_delete=django.db.models.deletion.DO_NOTHING, to='rfid.PaymentAccount'),
        ),
        migrations.AddField(
            model_name='deposit',
            name='user',
            field=models.ForeignKey(default='01', on_delete=django.db.models.deletion.DO_NOTHING, to='rfid.PaymentAccount'),
        ),
        migrations.AlterUniqueTogether(
            name='books',
            unique_together={('id', 'book_id')},
        ),
        migrations.AddField(
            model_name='bookreturn',
            name='book',
            field=models.ForeignKey(default='01', on_delete=django.db.models.deletion.DO_NOTHING, to='rfid.Books'),
        ),
        migrations.AddField(
            model_name='bookreturn',
            name='std_roll',
            field=models.ForeignKey(db_column='std_roll', default='01', on_delete=django.db.models.deletion.DO_NOTHING, to='rfid.StudentInfo'),
        ),
        migrations.AddField(
            model_name='bookissue',
            name='book',
            field=models.ForeignKey(default='01', on_delete=django.db.models.deletion.DO_NOTHING, to='rfid.Books'),
        ),
        migrations.AddField(
            model_name='bookissue',
            name='std_roll',
            field=models.ForeignKey(db_column='std_roll', default='01', on_delete=django.db.models.deletion.DO_NOTHING, to='rfid.StudentInfo'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='std_roll',
            field=models.ForeignKey(db_column='std_roll', default='01', on_delete=django.db.models.deletion.DO_NOTHING, to='rfid.StudentInfo'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='sub',
            field=models.ForeignKey(default='01', on_delete=django.db.models.deletion.DO_NOTHING, to='rfid.Subjects'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='tea',
            field=models.ForeignKey(default='01', on_delete=django.db.models.deletion.DO_NOTHING, to='rfid.Teachers'),
        ),
        migrations.AddField(
            model_name='assesment',
            name='sub',
            field=models.ForeignKey(default='01', on_delete=django.db.models.deletion.DO_NOTHING, to='rfid.Subjects'),
        ),
        migrations.AlterUniqueTogether(
            name='teachers',
            unique_together={('id', 'tea_id', 'address_0')},
        ),
        migrations.AlterUniqueTogether(
            name='studentinfo',
            unique_together={('id', 'std_roll', 'address')},
        ),
        migrations.AlterUniqueTogether(
            name='stdsubs',
            unique_together={('id', 'std_roll')},
        ),
        migrations.AlterUniqueTogether(
            name='paymentaccount',
            unique_together={('id', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='deposit',
            unique_together={('id', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together={('id', 'std_roll', 'sub', 'tea')},
        ),
        migrations.AlterUniqueTogether(
            name='assesment',
            unique_together={('id', 'ass_id')},
        ),
    ]