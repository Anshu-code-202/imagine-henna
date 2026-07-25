from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url="postgresql://postgres:12345@localhost:5432/postgres"
engine=create_engine(db_url)

# Bind the engine here:this configuration parameters inside sessionmaker() are required to define how your Python code talks to the database and to prevent accidental data bugs.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

"""1. bind=engine (Connecting to the Database)What it does:
 It links your session factory to your specific PostgreSQL database.Why it is required: sessionmaker is just a factory blueprint. 
 Without bind=engine, the sessions it creates won't know where to send your SQL queries or which connection credentials to use.
 2. autocommit=False (Transaction Control)What it does: It forces you to manually type db.commit() to save changes.Why it is required: 
 If set to True, every single database modification would instantly save to PostgreSQL. If you are updating 5 different things in a row and the 4th one crashes,
   your database is left corrupted with half-finished data. autocommit=False ensures your operations follow database ACID principles—everything succeeds together,
     or nothing changes at all.3. autoflush=False (Performance & State Control)What it does: It stops SQLAlchemy from automatically sending data changes to the database before every query you write.
     Why it is required: Automatic flushing can trigger unnecessary database communication and slow down your application. Disabling it gives you precise control over exactly when your Python changes are pushed to PostgreSQL
     , preventing weird bugs where objects are modified before you are ready.Summary of the WorkflowBy setting these options, SessionLocal acts as a factory that churns out predictable, safe, and connected session object
     
     
     
     
     The parameters (autocommit=False, autoflush=False, bind=engine) perform the exact same job for MySQL as they did for PostgreSQL. 
     SQLAlchemy acts as an abstraction layer. Once the connection string points to MySQL, SQLAlchemy automatically translates your session commands into MySQL-compliant SQL, 
     preserving your transaction safety controls without changing your core application logic."""