from typing import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader, OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app import crud
from app.core import config, security
from app.database.session import SessionLocal
from app.models import User
from app.schemas.token import TokenPayload

HEADER_KEY = APIKeyHeader(name="X-API-KEY")
reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="/api/v1/user/login/access-token/")


#
#
# def check_api_key(api_key: str = Depends(HEADER_KEY)):
#     if api_key != config.API_KEY:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED, detail="X-API-KEY header invalid"
#         )
#     return True
#
#
def get_db() -> Generator[Session, None, None]:
    """
    Get a database connection
    """
    try:
        db: Session = SessionLocal()
        yield db
    finally:
        db.close()


def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
) -> User:
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[security.ALGORITHM])
        token_data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError) as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        ) from e
    user = crud.crud_user.get_by_email(db=db, email=token_data.user_email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return user


#
#
# def get_current_active_user(
#     current_user: models.Customers = Depends(get_current_user),
# ) -> models.Customers:
#     if not crud.customer.is_active(current_user):
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN, detail="Inactive user"
#         )
#     return current_user
#
#
# def get_current_user_permission(
#     db: Session = Depends(get_db),
#     current_user: models.Customers = Depends(get_current_active_user),
# ) -> Roles:
#     return Roles(
#         crud.roles.get(
#             db,
#             id=current_user.role_id,
#         ).username
#     )
#
#
# def get_admin_user(
#     current_user: models.Customers = Depends(get_current_active_user),
#     role: Roles = Depends(get_current_user_permission),
# ) -> models.Customers:
#     if Roles.ORGADMIN not in role.permission():
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Only ADMIN can access this service.",
#         )
#     return current_user
#
#
# def get_tmadmin_user(
#     current_user: models.Customers = Depends(get_current_active_user),
#     role: Roles = Depends(get_current_user_permission),
# ) -> models.Customers:
#     if Roles.TMADMIN not in role.permission():
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Only TMADMIN can access this service.",
#         )
#     return current_user
#
#
# def get_all_workflows(
#     db: Session = Depends(get_db),
#     is_allowed: bool = Depends(check_api_key),
#     current_user: models.Customers = Depends(get_current_active_user),
#     role: Roles = Depends(get_current_user_permission),
# ) -> List[models.Workflows]:
#     """
#     Get the current tasks from the database
#     """
#
#     if Roles.ORGADMIN not in role.permission():
#         return [
#             mapping.workflow
#             for mapping in crud.pending_workflows.get_multi_by_customer_id(
#                 db, customer_id=current_user.id
#             )
#         ]
#     if Roles.TMADMIN in role.permission():
#         return crud.workflow.get_multi(db, skip=0, limit=100)
#     return [
#         mapping.workflow
#         for mapping in crud.available_workflows.get_multi_by_tenant_id(
#             db, tenant_id=current_user.tenant_id
#         )
#     ]
#
#
# def get_pending_workflows(
#     db: Session = Depends(get_db),
#     is_allowed: bool = Depends(check_api_key),
#     current_user: models.Customers = Depends(get_current_active_user),
# ) -> List[models.Workflows]:
#     """
#     Get the current tasks from the database
#     """
#     return [
#         mapping.workflow
#         for mapping in crud.pending_workflows.get_pending_workflows_by_customer_id(
#             db, customer_id=current_user.id
#         )
#     ]
#
#
# def get_current_step(
#     db: Session = Depends(get_db),
#     step_id: str = "",
#     is_allowed: bool = Depends(check_api_key),
# ) -> models.Workflow_Steps:
#     """
#     Get the current tasks from the database
#     """
#     steps = crud.step.get(db, id=step_id)
#     if not steps:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="step not found",
#         )
#     return steps
