from app import create_app, db
from app.models.tasks import Task

def init_database():
    app = create_app()
    with app.app_context():
        # Create all tables
        db.create_all()
        print("Database tables created.")

        # Check if there are any tasks
        if Task.query.first() is None:
            # Add a sample task if the table is empty
            sample_task = Task(title="Sample Task", description="This is a sample task.")
            db.session.add(sample_task)
            db.session.commit()
            print("Sample task added.")
        else:
            print("Tasks table already contains data.")

if __name__ == "__main__":
    init_database()
