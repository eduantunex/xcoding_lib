def tablebylist(list, max_caracteres):
    text = ""
    for linha in list:
        soma_text = 0
        for item in linha:
            item_formatado = item.ljust(max_caracteres)  # completa com espaços
            text += f"| {item_formatado} "
            soma_text += len(f"| {item_formatado} ")
        text += "|\n"
        text += "-" * soma_text + "\n"
    return text