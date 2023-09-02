"""REGISTRO"""
class Ticket:
    def __init__(self, codigo, patente, tipo_vehiculo, forma_pago, pais_cabina, km_recorrido):
        self.codigo = codigo
        self.patente = patente
        self.tipo_vehiculo = tipo_vehiculo
        self.forma_pago = forma_pago
        self.pais_cabina = pais_cabina
        self.km_recorridos = km_recorrido

    def __str__(self):
        return f'Codigo: {self.codigo} - Patente: {self.patente} - Tipo de vehiculo: {self.tipo_vehiculo} - \
Forma de pago: {self.forma_pago} - Pais de cabina: {self.pais_cabina} - Km recorridos: {self.km_recorridos}'


"""FUNCIONES"""
# Definir timestamp
def timestamp(linea):
    idioma = ""
    anterior = ""
    for caracter in linea:
        if anterior == "P" and caracter == "T":
            idioma = "portugués"
        if anterior == "E" and caracter == "S":
            idioma = "español"
        anterior = caracter
    return idioma


# Transformar la linea en objeto
def object_linea(linea):  # '0231258082 PYV0922 0 2 0 541'
    codigo = ''
    patente = ''
    vehiculo = ''
    forma_de_pago = ''
    pais_cabina = ''
    km_recorridos = ''
    for car in range(len(linea)):
        if 0 <= car <= 9:
            codigo += linea[car]

        elif 10 <= car <= 16:
            patente += linea[car]

        elif 17 == car:
            vehiculo = int(linea[car])

            if vehiculo == 0:
                vehiculo = 'Moto'

            elif vehiculo == 1:
                vehiculo = 'Auto'

            elif vehiculo == 2:
                vehiculo = 'Camion'

        elif 18 == car:
            forma_de_pago = int(linea[car])

            if forma_de_pago == 1:
                forma_de_pago = 'Manual'

            elif forma_de_pago == 2:
                forma_de_pago = 'Telepeaje'

        elif 19 == car:
            pais_cabina = int(linea[car])

            if pais_cabina == 0:
                pais_cabina = 'Argentina'

            elif pais_cabina == 1:
                pais_cabina = 'Bolivia'

            elif pais_cabina == 2:
                pais_cabina = 'Brasil'

            elif pais_cabina == 3:
                pais_cabina = 'Paraguay'

            elif pais_cabina == 4:
                pais_cabina = 'Uruguay'

            else:
                pais_cabina = 'Otro'

        elif 20 <= car <= 22:
            km_recorridos += linea[car]

    nuevo_ticket = Ticket(codigo, patente, vehiculo, forma_de_pago, pais_cabina, int(km_recorridos))
    # 'codigo' guardado como type: 'str'

    return nuevo_ticket

#Funcion para ordenar objetos de un array por ID
def order_tickets_by_id(tickets):
  # Ordena el array de tickets por el código de cada ticket.
  tickets.sort(key=lambda ticket: ticket.codigo, reverse=True)
  return tickets


if __name__ == '__main__':
    # Cargar las variables
    vehicle_1 = Ticket(300, 'AA300FF', 'Camion', 'Manual', 'Argentina', 5000)

