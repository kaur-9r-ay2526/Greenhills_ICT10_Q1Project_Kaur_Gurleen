# ICT Skillstest Receipt

from pyscript import document

def order(e):
    # Get checkboxes from HTML
    hashbrown = document.getElementById("hashbrown")
    pepperoni_pizza = document.getElementById("pepperoni_pizza")
    iced_tea = document.getElementById("iced_tea")
    spam_musubi = document.getElementById("spam_musubi")
    chicken_nuggets = document.getElementById("chicken_nuggets")

    subtotal = 0.0

    
    if hashbrown.checked:
        subtotal += float(hashbrown.value)
    if pepperoni_pizza.checked:
        subtotal += float(pepperoni_pizza.value)
    if iced_tea.checked:
        subtotal += float(iced_tea.value)
    if spam_musubi.checked:
        subtotal += float(spam_musubi.value)
    if chicken_nuggets.checked:
        subtotal += float(chicken_nuggets.value)

    
    vat = subtotal * 0.12
    total = subtotal + vat

    # Display results on the web page
    document.getElementById("subtotal").innerHTML = f"₱{subtotal:.2f}"
    document.getElementById("vat").innerHTML = f"₱{vat:.2f}"
    document.getElementById("total").innerHTML = f"₱{total:.2f}"