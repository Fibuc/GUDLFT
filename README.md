# English

## gudlift-registration

1. **Why**


    This is a proof of concept (POC) project to show a light-weight version of our competition booking platform. The aim is the keep things as light as possible, and use feedback from the users to iterate.

2. **Getting Started**

    This project uses the following technologies:

    * Python v3.x+

    * [Flask](https://flask.palletsprojects.com/en/1.1.x/)

        Whereas Django does a lot of things for us out of the box, Flask allows us to add only what we need. 
     

    * [Virtual environment](https://virtualenv.pypa.io/en/stable/installation.html)

        This ensures you'll be able to install the correct packages without interfering with Python on your machine.

        Before you begin, please ensure you have this installed globally. 


3. **Installation**

    - After cloning, change into the directory and type <code>virtualenv .</code>. This will then set up a a virtual python environment within that directory.

    - Next, type <code>source bin/activate</code> _(for windows <code>script/activate.bat</code>)_. You should see that your command prompt has changed to the name of the folder. This means that you can install packages in here without affecting affecting files outside. To deactivate, type <code>deactivate</code>

    - Rather than hunting around for the packages you need, you can install in one step. Type <code>pip install -r requirements.txt</code>. This will install all the packages listed in the respective file. If you install a package, make sure others know by updating the requirements.txt file. An easy way to do this is <code>pip freeze > requirements.txt</code>

    - Flask requires that you set an environmental variable to the python file. However you do that, you'll want to set the file to be <code>server.py</code>. Check [here](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application) for more details

    - You should now be ready to test the application. In the directory, type either <code>flask run</code> or <code>python -m flask run</code>. The app should respond with an address you should be able to go to using your browser. You can also use <code>python server.py</code> to run server in debug mode.

4. **Current Setup**

    - The app is powered by [JSON files](https://www.tutorialspoint.com/json/json_quick_guide.htm). This is to get around having a DB until we actually need one. The main ones are:
     
        * competitions.json - list of competitions
        * clubs.json - list of clubs with relevant information. You can look here to see what email addresses the app will accept for login.

    - To comply with Python conventions, we use the snake_case naming convention.

    - All tests must be organized by their nature in their respective folders within the parent `tests/` directory.

    - Utility functions for the application should be separated from the `server.py` file. These should be created in the `utils.py` file and imported later into your chosen module.


5. **Testing**

    In this project, we use the pytest testing module coupled with pytest-flask for unit and integration tests, as well as Locust for performance testing.

    - To run unit and integration tests, you need to go to the root folder and execute the command <code>pytest tests/</code>.

    - To check the test coverage, you should run the command <code>pytest --cov=. --cov-report=html tests/</code>. This will create an htmlcov folder in the root of the project where you can check the coverage by opening index.html. **Please do not include the coverage folder in the repository.**

    - To perform performance tests, simply navigate to the ./tests/performance_tests folder and execute the command <code>locust</code>. Note that performance tests require the server to be started beforehand. Note: The default number of users during the test is 6.


6. **Linter**

    We use the `flake8` module as a linter.

    - To perform a code check, you can run the command <code>flake8</code> in the root folder of the project.

    - To generate an HTML report, run the command <code>flake8 --format=html --htmldir=flake8_report</code>. This will create a folder called `flake8_report`. **Please do not include the linter report in the repository.**


# Français

## gudlift-registration

1. **Pourquoi**

    Il s'agit d'un projet de preuve de concept (POC) pour montrer une version allégée de notre plateforme de réservation de compétitions. L'objectif est de garder les choses aussi légères que possible et d'utiliser les retours des utilisateurs pour itérer.

2. **Commencer**

    Ce projet utilise les technologies suivantes :

    * Python v3.x+

    * [Flask](https://flask.palletsprojects.com/en/1.1.x/)

        Alors que Django fait beaucoup de choses pour nous dès le départ, Flask nous permet d'ajouter uniquement ce dont nous avons besoin. 
     
    * [Environnement virtuel](https://virtualenv.pypa.io/en/stable/installation.html)

        Cela garantit que vous pourrez installer les bons packages sans interférer avec Python sur votre machine.

        Avant de commencer, veuillez vous assurer que vous l'avez installé globalement. 

3. **Installation**

    - Après avoir cloné le dépôt, changez de répertoire et tapez <code>virtualenv .</code>. Cela configurera un environnement python virtuel dans ce répertoire.

    - Ensuite, tapez <code>source bin/activate</code> _(pour windows <code>script/activate.bat</code>)_. Vous devriez voir que votre invite de commande a changé pour afficher le nom du dossier. Cela signifie que vous pouvez installer des packages ici sans affecter les fichiers en dehors. Pour désactiver, tapez <code>deactivate</code>.

    - Plutôt que de chercher les packages dont vous avez besoin, vous pouvez tout installer en une seule étape. Tapez <code>pip install -r requirements.txt</code>. Cela installera tous les packages listés dans le fichier respectif. Si vous installez un package, assurez-vous d'en informer les autres en mettant à jour le fichier requirements.txt. Une façon simple de le faire est <code>pip freeze > requirements.txt</code>.

    - Flask nécessite que vous définissiez une variable d'environnement pour le fichier python. Peu importe comment vous le faites, vous voudrez définir le fichier sur <code>server.py</code>. Consultez [ici](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application) pour plus de détails.

    - Vous devriez maintenant être prêt à tester l'application. Dans le répertoire, tapez soit <code>flask run</code> soit <code>python -m flask run</code>. L'application devrait répondre avec une adresse à laquelle vous devriez pouvoir accéder via votre navigateur. Vous pouvez également utiliser <code>python server.py</code> pour exécuter le serveur en mode débogage.

4. **Configuration actuelle**

    - L'application est alimentée par des [fichiers JSON](https://www.tutorialspoint.com/json/json_quick_guide.htm). Cela permet de contourner le besoin d'une base de données jusqu'à ce que nous en ayons réellement besoin. Les principaux fichiers sont :
     
        * competitions.json - liste des compétitions
        * clubs.json - liste des clubs avec les informations pertinentes. Vous pouvez consulter ce fichier pour voir quelles adresses email l'application acceptera pour la connexion.

    - Pour se conformer aux conventions Python, nous utilisons la convention de nommage snake_case.

    - Tous les tests doivent être classés selon leur nature dans leur dossier respectif présents dans le dossier parent `tests/`.

    - Les fonctions utilitaires à l'application doivent être séparées du fichier `server.py`. Celles-ci doivent être créées dans le fichier `utils.py` et importées par la suite dans le module de votre choix.


5. **Tests**

    Dans ce projet, on utilise le module de test pytest couplé avec pytest-flask pour les tests unitaires et d'intégration ainsi que locust pour les tests de performance.

    - Pour exécuter les tests unitaires et les tests d'intégration, vous devez vous rendre dans le dossier racine et lancer la commande <code>pytest tests/</code>.

    - Pour vérifier la couverture de test, vous devez effectuer la commande <code>pytest --cov=. --cov-report=html tests/</code>. Cela vous créera un dossier htmlcov dans le dossier racine du projet dans lequel vous pouvez vérifier le coverage en ouvrant index.html. **Merci de pas inclure le dossier de la couverture dans le dépôt.**

    - Pour réaliser les tests de performance, il vous suffit de vous rendre dans le dossier ./tests/performance_tests et d'effectuer la commande <code>locust</code>. Attention, les tests de performances nécessitent le lancement du serveur préalablement. A noter: Le nombre par défaut d'utilisateur lors de la réalisation du test est de 6.


6. **Linter**

    Nous utilisons comme linter le module `flake8`.

    - Pour effectuer un contrôle du code, vous pouvez effectuer la commande <code>flake8</code> dans le dossier racine du projet.

    - Pour effectuer générer un rapport html, effectuez la commande <code>flake8 --format=html --htmldir=flake8_report</code>. Cela génèrera un dossier `flake8_report`. **Merci de ne pas inclure le rapport du linter dans le dépôt.**
