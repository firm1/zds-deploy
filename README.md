# zds-deploy

Dépot de déploiement d'une branche du projet zds-site sur des conteneurs docker.

## Prerequis

Pour lancer les outils il que les outils suivants soient installés:

- docker
- docker-compose


## Utilisation

### Mode simple

Le mode simple permet de déployer le minimum sur ZdS, pas de recherche, pas de génération d'epub, pdf, etc. 


Pour le déployer:

```bash
./build.py --user=<git_user> --branch=<git_branch>
```

Exemple (pour déployer la branche dev de zestedesavoir)

```bash
./build.py --user=zestedesavoir --branch=dev
```

En cas de problème lors du démarrage des containers, il est aussi possible de faire

```bash
make zds-start-lite
```

Pour démarrer les containers.

### Mode complet

Le mode complet permet de déployer toute la stack de ZdS, module recherche, et génération d'epub, pdf, etc. 

Pour le déployer :

```bash
./build.py --user=<git_user> --branch=<git_branch> --full
```

Exemple (pour déployer la branche dev de zestedesavoir)

```bash
./build.py --user=zestedesavoir --branch=dev --full
```

En cas de problème lors du démarrage des containers, il est aussi possible de faire

```bash
make zds-start-full
```

Pour démarrer les containers.

## Technologies

- Base de donnée : MySQL
- Système de cache : memcached
- Moteur d'indexation : elasticsearch
- Moteur de génération de pdf : Latex