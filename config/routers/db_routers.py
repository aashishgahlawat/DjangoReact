# class LocationRouter:
#     # location is the app we will be using to find nearby businesses
#     route_app_label = {'location', }
#
#     def db_for_read(self, model, **hints):
#         if model.__meta.app_label in self.route_app_label:
#             return 'postgres'
#         return None
#
#     def db_for_write(self, model, **hints):
#         if model.__meta.app_label in self.route_app_label:
#             return 'postgres'
#         return None
#
#     def allow_relation(self, obj1, obj2, **hints):
#         if(
#             obj1.__meta.app_label in self.route_app_label or
#             obj2.__meta.app_label in self.route_app_label
#         ):
#             return True
#         return False
#
#     def allow_migrations(self, db, app_label, model_name=None, **hints):
#         if app_label in self.route_app_label:
#             return db == 'postgres'
#         return None
#
