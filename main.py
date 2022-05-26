from flask import Flask, render_template, request, redirect
app = Flask('app')

contacts = [
  { 'name': 'João da Silva', 'email': '', 'phone': ''},
  { 'name': 'Maria Souza', 'email': '', 'phone': ''}
]

@app.route('/')
def index():
  return render_template(
    'index.html',
    contacts=contacts
  )

@app.route('/create', methods=['POST'])
def create():
  name = request.form.get('name')
  email = request.form.get('email')
  phone = request.form.get('phone')
  contacts.append({'name': name, 'email': email, 'phone': phone})
  return redirect('/')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)