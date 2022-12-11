def url_address(url: str, array_parameters: list) -> str:

    # array_parameters = ["true", "new", "tshort"]

    # Second parameter:
    #     new
    #     ozon_card_price
    #     price_desc
    #     discount
    #     rating

    for param in array_parameters:
        url = url.replace("@", str(param), 1)

    return url


print(url_address("https://www.ozon.ru/search/?from_global=@&sorting=@&text=@", ["true", "rating", "minecraft"]))
