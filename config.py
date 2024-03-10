rand_gen = True     #TODO: Генерировать клетки на поле случайным образом [True/False]
spawn_rarity = 2    #TODO: Шанс на появление клетки в ячейке == (1 к spawnspawn_rarity) 

rule_b = [3]        #TODO: Требуется соседей на рождение
rule_s = [2, 3]     #TODO: Требуется соседей для выживания

x = 185             #TODO: Defoult => 185
y = 45              #TODO: Defoult => 45

theme = 'light'     #TODO: light = НЕЖивые клетки Белые [light/dark]
                    #TODO: dark = НЕЖивые клетки Черные [light/dark]

update_mode = 'hand'#TODO: hamd = Нужно нажать Enter для обновления поля
                    #TODO: auto = Обновляется в определнный срок
update_time = 0.5   #TODO: Частота обновления в секундах