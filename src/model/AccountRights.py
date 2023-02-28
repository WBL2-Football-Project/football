from enum import Enum

class AccountRights(Enum):
    """Enum defining the types of account rights"""
    NotLoggedIn='Not Logged In'
    UserRights='User Rights'
    RefereeRights='Referee Rights'
