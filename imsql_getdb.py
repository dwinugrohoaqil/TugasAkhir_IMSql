from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import mysql.connector
from mysql.connector import Error
from kivy.clock import Clock
import time
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import mysql.connector
from kivy.animation import Animation
from kivy.core.window import Window
Window.clearcolor = (0.098,0.603,0.623,1)


class MainWindow(Screen):
    
    def val_in(self):
        global host, database, user, password
        host= self.ids.hst.text
        database= self.ids.db.text   
        user= self.ids.usr.text    
        password= self.ids.pwd.text 
        try:
            global connection
            connection = mysql.connector.connect(host= self.ids.hst.text,
                                                database= self.ids.db.text,
                                                user= self.ids.usr.text,
                                                password= self.ids.pwd.text)
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("You're connected to database: ", record)
                self.manager.current="menu"

        except Error as e:
            print("Error while connecting to MySQL", e)
            
    def close_application():
        App.get_running_app().stop()
        Window.close()
            
class MenuWindow(Screen,BoxLayout):
    pass

class SecondWindow(Screen,BoxLayout):
    def on_enter(self):
        Clock.schedule_interval(self.readComm, 1)

    def readComm(self,_):
        global db,data

        
        db = mysql.connector.connect(
            host=host, user=user, password=password, database=database)
        cursor = db.cursor()

        try:

            # Query untuk tabel cwp1
            sql_1 = "SELECT Paper_Level FROM cwp1 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_1)
            results_1 = cursor.fetchall()
            word_1 = ""
            for row in results_1:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_1 = f"{word_1}\n{paper_level}"
            self.ids.hasil1.text = word_1


            # Query untuk tabel cwp2
            sql_2 = "SELECT Paper_Level FROM cwp2 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_2)
            results_2 = cursor.fetchall()
            word_2 = ""
            for i in results_2:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_2 = f"{word_2}\n{paper_level}"
            self.ids.hasil2.text = word_2

            # Query untuk tabel cwp3
            sql_3 = "SELECT Paper_Level FROM cwp3 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_3)
            results_3 = cursor.fetchall()
            word_3 = ""
            for i in results_3:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_3 = f"{word_3}\n{paper_level}"
            self.ids.hasil3.text = word_3

            sql_4 = "SELECT Paper_Level FROM cwp4 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_4)
            results_4 = cursor.fetchall()
            word_4 = ""
            for row in results_4:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_4 = f"{word_4}\n{paper_level}"
            self.ids.hasil4.text = word_4


            # Query untuk tabel cwp5
            sql_5 = "SELECT Paper_Level FROM cwp5 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_5)
            results_5 = cursor.fetchall()
            word_5 = ""
            for i in results_5:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_5 = f"{word_5}\n{paper_level}"
            self.ids.hasil5.text = word_5

            # Query untuk tabel cwp3
            sql_6 = "SELECT Paper_Level FROM cwp6 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_6)
            results_6 = cursor.fetchall()
            word_6 = ""
            for i in results_6:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_6 = f"{word_6}\n{paper_level}"
            self.ids.hasil6.text = word_6

            sql_7 = "SELECT Paper_Level FROM cwp7 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_7)
            results_7 = cursor.fetchall()
            word_7 = ""
            for row in results_7:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_7 = f"{word_7}\n{paper_level}"
            self.ids.hasil7.text = word_7


            # Query untuk tabel cwp2
            sql_8 = "SELECT Paper_Level FROM cwp8 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_8)
            results_8 = cursor.fetchall()
            word_8 = ""
            for i in results_8:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_8 = f"{word_8}\n{paper_level}"
            self.ids.hasil8.text = word_8

            # Query untuk tabel cwp3
            sql_9 = "SELECT Paper_Level FROM cwp9 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_9)
            results_9 = cursor.fetchall()
            word_9 = ""
            for i in results_9:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_9 = f"{word_9}\n{paper_level}"
            self.ids.hasil9.text = word_9

            sql_10 = "SELECT Paper_Level FROM cwp10 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_10)
            results_10 = cursor.fetchall()
            word_10 = ""
            for row in results_10:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_10 = f"{word_10}\n{paper_level}"
            self.ids.hasil10.text = word_10

            sql_11 = "SELECT Paper_Level FROM cwp11 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_11)
            results_11 = cursor.fetchall()
            word_11 = ""
            for row in results_11:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_11 = f"{word_11}\n{paper_level}"
            self.ids.hasil11.text = word_11


            # Query untuk tabel cwp12
            sql_12 = "SELECT Paper_Level FROM cwp12 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_12)
            results_12 = cursor.fetchall()
            word_12 = ""
            for i in results_12:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_12 = f"{word_12}\n{paper_level}"
            self.ids.hasil12.text = word_12

            # Query untuk tabel cwp13
            sql_13 = "SELECT Paper_Level FROM cwp13 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_13)
            results_13 = cursor.fetchall()
            word_13 = ""
            for i in results_13:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_13 = f"{word_13}\n{paper_level}"
            self.ids.hasil13.text = word_13

            sql_14 = "SELECT Paper_Level FROM cwp14 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_14)
            results_14 = cursor.fetchall()
            word_14 = ""
            for row in results_14:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_14 = f"{word_14}\n{paper_level}"
            self.ids.hasil14.text = word_14


            # Query untuk tabel cwp15
            sql_15 = "SELECT Paper_Level FROM cwp15 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_15)
            results_15 = cursor.fetchall()
            word_15 = ""
            for i in results_15:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_15 = f"{word_15}\n{paper_level}"
            self.ids.hasil15.text = word_15

            # Query untuk tabel cwp13
            sql_16 = "SELECT Paper_Level FROM cwp16 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_16)
            results_16 = cursor.fetchall()
            word_16 = ""
            for i in results_16:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_16 = f"{word_16}\n{paper_level}"
            self.ids.hasil16.text = word_16

            sql_17 = "SELECT Paper_Level FROM cwp17 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_17)
            results_17 = cursor.fetchall()
            word_17 = ""
            for row in results_17:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_17 = f"{word_17}\n{paper_level}"
            self.ids.hasil17.text = word_17


            # Query untuk tabel cwp12
            sql_18 = "SELECT Paper_Level FROM cwp18 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_18)
            results_18 = cursor.fetchall()
            word_18 = ""
            for i in results_18:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_18 = f"{word_18}\n{paper_level}"
            self.ids.hasil18.text = word_18

            # Query untuk tabel cwp13
            sql_19 = "SELECT Paper_Level FROM cwp19 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_19)
            results_19 = cursor.fetchall()
            word_19 = ""
            for i in results_19:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_19 = f"{word_19}\n{paper_level}"
            self.ids.hasil19.text = word_19

            sql_20 = "SELECT Paper_Level FROM cwp20 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_20)
            results_20 = cursor.fetchall()
            word_20 = ""
            for row in results_20:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_20 = f"{word_20}\n{paper_level}"
            self.ids.hasil20.text = word_20


            sql_21 = "SELECT Paper_Level FROM cwp21 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_21)
            results_21 = cursor.fetchall()
            word_21 = ""
            for row in results_21:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_21 = f"{word_21}\n{paper_level}"
            self.ids.hasil21.text = word_21


            # Query untuk tabel cwp22
            sql_22 = "SELECT Paper_Level FROM cwp22 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_22)
            results_22 = cursor.fetchall()
            word_22 = ""
            for i in results_22:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_22 = f"{word_22}\n{paper_level}"
            self.ids.hasil22.text = word_22

            # Query untuk tabel cwp23
            sql_23 = "SELECT Paper_Level FROM cwp23 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_23)
            results_23 = cursor.fetchall()
            word_23 = ""
            for i in results_23:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_23 = f"{word_23}\n{paper_level}"
            self.ids.hasil23.text = word_23

            sql_24 = "SELECT Paper_Level FROM cwp24 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_24)
            results_24 = cursor.fetchall()
            word_24 = ""
            for row in results_24:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_24 = f"{word_24}\n{paper_level}"
            self.ids.hasil24.text = word_24


            sql_25 = "SELECT Paper_Level FROM cwp25 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_25)
            results_25 = cursor.fetchall()
            word_25 = ""
            for i in results_25:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_25 = f"{word_25}\n{paper_level}"
            self.ids.hasil25.text = word_25

            # Query untuk tabel cwp23
            sql_26 = "SELECT Paper_Level FROM cwp26 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_26)
            results_26 = cursor.fetchall()
            word_26 = ""
            for i in results_26:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_26 = f"{word_26}\n{paper_level}"
            self.ids.hasil26.text = word_26

            sql_27 = "SELECT Paper_Level FROM cwp27 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_27)
            results_27 = cursor.fetchall()
            word_27 = ""
            for row in results_27:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_27 = f"{word_27}\n{paper_level}"
            self.ids.hasil27.text = word_27


            # Query untuk tabel cwp22
            sql_28 = "SELECT Paper_Level FROM cwp28 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_28)
            results_28 = cursor.fetchall()
            word_28 = ""
            for i in results_28:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_28 = f"{word_28}\n{paper_level}"
            self.ids.hasil28.text = word_28

            # Query untuk tabel cwp23
            sql_29 = "SELECT Paper_Level FROM cwp29 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_29)
            results_29 = cursor.fetchall()
            word_29 = ""
            for i in results_29:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_29 = f"{word_29}\n{paper_level}"
            self.ids.hasil29.text = word_29

            sql_30 = "SELECT Paper_Level FROM cwp30 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_30)
            results_30 = cursor.fetchall()
            word_30 = ""
            for row in results_30:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_30 = f"{word_30}\n{paper_level}"
            self.ids.hasil30.text = word_30


            db.commit()

        except:
            print ("Error! Unable to fetch data" )  
        
        return
       
class ThirdWindow(Screen):

    def on_enter(self):
        Clock.schedule_interval(self.readComm, 1)

    def readComm(self,_):
        global db,data
        # namatblsensor= self.ids.adcsensor.text
        
        db = mysql.connector.connect(
            host=host, user=user, password=password, database=database)
        cursor = db.cursor()

        try:
            sql_30 = "SELECT Paper_Level FROM cwp30 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_30)
            results_30 = cursor.fetchall()
            word_30 = ""
            for row in results_30:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_30 = f"{word_30}\n{paper_level}"
            self.ids.hasil30.text = word_30


            sql_31 = "SELECT Paper_Level FROM cwp31 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_31)
            results_31 = cursor.fetchall()
            word_31 = ""
            for row in results_31:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_31 = f"{word_31}\n{paper_level}"
            self.ids.hasil31.text = word_31


            sql_32 = "SELECT Paper_Level FROM cwp32 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_32)
            results_32 = cursor.fetchall()
            word_32 = ""
            for row in results_32:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_32 = f"{word_32}\n{paper_level}"
            self.ids.hasil32.text = word_32


            sql_33 = "SELECT Paper_Level FROM cwp33 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_33)
            results_33 = cursor.fetchall()
            word_33 = ""
            for row in results_33:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_33 = f"{word_33}\n{paper_level}"
            self.ids.hasil33.text = word_33


            sql_34 = "SELECT Paper_Level FROM cwp34 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_34)
            results_34 = cursor.fetchall()
            word_34 = ""
            for row in results_34:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_34 = f"{word_34}\n{paper_level}"
            self.ids.hasil34.text = word_34


            sql_35 = "SELECT Paper_Level FROM cwp35 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_35)
            results_35 = cursor.fetchall()
            word_35 = ""
            for row in results_35:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_35 = f"{word_30}\n{paper_level}"
            self.ids.hasil35.text = word_35


            sql_36 = "SELECT Paper_Level FROM cwp36 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_36)
            results_36 = cursor.fetchall()
            word_36 = ""
            for row in results_36:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_36 = f"{word_36}\n{paper_level}"
            self.ids.hasil36.text = word_36


            sql_37 = "SELECT Paper_Level FROM cwp37 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_37)
            results_37 = cursor.fetchall()

            word_37 = ""
            for row in results_37:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_37 = f"{word_37}\n{paper_level}"
            self.ids.hasil37.text = word_37


            sql_38 = "SELECT Paper_Level FROM cwp38 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_38)
            results_38 = cursor.fetchall()

            word_38 = ""
            for row in results_38:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_38 = f"{word_38}\n{paper_level}"
            self.ids.hasil38.text = word_38


            sql_39 = "SELECT Paper_Level FROM cwp39 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_39)
            results_39 = cursor.fetchall()

            word_39 = ""
            for row in results_39:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_39 = f"{word_39}\n{paper_level}"
            self.ids.hasil39.text = word_39


            sql_40 = "SELECT Paper_Level FROM cwp40 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_40)
            results_40 = cursor.fetchall()
            word_40 = ""
            for row in results_40:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_40 = f"{word_40}\n{paper_level}"
            self.ids.hasil40.text = word_40



            sql_41 = "SELECT Paper_Level FROM cwp41 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_41)
            results_41 = cursor.fetchall()
            word_41 = ""
            for i in results_41:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_41 = f"{word_41}\n{paper_level}"
            self.ids.hasil41.text = word_41

            # Query untuk tabel cwp47
            sql_42 = "SELECT Paper_Level FROM cwp42 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_42)
            results_42 = cursor.fetchall()

            word_42 = ""
            for i in results_42:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_42 = f"{word_42}\n{paper_level}"
            self.ids.hasil42.text = word_42

            sql_43 = "SELECT Paper_Level FROM cwp43 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_43)
            results_43 = cursor.fetchall()

            word_43 = ""
            for i in results_43:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_43 = f"{word_43}\n{paper_level}"
            self.ids.hasil43.text = word_43

            sql_44 = "SELECT Paper_Level FROM cwp44 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_44)
            results_44 = cursor.fetchall()


            word_44 = ""
            for i in results_44:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_44 = f"{word_44}\n{paper_level}"
            self.ids.hasil44.text = word_44

            db.commit()


        except:
            print ("Error! Unable to fetch data" )  
        
        return


class FourWindow(Screen):
    # def stp_btn(self):
    #     dd.cancel()
    def on_enter(self):
        Clock.schedule_interval(self.readComm, 1)

    def readComm(self,_):
        global db,data
        # namatblsensor= self.ids.adcsensor.text
        
        db = mysql.connector.connect(
            host=host, user=user, password=password, database=database)
        cursor = db.cursor()

        try:

            sql_45 = "SELECT Paper_Level FROM cwp45 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_45)
            results_45 = cursor.fetchall()
            word_45 = ""
            for row in results_45:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_45 = f"{word_45}\n{paper_level}"
            self.ids.hasil45.text = word_45


            # Query untuk tabel cwp46
            sql_46 = "SELECT Paper_Level FROM cwp46 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_46)
            results_46 = cursor.fetchall()
            word_46 = ""
            for i in results_46:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_46 = f"{word_46}\n{paper_level}"
            self.ids.hasil46.text = word_46

            # Query untuk tabel cwp47
            sql_47 = "SELECT Paper_Level FROM cwp47 ORDER BY Timestamp DESC LIMIT 1;"
            cursor.execute(sql_47)
            results_47 = cursor.fetchall()
            word_47 = ""
            for i in results_47:
                paper_level = row[0]  # Mengambil nilai kolom "Paper_Level"
                word_47 = f"{word_47}\n{paper_level}"
            self.ids.hasil47.text = word_47

            db.commit()

        except:
            print ("Error! Unable to fetch data" )  
        
        return

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("imsql_gui.kv")
    
class MyMainApp(App):
    title = "IMSql"
    def build(self):
        return kv
    
if __name__ == '__main__':
    MyMainApp().run()