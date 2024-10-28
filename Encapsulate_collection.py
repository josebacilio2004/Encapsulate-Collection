class Clase:
    def __init__(self):
        # Lista privada de estudiantes
        self._estudiantes = []

    @property
    def estudiantes(self):
        """Devuelve una copia de la lista para evitar modificaciones externas directas"""
        return self._estudiantes.copy()

    def agregar_estudiante(self, nombre):
        """Agrega un estudiante a la lista si no está ya en ella"""
        if nombre not in self._estudiantes:
            self._estudiantes.append(nombre)

    def eliminar_estudiante(self, nombre):
        """Elimina un estudiante de la lista si está presente"""
        if nombre in self._estudiantes:
            self._estudiantes.remove(nombre)

    def numero_estudiantes(self):
        """Devuelve el número total de estudiantes"""
        return len(self._estudiantes)



