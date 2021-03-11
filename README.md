# Projet AIC - Analyse des recommandations du CIS

## The repository 

Ce référentiel contient le code du projet mais pas que, il permet de remonter les différents problèmes liés au fonctionnement du code et également d'y contribuer. Depuis cet espace, nous publiions les différents plans d'évolution et des axes d'améliorations. Ce code est entièrement sous Licence Apache 2.0.

## Le CIS

Le CIS est le Center pour la Sécurité d’Internet. Son objectif est de faire d’Internet un endroit plus sûr pour les personnes, les entreprises et les gouvernements grâce à des compétences fortes en matière de collaboration et d'innovation.

C’est une organisation à but non lucratif dirigée par une communauté qui s’occupe du CIS Controls® et du CIS Benchmarks ™, qui met en place des pratiques et des normes mondialement reconnues pour la sécurisation des systèmes et des données informatiques. Le CIS dirige une communauté mondiale de professionnels de l'informatique pour faire évoluer en permanence ces normes standardisées et fournir des produits et services pour se protéger de manière proactive contre les menaces émergentes. Le CIS Hardened Images® fournissent des environnements informatiques sécurisés, à la demande et évolutifs dans le cloud.

Le CIS abrite plusieurs centre dont le Multi-State Information Sharing and Analysis Center® (MS-ISAC®) et le Elections Infrastructure Information Sharing and Analysis Center® (EI-ISAC®), qui prend en charge l'évolution rapide des besoins en matière de cybersécurité des bureaux électoraux américains.

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
