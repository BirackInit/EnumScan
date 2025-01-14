# EnumScan : Network Scanning Tool

Un outil de scan réseau basé sur nmap pour détecter les hôtes actifs, scanner les ports et détecter les versions de service.

## Prérequis
- Python 3.6 ou plus récent
- `nmap` installé sur le système (nécessaire pour la bibliothèque `python-nmap`)

## Installation
1. Clonez le dépôt :
   ```bash
   https://github.com/BirackInit/EnumScan.git
   cd EnumScan
   
2. Installez les dépendances Python :
   ```bash
   python3 -m venv env
   source env/bin/activate
   pip3 install -r requirements.txt

- Lancez votre script pour vérifier son bon fonctionnement :  :
  ```bash
   python3 EnumScan.py
  
## Possibilités :

    --help, -h : Afficher l'aide
    1 : Scanner les hôtes actifs
    2 : Scanner des ports spécifiques
    3 : Détecter les versions de service 

    
