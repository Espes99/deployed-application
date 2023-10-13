import mysql.connector
from flask import Flask, jsonify, render_template, request, redirect, url_for

app = Flask(__name__)

def create_db_connection():
    return mysql.connector.connect(
        user="root",
        password="root",
        host="mysql",
        port="3306",
        database="db"
    )

@app.route('/')
def view_data():
    connection = create_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT blogpost FROM blog_db")
    results = cursor.fetchall()

    cursor.close()
    connection.close()
    print("results", results)
    return render_template('view_data.html', data=results)

@app.route('/add_data', methods=['GET', 'POST'])
def add_data():
    if request.method == 'POST':
        try:
            data = request.form.get('blogpost')
            if data:
                connection = create_db_connection()
                cursor = connection.cursor()

                query = "INSERT INTO blog_db (blogpost) VALUES (%s)"
                cursor.execute(query, (data,))
                connection.commit()

                cursor.close()
                connection.close()

                return redirect(url_for('view_data'))
            else:
                return "No data provided for insertion."
        except Exception as e:
            return "Error: " + str(e)
    else:
        return render_template('post_data.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
