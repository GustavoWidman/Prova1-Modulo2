import rclpy
import typer
from std_msgs.msg import String
from typing_extensions import Annotated

app = typer.Typer()

class Publisher:
	def __init__(self):
		rclpy.init()

		self.node = rclpy.create_node('publisher_gustavo_prova1_modulo2') # type: ignore
		self.publisher = self.node.create_publisher(String, 'topic', 10)

	def send_msg(self, msg: str):
		message = String()
		message.data = msg

		self.publisher.publish(message)

@app.command()
def main(
	vx: Annotated[float, typer.Option(help='Velocidade da tartaruga em X')] = 0.0,
	vy: Annotated[float, typer.Option(help='Velocidade da tartaruga em Y')] = 0.0,
	vt: Annotated[float, typer.Option(help='Velocidade angluar da tartaruga em torno do eixo Z')] = 0.0,
	t:  Annotated[int, typer.Option(help='Tempo que a tartaruga deve ficar executando o comando')] = 1000
):
	print(f'Sending message with vx={vx}, vy={vy}, vtheta={vt}, t={t}')
	publisher = Publisher()

	msg = f'{vx} {vy} {vt} {t}'
	publisher.send_msg(msg)


if __name__ == "__main__":
	app()