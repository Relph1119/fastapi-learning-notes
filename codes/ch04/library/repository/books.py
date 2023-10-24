from typing import Dict, Any

from fastapi.encoders import jsonable_encoder
from models.data.library import Book
from models.data.librarydb import book_tbl


class BookRepository:

    def insert_book(self, book: Book) -> bool:
        try:
            book_tbl[book.book_id] = book
        except:
            return False
        return True

    def update_book(self, book_id: int, details: Dict[str, Any]) -> bool:
        try:
            profile = book_tbl[book_id]
            profile_enc = jsonable_encoder(profile)
            profile_dict = dict(profile_enc)
            profile_dict.update(details)
            book_tbl[book_id] = Book(**profile_dict)
        except:
            return False
        return True

    def delete_book(self, book_id: int) -> bool:
        try:
            del book_tbl[book_id]
        except:
            return False
        return True

    def get_all_books(self):
        return book_tbl
