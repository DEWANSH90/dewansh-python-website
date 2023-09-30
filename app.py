from flask import Flask , render_template
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



@app.route("/")
def helloworld():
    jobs1 = load_job_from_db()
    return render_template('home.html', jobs=jobs1)

if __name__ == "__main__" :
  app.run(host='0.0.0.0' , debug=True)
        