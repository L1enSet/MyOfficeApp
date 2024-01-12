import sqlite3


def create_db():
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute(create_table_calls())
    cur.execute(create_table_roles())
    cur.execute(create_table_answers())
    con.commit()
    print("created!!")


def create_table_calls():
    request_text = """CREATE TABLE IF NOT EXISTS calls (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user VARCHAR(50),
        trouble TEXT,
        organization VARCHAR(100),
        phone VARCHAR(20),
        date VARCHAR(50)
    )"""

    return request_text


def create_table_roles():
    request_text = """CREATE TABLE IF NOT EXISTS roles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        role VARCHAR(50),
        category VARCHAR(20)
    )"""

    return request_text


def create_table_answers():
    request_text = """CREATE TABLE IF NOT EXISTS answers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHER(50),
        answer TEXT,
        category VARCHAR(20)
    )"""

    return request_text
    

class DriveDB():

    def __init__(self, db):
        self.db = db
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
    
    def sql_request(self, request_text):
        print(request_text)
        query_set = self.cur.execute(request_text)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
        return query_set
    
    def add_call(self, call_data):
        self.cur.execute("INSERT INTO calls ('user', 'trouble', 'organization', 'phone', 'date') VALUES(?, ?, ?, ?, ?)", call_data)
        self.con.commit()
        print("succes!!")

    def add_role(self, role_data):
        self.cur.execute("INSERT INTO roles ('role', 'category') VALUES(?, ?)", role_data)
        self.con.commit()
        print("succes!!")
    
    def add_answer(self, answer_data):
        self.cur.execute("INSERT INTO answers ('title', 'answer', 'category') VALUES(?, ?, ?)", answer_data)
        self.con.commit()
        print("succes!!")
    
    def delete_element(self, element):
        query = "DELETE from {} where id = {}".format(element[0], element[1])
        self.cur.execute(query)
        self.con.commit()
 
        
#create_db()

#base = DriveDB("database.db")
#base.add_call(call_data=("anton1", "ufhd1", "cbu1", "89526555098", "now"))
#base.add_role(role_data=('administarator spo', 'SPO'))
#base.add_answer(answer_data=('about trouble', 'please tell me abaut your problem3', 'school'))
#base.delete_element(element=('answers', '2'))
#base.sql_request()