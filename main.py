import urllib.request
import json
    
def main():
    print("Bienvenido al programa de eventos de GitHub")
    username = input("Ingrese el nombre de usuario de GitHub: ")
    if not username:
        print("El nombre de usuario no puede estar vacío.")
        return
    
    url = f"https://api.github.com/users/{username}/events"
    
    req = urllib.request.Request(
        url,
        headers={
            "X-GitHub-Api-Version": "2022-11-28",
        }
    )

    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            for event in data[:5]:
                print(f"- {event['type']} in {event['repo']['name']}")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("Usuario no encontrado.")
        else:
            print(f"Error al acceder a la API: {e}")
    except Exception as e:
        print(f"Error general: {e}")

if __name__ == "__main__":
    main()