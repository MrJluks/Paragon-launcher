import configparser
import os


class Jcfg:
    def __init__(self,ppath:str): # Инициализация
        self.path = ppath # Путь к папке с кэшем, косытль
        self.path_to_cfg = os.path.join(ppath, "config.ini") # Путь к файлу конфигурации
        
        self.config = configparser.ConfigParser() # Создание конфига
        self.config.read(self.path_to_cfg) # Чтение уже существующего

        with open(self.path_to_cfg, 'w') as config_file: # Перезапись, нужна для первой инициализации
            self.config.write(config_file) 

    def save_value(self,value,section:str,key:str): #С охранение значения по ключу 
        if not self.config.has_section(section): # Создать секцию, если нет 
            self.config.add_section(section)
        
        self.config.set(section,key,str(value)) # Установить зачение
        with open(self.path_to_cfg, 'w') as config_file: # Записать файл
            self.config.write(config_file)

    def get_value(self,section:str,key:str): # Получить значение по ключу
        try:
            return self.config.get(section,key) # Вернуть значение
        except:
            print("JCFG:can't find section/key") # Если не получилось вернуть нуль
            return 0
        
    def save_cfg(self):
        with open(self.path_to_cfg, 'w') as config_file: # Записать файл
            self.config.write(config_file)








