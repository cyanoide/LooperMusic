import streamlit as st
from pydub import AudioSegment
import io

st.set_page_config(page_title="Boucleur Audio Pro", page_icon="🎵")

st.title("🎵 Boucleur de Musique Automatique")
st.write("Chargez un son, définissez la boucle, et téléchargez le résultat.")

uploaded_file = st.file_uploader("Choisir un fichier MP3", type=["mp3", "wav"])

if uploaded_file is not None:
    # Charger l'audio en mémoire
    audio = AudioSegment.from_file(uploaded_file)
    duration_secs = len(audio) / 1000.0

    st.audio(uploaded_file)
    
    col1, col2 = st.columns(2)
    with col1:
        start_loop = st.number_input("Début de boucle (sec)", min_value=0.0, max_value=duration_secs, value=5.0)
        end_loop = st.number_input("Fin de boucle (sec)", min_value=0.0, max_value=duration_secs, value=duration_secs-5.0)
    
    with col2:
        num_loops = st.number_input("Nombre de répétitions", min_value=1, max_value=100, value=3)
        export_format = st.selectbox("Format de sortie", ["mp3", "wav"])

    if st.button("Générer le fichier"):
        with st.spinner("Traitement en cours..."):
            # Logique de découpe
            intro = audio[:start_loop * 1000]
            loop_part = audio[start_loop * 1000 : end_loop * 1000]
            outro = audio[end_loop * 1000:]
            
            # Construction
            final_audio = intro + (loop_part * num_loops) + outro
            
            # Export en mémoire buffer
            buffer = io.BytesIO()
            final_audio.export(buffer, format=export_format)
            
            st.success("Terminé !")
            st.download_button(
                label="⬇️ Télécharger le résultat",
                data=buffer.getvalue(),
                file_name=f"musique_bouclee.{export_format}",
                mime=f"audio/{export_format}"
            )
