import controller.get as get
import os

def allow_access_bucket(BUCKET,EMAILSERVICE):
    os.system("gsutil acl ch -u "+EMAILSERVICE+":W gs://"+BUCKET+"")

def allow_access_file(DUMPFILEINCLOUD,EMAILSERVICE):
    os.system("gsutil acl ch -u "+EMAILSERVICE+":R gs://"+DUMPFILEINCLOUD+"")

def deny_access_bucket(BUCKET,EMAILSERVICE):
    os.system("gsutil acl ch -d "+EMAILSERVICE+" gs://"+BUCKET+"")

def deny_access_file(DUMPFILEINCLOUD,EMAILSERVICE):
    os.system("gsutil acl ch -d "+EMAILSERVICE+" gs://"+DUMPFILEINCLOUD+"")

def allow_access(BUCKET,DUMPFILEINCLOUD,INSTANCENAME):
    print("Granting access to bucket and files")
    EMAILSERVICE = get.cloudsql_service_account_email_adress(INSTANCENAME)
    print(EMAILSERVICE)
    allow_access_bucket(BUCKET,EMAILSERVICE)
    allow_access_file(DUMPFILEINCLOUD,EMAILSERVICE)
    return "Done granting the access"

def deny_access(BUCKET,DUMPFILEINCLOUD,INSTANCENAME):
    print("Denying access to bucket and files")
    EMAILSERVICE = get.cloudsql_service_account_email_adress(INSTANCENAME)
    deny_access_bucket(BUCKET,EMAILSERVICE)
    deny_access_file(DUMPFILEINCLOUD,EMAILSERVICE)
    return "Done Denying the access"
