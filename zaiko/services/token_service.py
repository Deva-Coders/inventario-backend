from services.user_service import authenticate_user
from jose import JWTError, jwt
from datetime import datetime, timedelta
from decouple import config
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


SECRET_KEY = config("SECRET_KEY")
ALGORITHM = config("ALGORITHM")

def verify_token(token):
    logger.error(f"Token: {token}")
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            return False
    except JWTError as jwte:
        logger.error(f"JWTError: {jwte}")
        return False
    """
    return {"valido": True} 

async def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

#async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
async def login_for_access_token(username: str, password: str):
    logger.error(f"Valida: {username} - {password}")
    user = await authenticate_user(username, password)
    if user:
        access_token_expires = timedelta(minutes=int(config("ACCESS_TOKEN_EXPIRE_MINUTES")))
        access_token = await create_access_token(
            data={"sub": user.fullName}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}    
    return {"error": "Incorrect username or password"}
