import streamlit as st
from portafolio_generator.generator import generate_summary
from portafolio_generator.templates import create_pdf

st.set_page_config(page_title="Generador de CV", page_icon="📄")

st.title("📄 Generador Automático de CV")

with st.form("cv_form"):
    nombre = st.text_input("Nombre completo")
    profesion = st.text_input("Profesión o título")
    experiencia = st.text_area("Experiencia laboral (breve descripción o palabras clave)")
    educacion = st.text_area("Educación")
    habilidades = st.text_area("Habilidades (separadas por comas)")
    submitted = st.form_submit_button("Generar CV")

if submitted:
    with st.spinner("Generando resumen profesional con IA..."):
        resumen = generate_summary(experiencia)

    st.success("Resumen generado correctamente ✅")
    st.write(f"**Resumen profesional:** {resumen}")

    create_pdf(nombre, profesion, resumen, experiencia, educacion, habilidades)
    st.download_button(
        "Descargar CV en PDF",
        data=open("cv.pdf", "rb").read(),
        file_name="cv.pdf",
        mime="application/pdf"
    )
