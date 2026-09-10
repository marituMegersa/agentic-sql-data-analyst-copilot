from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.sql_data_analyst_copilot.schemas import AgenticSqlDataAnalystCopilotSessionCreate, AgenticSqlDataAnalystCopilotSessionResponse
from app.domain.sql_data_analyst_copilot.service import AgenticSqlDataAnalystCopilotService

router = APIRouter(prefix="/api/v1/sql_data_analyst_copilot", tags=["Agentic Sql Data Analyst Copilot Domain"])

@router.post("/sessions", response_model=AgenticSqlDataAnalystCopilotSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticSqlDataAnalystCopilotSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Sql Data Analyst Copilot.
    """
    return AgenticSqlDataAnalystCopilotService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticSqlDataAnalystCopilotSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticSqlDataAnalystCopilotService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
