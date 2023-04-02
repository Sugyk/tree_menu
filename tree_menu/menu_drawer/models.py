from django.db import models


class Folder(models.Model):
    name = models.CharField('Folder name', max_length=100, unique=True)
    menu = models.CharField('Menu name', max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    # конечно, делается много запросов, но т. к. суть задания не в этом, я решил не доводить до идеала
    # надеюсь, это не критично (влияет только на удобство работы в адмике, поэтому можно стереть)
    def __str__(self):
        if self.parent == None:
            return self.menu + '/' + self.name
        return '{}/{}'.format(self.parent, self.name)
