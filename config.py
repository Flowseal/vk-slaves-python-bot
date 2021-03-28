settings = {
    
    'info': {
        'TOKEN': '', # https://vkhost.github.io (VK ADMIN)
        'ID': , # Ваш ID (https://regvk.com/id/)
        'DEBUG': False, # Режим разработчика (большее количество логов)
    },


    # Автоматическая выдача работы
    'job_slaves': {
        'ENABLED': False, # Вкл/Выкл (True/False)
        'MULTI-THREAD': False, # Мультипоточность (💀)
        'JOBS': ['🏰', '👑', '🐱‍🐉', '🐱‍👓', '🐱‍🚀'], # Случайная работа
    },


    # Автоматическая цепь
    'fet_slaves': {
        'ENABLED': False, # Вкл/Выкл (True/False)
        'MULTI-THREAD': False, # Мультипоточность (💀)
        'MAX_PROFIT': False, # Сажать на цепь, только при максимальной профите (1000р)
    },


    # Таргетированое ворование рабов
    'steal_target': {
        'TARGETS': [], # цели для кражи рабов (ID's) (https://regvk.com/id/)
        'MULTI-THREAD': False, # Мультипоточность (💀)
        'MIN_PRICE': 0, # Минмальная цена для покупки
        'MAX_PRICE': 40000, # Максимальная цена для покупки
        'AUTO_FET': False, # Автоматически кидать цепь после покупки
    },


    # Ворование рабов у топ-игроков
    'steal_top': {
        'ENABLED': False, # Вкл/Выкл (True/False)
        'MULTI-THREAD': False, # Мультипоточность (💀💀)
        'MIN_PRICE': 0, # Минмальная цена для покупки
        'MAX_PRICE': 40000, # Максимальная цена для покупки
        'AUTO_FET': False, # Автоматически кидать цепь после покупки
    },


    # Перепродажа рабов для большей выгоды
    'abuse_slaves': {
        'ENABLED': False, # Вкл/Выкл (True/False)
        'MULTI-THREAD': False, # Мультипоточность (💀💀💀)
        'MIN_BALANCE': 100000000, # Минимальная цена для абуза
        'AUTO_FET': False, # Автоматически кидать цепь после абуза
        'LIMIT': 19500, # Лимит по цене продажи раба 
    },


    # Покупка минусовых ID
    'abuse_unknowns': {
        'ENABLED': False, # Вкл/Выкл (True/False)
        'MULTI-THREAD': False, # Мультипоточность (💀)
        'MIN_PRICE': 0, # Минимальная цена для покупки
        'MAX_PRICE': 100000, # Максимальная цена для покупки
        'AUTO_FET': False, # Автоматически кидать цепь после покупки
    },
    
}
