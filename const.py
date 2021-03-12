### Variables constantes

point_test = ["cramfs", "freevxfs", "jffs2", "hfs", "hfsplus", "udf", "squashfs"]
point_test_vfat = ["vfat"]
point_test_vardir = ["/tmp", "/var", "/var/tmp", "/var/log", "/var/log/audit"]
point_test_home = ["/home"]
sticky = "sticky bit"
bootloader = "/boot/grub/grub.cfg"
dev_shm = "/dev/shm"

################### Les fichiers temporaires ##########################

fichierContenu = "contenu.txt"
fichierRapport = "rapport.txt"
rep__pycache__ = "__pycache__"

### Context d'application 
context = "Context"
first_page = '''Ce rapport est automatiquement généré suite aux lancement du script CheckPoint.py . Ce script est conçu selon les recommandation du CIS afin de réaliser un ensemble de test de sécurité sur les systèmes Linux x86 et x64 afin de fournir des conseils normatifs pour l'établissement d'une configuration sécurisée.

Plusieurs points de contrôle sont effectués notamment sur les systèmes de fichier, des services, des clients et des protocoles réseau. Chaque point de contrôle fournit un ou plusieurs résultat en fonction de la configuration du systèmes sur lequel est réalisé ce test. 

Les rubrique de test sont composé d'un titre de rubrique en rapport avec le test effectué pour plus de cohérence, du résultat de test et des recommandations de paramétrages ou de configurations à mettre en place pour sécuriser votre configuration.

Les résultats des test doivent être analysés dans le contexte global de votre système et de la politique de sécurité mise en place par votre entité. Ensuite, il doivent être analyser par point de référencement afin d'appliquer les recommandations de sécurité.
'''

### Titre des rubriques des différents tests

titre_rub_file_sys = " \n [+] Test sur la désactivation du sytème de fichier "
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

### Résultats des tests

com_rub_file_sys0 = "Test réussi sur le système de fichier "
com_rub_file_sys1 = "Test réussi sur les options de montage de "
com_rub_file_sys2 = "Risque potentiel sur le système de fichier "
com_rub_vfat0 = "Test réussi sur le système de fichier "
com_rub_vfat1 = "Il y a un risque potentiel sur le système de fichier "
com_rub_vardir0 = " n'est pas monter sur une partition séparée "
com_rub_vardir1 = "Il y a u risque potentiel sur le montage de la partition "
com_rub_vardir_rec0 = " doit être monter dans le fichier /etc/fstab avec ces options : defaults,rw,nosuid,nodev,noexec,relatime 0 0"
com_rub_vardir_rec1 = "Test réussi sur les options de montage du fichier "
com_rub_home0 = " n'est pas monter sur une partition séparée "
com_rub_home1 = "Il y a un risque potentiel sur le système de fichiere "
com_rub_home2 = "Test réussi sur les options de montage de "
com_rub_home_rec0 = " doit être monter dans le fichier /etc/fstab avec ces options : /home type ext4 (rw,nodev,relatime,data=ordered)"
com_rub_sticky_bit0 = "Test réussi sur la définition du bit collant "
com_rub_sticky_bit1 = "Il y a un risque potentiel sur l'assignation du bit collant "
com_rub_bootloader0 = "Test réussi sur permissions du fichier "
com_rub_bootloader1 = "Il y a un risque potentiel sur les permissions de "
com_rub_bootloader_rec = " doit être monter avec ces options : Access: (0400/-r--------) Uid: (0/ root) Gid: ( 0/ root)"
com_rub_auth_single_user_mode0 = "Test réussi sur l'authentification du mode single user "
com_rub_auth_single_user_mode1 = "Il y a un risque potentiel sur l'authentification du mode single user "
com_rub_dev_shm0 = "Test réussi sur les options de "
com_rub_dev_shm1 = "Il y a un risque potentiel sur les options de "
com_rub_bootloader_pass0 = "Test réussi sur la configuration du mot de passe bootloader "
com_rub_bootloader_pass1 = "Il y a un risque potentiel sur la configuration du mot de passe bootloader "
com_rub_bootloader_pass_rec = ""

### Récommandations sur les tests


