__author__ = 'CamiloDiaz_DavidDelgado_IvanClaro'

import math
import matplotlib.pylab as plt
import struct
import wave



class Seno:
        wavearray=[]
        def __init__(self,frecuencia,sampleo,tiempo,bits, nombre):
            self.frecuency = frecuencia
            self.sampler = sampleo
            self.time = tiempo
            self.Bits = bits
            self.tamano =sampleo * tiempo
            self.nombre = nombre

        def generar(self):
            for i in range (0, self.tamano):
                wave = ((2**self.Bits)/2)*math.sin((2*math.pi*self.frecuency*i)/self.sampler)
                Seno.wavearray.append(wave)
                print wave

            return Seno.wavearray

            Archivo=wave.open(self.nombre,"rb")
            tamano = Archivo.getnframes()


            for	i in range(0,tamano):
                DatosArray = Archivo.readframes(1)
                Datos = struct.unpack('<H',DatosArray)
                sumatoria =	sumatoria	+	int(Datos[0])**2

            ValorRms = math.sqrt(sumatoria/tamano)
            ValorpicoRms = 20*math.log10(ValorRms/(2**self.Bits))

            print (ValorRms)
            print (ValorpicoRms)
