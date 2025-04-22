class DatabaseRouter:
    def db_for_read(self, model, **hints):
        """Point specific models to specific databases."""
        if model._meta.app_label == 'main':  # Store users in MySQL
            return 'default'
        if model._meta.app_label == 'side':  # Store song data in MongoDB
            return 'mongo'
        return None

    def db_for_write(self, model, **hints):
        """Point specific models to specific databases."""
        return self.db_for_read(model, **hints)

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relations if models are in the same database."""
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure migrations are directed properly."""
        if app_label == 'main':  # User models in MySQL
            return db == 'defult'
        if app_label == 'side':  # Song models in MongoDB
            return db == 'mongo'
        return None

