import os
import os.path
import subprocess
import sys


from colorama import Fore
from colorama import Style
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from textwrap import wrap
from fpdf import FPDF 

import const as c


################### Suppression de fichier temporaires ################

def suppressionFichier(fichierasuppr):
    # Suppression des fichiers temporaires
    print(f"[+] Suppression des fichiers temporaires")
    print("-------------------------------------------")
    if os.path.exists(fichierasuppr):
        os.remove(fichierasuppr)
        print("Les fichiers temporaires du processus ont été supprimés")

################### Ecriture de fichier temporaires ###################

def ecrireFichier(fichieraecrire):
    with open(c.fichierContenu, "w") as f:
        f.write(fichieraecrire)

################### Générer le rapport en fichier txt #################

def ajouterAurapport(textajouter):
    with open(c.fichierRapport, "a") as f:
        f.write(textajouter)

########### Processus de réalisation des différnts tests sur le vardir ##########

## Vérifier que le montage des systèmes de fichier non utilisés soit désactivé.
def verif_sys_fichier(point_test):
    for elem in point_test:
        elem_upper = elem.upper()
        output = subprocess.check_output(["modprobe", "-n", "-v", elem]).decode(sys.stdout.encoding).strip()
        # nous vérifions si le module est désactivé.
        if "install /bin/true" in output:   
            textajouter = c.titre_rub_file_sys + elem + "\n"
            ajouterAurapport(textajouter)
            textajouter = c.point + "\n \n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + c.com_rub_file_sys0 + elem + "\n"
            ajouterAurapport(textajouter)
            print(c.titre_rub_file_sys + elem )
            print(c.point)
            print()
            print(f"\t {c.com_rub_file_sys1}{elem} \t \t \t \t {Style.BRIGHT} [ {Fore.WHITE}{elem_upper} OK{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")
        else:
            textajouter = c.titre_rub_file_sys + elem + "\n"
            ajouterAurapport(textajouter)
            textajouter = c.point + "\n \n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + c.com_rub_file_sys2 + elem + "\n"
            ajouterAurapport(textajouter)
            print(c.titre_rub_file_sys + elem )
            print(c.point)
            print()
            print(f"\t {c.com_rub_file_sys2}{elem} \t \t \t \t {Style.BRIGHT} [ {Fore.RED}{elem_upper} EXPOSE{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")

### Vérifier que le montage du système de fichier FAT soit limité.
def verif_sys_vfat(point_test_vfat):
    for elem in point_test_vfat:
        output = os.popen("grep -i vfat /etc/fstab").read()
        elem_upper = elem.upper()
        if "umask=0077" in output:
            textajouter = c.titre_rub_vfat + elem + "\n"
            ajouterAurapport(textajouter)
            textajouter = c.point + "\n \n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + c.com_rub_vfat0 + elem + "\n"
            ajouterAurapport(textajouter)
            print(c.titre_rub_vfat + elem)
            print(c.point)
            print()
            # nous vérifions si le module est désactivé.
            print(f"\t {c.com_rub_vfat0}{elem} \t \t \t \t \t {Style.BRIGHT} [ {Fore.WHITE}{elem_upper} OK{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")
        else:
            textajouter = c.titre_rub_vfat + elem + "\n"
            ajouterAurapport(textajouter)
            textajouter = c.point + "\n \n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + c.com_rub_vfat1 + elem + "\n"
            ajouterAurapport(textajouter)
            print(c.titre_rub_vfat + elem)
            print(c.point)
            print()
            print(f"\t {c.com_rub_vfat1}{elem} \t \t \t \t \t {Style.BRIGHT} [ {Fore.RED}{elem_upper} EXPOSE{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")

## Vérifier que le montage de certains répertoire aient les bonne options de montage.
def test_vardir(point_test_vardir):
    for elem in point_test_vardir:
        elem_upper = str(elem).upper()
        ismount = os.path.ismount(elem)
        if ismount == False:   # nous vérifions si le répertoire  est monté.
            textajouter = c.titre_rub_vardir + elem + "\n"
            ajouterAurapport(textajouter)
            textajouter = c.point + "\n \n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + elem + c.com_rub_vardir0 + "\n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + c.com_rub_vardir1 + elem + "\n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + c.titre_remediation + elem + "\n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + c.point + "\n \n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + elem + c.com_rub_vardir_rec0 + "\n"
            ajouterAurapport(textajouter)
            print(c.titre_rub_vardir + elem)
            print(c.point)
            print()
            print(f"\t {elem}{c.com_rub_vardir0} \t \t \t \t {Style.BRIGHT} [ {Fore.RED}{elem_upper} EXPOSE{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}") 
            print(f"\t {elem} {c.com_rub_vardir1} \t \t {Style.BRIGHT} [ {Fore.RED}{elem_upper} EXPOSE{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")
        else:
            isverify = os.popen("mount | grep -E " "%s"%elem).read()
            ecrireFichier(isverify)
            if os.path.getsize(c.fichierContenu) == 0:
                textajouter = c.titre_rub_vardir + elem + "\n"
                ajouterAurapport(textajouter)
                textajouter = c.point + "\n \n"
                ajouterAurapport(textajouter)
                textajouter = "\t" + elem + c.com_rub_vardir_rec1 + elem + "\n"
                ajouterAurapport(textajouter)
                print(f"\t {elem} {c.com_rub_vardir1} \t \t \t \t {Style.BRIGHT} [ {Fore.RED}{elem_upper} EXPOSE{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")
                print()
                print(f"{c.titre_rub_vardir1}{elem}")
                print(c.point)
                print()
                print(f"\t {c.com_rub_vardir_rec1}{elem} \t \t \t \t {Style.BRIGHT} [ {Fore.WHITE}{elem_upper} OK{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")
            else:
                textajouter = c.titre_rub_vardir + elem + "\n"
                ajouterAurapport(textajouter)
                textajouter = c.point + "\n \n"
                ajouterAurapport(textajouter)
                textajouter = "\t" + elem + c.com_rub_vardir_rec1 + elem + "\n"
                ajouterAurapport(textajouter)
                print(f"\t {elem} {c.com_rub_vardir1} \t \t \t \t  {Style.BRIGHT} [ {Fore.RED}{elem_upper} EXPOSE{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")
                print()
                print(f"{c.titre_rub_vardir1}{elem}")
                print(c.point)
                print()
                print(f"\t {elem} {c.com_rub_vardir1} \t \t \t \t {Style.BRIGHT} [ {Fore.RED}{elem_upper} EXPOSE{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")

#### Vérifier que le répertoire /home soit monté avec les bonnes options
def verif_home():
    for elem in c.point_test_home:
        elem_upper = str(elem).upper()
        ismount = os.path.ismount(elem)
        if ismount == False: 
            textajouter = c.titre_rub_home0 + elem + "\n"
            ajouterAurapport(textajouter)
            textajouter = c.point + "\n \n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + elem + c.com_rub_home0 + "\n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + c.com_rub_home1 + elem + "\n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + c.titre_remediation + elem + "\n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + c.point + "\n \n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + elem + c.com_rub_home_rec0 + "\n"
            ajouterAurapport(textajouter)
            print(c.titre_rub_home0 + elem)
            print(c.point)
            print()
            print(f"\t {elem}{c.com_rub_home0} \t \t \t \t {Style.BRIGHT} [ {Fore.RED}{elem_upper} EXPOSE{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}") 
            print(f"\t {c.com_rub_home1} \t \t \t {Style.BRIGHT} [ {Fore.RED}{elem_upper} EXPOSE{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")
        isverify = os.popen("mount | grep -E " "%s"%elem).read()
        ecrireFichier(isverify)
        if os.path.getsize(c.fichierContenu) == 0:
            textajouter = c.titre_rub_home1 + elem + "\n"
            ajouterAurapport(textajouter)
            textajouter = c.point + "\n \n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + c.com_rub_home2 + elem + "\n"
            ajouterAurapport(textajouter)
            print(c.titre_rub_home1 + elem)
            print(c.titre_rub_sticky_bit + c.sticky)
            print(c.point)
            print()
            print(f"\t {c.com_rub_sticky_bit0} \t \t \t \t \t {Style.BRIGHT} [{Fore.WHITE} STICKY BIT OK{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")
        else:
            textajouter = c.titre_rub_sticky_bit + c.sticky + "\n"
            ajouterAurapport(textajouter)
            textajouter = c.point + "\n \n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + c.com_rub_sticky_bit1 + "\n"
            ajouterAurapport(textajouter)
            print(c.titre_rub_sticky_bit + c.sticky)
            print(c.point)
            print()
            print(f"\t {c.com_rub_sticky_bit1} \t \t \t \t {Style.BRIGHT} [ {Fore.RED}{c.sticky.upper} EXPOSE{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")

#### Vérifier que le bit collant est définit sur les répertoires accéssible en écriture pour tous
def verif_stickybit():
    isverify = os.popen(r"df --local -P | awk {'if (NR!=1) print $6'} | xargs -I '{}' find '{}' -xdev -type d \( -perm -0002 -a ! -perm -1000 \) 2>/dev/null").read()            
    with open(c.fichierContenu, "w") as f:
        f.write(isverify.strip())

    with open(c.fichierContenu, "r") as f:
        # findtext = ""
        if "" in f.read():
            textajouter = c.titre_rub_sticky_bit + c.sticky + "\n"
            ajouterAurapport(textajouter)
            textajouter = c.point + "\n \n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + c.com_rub_sticky_bit0 + "\n"
            ajouterAurapport(textajouter)
            print(c.titre_rub_sticky_bit + c.sticky)
            print(c.point)
            print()
            print(f"\t {c.com_rub_sticky_bit0} \t \t \t \t \t {Style.BRIGHT} [{Fore.WHITE} STICKY BIT OK{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")
        else:
            textajouter = c.titre_rub_sticky_bit + c.sticky + "\n"
            ajouterAurapport(textajouter)
            textajouter = c.point + "\n \n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + c.com_rub_sticky_bit1 + "\n"
            ajouterAurapport(textajouter)
            print(c.titre_rub_sticky_bit + c.sticky)
            print(c.point)
            print()
            print(f"\t {c.com_rub_sticky_bit1} \t \t \t \t {Style.BRIGHT} [ {Fore.RED}{c.sticky.upper} EXPOSE{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")

#### Vérification des permission sur le fichier de configuration bootloader.
def verif_bootloader(): 
    isverify = os.popen("stat /boot/grub/grub.cfg").read()
    with open(c.fichierContenu, "w") as f:
        f.write(isverify.strip())

    with open(c.fichierContenu, "r") as f:
        findtext = "(0400/-rw-------)"
        if findtext in f.read():
            textajouter = c.titre_rub_bootloader + c.bootloader + "\n"
            ajouterAurapport(textajouter)
            textajouter = c.point + "\n \n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + c.com_rub_bootloader0 + "\n"
            ajouterAurapport(textajouter)
            print(c.titre_rub_bootloader + c.bootloader)
            print(c.point)
            print()
            print(f"\t {c.com_rub_bootloader0}{c.bootloader} \t \t {Style.BRIGHT} [ {Fore.WHITE}{c.bootloader.upper()} OK{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")
        else:
            textajouter = c.titre_rub_bootloader + c.bootloader + "\n"
            ajouterAurapport(textajouter)
            textajouter = c.point + "\n \n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + c.com_rub_bootloader1 + c.bootloader + "\n"
            ajouterAurapport(textajouter)
            print(c.titre_rub_bootloader + c.bootloader)
            print(c.point)
            print()
            print(f"\t {c.com_rub_bootloader1}{c.bootloader} \t \t {Style.BRIGHT} [ {Fore.RED}{c.bootloader.upper()} EXPOSE{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")

#### Vérifier l'authentification en mode single user.
def verif_auth_single_user_mode():
    isverify = os.popen(r"grep ^root:[*\!]: /etc/shadow").read()
    with open(c.fichierContenu, "w") as f:
        f.write(isverify.strip())
    if os.path.getsize(c.fichierContenu) == 0:
        textajouter = c.titre_rub_auth_single_user_mode + "\n"
        ajouterAurapport(textajouter)
        textajouter = c.point + "\n \n"
        ajouterAurapport(textajouter)
        textajouter = "\t" + c.com_rub_auth_single_user_mode0 + "\n"
        ajouterAurapport(textajouter)
        print(c.titre_rub_auth_single_user_mode)
        print(c.point)
        print()    
        print(f"\t {c.com_rub_auth_single_user_mode0} \t \t \t {Style.BRIGHT} [ {Fore.WHITE} SINGLE USER MODE OK{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")
    else:
        textajouter = c.titre_rub_auth_single_user_mode + "\n"
        ajouterAurapport(textajouter)
        textajouter = c.point + "\n \n"
        ajouterAurapport(textajouter)
        textajouter = "\t" + c.com_rub_auth_single_user_mode1
        ajouterAurapport(textajouter)
        print(c.titre_rub_auth_single_user_mode)
        print(c.point)
        print()  
        print(f"\t {c.com_rub_auth_single_user_mode1} \t \t \t {Style.BRIGHT} [ {Fore.RED} ROOT PASSWORD{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")

#### Vérifier les options sur /dev/shm.
def verif_dev_shm(): 
    isverify = os.popen(r"mount | grep -E '\s/dev/shm\s' | grep -v nodev").read()
    with open(c.fichierContenu, "w") as f:
        f.write(isverify.strip())
    if os.path.getsize(c.fichierContenu) == 0:
        print(c.titre_rub_dev_shm)
        print(c.point)
        print()
        textajouter = c.titre_rub_dev_shm + "\n"
        ajouterAurapport(textajouter)
        textajouter = c.point + "\n \n"
        ajouterAurapport(textajouter)
        textajouter = "\t" + c.com_rub_dev_shm0 + c.dev_shm + "\n"
        ajouterAurapport(textajouter)
        print(f"\t {c.com_rub_dev_shm0}{c.dev_shm} \t \t \t \t \t {Style.BRIGHT} [ {Fore.WHITE} OK{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")
    else:
        textajouter = c.titre_rub_dev_shm
        print(c.point)
        print()
        ajouterAurapport(textajouter)
        textajouter = c.point + "\n \n"
        ajouterAurapport(textajouter)
        textajouter = "\t" + c.com_rub_dev_shm1 + "\n"
        ajouterAurapport(textajouter)
        print(c.titre_rub_auth_single_user_mode + "\n")
        print(f"\t {c.com_rub_dev_shm1}{c.dev_shm} \t \t \t \t \t {Style.BRIGHT} [ {Fore.RED} /DEV/SHM EXPOSE{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")

#### Vérifier la configuration du mot de passe bootloade.
def verif_bootloader_pass(): 
    isverify = os.popen(r'grep "^\s*password" /boot/grub/grub.cfg').read()
    if "password --md5" in isverify or "GRUB2_PASSWORD" in isverify or "set superusers" in isverify or "password_pbkdf2" in isverify:
        textajouter = c.titre_rub_bootloader_pass + "\n"
        ajouterAurapport(textajouter)
        textajouter = c.point
        ajouterAurapport(textajouter)
        ajouterAurapport(textajouter)
        textajouter = c.point + "\n \n"
        ajouterAurapport(textajouter)
        textajouter = "\t" + c.com_rub_bootloader_pass0 + "\n"
        ajouterAurapport(textajouter)
        print(c.titre_rub_bootloader_pass)
        print(c.point)
        print()
        print(f"\t {c.com_rub_bootloader_pass0} \t \t {Style.BRIGHT} [ {Fore.WHITE} BOOTLOADER OK{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")
    else:
        textajouter = c.titre_rub_bootloader_pass + "\n"
        ajouterAurapport(textajouter)
        textajouter = c.point + "\n \n"
        ajouterAurapport(textajouter)
        textajouter = "\t" + c.com_rub_bootloader_pass1 + "\n"
        ajouterAurapport(textajouter)
        print(c.titre_rub_bootloader_pass)
        print(c.point)
        print()
        print(f"\t {c.com_rub_bootloader_pass1} \t {Style.BRIGHT} [ {Fore.RED} BOOTLOADER EXPOSE{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")

# ## Procéder à la réalisation des différnts tests
verif_sys_fichier(c.point_test)
verif_sys_vfat(c.point_test_vfat)
test_vardir(c.point_test_vardir)
verif_home()
verif_stickybit()
verif_bootloader()
verif_auth_single_user_mode()
verif_dev_shm()
verif_bootloader_pass()

## Processus de génération du rapport en pdf

## Pour le pdf
fileName = "Rapport d'audit.pdf"
documentTitle = "Rapport de test de sécurité"
titleup = "Rapport du test d'audit"
title = titleup.upper()
subTitle = "Tests et récommandations"
image = "cover1.jpg"



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
pdf.set_left_margin(10)
pdf.set_right_margin(10)
pdf.cell(190, 5, txt = c.context.upper(), ln = 1, align = 'L') 
pdf.ln(5)
pdf.multi_cell(w=190, h=5, txt = c.first_page, align = 'J')
pdf.ln(220)
# Insérer le texte dans le doument pdf 
f = open(c.fichierRapport, "r") 
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

## Supprimer les fichier temporaires
suppressionFichier(c.fichierContenu)
suppressionFichier(c.fichierRapport)
