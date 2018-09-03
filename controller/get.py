import subprocess

def cloudsql_service_account_email_adress(INSTANCENAME):
    val=subprocess.check_output("gcloud sql instances describe "+INSTANCENAME+" | grep serviceAccountEmailAddress | sed 's/[^ ]* *//'", shell=True).rstrip().decode("utf-8") 
    return val

def cloudsql_public_ip_adress(INSTANCENAME):
    val=subprocess.check_output("gcloud sql instances describe "+INSTANCENAME+" | grep ipAddress:  | sed 's/- ipAddress:* *//'", shell=True).rstrip().decode("utf-8") 
    return val