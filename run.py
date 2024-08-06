from app import db, create_app
from app.models import Element  # Import Element model

app = create_app()

if __name__ == '__main__':
    print("Creating database ...")
    with app.app_context():
        # Create the database tables if they don't exist
        db.create_all()
        
        # Add values to the database - developtment
        print("Adding values to the database...")

        # add elements here

        # for element_name in elements:
        #     element = Element.query.filter_by(name=element_name).first()
        #     if not element:
        #         element = Element(name=element_name)
        #         db.session.add(element)
    
        db.session.commit()
        print("Categories populated successfully.")
                
    print("Database tables created successfully!")
    app.run(debug=True)
