from mongoengine import StringField, Document, connect, ObjectIdField, ReferenceField, ListField
import json

connect('tumblelog')

class Author(Document):
    id = ObjectIdField(primary_key=True)
    fullname = StringField(max_length=50)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=50)
    description = StringField(max_length=4000)
    meta = {'indexes':['born_date', 'born_location']}


class Quote(Document):
    id = ObjectIdField(primary_key=True)
    tags = ListField(StringField(max_length=50))
    quote = StringField(max_length=1050)

    author = ReferenceField(Author)



with open("authors.json", "r") as f:

    authors_data = json.load(f)

for author_data in authors_data: # для кожного словника в списку authors_data
    author = Author(**author_data) # створюємо екземпляр класу Author, використовуючи дані з словника
    author.save()

with open("quotes.json", "r") as f:
    quotes_data = json.load(f)


for quote_data in quotes_data:  # знаходимо автора цитати за його іменем, використовуючи метод objects
    author = Author.objects(fullname=quote_data["author"]).first()
    # якщо автор знайдений
    if author:
        # створюємо екземпляр класу Quote, використовуючи дані з словника
        # і передаємо об'єкт author як значення поля author
        quote = Quote(tags=quote_data["tags"], author=author, quote=quote_data["quote"])
        quote.save()
    # якщо автор не знайдений
    else:
        # виводимо повідомлення про помилку
        print(f"Author {quote_data['author']} not found in database.")


while True:
    command = input("Enter your command: ")
    if command == "exit":
        print("Exiting the script.")
        break
    else:
        keyword, value = command.split(":")
        if keyword == "name":
            quotes = Quote.objects(author__fullname=value)
            # якщо список цитат не порожній
            if quotes:
                # виводимо кількість знайдених цитат
                print(f"Found {len(quotes)} quotes by {value}:")
                for quote in quotes:
                    # виводимо текст цитати і теги, розділені комами
                    print(f"\"{quote.quote}\" ({', '.join(quote.tags)})")
            # якщо список цитат порожній
            else:
                print(f"No quotes found by {value}.")
        elif keyword == "tag":
            # знаходимо всі цитати, які мають такий тег, використовуючи метод objects
            quotes = Quote.objects(tags=value)
            if quotes:
                print(f"Found {len(quotes)} quotes with tag {value}:")
                # для кожної цитати в списку
                for quote in quotes:
                    # виводимо текст цитати і ім'я автора
                    print(f"\"{quote.quote}\" by {quote.author.fullname}")
            else:
                print(f"No quotes found with tag {value}.")
        elif keyword == "tags":
            tags = value.split(",")
            # знаходимо всі цитати, які мають хоча б один з цих тегів, використовуючи метод objects
            quotes = Quote.objects(tags__in=tags)
            if quotes:
                print(f"Found {len(quotes)} quotes with tags {value}:")
                for quote in quotes:
                    print(f"\"{quote.quote}\" by {quote.author.fullname} ({', '.join(quote.tags)})")
            else:
                print(f"No quotes found with tags {value}.")
        else:
            print(f"Invalid command. Please use one of the following formats: name: value, tag: value, tags: value1,value2,...")