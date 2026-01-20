import streamlit as st
from pydub import AudioSegment
import io

# Configuration de la page
st.set_page_config(page_title="Boucleur Audio Pro", page_icon="🎵", layout="centered")

st.title("🎵 Boucleur de Musique Automatique")
st.markdown("""
Chargez un morceau, définissez la zone à boucler, et téléchargez votre version longue personnalisée.
""")

# 1. Upload du fichier
uploaded_file = st.file_uploader("Choisir un fichier audio (MP3, WAV)", type=["mp3", "wav"])

if uploaded_file is not None:
    # Chargement du fichier audio
    with st.spinner("Analyse du fichier audio..."):
        audio = AudioSegment.from_file(uploaded_file)
    
    duration_secs = len(audio) / 1000.0
    st.audio(uploaded_file)
    st.info(f"📏 Durée totale : {duration_secs:.2f} secondes")

    # 2. Paramètres de la boucle
    st.header("✂️ Réglages de la boucle")
    col1, col2 = st.columns(2)
    
    with col1:
        start_loop = st.number_input("Début de boucle (sec)", min_value=0.0, max_value=duration_secs, value=0.0, step=0.1)
        end_loop = st.number_input("Fin de boucle (sec)", min_value=0.1, max_value=duration_secs, value=duration_secs, step=0.1)
    
    with col2:
        num_loops = st.number_input("Nombre de répétitions", min_value=1, max_value=100, value=3)
        crossfade_val = st.slider("Transition fluide (ms)", 0, 500, 50, help="Mélange légèrement les jonctions pour éviter les clics.")

    # 3. Paramètres de fondus (Fades)
    st.header("🎚️ Fondus (Fades)")
    col3, col4 = st.columns(2)
    
    with col3:
        fade_in_dur = st.slider("Fondu d'entrée (sec)", 0.0, 10.0, 0.5, step=0.1)
    with col4:
        fade_out_dur = st.slider("Fondu de sortie (sec)", 0.0, 10.0, 3.0, step=0.1)

    # 4. Traitement et Export
    st.markdown("---")
    export_format = st.selectbox("Format d'export", ["mp3", "wav"])
    
    if st.button("🚀 Générer le morceau", use_container_width=True):
        if start_loop >= end_loop:
            st.error("❌ Erreur : Le point de début doit être avant le point de fin !")
        else:
            try:
                with st.spinner("Traitement audio en cours..."):
                    # Découpage en millisecondes
                    intro = audio[:int(start_loop * 1000)]
                    loop_part = audio[int(start_loop * 1000):int(end_loop * 1000)]
                    outro = audio[int(end_loop * 1000):]
                    
                    # Construction de la boucle avec transition (crossfade)
                    combined_loop = loop_part
                    for _ in range(int(num_loops) - 1):
                        combined_loop = combined_loop.append(loop_part, crossfade=crossfade_val)
                    
                    # Assemblage final
                    final_audio = intro + combined_loop + outro
                    
                    # Application des fondus de début et de fin
                    if fade_in_dur > 0:
                        final_audio = final_audio.fade_in(int(fade_in_dur * 1000))
                    if fade_out_dur > 0:
                        final_audio = final_audio.fade_out(int(fade_out_dur * 1000))
                    
                    # Exportation dans un buffer mémoire
                    buffer = io.BytesIO()
                    final_audio.export(buffer, format=export_format)
                    processed_audio = buffer.getvalue()
                    
                    st.success("✅ Traitement terminé !")
                    
                    # Lecteur de prévisualisation
                    st.audio(processed_audio, format=f"audio/{export_format}")
                    
                    # Bouton de téléchargement
                    st.download_button(
                        label="⬇️ Télécharger le résultat",
                        data=processed_audio,
                        file_name=f"musique_bouclee.{export_format}",
                        mime=f"audio/{export_format}",
                        use_container_width=True
                    )
            except Exception as e:
                st.error(f"Une erreur est survenue lors du traitement : {e}")
