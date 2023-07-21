import sqlite3
def sqlite(username,isim,soyisim):
    with sqlite3.connect('User.db') as vt:
        im = vt.cursor()
        veriler = [(username,isim,soyisim)]

        im.execute("""CREATE TABLE IF NOT EXISTS Users
            (kullanıcı adı,isim, soyisim)""")

        for veri in veriler:
            im.execute("""INSERT INTO Users VALUES
                (? ,?, ?)""", veri)

        vt.commit()