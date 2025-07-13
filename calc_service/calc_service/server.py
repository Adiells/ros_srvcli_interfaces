from calc_interfaces.srv import DoMath
from rclpy.node import Node
import rclpy

class CalcServiceServer(Node):
    def __init__(self):
        super().__init__('calc_service_server')
        self.cli = self.create_service(DoMath, 'do_math', self.do_math_callback)
    def do_math_callback(self, request, response):
        operador = ''
        if request.operacao.lower() == 'soma':
            response.resultado = float(request.a + request.b)
            response.mensagem = f"a soma de {request.a} + {request.b} = {response.resultado}"
        elif request.operacao.lower() == 'subtracao':
            response.resultado = float(request.a - request.b)
            response.mensagem = f"a subtração de {request.a} - {request.b} = {response.resultado}"
        elif request.operacao.lower() == 'divisao':
            response.resultado = float(request.a / request.b)
            response.mensagem = f"a divisão de {request.a} / {request.b} = {response.resultado}"
        elif request.operacao.lower() == 'multiplicacao':
            response.resultado = float(request.a * request.b)
            response.mensagem = f"a multiplicação de {request.a} * {request.b} = {response.resultado}"
        else:
            response.resultado = float(0)
            response.mensagem = f"Operação inválida: {request.operacao}"

        self.get_logger().info("Números e operação requerida\na: %s b: %s operacao: %s" % (request.a, request.b, request.operacao))


        
        return response
    
def main():
    rclpy.init()

    calc_service_service = CalcServiceServer()
    rclpy.spin(calc_service_service)
    rclpy.shutdown()
if __name__ == '__main__':
    main()        