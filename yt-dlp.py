import yt_dlp

def download_video(url, quality="best"):
    ydl_opts = {
        'format': quality,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    print("Bienvenue dans l'outil de téléchargement de vidéos !")
    
    while True:
        print("\nMenu principal:")
        print("1. Télécharger une vidéo")
        print("2. Quitter")
        
        choix = input("Choisissez une option : ")
        
        if choix == "1":
            url = input("Entrez l'URL de la vidéo : ")
            
            print("\nChoisissez la qualité de la vidéo :")
            print("1. Meilleure qualité disponible")
            print("2. 1080p (Full HD)")
            print("3. 720p (HD)")
            print("4. 480p (SD)")
            print("5. 360p (SD basse qualité)")
            print("6. Audio uniquement")
            
            quality_choice = input("Choisissez une option : ")
            
            if quality_choice == "1":
                quality = "best"
            elif quality_choice == "2":
                quality = "136+140"  # 1080p avec audio
            elif quality_choice == "3":
                quality = "136+140"  # 720p avec audio (ajustez selon les options disponibles)
            elif quality_choice == "4":
                quality = "135+140"  # 480p avec audio
            elif quality_choice == "5":
                quality = "134+140"  # 360p avec audio
            elif quality_choice == "6":
                quality = "bestaudio"  # Audio uniquement
            else:
                print("Option non valide. Utilisation de la meilleure qualité par défaut.")
                quality = "best"
            
            try:
                download_video(url, quality)
                print("Téléchargement réussi !")
            except Exception as e:
                print(f"Erreur lors du téléchargement : {e}")
        
        elif choix == "2":
            print("Au revoir !")
            break
        
        else:
            print("Option non valide. Veuillez choisir à nouveau.")

if __name__ == "__main__":
    main()
