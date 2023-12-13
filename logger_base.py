import logging as log

# Emojis para cada nivel de logging
emojis = {
    'DEBUG': u'\U0001F41B',  # 🐛
    'INFO': u'\U0001F310',   # 🌐
    'WARNING': u'\U0001F6A8', # 🚨
    'ERROR': u'\U0000274C',   # ❌
    'CRITICAL': u'\U0001F6AB' # 🚫
}

# Clase de formateador personalizado
class CustomFormatter(log.Formatter):
    def format(self, record):
        # Inserta el emoji correspondiente al inicio del mensaje
        if not hasattr(record, 'emoji_added'):
          record.msg = f"{emojis[record.levelname]} : {record.msg}"
          record.emoji_added = True
        return super(CustomFormatter, self).format(record)

# Formato de logging y configuración de CustomFormatter
log_format = '%(asctime)s [%(filename)s:%(lineno)s] %(message)s'
date_format = '%H:%M:%S %d/%m/%Y'
formatter = CustomFormatter(log_format, date_format)

# Configurar el StreamHandler para la consola
console_handler = log.StreamHandler()
console_handler.setFormatter(formatter)

# Configurar el FileHandler para escribir en un archivo
file_handler = log.FileHandler('capa_datos.log', encoding='utf-8')
file_handler.setFormatter(formatter)

#Configurar el logging con ambos handlers
log.basicConfig(level=log.DEBUG, handlers=[console_handler, file_handler])

if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel de info')
    log.warning('Mensaje a nivel de warning')
    log.error('Mensaje a nivel de error')
    log.critical('Mensaje a nivel crítico')