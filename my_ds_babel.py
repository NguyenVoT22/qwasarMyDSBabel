import csv, sqlite3

class Convert:
    def sql_to_csv(self):
        connection = sqlite3.connect("all_fault_line.db")
        print(connection)
        curs = connection.cursor()
        data = curs.execute("SELECT * FROM " + "fault_lines")
        print(data)

        with open("all_fault_line.csv", "w") as csv_file:
            cwriter = csv.writer(csv_file)
            cwriter.writerow(['fault_name', 'length', 'location', 'sense_of_movement', 'time_of_movement', 'associated_earthquakes'])
            cwriter.writerows(data)
    
    def csv_to_sql(self):
        connection = sqlite3.connect("list_volcano.db")
        print(connection)
        curs = connection.cursor()
        print(curs)
        curs.execute("CREATE TABLE t (`Volcano Name`, `Country`, `Type`, `Latitude (dd)`, `Longitude (dd)`, `Elevation (m)`);")

        with open("list_volcano.csv", "r") as final:
            dictread = csv.DictReader(final)
            to_db = [(i['Volcano Name'], i['Country'], i['Type'], i['Latitude (dd)'], i['Longitude (dd)'], i['Elevation (m)']) for i in dictread]
        
        curs.executemany("INSERT INTO t (`Volcano Name`, `Country`, `Type`, `Latitude (dd)`, `Longitude (dd)`, `Elevation (m)`) VALUES (?, ?, ?, ?, ?, ?);", to_db)
        
        connection.commit()
        connection.close()

to_csv = Convert()
to_csv.sql_to_csv()

to_sql = Convert()
to_sql.csv_to_sql()
