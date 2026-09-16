from pyscript import document


def generate_sku(event):
    category = document.getElementById("category").value
    name = document.getElementById("prod_name").value.strip()
    qty = document.getElementById("quantity").value.strip()

    if not name or not qty:
        document.getElementById("sku_output").innerText = "Please fill in all fields!"
        return

    name_code = name[:3].upper()

    qty_code = str(qty).zfill(3)

    sku_code = f"{category}-{name_code}-{qty_code}"

    document.getElementById("sku_output").innerText = sku_code