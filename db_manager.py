import sqlite3

def add_pass(username, passw, mail, url, site):
    con = sqlite3.connect('pass.db')
    con.row_factory = sqlite3.Row
    vals = [username, passw, mail, url, site]
    con.execute("insert into pass values(?,?,?,?,?)", vals)
    con.commit()
    con.close()

def find_by_site(site):
    con = sqlite3.connect('pass.db')
    con.row_factory = sqlite3.Row
    rs = (con.execute("SELECT * from pass where site=?", [site])).fetchall()
    res = [list(x) for x in rs]
    con.close()
    return res

def find_by_mail(mail):
    con = sqlite3.connect('pass.db')
    con.row_factory = sqlite3.Row
    rs = (con.execute("SELECT username, mail, password, site from pass where mail=?", [mail])).fetchall()
    res = [list(x) for x in rs]
    con.close()
    return res
