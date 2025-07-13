from calc_interfaces.srv import DoMath
import sys
import rclpy
from rclpy.node import Node

class CalcServiceClient(Node):
    def __init__(self):
        super().__init__('calc_service_client')
        self.cli = self.create_client(DoMath, 'do_math')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Serviço não disponível, espere um pouco...')
        self.req = DoMath.Request()
    
    def send_request(self):
        self.req.a = int(sys.argv[1])
        self.req.b = int(sys.argv[2])
        self.req.operacao = str(sys.argv[3])
        self.future = self.cli.call_async(self.req)

def main(args=None):
    rclpy.init(args=args)

    calc_service_client = CalcServiceClient()
    calc_service_client.send_request()
    while rclpy.ok():
        rclpy.spin_once(calc_service_client)
        if(calc_service_client.future.done()):
            try:
                response = calc_service_client.future.result()
            except Exception as e:
                calc_service_client.get_logger().info('Service call failed %r' % (e, ))
            else:
                calc_service_client.get_logger().info(
                    'Resultado: %.2f\nMensagem: %s' % (response.resultado, response.mensagem)
                )
            break
    calc_service_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()