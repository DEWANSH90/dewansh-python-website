from flask import Flask , render_template

app = Flask(__name__)

jobs1 = [
  {
  'id': 1 ,
  'role':'DataEngineer',
  'location':'Bengaluru,india'
  },
  {
  'id': 2 ,
  'role':'DataScientist',
  'location':'Pune,india'
    
  },
  {
  'id': 3 ,
  'role':'DataAnalyst',
  'location':'NewDelhi,india'
  },
  {
  'id': 4 ,
  'role':'DataRecriter',
  'location':'Hyderabad,india'
  }
]
@app.route("/")
def helloworld():
   return render_template('home.html', jobs=jobs1)

if __name__ == "__main__" :
  app.run(host='0.0.0.0' , debug=True)
        