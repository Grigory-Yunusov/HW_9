from main import Author, Quote

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