from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from models.data.sqlalchemy_models import Profile
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from db_config.sqlalchemy_connect import sess_db
from models.request.profile import ProfileReq
from repository.profile import ProfileRepository
from security.secure import authenticate

router = APIRouter()

crypt_context = CryptContext(schemes=["sha256_crypt", "md5_crypt"])
SECRET_KEY = "565f2855e4cea6b54714347ed73d1b3ba57ed696428867d4cbf89d575a3c7c4c"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


@router.post("/profile/add", dependencies=[Depends(authenticate)])
def add_profile(req: ProfileReq, sess: Session = Depends(sess_db)):
    profile_dict = req.dict(exclude_unset=True)
    repo: ProfileRepository = ProfileRepository(sess)
    profile = Profile(**profile_dict)
    result = repo.insert_profile(profile)
    if result == True:
        return profile
    else:
        return JSONResponse(content={'message': 'create profile problem encountered'}, status_code=500)


@router.patch("/profile/update", dependencies=[Depends(authenticate)])
def update_profile(id: int, req: ProfileReq, sess: Session = Depends(sess_db)):
    profile_dict = req.dict(exclude_unset=True)
    repo: ProfileRepository = ProfileRepository(sess)
    result = repo.update_profile(id, profile_dict)
    if result:
        return JSONResponse(content={'message': 'profile updated successfully'}, status_code=201)
    else:
        return JSONResponse(content={'message': 'update profile error'}, status_code=500)


@router.delete("/profile/delete/{id}", dependencies=[Depends(authenticate)])
def delete_profile(id: int, sess: Session = Depends(sess_db)):
    repo: ProfileRepository = ProfileRepository(sess)
    result = repo.delete_profile(id)
    if result:
        return JSONResponse(content={'message': 'signup updated successfully'}, status_code=201)
    else:
        return JSONResponse(content={'message': 'update signup error'}, status_code=500)


@router.get("/profile/list", dependencies=[Depends(authenticate)])
def list_all_profile(sess: Session = Depends(sess_db)):
    repo: ProfileRepository = ProfileRepository(sess)
    result = repo.get_all_profile()
    return result


@router.get("/profile/{id}", dependencies=[Depends(authenticate)])
def get_profile(id: int, sess: Session = Depends(sess_db)):
    repo: ProfileRepository = ProfileRepository(sess)
    result = repo.get_profile(id)
    return result
