import os

def dump_to_cloud_storage(CLOUDSTORAGEBUCKET, DUMPFILE):
    os.system("gsutil cp "+DUMPFILE+" gs://"+CLOUDSTORAGEBUCKET+"/")
    return "DUMPFILE HAS BEEN UPLOADED TO CLOUD STORAGE"
    
