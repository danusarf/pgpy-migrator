# pgpy-migrator

**pgpy-migrator** will help you to migrate database from any PostgreSQL to GCP's PostgreSQL Cloud SQL written in **python3**. Utilizing pyscopg2 and gcloud cli, you may need to install some dependency before using this tool.

# How to Use

This section will help you to start the migration right away and smoothly.

## 1. Installing Dependencies

You need to have python3 installed in your machine before proceeding to this section. Use `python3 --version` to check the python3 version. Developer is using `Python 3.7.0`.
1. Install the psycopg2 by using pip `python3 -m pip install psycopg2`.
2. Install the configparser by using pip `python3 -m pip install configparser`.

## 2. Setting up gcloud access
To start the migration you need to have google cloud access please check on your machine, whether it's installed and configured by typing `gcloud -v`. To setup the gcloud please refer to this google's official documentation https://cloud.google.com/sdk/gcloud/

Below is the version of gcloud that developer used to write this tool:

    Google Cloud SDK 213.0.0
    bq 2.0.34
    core 2018.08.17
    gsutil 4.33

 

## 3. Create config.ini

On the directory of the project of this Repository, you will find config.ini.example. Rename it or create new `config.ini` and change the value of that file.

    [DATABASE]
    HOST = host of source db, could be rds hostname or any db public ip address
    PORT = port of source db, use 5432 as default PostgreSQL port
    NAME = database name of source db
    USER = username of the source db
    PASSWORD = password of the source db
    INSTANCENAME = name of the cloud sql instance on gcp that you created to restore the db (instance name of the database)
    
    [CLOUDSTORAGE]
    BUCKET =BUCKET = name of the bucket
	BUCKET_SUBFOLDER = subfolder on the bucket

## 4. Start the migration

Start the migration process by executing main.py: `python3 main.py`
