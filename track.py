from flask import *
import sqlite3

app = Flask(__name__)
DATABASE = 'crud.db'


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/viewsinglerecord", methods=['GET', 'POST'])
def readSqliteTable():
    name = str(request.form['name'])
    try:
     con = sqlite3.connect(DATABASE)
     #con.row_factory = sqlite3.Row
     cur = con.cursor()
     sql = 'SELECT GRADE FROM student_percent WHERE NAME = ?'
     cur.execute(sql,(name,))
     rows = cur.fetchone()
     print(rows)
    except:
      rows = 'Not available'
    finally:
      return render_template("viewsinglerecord.html", rows=rows)
      con.close()

if __name__ == "__main__":
   app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   
#name = request.form["name"]
#sqliteConnection = sqlite3.connect('Student_Score.db')
#cursor = sqliteConnection.cursor()
#sql_select_query = """select Grade from STUDENT_RESULT where Name = ?"""
#cursor.execute(sql_select_query, (name,))
#records = cursor.fetchone()
#sqliteConnection.commit()
#msg = "Successfully selected"
#return render_template("viewsinglerecord.html")
#return render_template("viewsinglerecord.html",records = 'Result is : {}'.format(rows))


