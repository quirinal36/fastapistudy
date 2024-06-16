from app.database import engine, Base
from app.models import User

# 데이터베이스 및 테이블 생성
Base.metadata.create_all(bind=engine)
