import urllib.request
import json
def main():
    print("Bienvenido al visor de eventos de GitHub")
    username = input("Ingrese el nombre de usuario de GitHub: ").strip()
    if not username:
        print("⚠️ El nombre de usuario no puede estar vacío.")
        return

    url = f"https://api.github.com/users/{username}/events"
    

    req = urllib.request.Request(url, headers = {
        "X-GitHub-Api-Version": "2022-11-28"
    })

    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())

            if not data:
                print("ℹ️ Este usuario no tiene actividad pública reciente.")
                return

            cantidad = input("Cuantos datos quieres ver? (por defecto 5): ")
            cantidad = int(cantidad) if cantidad.isdigit() else 5

            print(f"\n📄 Mostrando los últimos {min(cantidad, len(data))} eventos de @{username}:\n")
            for event in data[:cantidad]:
                print("- " + describir_evento(event))

    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("❌ Usuario no encontrado.")
        else:
            print(f"❌ Error al acceder a la API: {e}")
    except Exception as e:
        print(f"⚠️ Error general: {e}")
        
def describir_evento(event):
    tipo = event["type"]
    repo = event["repo"]["name"]
    if tipo == "PushEvent":
        commits = len(event["payload"].get("commits", []))
        return f"💾 Pushed {commits} commit(s) to {repo}"
    elif tipo == "WatchEvent":
        return f"⭐ Starred {repo}"
    elif tipo == "ForkEvent":
        return f"🍴 Forked {repo}"
    elif tipo == "IssuesEvent":
        action = event["payload"].get("action", "did something with")
        return f"🐛 {action.capitalize()} issue in {repo}"
    else:
        return f"📌{tipo} in {repo}"

if __name__ == "__main__":
    main()
