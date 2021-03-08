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


################### Les fichiers temporaires ##########################

fichierContenu = "contenu.txt"
fichierRapport = "rapport.txt"

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
    with open(fichierContenu, "w") as f:
        f.write(fichieraecrire)

################### Générer le rapport en fichier txt #################

def ajouterAurapport(textajouter):
    with open(fichierRapport, "a") as f:
        f.write(textajouter)

################### Variables ################

## Pour le commentaire
titre_rub_file_sys = "\n [+] Test sur la désactivation du sytème de fichier "
titre_rub_vfat = "\n [+] Test sur le montage du système de fichier "
titre_rub_vardir = "\n [+] Test du montage du répertoire "
titre_rub_vardir1 = "\n [+] Test des options de montage du répertoire "
titre_rub_home0 = "\n [+] Test du montage du répertoire "
titre_rub_home1 = "\n [+] Test des options de montage du répertoire "
titre_rub_sticky_bit = "\n [+] Test de définition du "
titre_rub_bootloader = "\n [+] Test des permissions sur le fichier "
titre_rub_auth_single_user_mode = "\n [+] Test de l'authentification du mode single user "
titre_remediation = "\n [+] Remédiation pour "
titre_rub_dev_shm = "\n [+] Test des options sur /dev/shm."
titre_rub_bootloader_pass = "\n [+] Test sur la configuration du mot de passe bootloader "
point = "--------------------------------------------------------"
com_rub_file_sys0 = "Test réussi sur le système de fichier "
com_rub_file_sys1 = "Test réussi sur les options de montage de "
com_rub_file_sys2 = "Risque potentiel sur le système de fichier "
com_rub_vfat0 = "Test réussi sur le système de fichier "
com_rub_vfat1 = "Il y a un risque potentiel sur le système de fichier "
com_rub_vardir0 = " n'est pas monté sur une partition séparée "
com_rub_vardir1 = "Il y a u risque potentiel sur le montage de la partition "
com_rub_vardir_rec0 = " doit être monter dans le fichier /etc/fstab avec ces options : defaults,rw,nosuid,nodev,noexec,relatime 0 0"
com_rub_vardir_rec1 = "Test réussi sur les options de montage du fichier "
com_rub_home0 = " n'est pas monté sur une partition séparée "
com_rub_home1 = "Il y a un risque potentiel sur le système de fichiere "
com_rub_home2 = "Test réussi sur les options de montage de "
com_rub_home_rec0 = " doit être monter dans le fichier /etc/fstab avec ces options : /home type ext4 (rw,nodev,relatime,data=ordered)"
com_rub_sticky_bit0 = "Test réussi sur la définition du bit collant "
com_rub_sticky_bit1 = "Il y a un risque potentiel sur l'assignation du bit collant "
com_rub_bootloader0 = "Test réussi sur permissions du fichier "
com_rub_bootloader1 = "Il y a un risque potentiel sur les permissions de "
com_rub_bootloader_rec = " doit être monté avec ces options : Access: (0400/-r--------) Uid: (0/ root) Gid: ( 0/ root)"
com_rub_auth_single_user_mode0 = "Test réussi sur l'authentification du mode single user "
com_rub_auth_single_user_mode1 = "Il y a un risque potentiel sur l'authentification du mode single user "
com_rub_dev_shm0 = "Test réussi sur les options de "
com_rub_dev_shm1 = "Il y a un risque potentiel sur les options de "
com_rub_bootloader_pass0 = "Test réussi sur la configuration du mot de passe bootloader "
com_rub_bootloader_pass1 = "Il y a un risque potentiel sur la configuration du mot de passe bootloader "
com_rub_bootloader_pass_rec = ""


## Pour le pdf
fileName = "Rapport d'audit.pdf"
documentTitle = "Rapport de test de sécurité"
title = "Rapport d'audit"
subTitle = "Tests et récommandations"
image = "image.jpg"

################### Les fonctions ############################

#### Vérifier que les répertoires soient montés sur des partitions séparées avec les bonnes options de montage

## Supprimer les fichier précédents
# suppressionFichier(fichierContenu)

point_test = ["cramfs", "freevxfs", "jffs2", "hfs", "hfsplus", "udf", "squashfs"]
point_test_vfat = ["vfat"]
point_test_vardir = ["/tmp", "/var", "/var/tmp", "/var/log", "/var/log/audit"]
point_test4 = ["/home"]
sticky = "sticky bit"
bootloader = "/boot/grub/grub.cfg"
dev_shm = "/dev/shm"

########### Processus de réalisation des différnts tests sur le vardir ##########

## Vérifier que le montage des systèmes de fichier non utilisés soit désactivé.
def verif_sys_fichier(point_test):
    for elem in point_test:
        elem_upper = elem.upper()
        output = subprocess.check_output(["modprobe", "-n", "-v", elem]).decode(sys.stdout.encoding).strip()
        # nous vérifions si le module est désactivé.
        if "install /bin/true" in output:   
            textajouter = titre_rub_file_sys + elem + "\n"
            ajouterAurapport(textajouter)
            textajouter = point + "\n \n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + com_rub_file_sys0 + elem + "\n"
            ajouterAurapport(textajouter)
            print(titre_rub_file_sys + elem )
            print(point)
            print()
            print(f"\t {com_rub_file_sys1}{elem} \t \t \t \t {Style.BRIGHT} [ {Fore.WHITE}{elem_upper} OK{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")
        else:
            textajouter = titre_rub_file_sys + elem + "\n"
            ajouterAurapport(textajouter)
            textajouter = point + "\n \n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + com_rub_file_sys2 + elem + "\n"
            ajouterAurapport(textajouter)
            print(titre_rub_file_sys + elem )
            print(point)
            print()
            print(f"\t {com_rub_file_sys2}{elem} \t \t \t \t {Style.BRIGHT} [ {Fore.RED}{elem_upper} EXPOSE{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")

### Vérifier que le montage du système de fichier FAT soit limité.
def verif_sys_vfat(point_test_vfat):
    for elem in point_test_vfat:
        output = os.popen("grep -i vfat /etc/fstab").read()
        elem_upper = elem.upper()
        if "umask=0077" in output:
            textajouter = titre_rub_vfat + elem + "\n"
            ajouterAurapport(textajouter)
            textajouter = point + "\n \n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + com_rub_vfat0 + elem + "\n"
            ajouterAurapport(textajouter)
            print(titre_rub_vfat + elem)
            print(point)
            print()
            # nous vérifions si le module est désactivé.
            print(f"\t {com_rub_vfat0}{elem} \t \t \t \t \t {Style.BRIGHT} [ {Fore.WHITE}{elem_upper} OK{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")
        else:
            textajouter = titre_rub_vfat + elem + "\n"
            ajouterAurapport(textajouter)
            textajouter = point + "\n \n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + com_rub_vfat1 + elem + "\n"
            ajouterAurapport(textajouter)
            print(titre_rub_vfat + elem)
            print(point)
            print()
            print(f"\t {com_rub_vfat1}{elem} \t \t \t \t \t {Style.BRIGHT} [ {Fore.RED}{elem_upper} EXPOSE{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")

## Vérifier que le montage de certains répertoire aient les bonne options de montage.
def test_vardir(point_test_vardir):
    for elem in point_test_vardir:
        elem_upper = str(elem).upper()
        ismount = os.path.ismount(elem)
        if ismount == False:   # nous vérifions si le répertoire  est monté.
            textajouter = titre_rub_vardir + elem + "\n"
            ajouterAurapport(textajouter)
            textajouter = point + "\n \n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + elem + com_rub_vardir0 + "\n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + com_rub_vardir1 + elem + "\n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + titre_remediation + elem + "\n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + point + "\n \n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + elem + com_rub_vardir_rec0 + "\n"
            ajouterAurapport(textajouter)
            print(titre_rub_vardir + elem)
            print(point)
            print()
            print(f"\t {elem}{com_rub_vardir0} \t \t \t \t {Style.BRIGHT} [ {Fore.RED}{elem_upper} EXPOSE{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}") 
            print(f"\t {elem} {com_rub_vardir1} \t \t {Style.BRIGHT} [ {Fore.RED}{elem_upper} EXPOSE{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")
        else:
            isverify = os.popen("mount | grep -E " "%s"%elem).read()
            ecrireFichier(isverify)
            if os.path.getsize(fichierContenu) == 0:
                textajouter = titre_rub_vardir + elem + "\n"
                ajouterAurapport(textajouter)
                textajouter = point + "\n \n"
                ajouterAurapport(textajouter)
                textajouter = "\t" + elem + com_rub_vardir_rec1 + elem + "\n"
                ajouterAurapport(textajouter)
                print(f"\t {elem} {com_rub_vardir1} \t \t \t \t {Style.BRIGHT} [ {Fore.RED}{elem_upper} EXPOSE{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")
                print()
                print(f"{titre_rub_vardir1}{elem}")
                print(point)
                print()
                print(f"\t {com_rub_vardir_rec1}{elem} \t \t \t \t {Style.BRIGHT} [ {Fore.WHITE}{elem_upper} OK{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")
            else:
                textajouter = titre_rub_vardir + elem + "\n"
                ajouterAurapport(textajouter)
                textajouter = point + "\n \n"
                ajouterAurapport(textajouter)
                textajouter = "\t" + elem + com_rub_vardir_rec1 + elem + "\n"
                ajouterAurapport(textajouter)
                print(f"\t {elem} {com_rub_vardir1} \t \t \t \t  {Style.BRIGHT} [ {Fore.RED}{elem_upper} EXPOSE{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")
                print()
                print(f"{titre_rub_vardir1}{elem}")
                print(point)
                print()
                print(f"\t {elem} {com_rub_vardir1} \t \t \t \t {Style.BRIGHT} [ {Fore.RED}{elem_upper} EXPOSE{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")

#### Vérifier que le répertoire /home soit monté avec les bonnes options
def verif_home():
    for elem in point_test4:
        elem_upper = str(elem).upper()
        ismount = os.path.ismount(elem)
        if ismount == False: 
            textajouter = titre_rub_home0 + elem + "\n"
            ajouterAurapport(textajouter)
            textajouter = point + "\n \n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + elem + com_rub_home0 + "\n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + com_rub_home1 + elem + "\n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + titre_remediation + elem + "\n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + point + "\n \n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + elem + com_rub_home_rec0 + "\n"
            ajouterAurapport(textajouter)
            print(titre_rub_home0 + elem)
            print(point)
            print()
            print(f"\t {elem}{com_rub_home0} \t \t \t \t {Style.BRIGHT} [ {Fore.RED}{elem_upper} EXPOSE{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}") 
            print(f"\t {com_rub_home1} \t \t \t {Style.BRIGHT} [ {Fore.RED}{elem_upper} EXPOSE{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")
        isverify = os.popen("mount | grep -E " "%s"%elem).read()
        ecrireFichier(isverify)
        if os.path.getsize(fichierContenu) == 0:
            textajouter = titre_rub_home1 + elem + "\n"
            ajouterAurapport(textajouter)
            textajouter = point + "\n \n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + com_rub_home2 + elem + "\n"
            ajouterAurapport(textajouter)
            print(titre_rub_home1 + elem)
            print(point)
            print()
            print(f"\t {com_rub_home2}{elem} \t \t \t \t {Style.BRIGHT} [ {Fore.WHITE} OK{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")

#### Vérifier que le bit collant est définit sur les répertoires accéssible en écriture pour tous
def verif_stickyNit():
    isverify = os.popen(r"df --local -P | awk {'if (NR!=1) print $6'} | xargs -I '{}' find '{}' -xdev -type d \( -perm -0002 -a ! -perm -1000 \) 2>/dev/null").read()            
    with open(fichierContenu, "w") as f:
        f.write(isverify.strip())

    with open(fichierContenu, "r") as f:
        # findtext = ""
        if "" in f.read():
            textajouter = titre_rub_sticky_bit + sticky + "\n"
            ajouterAurapport(textajouter)
            textajouter = point + "\n \n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + com_rub_sticky_bit0 + "\n"
            ajouterAurapport(textajouter)
            print(titre_rub_sticky_bit + sticky)
            print(point)
            print()
            print(f"\t {com_rub_sticky_bit0} \t \t \t \t \t {Style.BRIGHT} [{Fore.WHITE} STICKY BIT OK{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")
        else:
            textajouter = titre_rub_sticky_bit + sticky + "\n"
            ajouterAurapport(textajouter)
            textajouter = point + "\n \n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + com_rub_sticky_bit1 + "\n"
            ajouterAurapport(textajouter)
            print(titre_rub_sticky_bit + sticky)
            print(point)
            print()
            print(f"\t {com_rub_sticky_bit1} \t \t \t \t {Style.BRIGHT} [ {Fore.RED}{sticky.upper} EXPOSE{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")

#### Vérification des permission sur le fichier de configuration bootloader.
def verif_bootloader(): 
    isverify = os.popen("stat /boot/grub/grub.cfg").read()
    with open(fichierContenu, "w") as f:
        f.write(isverify.strip())

    with open(fichierContenu, "r") as f:
        findtext = "(0400/-rw-------)"
        if findtext in f.read():
            textajouter = titre_rub_bootloader + bootloader + "\n"
            ajouterAurapport(textajouter)
            textajouter = point + "\n \n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + com_rub_bootloader0 + "\n"
            ajouterAurapport(textajouter)
            print(titre_rub_bootloader + bootloader)
            print(point)
            print()
            print(f"\t {com_rub_bootloader0}{bootloader} \t \t {Style.BRIGHT} [ {Fore.WHITE}{bootloader.upper()} OK{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")
        else:
            textajouter = titre_rub_bootloader + bootloader + "\n"
            ajouterAurapport(textajouter)
            textajouter = point + "\n \n"
            ajouterAurapport(textajouter)
            textajouter = "\t" + com_rub_bootloader1 + bootloader + "\n"
            ajouterAurapport(textajouter)
            print(titre_rub_bootloader + bootloader)
            print(point)
            print()
            print(f"\t {com_rub_bootloader1}{bootloader} \t \t {Style.BRIGHT} [ {Fore.RED}{bootloader.upper()} EXPOSE{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")

#### Vérifier l'authentification en mode single user.
def verif_auth_single_user_mode():
    isverify = os.popen(r"grep ^root:[*\!]: /etc/shadow").read()
    with open(fichierContenu, "w") as f:
        f.write(isverify.strip())
    if os.path.getsize(fichierContenu) == 0:
        textajouter = titre_rub_auth_single_user_mode + "\n"
        ajouterAurapport(textajouter)
        textajouter = point + "\n \n"
        ajouterAurapport(textajouter)
        textajouter = "\t" + com_rub_auth_single_user_mode0 + "\n"
        ajouterAurapport(textajouter)
        print(titre_rub_auth_single_user_mode)
        print(point)
        print()    
        print(f"\t {com_rub_auth_single_user_mode0} \t \t \t {Style.BRIGHT} [ {Fore.WHITE} SINGLE USER MODE OK{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")
    else:
        textajouter = titre_rub_auth_single_user_mode + "\n"
        ajouterAurapport(textajouter)
        textajouter = point + "\n \n"
        ajouterAurapport(textajouter)
        textajouter = "\t" + com_rub_auth_single_user_mode1
        ajouterAurapport(textajouter)
        print(titre_rub_auth_single_user_mode)
        print(point)
        print()  
        print(f"\t {com_rub_auth_single_user_mode1} \t \t \t {Style.BRIGHT} [ {Fore.RED} ROOT PASSWORD{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")

#### Vérifier les options sur /dev/shm.
def verif_dev_shm(): 
    isverify = os.popen(r"mount | grep -E '\s/dev/shm\s' | grep -v nodev").read()
    with open(fichierContenu, "w") as f:
        f.write(isverify.strip())
    if os.path.getsize(fichierContenu) == 0:
        print(titre_rub_dev_shm)
        print(point)
        print()
        textajouter = titre_rub_dev_shm + "\n"
        ajouterAurapport(textajouter)
        textajouter = point + "\n \n"
        ajouterAurapport(textajouter)
        textajouter = "\t" + com_rub_dev_shm0 + dev_shm + "\n"
        ajouterAurapport(textajouter)
        print(f"\t {com_rub_dev_shm0}{dev_shm} \t \t \t \t \t {Style.BRIGHT} [ {Fore.WHITE} OK{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")
    else:
        textajouter = titre_rub_dev_shm
        print(point)
        print()
        ajouterAurapport(textajouter)
        textajouter = point + "\n \n"
        ajouterAurapport(textajouter)
        textajouter = "\t" + com_rub_dev_shm1 + "\n"
        ajouterAurapport(textajouter)
        print(titre_rub_auth_single_user_mode + "\n")
        print(f"\t {com_rub_dev_shm1}{dev_shm} \t \t \t \t \t {Style.BRIGHT} [ {Fore.RED} /DEV/SHM EXPOSE{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")

#### Vérifier la configuration du mot de passe bootloade.
def verif_bootloader_pass(): 
    isverify = os.popen(r'grep "^\s*password" /boot/grub/grub.cfg').read()
    if "password --md5" in isverify or "GRUB2_PASSWORD" in isverify or "set superusers" in isverify or "password_pbkdf2" in isverify:
        textajouter = titre_rub_bootloader_pass + "\n"
        ajouterAurapport(textajouter)
        textajouter = point
        ajouterAurapport(textajouter)
        ajouterAurapport(textajouter)
        textajouter = point + "\n \n"
        ajouterAurapport(textajouter)
        textajouter = "\t" + com_rub_bootloader_pass0 + "\n"
        ajouterAurapport(textajouter)
        print(titre_rub_bootloader_pass)
        print(point)
        print()
        print(f"\t {com_rub_bootloader_pass0} \t \t {Style.BRIGHT} [ {Fore.WHITE} BOOTLOADER OK{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")
    else:
        textajouter = titre_rub_bootloader_pass + "\n"
        ajouterAurapport(textajouter)
        textajouter = point + "\n \n"
        ajouterAurapport(textajouter)
        textajouter = "\t" + com_rub_bootloader_pass1 + "\n"
        ajouterAurapport(textajouter)
        print(titre_rub_bootloader_pass)
        print(point)
        print()
        print(f"\t {com_rub_bootloader_pass1} \t {Style.BRIGHT} [ {Fore.RED} BOOTLOADER EXPOSE{Style.RESET_ALL}{Style.BRIGHT} ]{Style.RESET_ALL}")

# ## Procéder à la réalisation des différnts tests
verif_sys_fichier(point_test)
verif_sys_vfat(point_test_vfat)
test_vardir(point_test_vardir)
verif_home()
verif_stickyNit()
verif_bootloader()
verif_auth_single_user_mode()
verif_dev_shm()
verif_bootloader_pass()

## Processus de génération du rapport en pdf
### Initier la class PDF
class PDF(FPDF):
    # L'entête du pdf
    def header(self):
        # Insertion du logo
        self.image('logo.jpg', 10, 8, 33)
        # Initier la police du document
        self.set_font('Arial', 'B', 15)
        # Initier la position de l'entête et sa couleur
        w = self.get_string_width(title) + 6
        self.set_x((210 - w) / 2)
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50, 50)
        self.cell(w, 9, title, 1, 1, 'C', 1)
        # Alligner le titre du document
        self.cell(50)
        # Inserer un saut de ligne
        self.ln(25)

    # Pied de page du pdf footer
    def footer(self):
        # Positionnement à 1.5 cm du bas de page
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
pdf.set_font("Arial", size = 12) 
pdf.set_left_margin(10)
# Insérer le texte dans le doument pdf 
f = open(fichierRapport, "r") 
for x in f:
    if "[+]" in x or ("---") in x:
        pdf.cell(200, 5, txt = x, ln = 1, align = 'L') 
    else:
        pdf.set_x(10)
        pdf.multi_cell(200, 5, txt = x, align = 'L') 

### Générer le rapport des tests en pdf
pdf.output(fileName) 

## Supprimer les fichier temporaires
suppressionFichier(fichierContenu)
suppressionFichier(fichierRapport)
