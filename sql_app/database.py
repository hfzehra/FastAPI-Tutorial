from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import cloudinary

cloudinary.config(
    cloud_name= "dmlq1kfql",
    api_key= "445535963212455",
    api_secret ="UMU88hYO8lKL5pCql0eyHdXI1fQ"
)

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgres://cstnlvpsuqscqi:2013bbbd36b5c9589995bf143219b078eae6303e543d9ed83b3b35e29fc06070@ec2-34-239-196-254.compute-1.amazonaws.com:5432/d5tgjt35a4ggbe"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
