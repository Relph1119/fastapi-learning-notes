from models.data.students import Login
from models.data.studentsdb import stud_login_tbl


class StudentLoginRepository:

    def insert_login(self, login: Login) -> bool:
        try:
            stud_login_tbl[login.user_id] = login
        except:
            return False
        return True

    def update_password(self, user_id: int, newpass: str) -> bool:
        try:
            login = stud_login_tbl[user_id]
            login.password = newpass
        except:
            return False
        return True

    def delete_login(self, user_id: int) -> bool:
        try:
            del stud_login_tbl[user_id]
        except:
            return False
        return True

    def get_login(self, username: str):
        list_login = [account for account in stud_login_tbl.values() if account.username == username]
        if not len(list_login) == 0:
            return list_login[0]
        else:
            return None

    def get_all_login(self):
        return stud_login_tbl
