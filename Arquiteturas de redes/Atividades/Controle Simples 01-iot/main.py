from machine import Pin, I2C
import ssd1306
import machine

led = machine.Pin(25, machine.Pin.OUT)
led2 = machine.Pin(17, machine.Pin.OUT)
botao = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
botao1 = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)

i2c = I2C(0, scl=Pin(22), sda=Pin(21))

largura = 128
altura = 64

tela = ssd1306.SSD1306_I2C(largura, altura, i2c)
while True:
    vermelho = botao.value()
    azul = botao1.value()
    if vermelho == 0:
        led.value(1)
        led2.value(0)
        tela.fill(0)
        tela.text('a umidade', 0, 0)
        tela.text('do ar e de', 0, 10)
        tela.text('15%', 0, 20)
        tela.show()
    
    if azul == 0:
        led.value(0)
        led2.value(1)
        tela.fill(0)
        tela.text('a temperatura', 0, 0)
        tela.text('do quarto e de', 0, 10)
        tela.text('30 graus', 0, 20)
        tela.show()
