class Conversor_ps:
  def __init__(self):
   
     self.pca = 100000
     self.psi = 14.5038
   
  def converter_barXpsi(self, bar):
     
     result = bar * self.psi 
     return result

conv = Conversor_ps()

print(conv.converter_barXpsi(2), "psi")