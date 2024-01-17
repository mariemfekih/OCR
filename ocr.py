import PyPDF2
from PIL import Image
import re
import streamlit as st
import pdfplumber
from bidi.algorithm import get_display

# Fonction pour extraire le texte d'un PDF
def extraire_texte_pdf(chemin_pdf):
    texte = ""
    try:
        with pdfplumber.open(chemin_pdf) as pdf:
            for page in pdf.pages:
                texte += get_display(page.extract_text())
    except Exception as e:
        st.error(f"Erreur lors de l'ouverture du fichier PDF : {e}")
    return texte

liste_de_noms = ["ھﺷﺎم ﻧﺟﺎح", " ﻣﺣﻣد ﺑوﺷﺑﺎﺑك"]


'''************'''

st.title("Extraction de données depuis un PDF")
pdf_path = st.file_uploader("Sélectionnez un fichier PDF", type="pdf")

if pdf_path is not None:
    # Extraction du texte du PDF
    pdf_text = extraire_texte_pdf(pdf_path)

    # Affichage du texte extrait
    st.subheader("Texte extrait du PDF:")
    st.text(pdf_text)

    cin_pattern = re.compile(r'\b[01]\d{7}\b')
    cin = cin_pattern.findall(pdf_text)

    num_tel_pattern = re.compile(r'\b[2579]\d{7}\b')
    num_tel = num_tel_pattern.findall(pdf_text)
    nouns_pattern = re.compile("|".join(map(re.escape, liste_de_noms)), re.IGNORECASE)
    nouns = list(set(nouns_pattern.findall(pdf_text)))
    
    date_pattern = re.compile(r'(\d{4}/\d{2}/\d{2})')
    dates = date_pattern.findall(pdf_text)

    st.subheader("الاسماء")
    st.write(nouns)

    st.subheader("رقم بطاقة التعريف")
    st.write(cin)

   

    st.subheader("  التواريخ")
    st.write(dates)

    # Save the extracted data to a file
    with open("extracted_data.txt", "w", encoding="utf-8") as file:
        file.write("الاسماء:\n")
        file.write(str(nouns) + "\n")
        file.write("رقم بطاقة التعريف:\n")
        file.write(str(cin) + "\n")
        file.write("التواريخ:\n")
        file.write(str(dates) + "\n")

    output_file_path = "output_pdf.txt"
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
     output_file.write(pdf_text)
    st.success("تم حفظ البيانات المستخرجة في ملف extracted_data.txt and output_pdf.txt ")