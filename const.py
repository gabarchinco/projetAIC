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
first_page = '''Ce rapport d'audit est automatiquement généré suite au lancement du programme CheckPoint.py . Il est conçu afin d'aider à la mise en place de configuration sécurisé respectant au mieux les recommandations du CIS. 

Pour ce faire, le programme CheckPoint.py permet la réalisation d'un ensemble de test de sécurité sur les systèmes Linux en x86 et x64 afin de fournir des conseils normatifs pour l'établissement d'une configuration sécurisée.

Plusieurs points de contrôle sont effectués notamment sur les systèmes de fichier, des services, des clients et des protocoles réseau. Chaque point de contrôle fournit un ou plusieurs résultat en fonction de la configuration du système sur lequel ce test est réalisé. 

Les rubriques des tests sont composés de quatres sections : le test réalisé, la description, les résultats de test et en fin les recommandations. 

Le test réalisé est indiqué par un titre commençant par l'indication [+]. Il est assez évocateur pour plus de lisibilité. Les résultats de test, quant à eux, sont les interprétations des retours des processus de test opéré sur l'état d'un ou de plusieurs points de test. Enfin , les recommandations, comme leur nom l'indique, elles constituent les propositions de remédiations aux résultats différents de ceux du CIS.

Toutefois, les résultats des tests doivent être analysés dans le contexte global de votre système et de la politique de sécurité mise en place par votre entité. Ensuite, il doivent être analyser par point de référencement afin d'appliquer les recommandations de sécurité qui sont nécéssaires aux exigences de votre environne
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
point = "######################################################"

### Résultats des tests
titre_result_test = "Résultat de test"
uderline_result = "--------------------"
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

### Descriptions
titre_description = "Description \n"
uderline_description = "-----------------"

description_cramfs = """Le système de fichiers cramfs est un système de fichiers Linux compressé en lecture seule intégré dans de petits systèmes d'empreinte. Une image cramfs peut être utilisée sans avoir à décompresser au préalable l'image.
""" 

description_freevxfs = """Le type de système de fichiers freevxfs est une version gratuite du système de fichiers de type Veritas. Il s'agit du type de système de fichiers principal pour les systèmes d'exploitation HP-UX.
""" 

description_jffs2 = """Le type de système de fichiers jffs2 (système de fichiers flash journalisé 2) est un système de fichiers de journalisation structuré utilisé dans les périphériques de mémoire flash.
"""

description_hfs = """Le type de système de fichiers hfs est un système de fichiers hiérarchique qui vous permet de monter des systèmes de fichiers Mac OS.
"""

description_hfsplus = """Le type de système de fichiers hfsplus est un système de fichiers hiérarchique conçu pour remplacer hfs qui vous permet de monter des systèmes de fichiers Mac OS.
"""

description_udf = """Le type de système de fichiers udf est le format de disque universel utilisé pour implémenter les spécifications ISO / CEI 13346 et ECMA-167. Il s'agit d'un type de système de fichiers de fournisseur ouvert pour le stockage de données sur une large gamme de supports. Ce type de système de fichiers est nécessaire pour prendre en charge l'écriture de DVD et les nouveaux formats de disque optique.
"""

description_squashfs = """Le type de système de fichiers squashfs est un système de fichiers Linux compressé en lecture seule intégré dans des systèmes à faible encombrement (similaire à cramfs). Une image squashfs peut être utilisée sans avoir à décompresser l'image au préalable.
"""

### Récommandations sur les tests
com_rub_file_sys_rec = """

"""
