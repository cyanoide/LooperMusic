🎵 Looper Music 🌀
Un outil web simple et efficace pour créer des boucles audio personnalisées. Idéal pour transformer un morceau avec une intro/outro en une version longue (extended) pour du mix ou du stream.

✨ Fonctionnalités
Découpe précise : Définissez le début et la fin de la boucle au dixième de seconde près.

Multiplicateur : Répétez la boucle jusqu'à 100 fois.

Transitions fluides : Crossfade automatique entre les boucles pour éviter les clics sonores.

Fondus (Fades) : Ajoutez un Fade-in au début et un Fade-out à la fin pour un rendu pro.

Formats : Exportation en MP3 ou WAV.

🚀 Utilisation en ligne
L'application est accessible via Streamlit Cloud :

👉 [🎵 Looper Music 🌀](https://loopermusic.streamlit.app/)

🛠️ Installation (pour le développement local)
Prérequis
Python 3.11 (recommandé)

FFmpeg (obligatoire pour le traitement MP3)

Windows : choco install ffmpeg

Mac : brew install ffmpeg

Linux : sudo apt install ffmpeg

Lancement
Clonez le dépôt :

Bash

git clone https://github.com/votre-nom/looper-music.git
cd looper-music
Installez les dépendances :

Bash

pip install -r requirements.txt
Lancez l'application :

Bash

streamlit run app.py
📦 Structure du projet
app.py : Le code source de l'application.

requirements.txt : Liste des bibliothèques Python (pydub, streamlit).

packages.txt : Dépendance système pour le serveur (ffmpeg).
