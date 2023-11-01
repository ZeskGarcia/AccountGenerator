import os, sys, fade, inquirer, importlib
from colorama import Fore
from tabulate import tabulate



ScriptMenu = fade.greenblue("""

  ______    _  __                      _____ ______ _   _   
 |___  /   | |/ /     /\              / ____|  ____| \ | |  
    / / ___| ' /     /  \   ___ ___  | |  __| |__  |  \| |  
   / / / __|  <     / /\ \ / __/ __| | | |_ |  __| | . ` |  
  / /__\__ \ . \   / ____ \ (_| (__  | |__| | |____| |\  |
 /_____|___/_|\_\ /_/    \_\___\___|  \_____|______|_| \_|


""")

ScriptAuthor = fade.random("Made by ZsK")

class AccGen:

  def __init__(self):
    self.ModulesFolder = "modules"
    moduleNames = ["discordBooster"]
    self.Modules = {}
    for mName in moduleNames:
      try:
        self.Modules[mName] = importlib.import_module(self.ModulesFolder+"."+mName)
      except ModuleNotFoundError:
          print(f"No se encontró el módulo {mName}.")
          continue
        
    print(ScriptMenu)
    print("\n")
    print(ScriptAuthor)
    print("\n")
    while True:
      self.Services = [
        "Discord Account Generator",
        "Mierda"
      ]

      self.display_menu(self.Services)
      print("0. Exit")
      choice = input("Select an option (0 to exit): ")
      if choice == 0:
        print("Exiting the program")
        break
      elif choice.isdigit() and 1 <= int(choice) <= len(self.Services):
          selected_option = self.Services[int(choice) - 1]
          print(f"Selected Service: {selected_option}")
          self.optionSelected(selected_option, int(choice))
          break
      else:
          print("Opción no válida. Por favor, selecciona una opción válida.")

    
  def optionSelected(self, selection, optionId):
    if optionId == 1:
      self.Modules['discordBooster'].discordBooster()
    
  def display_menu(self, options, items_per_row=5):
    table = []
    for i in range(0, len(options), items_per_row):
        row = options[i:i + items_per_row]
        table.append([f"{j + 1}. {option}" for j, option in enumerate(row)])

    print(tabulate(table, tablefmt="fancy_grid"))

if __name__ == "__main__":
    AccGen()
