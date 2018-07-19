import pymysql

playerName = "Miguel"

# Connect to the database
connection = pymysql.connect(host='138.68.231.130',
                             user='python',
                             password='password',
                             db='blocky',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
class DBCONN(object):

    def insertPixel(self, pixel):

        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `pixel_dead` (`id`, `name`,`pixel`) VALUES (NULL,%s, %s)"
            cursor.execute(sql, (playerName, pixel))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

    def insertTime(self, time):

        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `time_completed` (`id`, `name`,`time`) VALUES (NULL,%s, %s)"
            cursor.execute(sql, (playerName, time))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()


    def closeConn(self):
        connection.close()
