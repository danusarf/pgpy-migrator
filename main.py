import os, configparser

if __name__ == '__main__':
    #READ CONFIG.JSON
    config = configparser.ConfigParser()
    config.read('config.ini')

    #CONFIGURATION
    DBHOST = config['DATABASE']['HOST']
    DBPORT = config['DATABASE']['PORT']
    DBNAME = config['DATABASE']['NAME']
    DBUSER = config['DATABASE']['USER']
    DBPASSWORD = config['DATABASE']['PASSWORD']
    CLOUDSTORAGEBUCKET = config['CLOUDSTORAGE']['BUCKET']

    #AUTO-DECLARATION
    PG_DUMP_SYNTAX = "postgresql://"+DBUSER+":"+DBPASSWORD+"@"+DBHOST+":"+DBPORT+"/"+DBNAME+"" #postgresql://<USER>:<PASSWORD>@<HOST>:<PORT>/<DBNAME>
    CURDIR = os.getcwd()
    DUMPFILE = CURDIR+"/pg_dump_output.sql"
    
    #RUN ALL FUNCTION
    print(dump.database(SOURCE_DB_PATH,DUMPFILE))
    print(send.dump_to_cloud_storage(CLOUDSTORAGEBUCKET,DUMPFILE))
    print(restore.pg_on_gcp())

    #COMING SOON FEATURES
    # print(get.installed_extensions()) Features not yet available, please add extension manually
