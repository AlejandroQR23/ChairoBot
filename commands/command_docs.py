commands = {
    "/ayuda": "Muestra los comandos disponibles",
    "/inicio": "Muestra el mensaje inicial del bot",
    "/hola": "Envia un saludo",
    "/gato": "Envia una foto aleatoria de un gato",
    "/traducir": "Traduce una palabra. Recibe el codigo del lenguaje ('es', 'en', etc) \nej de uso: /traducir es dog",
}


def get_commands():
    str_commands = ""
    for key in commands:
        str_commands += f"\n {key}: {commands[key]}"
    return str_commands
