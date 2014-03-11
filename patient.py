from bottle import route, post, get, put, delete, run, template, request

patient_info = []
patient_dict = {}
@post('/register')
def register():
    idn = request.POST['id']
    name = request.POST['name']
    gender = request.POST['gender']
    age = request.POST['age']
    address = request.POST['address']
    phone = request.POST['phone']
    if idn not in patient_dict.keys():
        patient_info = ' '.join([name, gender, age, address, phone])
        patient_dict.update({idn:patient_info})
        return patient_dict
    else:
        return 'Already recorded for member id ',idn
    
@get('/showpatient/<idn>')
def show_patient_details(idn):
    if idn in patient_dict.keys():
        return patient_dict[idn]
    else:
        return 'No such record for id ',idn

@put('/update/<idn>')
def update_patient_details(idn):
    if idn in patient_dict.keys():
        patient_dict.update(name = request.POST['name'],gender = request.POST['gender'],age = request.POST['age'],address = request.POST['address'],phone = request.POST['phone'])
        return 'Updated Sucessfully'
    else:
        return 'No such record for id ',idn

@delete('/delete/<idn>')
def delete_patient(idn):
    if idn in patient_dict.keys():
        del(patient_dict[idn])
        return 'Record deleted.'
    else:
        return 'No such record for id ',idn
    

run(host='localhost', port=8080)
