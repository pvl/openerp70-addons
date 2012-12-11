# -*- coding: utf-8 -*-
import xmlrpclib
import csv

username = 'admin'
pwd = 'admin'
dbname = 'ddrapeau_project_scrum'

class fontColors(object):
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

sock_common = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/common')
uid = sock_common.login(dbname, username, pwd)
sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/object', allow_none=True)

def delete_lines(model, condition):
    ids_to_delete = sock.execute(dbname, uid, pwd, model, 'search', condition)
    print "ids to delete : ", ids_to_delete
    sock.execute(dbname, uid, pwd, model, 'unlink', ids_to_delete)
    return True

def update_devteam_for_res_users():
    ids_to_update = sock.execute(dbname, uid, pwd, 'res.users', 'search', [])
    sock.execute(dbname, uid, pwd, 'res.users', 'write', ids_to_update, {'scrum_devteam_id': None})

def get_country_id(name):
    country_id = sock.execute(dbname, uid, pwd, 'res.country', 'search', [('name', '=', name)])
    if len(country_id) > 0:
        return country_id[0]
    else:
        return None

# USER
def create_user(fields):
    return sock.execute(dbname, uid, pwd, 'res.users', 'create', fields)

def test_user(vals):
    user_id = create_user(vals)
    if user_id:
        print fontColors.OKGREEN + "OK "+ fontColors.ENDC + "create user with fields ", vals
        return user_id
    else:
        print fontColors.FAIL + "FAILED "+ fontColors.ENDC + "create user with fields ", vals
        return False

# PARTNER
def create_partner(fields):
    return sock.execute(dbname, uid, pwd, 'res.partner', 'create', fields)

def test_partner(vals):
    partner_id = create_partner(vals)
    if partner_id:
        print fontColors.OKGREEN + "OK "+ fontColors.ENDC + "create partner with fields ", vals
        return partner_id
    else:
        print fontColors.FAIL + "FAILED "+ fontColors.ENDC + "create partner with fields ", vals
        return False

# PRODUCT
def create_product_product(fields):
    return sock.execute(dbname, uid, pwd, 'product.product', 'create', fields)

def test_product(fields):
    product_id = create_product_product(fields)
    if product_id:
        print fontColors.OKGREEN + "OK "+ fontColors.ENDC + "create product with fields ", fields
        return product_id
    else:
        print fontColors.FAIL + "FAILED "+ fontColors.ENDC + "create product with fields ", fields
        return False

# PROJECT
def create_project(fields):
    return sock.execute(dbname, uid, pwd, 'project.project', 'create', fields)

def test_project(vals):
    project_id = create_project(vals)
    if project_id:
        print fontColors.OKGREEN + "OK "+ fontColors.ENDC + "create project with vals ", vals
        return project_id
    else:
        print fontColors.FAIL + "FAILED "+ fontColors.ENDC + "create project with vals ", vals
        return False

# RELEASE
def create_release(fields):
    return sock.execute(dbname, uid, pwd, 'project.scrum.release', 'create', fields)

def test_release(vals):
    release_id = create_release(vals)
    if release_id:
        print fontColors.OKGREEN + "OK "+ fontColors.ENDC + "create release with vals ", vals
        return release_id
    else:
        print fontColors.FAIL + "FAILED "+ fontColors.ENDC + "create release with vals ", vals
        return False

# SPRINT
def create_sprint(fields):
    return sock.execute(dbname, uid, pwd, 'project.scrum.sprint', 'create', fields)
    
def test_sprint(vals):
    sprint_id = create_sprint(vals)
    if sprint_id:
        print fontColors.OKGREEN + "OK "+ fontColors.ENDC + "create sprint with vals ", vals
        sprint_line = sock.execute(dbname, uid, pwd, 'project.scrum.sprint', 'read', sprint_id, [])
        print "sprint line created = ", sprint_line
        return sprint_id
    else:
        print fontColors.FAIL + "FAILED "+ fontColors.ENDC + "create sprint with vals ", vals
        return False

# ROLE
def create_role(fields):
    return sock.execute(dbname, uid, pwd, 'project.scrum.role', 'create', fields)
    
def test_role(vals):
    role_id = create_role(vals)
    if role_id:
        print fontColors.OKGREEN + "OK "+ fontColors.ENDC + "create role with vals ", vals
        return role_id
    else:
        print fontColors.FAIL + "FAILED "+ fontColors.ENDC + "create role with vals ", vals
        return False

# USER STORY DONE
def create_scrum_done(fields):
    return sock.execute(dbname, uid, pwd, 'project.scrum.done', 'create', fields)
    
def test_scrum_done(vals):
    role_id = create_scrum_done(vals)
    if role_id:
        print fontColors.OKGREEN + "OK "+ fontColors.ENDC + "create role with vals ", vals
        return role_id
    else:
        print fontColors.FAIL + "FAILED "+ fontColors.ENDC + "create role with vals ", vals
        return False

# PRODUCT BACKLOG
def create_product_backlog(fields):
    return sock.execute(dbname, uid, pwd, 'project.scrum.product.backlog', 'create', fields)
    
def test_product_backlog(vals):
    user_story_id = create_product_backlog(vals)
    if user_story_id:
        print fontColors.OKGREEN + "OK "+ fontColors.ENDC + "create user story with vals ", vals
        return user_story_id
    else:
        print fontColors.FAIL + "FAILED "+ fontColors.ENDC + "create user story with vals ", vals
        return False
    
# DEV TEAM
def create_devteam(fields):
    return sock.execute(dbname, uid, pwd, 'project.scrum.devteam', 'create', fields)
    
def test_devteam(vals):
    devteam_id = create_devteam(vals)
    if devteam_id:
        print fontColors.OKGREEN + "OK "+ fontColors.ENDC + "create Devteam with vals ", vals
        return devteam_id
    else:
        print fontColors.FAIL + "FAILED "+ fontColors.ENDC + "create Devteam with vals ", vals
        return False
  

print "delete daily meetings..."
delete_lines('project.scrum.meeting', [])

print "delete user stories..."
delete_lines('project.scrum.product.backlog', [])

print "delete done steps..."
delete_lines('project.scrum.done', [])

print "delete roles..."
delete_lines('project.scrum.role', [])

print "delete sprints..."
delete_lines('project.scrum.sprint', [])

print "delete releases..."
delete_lines('project.scrum.release', [])

print "delete tasks of projects..."
delete_lines('project.task', [])

print "delete projects..."
delete_lines('project.project', [])

print "delete products..."
delete_lines('product.product', [])

print "delete partners..."
delete_lines('res.partner', [('id', '>', 2)])

print "delete addresses..."
delete_lines('res.partner.address', [('id', '>', 2)])

print "delete mail alias..."
delete_lines('mail.alias', [('id', '>', 2)])

#NOTE Do not delete res_users because deleted by mail.alias with DELETE ON CASCADE
#print "delete users..."
#delete_lines('res.users', [('id', '>', 2)])

print "delete devteam..."
delete_lines('project.scrum.devteam', [])



print "=========================="
print "===== TESTS STARTING ====="

print "create devteam..."
devteam_vals = {
    'name': "team 01",
    'code': "TEAM01",
    'active':True,
}
devteam01_id = test_devteam(devteam_vals)

print "create partners..."
partner_vals = {
    'name': "Client 001",
    'is_company':True,
    'lang': 'fr_FR',
    'type': 'default',
    'employee': False,
    'supplier': False,
    'customer': True,
    'active': True,
    'country_id': get_country_id('France'),
}
partner_id = test_partner(partner_vals)

print "create products..."
product_id = test_product({'name': "product 001"})

print "create user with role 'Product Owner'..."
group_po_id = sock.execute(dbname, uid, pwd, 'res.groups', 'search', [('name', '=', 'Product Owner')])
PO01_id = test_user({'name': "Product Owner 01", 'login': "po01", 'password': "a", 'lang': "fr_FR", 'groups_id': [(6, 0, group_po_id)]})
PO02_id = test_user({'name': "Product Owner 02", 'login': "po02", 'password': "a", 'lang': "fr_FR", 'groups_id': [(6, 0, group_po_id)]})

print "create user with role 'Scrum Master'..."
group_sm_id = sock.execute(dbname, uid, pwd, 'res.groups', 'search', [('name', '=', 'Scrum Master')])
scrum_master_id = test_user({'name': "Scrum Master", 'login': "sm", 'password': "a", 'lang': "fr_FR", 'groups_id': [(6, 0, group_sm_id)]})

print "create user with role 'Developer'..."
group_dev_id = sock.execute(dbname, uid, pwd, 'res.groups', 'search', [('name', '=', 'Developer')])
developer01_id = test_user({'name': "Developer 01", 'login': "dev01", 'password': "a", 'lang': "fr_FR", 'scrum_devteam_id': devteam01_id, 'groups_id': [(6, 0, group_dev_id)]})

print "create projects..."
project01_id = test_project({'name': "project 001",'product_owner_id': PO01_id, 'vision' : "ceci est la vision du projet 1"})
project02_id = test_project({'name': "project 002",'product_owner_id': PO02_id, 'vision' : "ceci est la vision du projet 1"})
project03_id = test_project({'name': "project 003",'product_owner_id': PO02_id, 'vision' : "ceci est la vision du projet 1"})
project04_id = test_project({'name': "project 004",'product_owner_id': PO01_id, 'vision' : "ceci est la vision du projet 1"})

print "create releases..."
release001_id = test_release({'name':"release 001", 'project_id':project01_id})


print "create sprints..."
sprint_vals = {
    'name': "sprint 001",
    'release_id': release001_id,
    'date_start':'2012-11-06',
    'date_stop':'2012-11-16',
    'product_owner_id': PO01_id,
    'scrum_master_id': scrum_master_id,
    'scrum_devteam_id': devteam01_id,
    'sprint_goal':"Premiere approche"
}
sprint01_id = test_sprint(sprint_vals)

sprint_vals = {
    'name': "sprint 002",
    'release_id': release001_id,
    'date_start':'2012-11-06',
    'date_stop':'2012-11-16',
    'product_owner_id': PO01_id,
    'scrum_master_id': scrum_master_id,
    'scrum_devteam_id': devteam01_id
}
sprint02_id = test_sprint(sprint_vals)

print "create scrum done steps..."
scrum_done_value_step1 = {
    'name': "Draft",
    'code': 'draft',
    'project_id': project01_id,
    'sequence': 1,
}
scrum_done_step01_id = test_scrum_done(scrum_done_value_step1)

scrum_done_value_step2 = {
    'name': "Todo",
    'code': 'todo',
    'project_id': project01_id,
    'sequence': 2,
}
scrum_done_step02_id = test_scrum_done(scrum_done_value_step2)

scrum_done_value_step3 = {
    'name': "In progress",
    'code': 'in_progress',
    'project_id': project01_id,
    'sequence': 3,
}
scrum_done_step03_id = test_scrum_done(scrum_done_value_step3)

scrum_done_value_step4 = {
    'name': "Done",
    'code': 'done',
    'project_id': project01_id,
    'sequence': 4,
}
scrum_done_step04_id = test_scrum_done(scrum_done_value_step4)



print "create roles..."
scrum_role_id = test_role({'name':"role 01", 'code': "SR01"})

print "create user stories..."
user_story_vals = {
    'role_id': scrum_role_id,
    'name': "create a group Cogitae",
    'for': "Describe rights for this role",
    'project_id': project01_id,
    'release_id': release001_id,
    'scrum_done_id': scrum_done_step01_id,
}
user_story_id = test_product_backlog(user_story_vals)



