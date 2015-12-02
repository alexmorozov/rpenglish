# --coding: utf8--


from kupola.fabric_class import DjangoFabric,\
    add_class_methods_as_functions


class Fabric(DjangoFabric):
    host = 'localhost'
    app_name = 'rpenglish'
    repository = 'git@repo.kupo.la:kupola/rpenglish.git'
    remote_db_name = 'rpenglish'
    local_db_name = 'rpe_i'
    use_bower = True


__all__ = add_class_methods_as_functions(Fabric(), __name__)
