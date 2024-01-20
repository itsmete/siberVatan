def alan_hesapla(taban,yukseklik):
                  alan = (taban*yukseklik) / 2
                  return alan

taban = int(input('taban girin'))
yukseklik = int(input('yukseklik girin'))

result = alan_hesapla(taban=taban,yukseklik=yukseklik)

print(result)

