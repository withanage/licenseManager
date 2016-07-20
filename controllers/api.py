# -*- coding: utf-8 -*-
def licenses():
    import gluon.contrib.simplejson
    if len(request.args) == 0:
        licenses = {}
    else:
        table = db.t_licenses
        licenses = db(table.id == request.args[0]).select().first().as_dict()

    return gluon.contrib.simplejson.dumps(licenses)
