# I affirm that I have carried out my academic endeavors with full academic honesty.
# Rathika Nair

from graph import graph


def print_introduction(): 
  """
  function introduces qhat program will do
  """  
  print("------------------------------------------------------------")
  print("This program will search throught the exoplanet archive and find the most Earth-like planet.")
  print("------------------------------------------------------------")



def clean_up(filename):
  """
  Function turns each line in text file into a list and puts all lists into one big list.

  :param filename: the file that is getting turned into lists
  :return: returns the lists of lists with all of the data
  """
  f = open(filename, "r") 

  for i in range(71):
    x = f.readline() 


  total_data = []
  for line in f:
    exoplanet_list = line.split(",") 
    total_data.append(exoplanet_list)

  return total_data



def get_mass(list):
 
  """
  Function finds each exoplanet's mass.
  If an exoplanet mass is in between range, planet remains as habitable. 
  Else, exoplanet is removed

  :param list: the list of exoplanets used to find each mass 
  :return: returns the list of habitable planets
  """  
  
  data_list = []
  for i in range(len(list)):
    
    pl_bmasse = list[i][14]
    
    if pl_bmasse == '':
     pl_bmasse = 0
    else: 
      pl_bmasse = float(pl_bmasse) 

    if pl_bmasse >= .27 and pl_bmasse < 5.0:
     data_list.append(list[i])
    
  return data_list    
    


def spectral_type(list):
  """
  Function finds each planet's spectral type (star type)
  If star is type F, G, or K, planet stays.
  Else, planet is removed from list.

  :param list: the list of exoplanets used to find each spectral type 
  :return: returns the list of habitable planets
  """
  data_list = []
  for i in range(len(list)):
    st_spectype = list[i][30]

    if "F" in st_spectype or "G" in st_spectype or "K" in st_spectype:
      data_list.append(list[i])

  return data_list  



def pl_distance(list):
  """
  Function finds each planet's orbital distance
  If planet is in optimal orbital distance  then it stays.
  Else, planet is removed from list.

  :param list: the list of exoplanets used to find each distance 
  :return: returns the list of habitable planets
  """
  data_list = []
  for i in range(len(list)):
    pl_orbsmax = list[i][10]

    if pl_orbsmax == '':
     pl_orbsmax = 0
    else: 
      pl_orbsmax = float(pl_orbsmax) 

    if pl_orbsmax >= .38 and pl_orbsmax < 10.0:
     data_list.append(list[i])

  return data_list



def habitable(list):
  """
  Function prints the names pf the habitable planets 

  :param list: the list of exoplanets used 
  """
  for i in range(len(list)):
    pl_name = list[i][0]
    print(pl_name)



def info(list):
  for i in range(len(list)):
    pl_name = list[i][0]
    st_spectype = list[i][30]
    pl_bmasse = list[i][14]
    pl_orbsmax = list[i][10]
    
    print(pl_name, st_spectype, pl_bmasse, pl_orbsmax)



def main():
  print_introduction()
  data_list = clean_up("exoplanet_data.csv")
  mass = get_mass(data_list)
  star_type = spectral_type(mass)
  planet_distance = pl_distance(star_type)

  print("These are the most habitable planets from the known exoplanets in the NASA exoplanet archive.")
  habitable(planet_distance)

  #info(planet_distance)
  graph()  


main()


