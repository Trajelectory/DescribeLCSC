# DescribeLCSC

## Description

Ce projet propose un script Python qui permet d'enrichir un fichier CSV contenant des références de composants LCSC en ajoutant automatiquement les liens vers les datasheets et les descriptions correspondantes. L'utilisateur fournit le chemin vers le fichier CSV à modifier, et le script génère un nouveau fichier `output.csv` dans le même répertoire avec les informations supplémentaires.

## Installation et Configuration

### 1️⃣ Prérequis

Avant d'utiliser ce script, assurez-vous d'avoir installé les éléments suivants :

- **Python 3.8+** : [Télécharger ici](https://www.python.org)
- **pip** : Gestionnaire de paquets Python (généralement inclus avec Python)

### 2️⃣ Cloner le dépôt

Clonez ce dépôt GitHub sur votre machine locale :

```bash
git clone https://github.com/votre-utilisateur/describeLCSC.git
cd describeLCSC
```

### 3️⃣ Installer les dépendances Python

Installez les dépendances requises avec la commande suivante :

```bash
pip install -r requirements.txt
```

## Utilisation

1. **Préparation du fichier CSV** : Assurez-vous que votre fichier CSV contient une colonne intitulée `LCSC` ou `LCSC Part` avec les numéros de pièces correspondants.

2. **Exécution du script** : Lancez le script en exécutant la commande suivante dans votre terminal :

   ```bash
   python describeLCSC.py
   ```

   Le script vous demandera d'entrer le chemin du fichier CSV à modifier. Après traitement, un fichier `output.csv` sera créé dans le même répertoire que le fichier d'entrée, contenant les colonnes supplémentaires `Datasheet` et `Description`.

## Exemple de fichier CSV

### Fichier d'entrée (`input.csv`)

| LCSC   | Nom               | Quantité |
|--------|------------------|----------|
| C12345 | Résistance 10k   | 100      |
| C67890 | Condensateur 1uF | 50       |

### Fichier de sortie (`output.csv`)

| LCSC   | Nom               | Quantité | Datasheet                                 | Description                        |
|--------|------------------|----------|------------------------------------------|------------------------------------|
| C12345 | Résistance 10k   | 100      | https://datasheet.example.com/12345     | Résistance 10kΩ 1%                |
| C67890 | Condensateur 1uF | 50       | https://datasheet.example.com/67890     | Condensateur céramique 1µF 50V    |

## Remarques

- Si un composant n'est pas trouvé ou si une erreur survient lors de la récupération des données, les colonnes `Datasheet` et `Description` contiendront le message d'erreur correspondant.

- Le script gère les colonnes `LCSC` et `LCSC Part` pour identifier les numéros de pièces. Assurez-vous que votre fichier CSV contient l'une de ces colonnes.

## Auteur

Ce script a été développé pour faciliter l'enrichissement des fichiers CSV de composants en automatisant la récupération des informations depuis la plateforme LCSC.

