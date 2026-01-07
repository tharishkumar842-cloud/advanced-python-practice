products = {"pen": 10, "notebook": 50, "eraser": 5, "pencil": 8}
products={k:(v+20 if k=="notebook" else v)for k,v in products.items() }
print(products)
