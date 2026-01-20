# 🎵 Looper Music 🌀

**Looper Music** est un outil web simple et efficace pour créer des boucles audio personnalisées. Idéal pour transformer un morceau avec une intro/outro en une version longue (*extended*) pour du mix, du stream ou de la production.



## ✨ Fonctionnalités

* **✂️ Découpe précise :** Définissez le début et la fin de la boucle au dixième de seconde près.
* **🔁 Multiplicateur :** Répétez la partie centrale jusqu'à **100 fois**.
* **🌊 Transitions fluides :** Crossfade automatique ajustable entre les boucles pour éliminer les "clics" sonores.
* **🪄 Fondus (Fades) :** Ajoutez un *Fade-in* au début et un *Fade-out* à la fin pour une sortie en douceur.
* **💾 Formats :** Exportation instantanée en **MP3** ou **WAV**.

---

## 🚀 Utilisation en ligne

L'application est hébergée et prête à l'emploi sur Streamlit Cloud :  
👉 [**Lancer Looper Music**](https://loopermusic.streamlit.app/)

---

## 🛠️ Installation (Développement local)

Si vous souhaitez faire tourner l'outil sur votre propre machine :

### 1. Prérequis
* **Python 3.11** (recommandé)
* **FFmpeg** (obligatoire pour la lecture/écriture des fichiers audio)
    * **Windows :** `choco install ffmpeg`
    * **Mac :** `brew install ffmpeg`
    * **Linux :** `sudo apt install ffmpeg`

### 2. Lancement
```bash
# Clonez le dépôt
git clone [https://github.com/votre-nom/looper-music.git](https://github.com/votre-nom/looper-music.git)
cd looper-music

# Installez les dépendances
pip install -r requirements.txt

# Lancez l'interface
streamlit run app.py
