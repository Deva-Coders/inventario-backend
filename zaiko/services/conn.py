
@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user(user_id: int):
    with get_db() as db:
        return db.query(User).filter(User.id == user_id).first()

