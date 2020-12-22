from flask import Flask,render_template,request,redirect
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    mydb = psycopg2.connect(
    host="localhost",
    port=55001,
    database="postgres",
    user="postgres",
    password="Dfuv8fe1")

    # create a cursor
    mycursor = mydb.cursor()
        

    if request.method == 'POST':
        data = request.form.to_dict()

        sql = "INSERT INTO form (email, subject, message) VALUES (%s, %s, %s)"
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')

    	# execute a statement
        val = (email,subject,message)
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")

	    # close the communication with the PostgreSQL
        mycursor.close()
        return redirect('thankyou.html')
    else:
        return 'some went wrong'    
