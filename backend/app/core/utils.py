import uuid
from datetime import datetime, timezone
from typing import Dict, Optional

from itsdangerous import URLSafeTimedSerializer
from sendgrid import HtmlContent, Mail, SendGridAPIClient

from . import config


def random_hash() -> str:
    return str(uuid.uuid4().hex)


def get_current_time() -> datetime:
    return datetime.now(timezone.utc)


def get_domain_from_email(email: str) -> str:
    return email.split("@")[1]


def generate_new_account_token(email: str, username: str) -> str:
    serializer = URLSafeTimedSerializer(config.SECRET_KEY)
    data = {"user_email": email, "username": username}
    return serializer.dumps(data, salt=config.SECRET_SALT)


def verify_new_account_token(token: str) -> Optional[Dict[str, str]]:
    try:
        serializer = URLSafeTimedSerializer(config.SECRET_KEY)
        return serializer.loads(
            token,
            salt=config.SECRET_SALT,
            max_age=config.EMAIL_RESET_TOKEN_EXPIRE_HOURS * 60 * 60,
        )
    except Exception as e:
        print(e)
        return None


def send_email(
    email_to: str,
    subject_template: str = "",
    html_template: str = "",
) -> bool:
    message = Mail(
        from_email=config.EMAIL_FROM,
        to_emails=[email_to],
        subject=subject_template,
        html_content=HtmlContent(html_template),
    )
    try:
        sg = SendGridAPIClient(config.SENDGRID_APIKEY)
        sg.send(message)
        return True
    except Exception as e:
        print(e)
        return False


def send_new_account_email(
    email_to: str, token: str, username: str, server_host: str
) -> bool:
    project_name = "VaultSafe"
    subject = f"Welcome to {project_name}, {username}"
    link = f"{server_host}/new-account/{token}"
    print(link)
    message = f"""
    <html>
        <body>
            Hi {username}, \nWelcome to {project_name}. Click on the following link to complete your registration. \n\n{link}
            - VaultSafe Team
        </body>
    </html>
    """
    return send_email(
        email_to=email_to,
        subject_template=subject,
        html_template=message,
    )
