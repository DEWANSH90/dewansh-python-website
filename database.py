from sqlalchemy import create_engine, text
dbconnstring = "mysql+pymysql://hy1wbbcjzkfycfbcu3c4:pscale_pw_93ct91MMqvKppGghdlXcdtO4Gli95F7t4FSlIJtxXis@aws.connect.psdb.cloud/dewanshjobs?charset=utf8mb4"

engine = create_engine(dbconnstring,
  connect_args={
    "ssl":{
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })

with  engine.connect() as conn:
  result= conn.execute(text("select * from jobs"))

  result_all = result.all()
  for row in result.all():
    firstdictresult[] = (result_all[row])

  print(firstdictresult)

    

  
