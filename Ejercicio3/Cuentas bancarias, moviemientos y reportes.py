# Ejercicio 3 — Cuentas bancarias, movimientos y reporte
# Un banco necesita un sistema para administrar las cuentas de sus clientes, registrar los movimientos
# que se realizan y generar reportes de saldos e historial.
# Como usuario del sistema, se requiere que éste permita:
# 1. Registrar cuentas bancarias de clientes, almacenando al menos:
# • Número de cuenta.
# • Nombre del titular.
# • Saldo actual.
# • Tipo de cuenta (por ejemplo: cuenta corriente, cuenta de ahorro).
# 2. Registrar distintos tipos de cuentas, donde:
# • Las cuentas corrientes puedan operar con línea de crédito, es decir, permitir que el saldo
# baje de cero hasta cierto límite negativo.
# • Las cuentas de ahorro puedan tener asociada una tasa de interés mensual, que permita
# actualizar el saldo aplicando dicho interés.
# 3. Registrar y controlar movimientos de dinero en una cuenta, específicamente:
# • Depósitos, que aumenten el saldo, rechazando montos no válidos (cero o negativos).
# • Retiros, que disminuyan el saldo:
# o En cuentas normales o de ahorro, solo si hay saldo suficiente.
# o En cuentas corrientes, permitiendo sobregiro hasta el límite de la línea de crédito.
# • Cada movimiento debe quedar registrado como un texto legible (por ejemplo, “DEPÓSITO
# 100.000”, “RETIRO 50.000”, “INTERÉS 2.500”).
# 4. Aplicar intereses a las cuentas de ahorro, de forma que:
# • Dado un periodo mensual, el sistema pueda calcular el interés correspondiente según la
# tasa definida para esa cuenta.
# • El saldo se actualice sumando el interés calculado.
# • El interés aplicado quede igualmente registrado como un movimiento.
# 5. Consultar la información de una cuenta bancaria, permitiendo:
# • Buscar una cuenta por su número.
# • Ver el titular, el tipo de cuenta y su saldo actual.
# • Obtener el historial de movimientos realizados en esa cuenta, en orden cronológico.
# 6. Administrar el conjunto de cuentas del banco, pudiendo:
# • Agregar nuevas cuentas.
# • Consultar si una cuenta existe a partir de su número.
# • Obtener el saldo total administrado por el banco, sumando el saldo de todas las cuentas
# registradas.
# 7. Probar el sistema desde un programa principal, donde se simule:
# • La creación de varias cuentas de distintos tipos (por ejemplo, dos cuentas corrientes y dos
# cuentas de ahorro).
# • La ejecución de depósitos y retiros en distintas cuentas.
# • La aplicación de intereses en al menos una cuenta de ahorro.
# • La impresión de:
# o El saldo y tipo de cada cuenta.
# o El historial de movimientos de una cuenta específica.
# o El saldo total administrado por el banco.
--------------------------------------------------------------------------------------------
class CuentaBancaria:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self._saldo = saldo
        self.historial = []

    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            self.historial.append(f"DEPÓSITO {monto}")
            return True
        return False

    def obtener_resumen(self):
        return f"Titular: {self.titular} | Saldo: ${self._saldo}"

class CuentaCorriente(CuentaBancaria):
    def __init__(self, numero, titular, saldo, linea_credito):
        super().__init__(numero, titular, saldo)
        self.linea_credito = linea_credito

    def retirar(self, monto):
        if monto <= (self._saldo + self.linea_credito):
            self._saldo -= monto
            self.historial.append(f"RETIRO {monto}")
            return True
        return False

class CuentaAhorro(CuentaBancaria):
    def __init__(self, numero, titular, saldo, tasa_interes):
        super().__init__(numero, titular, saldo)
        self.tasa_interes = tasa_interes

    def aplicar_interes(self):
        interes = self._saldo * self.tasa_interes
        self._saldo += interes
        self.historial.append(f"INTERÉS {interes}")

        ----------------------------------------FIN--------------------------------------------