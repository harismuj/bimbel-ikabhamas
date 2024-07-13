def calc_run(distance,ref):

  # Hitung rasio
  distance_ratio = distance / ref # ref = laki-laki 3500, perempuan 3100
  time_ratio = 12 / 12

  # Asumsikan sistem penilaian linier.
  # Hitung nilai dengan proporsi.
  score = 100 * (distance_ratio * time_ratio)

  return int(score)

def calc_up(banyak, ref):
  '''ref :
      pull up 17, chinning 72
      situp = laki-laki 50, perempuan 40
      push up = laki-laki 42, perempuan 37
  '''
  nilai_satuan = 100 / ref 
  score = banyak * nilai_satuan
  return int(score)


# untuk penilaian shuttle run dan renang
def calc_interpolasi(target_x, data):
  """
    data diisi dengan array
    [(16.2, 100), (17, 90), (19, 51)]
  """

  data.sort(key=lambda p: p[0])

  if target_x <= data[0][0]:
    return data[0][1]  

  for i in range(len(data) - 1):
    x1, y1 = data[i]
    x2, y2 = data[i + 1]

    
    if target_x > x1 and target_x <= x2:
      
      m = (y2 - y1) / (x2 - x1)
      
      target_y = m * target_x + (y1 - m * x1)
      return int(target_y)
    
  return data[-1][1]



