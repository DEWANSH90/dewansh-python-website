from flask import Flask , render_template, request
from flask.json import jsonify
from database import engine
from sqlalchemy import text

app = Flask(__name__)

def load_job_from_db():
  with  engine.connect() as conn:
    result= conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._mapping)
    return jobs

def load_eachjob_from_db(id):
  with  engine.connect() as conn:
  
    result = conn.execute(text("select * from jobs where id = :val"), {'val':id})
    rows = result.all()
      
    if (len(rows)==0):
      return None
    else:
     return rows[0]._mapping


@app.route("/")
def helloworld():
    jobs1 = load_job_from_db()
    return render_template('home.html', jobs=jobs1)

@app.route("/jobs/<id>")
def showjob(id):
  job = load_eachjob_from_db(id)
  return render_template('jobdetails.html', jobs=job)


@app.route("/jobs/<id>/apply", methods = ['post'])
def formdata(id):
  data = request.form
  
  return render_template('applicationsubmitted.html', app=data)
  
  

if __name__ == "__main__" :
  app.run(host='0.0.0.0' , debug=True)
        