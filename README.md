# Projet AIC - Analyse des recommandations du CIS

## The repository 

Ce référentiel contient le code du projet mais pas que, il permet de remonter les différents problèmes liés au fonctionnement du code et  d'y contribuer. Depuis cet espace, nous publiuons les différents plans d'évolution et des axes d'améliorations. Ce code est entièrement sous Licence Apache 2.0.

## The script

CheckPoint.py est un code qui permet d'analyser selon les recommandations du du [CIS][1] certains points de configuration sur les systèmes Linux  en x86 et x64 et de fournir des conseils normatifs pour l'établissement d'une configuration sécurisée. 

L'analyse effectué par le script inclut celles sur les types de systèmes de fichier, des services, des clients et des protocoles réseau. Afin de permettre un test efficace et des sorties en corrélation avec l'état du système analysé, ce script doit être lancé sous l'utilisateur root >> root@machine~# et non pas avec sudo python3 CheckPoint.py .

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

Pour lancer le script, il est recommandé de le lancer sous l'utilisateur root afin d'éviter les erreurs de sortie.

```bash
$ cd projetAIC
$ sudo -s
$ root@xxx:/homa/user/projetAIC# python3 CheckPoint.py
```


[1]: https://www.cisecurity.org/
