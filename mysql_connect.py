import mysql.connector

def s3_mysql(KEY, object_url, file_size, file_name):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="manic001@",
        database="s3_location"
        )

        print(mydb)
        print("db connection made suceesfull")
        
        myvalues = mydb.cursor()
        sql = "INSERT INTO filelocation (file_name, location, filesize) VALUES (%s, %s, %s)"
        val = (KEY, object_url , file_size)
        myvalues.execute(sql, val)
        mydb.commit()
        print("the {} is inserted in mysql".format(file_name))
        mydb.close()