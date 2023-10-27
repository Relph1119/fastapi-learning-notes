from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBasicCredentials
from models.data.sqlalchemy_models import Auctions
from sqlalchemy.orm import Session

from db_config.sqlalchemy_connect import sess_db
from models.request.auctions import AuctionsReq
from repository.auctions import AuctionsRepository
from security.secure import http_basic

router = APIRouter()


@router.post("/auctions/add")
def add_auction(req: AuctionsReq, credentials: HTTPBasicCredentials = Depends(http_basic),
                sess: Session = Depends(sess_db)):
    auc_dict = req.dict(exclude_unset=True)
    repo: AuctionsRepository = AuctionsRepository(sess)
    auction = Auctions(**auc_dict)
    result = repo.insert_auction(auction)
    if result == True:
        return auction
    else:
        return JSONResponse(content={'message': 'create auction problem encountered'}, status_code=500)


@router.patch("/auctions/update")
def update_auction(id: int, req: AuctionsReq, credentials: HTTPBasicCredentials = Depends(http_basic),
                   sess: Session = Depends(sess_db)):
    auc_dict = req.dict(exclude_unset=True)
    repo: AuctionsRepository = AuctionsRepository(sess)
    result = repo.update_auction(id, auc_dict)
    if result:
        return JSONResponse(content={'message': 'auction updated successfully'}, status_code=201)
    else:
        return JSONResponse(content={'message': 'update auction error'}, status_code=500)


@router.delete("/auctions/delete/{id}")
def delete_auction(id: int, credentials: HTTPBasicCredentials = Depends(http_basic), sess: Session = Depends(sess_db)):
    repo: AuctionsRepository = AuctionsRepository(sess)
    result = repo.delete_auction(id)
    if result:
        return JSONResponse(content={'message': 'auction updated successfully'}, status_code=201)
    else:
        return JSONResponse(content={'message': 'update auction error'}, status_code=500)


@router.get("/auctions/list")
def list_all_auction(credentials: HTTPBasicCredentials = Depends(http_basic), sess: Session = Depends(sess_db)):
    repo: AuctionsRepository = AuctionsRepository(sess)
    result = repo.get_all_auctions()
    return result


@router.get("/auctions/{id}")
def get_auction(id: int, credentials: HTTPBasicCredentials = Depends(http_basic), sess: Session = Depends(sess_db)):
    repo: AuctionsRepository = AuctionsRepository(sess)
    result = repo.get_auction(id)
    return result
