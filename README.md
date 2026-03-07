# Arduinopy - Python interface para comunicação com Arduino Uno via ROS 2

Pacote desenvolvido em Python para comunicação entre Arduino Uno e laptop via ROS 2. O propósito é permitir o processamento no laptop e enviar os comandos de saída para o Arduino. O embarcado faz a leitura dos dados e os envia aos atuadores.

## Requisitos

- Ubuntu 22.04
- ROS 2 Humble
- Arduino IDE

## Instalação e Inicialização 

### Arduino IDE

Para instalar o Arduino IDE no Ubuntu:

```bash
sudo snap install arduino
```

Para iniciar a IDE, basta o comando:

```bash
arduino
```

Adicione o seu usuário ao `groups` para que as permissões necessárias sejam dadas:

```bash
sudo usermod -aG dialout $USER
```

Após conectar o Arduino ao computador, um dispositivo USB deve ficar visível em `/dev`. Procure por `ttyUSB0` ou `ttyACM0` com:

```bash
ls /dev/tty*
```

**Nota**: caso a porta não apareça, remova o pacote `brltty` do sistema, pois este pode estar impedindo o acesso à porta serial:

```bash
sudo apt remove brltty
```

### Arduinopy

Clone o repositório em `ros2_ws/src`:

```bash
git clone https://github.com/lucasbme/arduinopy
```

Configure a seguinte linha de acordo com sua porta serial e o *baud rate* do Arduino:

```python
    self.ser = serial.Serial('/dev/ttyUSB0', 9600)
```

Compile:

```bash
cd ros2_ws
colcon build --packages-select arduinopy

source install/setup.bash
```

Rode o nó:

```bash
ros2 run arduinopy serial_node
```