class Conversora:
    def __init__(self):
        self.const_ = 100          # 1 metro = 100 centímetros
        self.pe_em_centimetros = 30.48  # 1 pé = 30.48 centímetros

    def conversor_metrosXcentimetros(self, metros):
        return metros * self.const_

    def conversor_centimetrosXmetros(self, centimetros):
        if centimetros != 0:
            return centimetros / self.const_
        else:
            return "Divisão por zero impossível!"

    def conversor_centimetrosXpes(self, centimetros):
        if centimetros != 0:
            return centimetros / self.pe_em_centimetros
        else:
            return "Divisão por zero impossível!"

    def conversor_metrosXpes(self, metros):
        centimetros = self.conversor_metrosXcentimetros(metros)
        return self.conversor_centimetrosXpes(centimetros)

    def conversor_peXcentimetros(self, pe):
        return pe * self.pe_em_centimetros

    def conversor_peXmetros(self, pe):
        centimetros = self.conversor_peXcentimetros(pe)
        return self.conversor_centimetrosXmetros(centimetros)

        
    
conv = Conversora()

print(conv.conversor_metrosXcentimetros(4.2) ,"centimetros")
print(conv.conversor_centimetrosXmetros(200) ,"metros")
print(conv.conversor_centimetrosXpes(4), "pés")
print(conv.conversor_metrosXpes(1), "pés")
print(conv.conversor_peXcentimetros(0.3), "centimetros")
print(conv.conversor_peXmetros(4), "metros")
