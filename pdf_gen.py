from fpdf import FPDF 

fichierRapport = "rapport.txt"

## Pour le pdf
fileName = "Rapport d'audit.pdf"
documentTitle = "Rapport de test de sécurité"
titleup = "Rapport du test d'audit"
title = titleup.upper()
subTitle = "Tests et récommandations"
image = "cover4.jpg"
image0 = "cover1.jpg"


## Processus de génération du rapport en pdf
### Initier la class PDF
class PDF(FPDF):
        # L'entête du pdf
    def header(self):
        # Initier la police du document
        self.set_font('Arial', 'B', 12)
        # Initier la position du titre et sa couleur
        w = self.get_string_width(title) + 151
        self.set_x((210 - w) / 2)
        # Initier la position du sous-titre et sa couleur
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50, 50)
        self.cell(w, 6, title, 1, 1, 'C', 1)
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
pdf = PDF()
pdf.alias_nb_pages()
# Créer la page
pdf.add_page() 
# Définir le style et la marge gauche
# pdf.set_left_margin(10)
pdf.set_font('Arial', 'B', 18)

pdf.image(image, 0, 0, h=300, w=210)

pdf.set_font('Arial', 'B', 18)
pdf.set_left_margin(0)
pdf.set_draw_color(0, 80, 180)
pdf.set_fill_color(230, 230, 0)
pdf.set_text_color(220, 50, 50)
w = pdf.get_string_width(title) + 123
pdf.set_x((209 - w) / 2)
pdf.set_y(10)
pdf.cell(w, 12, title, 0, 1, 'C', 1)
pdf.ln(250)


pdf.set_font("Arial", size = 12) 
# Insérer le texte dans le doument pdf 
f = open(fichierRapport, "r") 
for x in f:
    if "[+]" in x or ("---") in x:
        pdf.set_left_margin(10)
        pdf.cell(200, 5, txt = x, ln = 1, align = 'L') 
    else:
        pdf.set_left_margin(10)
        pdf.set_x(10)
        pdf.multi_cell(200, 5, txt = x, align = 'L') 

### Générer le rapport des tests en pdf
pdf.output(fileName) 