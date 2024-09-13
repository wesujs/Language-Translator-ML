from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas
from app.database import get_db
from app.services.translator import translate_text
from app.routers.auth import oauth2_scheme

router = APIRouter()

@router.post("/translate/", response_model=schemas.TranslationResponse)
async def translate(
    translation: schemas.TranslationRequest,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    try:
        result = await translate_text(translation.text, translation.target_language)
        return schemas.TranslationResponse(
            original_text=translation.text,
            translated_text=result['text'],
            source_language=result['src'],
            target_language=translation.target_language
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))