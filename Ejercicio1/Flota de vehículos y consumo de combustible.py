# E1 — Flota de Vehículos y Consumo de Combustible
# Una empresa de transporte quiere contar con un sistema para gestionar su flota de vehículos y
# estimar el consumo de combustible de cada uno, así como el consumo total para ciertos trayectos.
# Se necesita que éste permita:
# 1. Registrar vehículos de la flota, almacenando al menos:
# • Identificación del vehículo (por ejemplo, patente).
# • Marca.
# • Modelo.
# • Año de fabricación.
# 2. Trabajar con distintos tipos de vehículos dentro de la misma flota, por ejemplo:
# • Automóviles.
# • Motocicletas.
# • Camiones.
# Cada tipo de vehículo debe considerar información adicional relevante a su naturaleza (por
# ejemplo, cantidad de puertas, cilindrada, capacidad de carga, etc.), y esa información debe influir
# en cómo se estima su consumo de combustible.
# 3. Calcular el consumo estimado de combustible para un vehículo específico, dado un trayecto de
# cierta cantidad de kilómetros.
# • La forma de calcular el consumo no debe ser igual para todos, sino que debe poder
# diferenciar entre los distintos tipos de vehículo.
# 4. Obtener una descripción legible de cada vehículo, donde se pueda ver claramente:
# • Identificación (patente u otro identificador único).
# • Marca, modelo y año.
# • Tipo de vehículo.
# 5. Administrar la flota completa, pudiendo:
# • Agregar nuevos vehículos asegurando que no se repitan identificadores.
# • Eliminar vehículos a partir de su identificador.
# • Buscar un vehículo por su identificador para consultar sus datos y su consumo estimado.
# 6. Calcular indicadores globales de la flota, al menos:
# • Consumo total estimado de combustible para un trayecto de X kilómetros, considerando
# todos los vehículos registrados.
# • (Opcional) Listado de consumos individuales para comparar qué vehículos son más o
# menos eficientes.
# 7. Probar el sistema desde un programa principal, donde se simule lo siguiente:
# • Crear varios vehículos de distintos tipos con datos de ejemplo.
# • Agregarlos a la flota.
# • Mostrar la información de cada vehículo.
# • Calcular y mostrar el consumo estimado por vehículo y el consumo total de la flota para un
# trayecto común (por ejemplo, 150 km

-------------------------------------------------------------------------------------------------
class Vehiculo:
    def __init__(self, patente, marca, modelo, anio):
        self._patente = patente
        self._marca = marca
        self._modelo = modelo
        self._anio = anio

    def get_patente(self):
        return self._patente

    def calcular_consumo(self, distancia):
        raise NotImplementedError("No está implementado")
    def __str__(self):
        return f"{self._marca} {self._modelo} ({self._anio}) - Patente: {self._patente}"

class Automovil(Vehiculo):
    def __init__(self, patente, marca, modelo, anio, puertas):
        super().__init__(patente, marca, modelo, anio)
        self.puertas = puertas

    def calcular_consumo(self, distancia):
        return distancia / 12  
    class Camion(Vehiculo):
    def __init__(self, patente, marca, modelo, anio, capacidad_carga):
        super().__init__(patente, marca, modelo, anio)
        self.capacidad_carga = capacidad_carga

    def calcular_consumo(self, distancia):
        return distancia / 4 

class Flota:
    def __init__(self):
        self.vehiculos = {}
def __init__(self):
        self.vehiculos = {}

    def agregar_vehiculo(self, vehiculo):
        if vehiculo.get_patente() not in self.vehiculos:
            self.vehiculos[vehiculo.get_patente()] = vehiculo
            return True
        return False

    def calcular_consumo_total(self, km):
        return sum(v.calcular_consumo(km) for v in self.vehiculos.values())

----------------------------------FIN--------------------------------------------