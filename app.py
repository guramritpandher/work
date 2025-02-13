from flask import Flask, render_template, request, redirect, url_for, flash, session 
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app=Flask(__name__)


# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Database file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Required for flash messages


# Initialize the database
db = SQLAlchemy(app)


# Define the User model (table structure)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


# Create the database and table
with app.app_context():
    db.create_all()


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        # Create a new user instance
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')


        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)  # Add user to the session
        db.session.commit()  # Save to database

        flash('Registration successful!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Find user by email
        user = User.query.filter_by(email=email).first()

        # Verify password
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id  # Store user ID in session
            return redirect(url_for('hello'))  # Redirect to dashboard
        else:
            flash('Invalid email or password.', 'danger')

    return render_template('login.html')


@app.route('/hello')
def hello():
    if 'user_id' not in session:
        flash('Please log in first.', 'warning')
        return redirect(url_for('login'))
    
    return "Hello, World!"



if __name__ == '__main__':
    app.run(debug=True)