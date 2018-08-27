import os, configparser
import controller.dump as dump
import controller.send as send
import controller.restore as restore

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
    SOURCE_DB_PATH = "postgresql://"+DBUSER+":"+DBPASSWORD+"@"+DBHOST+":"+DBPORT+"/"+DBNAME+"" #postgresql://<USER>:<PASSWORD>@<HOST>:<PORT>/<DBNAME>
    CURDIR = os.getcwd()
    DUMPFILE = CURDIR+"/"+DBNAME+".sql"
    DUMPFILEINCLOUD = CLOUDSTORAGEBUCKET+"/pg_dump_output.sql"
    
    #RUN ALL FUNCTION
    print(dump.database(SOURCE_DB_PATH,DUMPFILE))
    print(send.dump_to_cloud_storage(CLOUDSTORAGEBUCKET,DUMPFILE))
    print(restore.pg_on_gcp(INSTANCENAME,CLOUDSTORAGEBUCKET,DUMPFILEINCLOUD,DBNAME))

    #COMING SOON FEATURES
    # print(get.installed_extensions()) Features not yet available, please add extension manually
