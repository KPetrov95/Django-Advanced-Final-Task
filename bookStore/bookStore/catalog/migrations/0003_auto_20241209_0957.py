# Generated by Django 5.1.2 on 2024-12-09 07:57

from django.db import migrations,   models
import datetime


def populate_data(apps, schema_editor):
    Author = apps.get_model('catalog', 'Author')
    Genre = apps.get_model('catalog', 'Genre')
    Book = apps.get_model('catalog', 'Book')

    # Genres
    genres = [
        "Fiction", "Science Fiction", "Fantasy", "Mystery", "Romance",
        "Horror", "Historical Fiction", "Biography", "Self-Help", "Philosophy"
    ]

    genre_objects = []
    for name in genres:
        genre_objects.append(Genre(name=name, description=f"Books related to {name}."))

    Genre.objects.bulk_create(genre_objects)

    genre_map = {genre.name: genre for genre in Genre.objects.all()}
    # Authors and Books
    authors_and_books = [
        {
            "first_name": "Jane", "last_name": "Austen",
            "photo": "https://res.cloudinary.com/drbktnxop/image/upload/v1733732069/jane_austen_gwrpz7.jpg",
            "biography": "English novelist.", "birth_date": datetime.date(1775, 12, 16),
            "books": [
                {"title": "Pride and Prejudice", "description": "A romantic novel.", "isbn": "9781234567890",
                 "price": 15.99, "genre": "Romance",
                 "cover": "https://res.cloudinary.com/drbktnxop/image/upload/v1733733018/pride_and_prejudice_wyilou.jpg"},
                {"title": "Sense and Sensibility", "description": "A story of two sisters.", "isbn": "9782345678901",
                 "price": 14.99, "genre": "Romance",
                 "cover": "https://res.cloudinary.com/drbktnxop/image/upload/v1733733014/815jwDpyguL._AC_UF1000_1000_QL80__pazxnt.jpg"},
            ]
        },
        {
            "first_name": "Mark", "last_name": "Twain",
            "photo": "https://res.cloudinary.com/drbktnxop/image/upload/v1733732069/Mark-Twain_hxppyn.webp",
            "biography": "American writer.", "birth_date": datetime.date(1835, 11, 30),
            "books": [
                {"title": "The Adventures of Tom Sawyer", "description": "A classic adventure novel.",
                 "isbn": "9783456789012", "price": 12.99, "genre": "Fiction",
                 "cover": "https://res.cloudinary.com/drbktnxop/image/upload/v1733733020/The_Adventures_of_Tom_Sawyer_z5qkbs.jpg"},
                {"title": "Adventures of Huckleberry Finn", "description": "Sequel to Tom Sawyer.",
                 "isbn": "9784567890123", "price": 13.99, "genre": "Fiction",
                 "cover": "https://res.cloudinary.com/drbktnxop/image/upload/v1733733019/The_Adventures_of_Huckleberry_Finn_f4hpdq.jpg"},
            ]
        },
        {
            "first_name": "George", "last_name": "Orwell",
            "photo": "https://res.cloudinary.com/drbktnxop/image/upload/v1733732068/George_Orwell_press_photo_peotgs.jpg",
            "biography": "English novelist.", "birth_date": datetime.date(1903, 6, 25),
            "books": [
                {"title": "1984", "description": "Dystopian social science fiction novel.", "isbn": "9785678901234",
                 "price": 16.99, "genre": "Science Fiction",
                 "cover": "https://res.cloudinary.com/drbktnxop/image/upload/v1733733015/1984_sx9gil.jpg"},
                {"title": "Animal Farm", "description": "Allegorical novella.", "isbn": "9786789012345", "price": 10.99, "genre": "Fiction",
                 "cover": "https://res.cloudinary.com/drbktnxop/image/upload/v1733733015/animal_farm_rrhbdl.jpg"},
            ]
        },
        {
            "first_name": "J.K.", "last_name": "Rowling",
            "photo": "https://res.cloudinary.com/drbktnxop/image/upload/v1733732068/jk_rowling_ibit6n.jpg",
            "biography": "British author.", "birth_date": datetime.date(1965, 7, 31),
            "books": [
                {"title": "Harry Potter and the Sorcerer's Stone", "description": "The first Harry Potter novel.",
                 "isbn": "9787890123456", "price": 19.99, "genre": "Fantasy",
                 "cover": "https://res.cloudinary.com/drbktnxop/image/upload/v1733733018/harry_potter_1_qph1ym.jpg"},
                {"title": "Harry Potter and the Chamber of Secrets", "description": "Second in the series.",
                 "isbn": "9788901234567", "price": 19.99, "genre": "Fantasy",
                 "cover": "https://res.cloudinary.com/drbktnxop/image/upload/v1733733017/harry_potter_2_fz1riz.jpg"},
            ]
        },
        {
            "first_name": "J.R.R.", "last_name": "Tolkien",
            "photo": "https://res.cloudinary.com/drbktnxop/image/upload/v1731767885/santbel0bb0efsvqkafb.jpg",
            "biography": "British author.", "birth_date": datetime.date(1965, 7, 31),
            "books": [
                {"title": "The Hobbit", "description": "Children's fantasy novel.",
                 "isbn": "9780048231888", "price": 19.99, "genre": "Fantasy",
                 "cover": "https://res.cloudinary.com/drbktnxop/image/upload/v1733733020/the_hobbit_o9lnkb.jpg"},
                {"title": "The Lord of the Rings", "description": "Epic fantasy adventure. Sequel to The Hobbit.",
                 "isbn": "9788845292613", "price": 29.99, "genre": "Fantasy",
                 "cover": "https://res.cloudinary.com/drbktnxop/image/upload/v1731768107/wxdgqmw7gemko9vy57pb.jpg"},
            ]
        },
    ]

    author_objects = []
    book_objects = []

    genres = list(Genre.objects.all())

    for author_data in authors_and_books:
        author = Author(
            first_name=author_data["first_name"],
            last_name=author_data["last_name"],
            biography=author_data["biography"],
            birth_date=author_data["birth_date"],
            photo=author_data["photo"]
        )
        author_objects.append(author)

    Author.objects.bulk_create(author_objects)
    created_authors = Author.objects.all()

    for author, author_data in zip(created_authors, authors_and_books):
        for book_data in author_data["books"]:
            book_objects.append(Book(
                title=book_data["title"],
                description=book_data["description"],
                price=book_data["price"],
                isbn=book_data["isbn"],
                author=author,
                genre=genre_map[book_data["genre"]],
                cover=book_data["cover"]
            ))

    Book.objects.bulk_create(book_objects)


class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0002_alter_book_author_alter_book_genre'),
    ]

    operations = [
        migrations.RunPython(populate_data),
    ]