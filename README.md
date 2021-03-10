# Projet AIC - Analyse des récommandations du CIS

## The repository 

Ce référentiel contient le code du projet mais pas que, il permet de remonter les différents problèmes liés au fonctionnement du code et  d'y contribuer. Dépuis cet espace, nous publiuons les différents plans d'évolution et des axes d'améliorations. Ce code est entièrement sous Licence Apache 2.0.

## The script

CheckPoint.py est un code qui permet d'analyser selon les recommandation du du [CIS][1] certains point de configuraton sur les systèmes Linux  en x86 et x64 et de fournir des conseils normatifs pour l'établissement d'une configuration sécurisée. 

L'analyse effectuer par le script inclut celles sur les types de systèmes de fichier, des services, des clients et des protocols réseau. Afin depermettre un test efficace et des sorties en corélation avec l'état du système analysé, ce script doit être lancé sous l'utilisateur root >> root@machine~# et non pas avec sudo python3 CheckPoint.py .

## Requierment

  * python3
  * module suprocess
  * module colorama
  * module textwrap
  * module fpdf

## Clone the repository

Pour utiliser ce script vous pouvez le clonner avec les commandes suivantes

```bash
$ cd ~/home/user
$ git clone git@github.com:gabarchinco/projetAIC.git
```
## Usage

Pour lancer le script, il est recommandé de le lanceer sous l'utilisateur root afin d'éviter les erreurs de sortie.

```bash
$ cd projetAIC
$ sudo -s
$ root@xxx:/homa/user/projetAIC# python3 CheckPoint.py
```


[1]: https://www.cisecurity.org/
