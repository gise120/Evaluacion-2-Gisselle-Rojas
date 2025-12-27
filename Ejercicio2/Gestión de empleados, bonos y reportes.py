# Ejercicio 2 — Gestión de empleados, bonos y reportes de sueldo
# Una empresa quiere contar con un sistema para administrar a sus trabajadores y estimar el gasto
# mensual en sueldos, considerando que existen distintos tipos de colaboradores con formas
# diferentes de cálculo de remuneración.
# Se requiere que éste permita:
# 1. Registrar trabajadores de la empresa, almacenando como mínimo:
# • Nombre completo.
# • Identificación (por ejemplo, RUT).
# • Sueldo base.
# • Estado del trabajador (activo o inactivo).
# 2. Manejar distintos tipos de trabajadores, tales como por ejemplo:
# • Vendedores.
# • Gerentes.
# • Practicantes (o trabajadores a honorarios por hora).
# Cada tipo de trabajador debe considerar información adicional propia de su rol (por ejemplo:
# comisiones, bonos, horas trabajadas, etc.) y esa información debe afectar la forma en que se calcula
# su remuneración final.
# 3. Calcular la remuneración mensual final de cada trabajador, de manera que:
# • Exista un cálculo base a partir del sueldo asignado.
# • Para quienes reciben comisiones (como los vendedores), la remuneración final considere
# las ventas del mes y el porcentaje de comisión.
# • Para quienes reciben bonos fijos (como los gerentes), la remuneración final incorpore dicho
# bono al sueldo base.
# • Para quienes trabajan por hora (como practicantes), la remuneración se calcule según
# cantidad de horas trabajadas y valor por hora.
# 4. Obtener un resumen legible de cada trabajador, donde se pueda ver, al menos:
# • Nombre.
# • Identificación.
# • Tipo de trabajador.
# • Sueldo base.
# • Remuneración final calculada para el mes.
# 5. Administrar el conjunto de trabajadores de la empresa, pudiendo:
# • Agregar nuevos trabajadores indicando su tipo y la información asociada.
# • Mantener un listado de todos los trabajadores.
# • Filtrar o listar solamente los trabajadores activos (es decir, aquellos que deben considerarse
# para el cálculo de sueldos del mes).
# 6. Calcular indicadores globales de la empresa, en particular:
# • El gasto total mensual en sueldos, considerando únicamente a los trabajadores activos.
# • (Opcional) Un listado donde se puedan comparar las remuneraciones finales por trabajador
# para identificar quiénes representan mayor o menor costo mensual.
# 7. Probar el sistema desde un programa principal, donde se simule:
# • La creación de varios trabajadores de distintos tipos (vendedores, gerentes, practicantes)
# con datos de ejemplo.
# • Su incorporación al conjunto de trabajadores de la empresa.
# • La obtención de un reporte que muestre:
# o Nombre, tipo de trabajador y remuneración final de cada uno.
# o El gasto total mensual de la empresa en sueldos.
--------------------------------------------------------------------------------------------------
class Empleado:
    def __init__(self, nombre, rut, sueldo_base):
        self.nombre = nombre
        self.rut = rut
        self.sueldo_base = sueldo_base
        self.activo = True

    def calcular_remuneracion(self):
        return self.sueldo_base

class Vendedor(Empleado):
    def __init__(self, nombre, rut, sueldo_base, ventas, comision_pct):
        super().__init__(nombre, rut, sueldo_base)
        self.ventas = ventas
        self.comision_pct = comision_pct

    def calcular_remuneracion(self):
        return self.sueldo_base + (self.ventas * self.comision_pct)

class Gerente(Empleado):
    def __init__(self, nombre, rut, sueldo_base, bono):
        super().__init__(nombre, rut, sueldo_base)
        self.bono = bono

    def calcular_remuneracion(self):
        return self.sueldo_base + self.
    
    ------------------------------FIN----------------------------------------------