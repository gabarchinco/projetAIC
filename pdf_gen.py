import os
from fpdf import FPDF 
import const as c
import pdf_cons as pdfcons


## Processus de génération du rapport en pdf
### Initier la class PDF
class PDF(FPDF):
        # L'entête du pdf
    def header(self):
        # Initier la police du document
        self.set_font('Arial', 'B', 12)
        # Initier la position du titre et sa couleur
        w = self.get_string_width(pdfcons.title) + 151
        self.set_x((210 - w) / 2)
        # Initier la position du sous-titre et sa couleur
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50, 50)
        self.cell(w, 6, pdfcons.title, 1, 1, 'C', 1)
        # Inserer un saut de ligne
        self.ln(8)

    # Pied de page du pdf footer
    def footer(self):
        # Positionnement à 1.5 cm du b20as de page
        self.set_y(-15)
        # Initier la police en Arial italic de taille 8
        self.set_font('Arial', 'I', 8)
        # Insere les numéros de page
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

# Instancier la class PDF
def generatepdf():
    pdf = PDF()
    pdf.alias_nb_pages()
    # Créer la page
    pdf.add_page() 
    # Définir le style et la marge gauche
    pdf.set_font('Arial', 'B', 18)

    try:
        if open(pdfcons.image):
            pdf.image(pdfcons.image, 0, 0, h=300, w=210)
    except FileNotFoundError:
        print("Erreur : Le fichier image pour le pdf n'existe pas ")
        raise

    pdf.set_font('Arial', 'B', 18)
    pdf.set_left_margin(0)
    pdf.set_draw_color(0, 80, 180)
    pdf.set_fill_color(230, 230, 0)
    pdf.set_text_color(220, 50, 50)
    w = pdf.get_string_width(pdfcons.title) + 123
    pdf.set_x((209 - w) / 2)
    pdf.set_y(10)
    pdf.cell(w, 12, pdfcons.title, 0, 1, 'C', 1)
    pdf.ln(250)


    pdf.set_font("Arial", "B", size = 12) 
    pdf.set_left_margin(10)
    pdf.set_right_margin(10)
    pdf.cell(190, 5, txt = c.context.upper(), ln = 1, align = 'L') 
    pdf.ln(5)
    pdf.set_font("Arial", size = 12) 
    pdf.multi_cell(w=190, h=5, txt = c.first_page, align = 'J')
    pdf.ln(220)
    # Insérer le texte dans le doument pdf 
    f = open(c.fichierRapport, "r") 
    for x in f:
        if "[+]" in x or ("---") in x:
            pdf.set_left_margin(10)
            pdf.set_right_margin(10)
            pdf.cell(190, 5, txt = x, ln = 1, align = 'L') 
        else:
            pdf.set_left_margin(10)
            pdf.set_right_margin(10)
            pdf.set_x(10)
            pdf.multi_cell(190, 5, txt = x, align = 'L') 

    ### Générer le rapport des tests en pdf
    pdf.output(pdfcons.fileName) 
generatepdf()