#!flask/bin/python
from flask import Flask, jsonify
from flask import make_response
from flask import request
from flask_cors import CORS
import pyodbc
import sentimentAnalysist
con = pyodbc.connect("DRIVER={SQL Server};server=localhost;database=bilvideo")
cursor = con.cursor()
cursor1 = con.cursor()
cursor2 = con.cursor()
cursor3 = con.cursor()
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

def getcommentsofvideo(videoNo):
    cursor.execute("select * from Comment where videoNo = (?)", videoNo)
    rows = [x for x in cursor]
    return rows

def insertvideo(a,b,c,d,e,f,g,h,i,j,k,l,m,n):
    cursor.execute("insert into Video values (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (a, b, c, d, e, f, g, h, i, j, k, l, m, n))
    con.commit()

def getvideo(videoNo):
    cursor.execute("select * from Video where videoNo = (?)", videoNo)
    rows = [x for x in cursor]
    return rows

def getlastvideo():
    cursor.execute("select * from Video order by videoNo desc")
    rows = [x for x in cursor]
    row = rows[0]
    return row[0]

def getcomment(commentId):
    cursor.execute("select * from Comment where commentId = (?)", commentId)
    rows = [x for x in cursor]
    return  rows

def insertcomment(a,b,c,d,e,f,g,h):
    cursor.execute("insert into Comment values (?,?,?,?,?,?,?,?)", (a, b, c, d, e, f, g, h))
    con.commit()

def getcomments():
    cursor.execute("select * from Comment order by commentId desc")
    rows = [x for x in cursor]
    return  rows

def commentsentiment():
    cursor.execute("select * from Comment order by commentId desc")
    rows = [x for x in cursor]
    row = rows[0]
    from sentimentAnalysist import duygu_analizi
    sonucdgr = duygu_analizi().classification(row[3])
    if sonucdgr == [0]:
        #sonuc = 'olumsuz'
        updatecomment(row[0], bool(0))
    elif sonucdgr == [1]:
        #sonuc = 'olumlu'
        updatecomment(row[0], bool(1))
    #else:
        #sonuc = 'nötür'
    updatevideo(row[1])

def updatecomment(commentId,sentiment):
    #cursor.execute("update Comment set sentiment = (?) where commentId =  (?)", (sentiment, commentId))
    rows = getcomment(commentId)
    cursor.execute("delete from Comment where commentId =  (?)", commentId)
    con.commit()
    for row in rows:
        insertcomment(row[1], row[2], row[3], row[4], row[5], sentiment, row[7], row[8])
    # comment = cursor.fetchall()
    # return comment

def getvideorate(videoNo):
    cursor.execute("select sentiment from Comment where videoNo = (?)", videoNo)
    rows = [x for x in cursor]
    olumsuz = 0
    olumlu = 0
    for row in rows:
        if row[0]:
            olumlu = olumlu + 1
        elif not row[0]:
            olumsuz = olumsuz + 1
    rate = olumlu / (olumlu + olumsuz)
    return rate

def updatevideo(videoNo):
    rate = getvideorate(videoNo)
    videos = getvideo(videoNo)
    rows = getcommentsofvideo(videoNo)
    cursor.execute("delete from Video where videoNo =  (?)", videoNo)
    con.commit()
    for video in videos:
        insertvideo(video[1], video[2], video[3], video[4], video[5], video[6], video[7], rate, video[9], video[10], video[11], video[12], video[13], video[14])
        LastvideoNo = getlastvideo()
    for row in rows:
        insertcomment(LastvideoNo, row[2], row[3], row[4], row[5], row[6], row[7], row[8])

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


@app.route('/api/getcomments', methods=['GET'])
def get_comment():
    commentsentiment()
    videoNo = getlastvideo()
    return jsonify(videoNo)

@app.errorhandler(404)
def not_found(error):
    return make_response(
        jsonify({'HTTP 404 Error': 'The content you looks for does not exist. Please check your request.'}), 404)


if __name__ == '__main__':
    app.run(debug=True)  # !flask/bin/python
con.close()