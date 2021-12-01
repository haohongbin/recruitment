# settings/router.py
# database router to multiple database by app label

# 这里面定义了数据库表的路由
class DatabaseRouter:
    # 应用的label
    route_app_labels = {'running'}

    def db_for_read(self, model, **hints):
        """
        对于特定的model，进行读操作时访问哪个数据库
        :param model:
        :param hints:
        :return:
        """
        if model._meta.app_label in self.route_app_labels:
            return 'running'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'running'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        是否允许表之间有关系
        :param obj1:
        :param obj2:
        :param hints:
        :return:
        """
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        遗留数据库中的表不允许迁移
        """
        if app_label in self.route_app_labels:
            return False
        return True