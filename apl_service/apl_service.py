from flask import Flask,request,jsonify
from flask_cors import CORS
import psycopg2i, os 

app=Flask(_name_)
CORS(app)

DATABASE_URL=os.getenv(
  "DATABASE_URL",
  ""

def connect_db():
  return psycopg2.connect( "postgresql://bulut_proje_user:NwqSCQV8KCfKJmvghYiTAIHp7Xba2Fk6@dpg-d6ttgqshg0os7381hnpg-a.oregon-postgres.render.com/bulut_proje")

@app.route("/ziyaretciler",methods=["GET","POST"])
def ziyaretciler():
  conn=connect_db()
  cur=conn.cursor()
  cur.execute("CREATE TABLE IF NOT EXISTS ziyaretciler (id SERIAL PRIMARY KEY,isim TEXT)")

if request.method =="POST":
    isim=request.json.get("isim")
    if isim:
      cur.execute("INSERT INTO ziyaretciler (isim) VALUES (%s)",(isim,))
      conn.commit()
    cur.execute("SELECT isim FROM ziyaretciler ORDER BY id DESC LIMIT 10")
    isimler=[row[0] for now in cur.fetchall()]

    cur.close()
    conn.close()

    return jsonify(isimler)
if_name_=="__main__":
  app.run(host="0.0.0.0",port=5001)




      
          
 
