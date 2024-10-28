import Encapsulate_collection from Encapsulate_collection

clase = Clase()

clase.agregar_estudiante("Alice")
clase.agregar_estudiante("Bob")

print(clase.estudiantes)  # ['Alice', 'Bob']
print(clase.numero_estudiantes())  # 2

clase.eliminar_estudiante("Alice")
print(clase.estudiantes)  # ['Bob']