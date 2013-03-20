#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import bottle
import uuid
import user
import counters
import datetime

bottle.debug(False)

bottle.TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi', 'template'))

def get_session():
  session = bottle.request.get_cookie('session', secret='secret')
  return session;

def save_session(uid):
  session = {}
  session['uid'] = uid
  session['sid'] = uuid.uuid4().hex
  bottle.response.set_cookie('session', session, secret='secret')
  return session;

def invalidate_session():
  bottle.response.delete_cookie('session', secret='secret')
  return

@bottle.route('/')
def index():
  session = get_session()
  if session:
    return bottle.template('index',auth=True)
  return bottle.template('index',auth=False)

@bottle.route('/edit')
def edit():
  session = get_session()
  if not session: bottle.redirect('/')
  luser = user.find(session['uid'])
  if not luser: bottle.redirect('/logout')
  return bottle.template('edit')

@bottle.route('/signup', method='POST')
def post_signup():
  if 'login' in bottle.request.POST and 'password' in bottle.request.POST and 'apartment' in bottle.request.POST and 'home' in bottle.request.POST:
    login = bottle.request.POST['login']
    password = bottle.request.POST['password']
    home = bottle.request.POST['home']
    apartment = bottle.request.POST['apartment']
    if user.add_user(login,password,home,apartment):
      save_session(login)
      bottle.redirect('/edit')
  return bottle.redirect('/')

@bottle.route('/login', method='POST')
def post_login():
  if 'login' in bottle.request.POST and 'password' in bottle.request.POST:
    login = bottle.request.POST['login']
    password = bottle.request.POST['password']
    if user.auth(login,password):
      save_session(login)
      bottle.redirect('/edit')
  return bottle.redirect('/')

@bottle.route('/logout')
def logout():
  invalidate_session()
  bottle.redirect('/')

@bottle.route('/edit', method='POST')
def post_edit():
  session = get_session()
  if not session: bottle.redirect('/')
  luser = user.find(session['uid'])
  if not luser: bottle.redirect('/logout')
  data = user.get_data(session['uid'])
  cold = bottle.request.POST['cold']
  hot = bottle.request.POST['hot']
  counters.update(data[0],data[1],cold,hot,datetime.date.today(),session['uid'])
  return bottle.redirect('/report')

@bottle.route('/report')
def report():
  session = get_session()
  if not session: bottle.redirect('/')
  luser = user.find(session['uid'])
  if not luser: bottle.redirect('/logout')
  return bottle.template('report',List=0,home=False)

@bottle.route('/report', method='POST')
def post_report():
  apartment = bottle.request.POST['apartment']
  home = bottle.request.POST['home']
  if apartment !='' and home !='':
    data = counters.get_apartment(home,apartment)
    return bottle.template('report',List=data,home=False)
  if apartment =='' and home !='':
    data = counters.get_home(home)
    cold = 0
    hot = 0
    for x in data:
      cold += x[3]
      hot += x[4]
  return bottle.template('report',List=data,home=True,sumcold=cold,sumhot=hot)
  return bottle.template('report',List=data,home=False)

@bottle.route('/DEBUG/cwd')
def dbg_cwd():
  return "<tt>cwd is %s</tt>" % os.getcwd()

@bottle.route('/DEBUG/env')
def dbg_env():
  env_list = ['%s: %s' % (key, value)
  for key, value in sorted(os.environ.items())]
  return "<pre>env is\n%s</pre>" % '\n'.join(env_list)

@bottle.route('/template/js/:filename')
def static_file(filename):
  bottle.send_file(filename,
                   root= os.path.join(os.environ['OPENSHIFT_REPO_DIR'],
                                      'wsgi', 'template','js'))
@bottle.route('/template/img/:filename')
def static_file(filename):
  bottle.send_file(filename,
                   root= os.path.join(os.environ['OPENSHIFT_REPO_DIR'],
                                      'wsgi', 'template','img'))
@bottle.route('/template/css/:filename')
def static_file(filename):
  bottle.send_file(filename,
                   root= os.path.join(os.environ['OPENSHIFT_REPO_DIR'],
                                      'wsgi', 'template','css'))

application = bottle.default_app()
