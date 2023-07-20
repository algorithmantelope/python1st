class MonContextManager:
    def __enter__(self):
        print("Début du contexte")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Fin du contexte")
        if exc_type is not None:
            print(f"Une exception de type {exc_type} a été levée : 
{exc_value}")
        return False

# Utilisation du context manager personnalisé
with MonContextManager() as cm:
    print("Dans le bloc with")
    raise ValueError("Une erreur s'est produite !")
