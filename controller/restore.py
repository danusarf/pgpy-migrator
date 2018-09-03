#step 4 initiate the dest db on gcp
import os, psycopg2

def user(DBUSER,INSTANCENAME,DBPASSWORD):
    os.system("gcloud sql users create "+DBUSER+" --instance="+INSTANCENAME+" --password="+DBPASSWORD+"")
def database(DBNAME,INSTANCENAME):
    os.system("gcloud sql databases create "+DBNAME+" --instance="+INSTANCENAME+"")
def data(INSTANCENAME,DUMPFILEINCLOUD,DBNAME,DBUSER):
    os.system("gcloud sql import sql "+INSTANCENAME+" gs://"+DUMPFILEINCLOUD+" --database="+DBNAME+" --user="+DBUSER+"")

def extension(DSTHOST,DBHOST,DBNAME,DBUSER,DBPASSWORD):
    print("Creating Connection to Source Database")
    conn=psycopg2.connect("host='"+DBHOST+"' dbname='"+DBNAME+"' user='"+DBUSER+"' password='"+DBPASSWORD+"'")
    cur = conn.cursor()
    print("CONNECTION ESTABLISED")
    try:
        cur.execute("""SELECT extname from pg_extension""")
    except:
        print ("FAILED GETTING pg_extension")
    rows = cur.fetchall()
    i=0
    str = ''
    print("Succesfully retriving current pg_extension")
    conn.close()
    cur.close()

    print("Creating Connection to Destination Database")
    conn=psycopg2.connect("host='"+DSTHOST+"' dbname='"+DBNAME+"' user='"+DBUSER+"' password='"+DBPASSWORD+"'")
    cur = conn.cursor()
    print("CONNECTION ESTABLISED")
    for row in rows:
        ext = str +''.join(rows[i])
        try:
            cur.execute("CREATE EXTENSION IF NOT EXISTS \""+ext+"\";")
        except:
            print ("FAILED CREATING EXTENSION: "+ext+"")
        i=i+1
    print("Successfuly restoring all pg_extension, Closing connection..")
    conn.commit()
    conn.close()
    cur.close()

def pg_on_gcp(INSTANCENAME,CLOUDSTORAGEBUCKET,DUMPFILEINCLOUD,DSTHOST,DBHOST,DBNAME,DBUSER,DBPASSWORD):
    user(DBUSER,INSTANCENAME,DBPASSWORD)
    database(DBNAME,INSTANCENAME)
    extension(DSTHOST,DBHOST,DBNAME,DBUSER,DBPASSWORD)
    data(INSTANCENAME,DUMPFILEINCLOUD,DBNAME,DBUSER)
    return("Done restoring database")