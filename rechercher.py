import webbrowser

choice = input ("Entrez la recherche que vous souhaitez faire: ")
new = 2 # NE PAS TOUCHER.
open = webbrowser.open

if choice == "python" or "py":
    open("https://www.python.org", new=new)
elif choice == "python doc" or "py doc":
    open("https://docs.python.org/3/", new=new)
elif choice == "youtube" or "yt":
    open("https://www.youtube.com", new=new)
elif choice == "twitch":
    open("https://www.twitch.tv", new=new)
elif choice == "github":
    open("https://github.com", new=new)
elif choice == "discord":
    open("https://discord.com", new=new)
elif choice == "spotify":
    open("https://www.spotify.com/fr/home/", new=new)
elif choice == "visual studio" or "vs":
    open("https://code.visualstudio.com", new=new)
else:
    print("La recherche n'est pas répértoriée.")

# Libre a vous de vous faire votre propre navigateur privé en Python d'ajouter une interface etc...
# C'est uniquement la base !