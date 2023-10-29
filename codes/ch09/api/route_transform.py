from typing import Optional

from fastapi import APIRouter, Depends, File, UploadFile

from util.auth_session import get_current_user
from util.custom_routes import FileStreamRoute

router = APIRouter()
router.route_class = FileStreamRoute


@router.post("/files/")
async def create_file(file: Optional[bytes] = File(...), user: str = Depends(get_current_user)):
    return {"file_size": len(file)}


@router.post("/files/upload")
async def create_file_2(file: Optional[UploadFile] = File(...), user: str = Depends(get_current_user)):
    print(file.content_type)
    fs = await file.read()
    return {"file_size": len(fs)}
