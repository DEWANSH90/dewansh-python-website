from sqlalchemy import create_engine, text
import os

dbconnstring = os.environ['DB_CONN_STRING']

engine = create_engine(dbconnstring,
  connect_args={
    "ssl":{
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })



  


 


    

  
