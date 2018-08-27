#step 4 initiate the dest db on gcp
import os

def pg_on_gcp(INSTANCENAME,BUCKET_NAME,DUMPFILEINCLOUD,DBNAME):
    os.system("gcloud sql import sql "+INSTANCENAME+" gs://"+BUCKET_NAME+"/pg_dump_output.sql --database="+DBNAME+"")


    ## Coming Soon features, please create db, user, and extension manually
    ##run gcp create db
    ##run gcp create db user
    ##run create extension query