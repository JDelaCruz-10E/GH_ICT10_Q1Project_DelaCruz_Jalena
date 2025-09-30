from pyscript import display, document

order = 'Order Summary'  # String

def ordering_form(e):
    item1 = document.getElementById('menu1')
    item2 = document.getElementById('menu2')
    item3 = document.getElementById('menu3')
    item4 = document.getElementById('menu4')
    item5 = document.getElementById('menu5')
    name = document.getElementById('name').value
    add = document.getElementById('address').value
    num = document.getElementById('contact').value

    total = (float(item1.value) * item1.checked + 
             float(item2.value) * item2.checked + 
             float(item3.value) * item3.checked +
             float(item4.value) * item4.checked +
             float(item5.value) * item5.checked)

    display(order, target='output')
    display(f'Name: {name}', target='output')
    display(f'Address: {add}', target='output')
    display(f'Contact number: {num}', target='output')
    display(f'Total amount: ₱ {total}', target='output')
