from mealchooser import app
from mealchooser import db
from mealchooser.models import User

if __name__ == "__main__":
    app.run(debug=True)
    db.create_all()
    
    

    