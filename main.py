import os, configparser
import controller.dump as dump
import controller.send as send
import controller.restore as restore
import controller.configure as configure
import controller.get as get

if __name__ == '__main__':
    #READ CONFIG.JSON
    config = configparser.ConfigParser()
    config.read('config.ini')

    #CONFIGURATION
    INSTANCENAME = config['DATABASE']['INSTANCENAME']
    DBHOST = config['DATABASE']['HOST']
    DBPORT = config['DATABASE']['PORT']
    DBNAME = config['DATABASE']['NAME']
    DBUSER = config['DATABASE']['USER']
    DBPASSWORD = config['DATABASE']['PASSWORD']
    BUCKET = config['CLOUDSTORAGE']['BUCKET']

    #AUTO-DECLARATION
    CLOUDSTORAGEBUCKET = config['CLOUDSTORAGE']['BUCKET'] + config['CLOUDSTORAGE']['BUCKET_SUBFOLDER']
    SOURCE_DB_PATH = "postgresql://"+DBUSER+":"+DBPASSWORD+"@"+DBHOST+":"+DBPORT+"/"+DBNAME+"" #postgresql://<USER>:<PASSWORD>@<HOST>:<PORT>/<DBNAME>
    CURDIR = os.getcwd()
    DUMPFILE = CURDIR+"/"+DBNAME+".sql"
    DUMPFILEINCLOUD = CLOUDSTORAGEBUCKET+"/"+DBNAME+".sql"
    DSTHOST = get.cloudsql_public_ip_adress(INSTANCENAME)
    
    #RUN ALL FUNCTION
    print(dump.database(SOURCE_DB_PATH,DUMPFILE))
    print(send.dump_to_cloud_storage(CLOUDSTORAGEBUCKET,DUMPFILE))
    print(configure.allow_access(BUCKET,DUMPFILEINCLOUD,INSTANCENAME))
    print(restore.pg_on_gcp(INSTANCENAME,CLOUDSTORAGEBUCKET,DUMPFILEINCLOUD,DSTHOST,DBHOST,DBNAME,DBUSER,DBPASSWORD))
    print(configure.deny_access(BUCKET,DUMPFILEINCLOUD,INSTANCENAME))
