from ejercicio1.clases.vehiculos import Flota, Automovil, Camion
from ejercicio2.clases.empleados import Vendedor, Gerente
from ejercicio3.clases.banco import CuentaCorriente, CuentaAhorro
from ejercicio4.clases.tienda import ProductoFisico, Carrito

def ejecutar_pruebas():
    # E1: Flota
    print("--- PRUEBA E1: VEHÍCULOS ---")
    flota = Flota()
    flota.agregar_vehiculo(Automovil("ABCD12", "Toyota", "Yaris", 2023, 4))
    flota.agregar_vehiculo(Camion("CCDD44", "Volvo", "FH", 2020, 30000))
    print(f"Consumo total (150km): {flota.calcular_consumo_total(150):.2f} L\n")

    # E2: Empleados
    print("--- PRUEBA E2: EMPLEADOS ---")
    v = Vendedor("Juan Pérez", "12.345.678-9", 500000, 2000000, 0.1)
    g = Gerente("Ana Marta", "9.876.543-2", 1500000, 300000)
    print(f"{v.nombre} Remuneración: ${v.calcular_remuneracion()}")
    print(f"{g.nombre} Remuneración: ${g.calcular_remuneracion()}\n")

    # E3: Banco
    print("--- PRUEBA E3: BANCO ---")
    corriente = CuentaCorriente("111", "Diego", 10000, 50000)
    corriente.retirar(40000) 
    print(corriente.obtener_resumen())
    print(f"Historial: {corriente.historial}\n")

    # E4: Tienda
    print("--- PRUEBA E4: TIENDA ---")
    prod = ProductoFisico("P01", "Libro POO", 25000, 10, 1.5)
    carro = Carrito()
    if carro.agregar(prod, 2):
        print(f"Total carrito: ${carro.calcular_total()}")
        print(f"Stock restante: {prod.stock}")

if __name__ == "__main__":
    ejecutar_pruebas()