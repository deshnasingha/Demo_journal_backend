from backend.main import app
from fastapi import APIRouter, Depends, JSONResponse
from sqlalchemy.orm import Session
from backend.db.enginedb import get_db
from backend.db.tables.journal import Journal

router = APIRouter()

@router.get("/")
def all_journal_entries(db: Session = Depends(get_db)):
    try:
        entries = db.query(Journal).all()
        return JSONResponse(status_code=200, content={"journal_entries": [entry.__dict__ for entry in entries]})
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": "Error retrieving journal entries", "error": str(e)})

@router.post("/add")
def add_journal_entry(entry_data: dict, db: Session = Depends(get_db)):
    try:
        new_entry = Journal(**entry_data)
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
        return JSONResponse(status_code=201, content={"message": "Journal entry added successfully", "entry": new_entry.__dict__})
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"message": "Error adding journal entry", "error": str(e)})
    
@router.delete("/delete/{entry_id}")
def delete_journal_entry(entry_id: int, db: Session = Depends(get_db)):
    try:
        entry = db.query(Journal).filter(Journal.id == entry_id).first()
        if entry:
            db.delete(entry)
            db.commit()
            return JSONResponse(status_code=200, content={"message": "Journal entry deleted successfully"})
        else:
            return JSONResponse(status_code=404, content={"message": "Journal entry not found"})
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"message": "Error deleting journal entry", "error": str(e)})
    
@router.get("/{entry_id}")
def get_journal_entry(entry_id: int, db: Session = Depends(get_db)):
    try:
        entry = db.query(Journal).filter(Journal.id == entry_id).first()
        if entry:
            return JSONResponse(status_code=200, content={"entry": entry.__dict__})
        else:
            return JSONResponse(status_code=404, content={"message": "Journal entry not found"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": "Error retrieving journal entry", "error": str(e)})

@router.get("/by_date")
def get_journal_entries_by_date(date: str, db: Session = Depends(get_db)):
    try:
        entries = db.query(Journal).filter(Journal.date == date).all()
        return JSONResponse(status_code=200, content={"journal_entries": [entry.__dict__ for entry in entries]})
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": "Error retrieving journal entries by date", "error": str(e)})