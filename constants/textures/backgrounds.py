import pygame
from lib.drawer import VideoReader, CutScene

# Фоновые текстуры
ruins = pygame.image.load(r"assets\images\background\ruins.png").convert_alpha()
shop = pygame.image.load(r"assets\images\background\shop.png").convert_alpha()
buildings = pygame.image.load(r"assets\images\background\buildings.png").convert_alpha()
broken_robot = pygame.image.load(r"assets\images\background\broken_robot.png").convert_alpha()
lab_mais = pygame.image.load(r"assets\images\background\mais_lab.png").convert_alpha()
parlament = pygame.image.load(r"assets\images\background\parlament.png").convert_alpha()
city_ruins = pygame.image.load(r"assets\images\background\city_ruins.png").convert_alpha()
aboba = pygame.image.load(r"assets\images\background\aboba.png").convert_alpha()
velicolepnoye = pygame.image.load(r"assets\images\background\in_the_heart_of_japan.png").convert_alpha()
shelter = pygame.image.load(r"assets\images\background\shelter.png").convert_alpha()
explosion = pygame.image.load(r"assets\images\background\explosion.png").convert_alpha()
city_center = pygame.image.load(r"assets\images\background\city_center.png").convert_alpha()
angar = pygame.image.load(r"assets\images\background\angar.png").convert_alpha()
corporation_lab = pygame.image.load(r"assets\images\background\corporation_lab.png").convert_alpha()
america_rooftops = pygame.image.load(r"assets\images\background\america_rooftops.png").convert_alpha()
fight_tip = pygame.image.load(r"assets\images\background\fight_tip.png").convert_alpha()
main_menu = pygame.image.load(r"assets\images\background\menu.png").convert_alpha()
options_menu = pygame.image.load(r"assets\images\background\options.png").convert_alpha()
adymnar = pygame.image.load(r"assets\images\background\abdolbnar.png").convert_alpha()
adymnar_2050 = pygame.image.load(r"assets\images\background\abdolbnar_2050.png").convert_alpha()
kazan_city = pygame.image.load(r"assets\images\background\city_kazan.png").convert_alpha()
kazan_city_2050 = pygame.image.load(r"assets\images\background\city_kazan_2050.png").convert_alpha()
moiseev_collider = pygame.image.load(r"assets\images\background\collider.png").convert_alpha()
moiseev_garage = pygame.image.load(r"assets\images\background\garage.png").convert_alpha()
iskhakov_industries = pygame.image.load(r"assets\images\background\iskhakov_ind.png").convert_alpha()
daun_corp = pygame.image.load(r"assets\images\background\daun_corp.png").convert_alpha()
daun_corp_2050 = pygame.image.load(r"assets\images\background\daun_corp2.png").convert_alpha()
saratov_iskhakov = pygame.image.load(r"assets\images\background\saratov_iskhacov.png").convert_alpha()
saratov_moiseev = pygame.image.load(r"assets\images\background\moiseev_house.png").convert_alpha()
lab_mais_tutorial = pygame.image.load(r"assets\images\background\mais_lab_tutorial.png").convert_alpha()
bunker = pygame.image.load(r"assets\images\background\bunker.png").convert_alpha()
portal = pygame.image.load(r"assets\images\background\portal.png").convert_alpha()
portal_albina = pygame.image.load(r"assets\images\background\portal_albina.png").convert_alpha()
saratov_cinema = pygame.image.load(r"assets\images\background\cinema.png").convert_alpha()
canals = pygame.image.load(r"assets\images\background\canals.png").convert_alpha()
kazan_afterwar = pygame.image.load(r"assets\images\background\kazanwar.png").convert_alpha()
kremlin = pygame.image.load(r"assets\images\background\kremlin.png").convert_alpha()
subway = pygame.image.load(r"assets\images\background\subway.png").convert_alpha()
angar2 = pygame.image.load(r"assets\images\background\angar2.png").convert_alpha()
bulat_lab = pygame.image.load(r"assets\images\background\bulat_lab.png").convert_alpha()
america_streets = pygame.image.load(r"assets\images\background\america_rooftops.png").convert_alpha()
destroyed_iskhakov = pygame.image.load(r"assets\images\background\saratov_ruins.png").convert_alpha()
american_collider = pygame.image.load(r"assets\images\background\american_collider.png").convert_alpha()
broken_conveyer = pygame.image.load(r"assets\images\background\broken_conveyer.png").convert_alpha()
japan_lisa_fight = pygame.image.load(r"assets\images\background\japan_lisa_fight.png").convert_alpha()

yellow = pygame.image.load(r"assets\images\background\yellow.png").convert_alpha()
black = pygame.image.load(r"assets\images\background\black.png").convert_alpha()
blue = pygame.image.load(r"assets\images\background\blue.png").convert_alpha()

loading_screen = pygame.image.load(r"assets\images\background\loading_screen.png").convert_alpha()
online_menu = pygame.image.load(r"assets\images\background\world_collapse.png").convert_alpha()
choose_hero = pygame.image.load(r"assets\images\background\hero_pick.png").convert_alpha()
hero_pick_menu = pygame.image.load(r"assets\images\background\hero_pick_menu.png").convert_alpha()
bulat_boss = pygame.image.load(r"assets\images\background\bulat_boss.png").convert_alpha()
lisa_boss = pygame.image.load(r"assets\images\background\lisa_boss.png").convert_alpha()
bulat_smile = pygame.image.load(r"assets\images\background\bulat_smile.png").convert_alpha()

# видео фоны
game_menu_animated = r"assets\images\animated_background\city_kazan.mp4"
war_kazan = VideoReader(r"assets\images\animated_background\war_kazan.mp4")
moiseev_collider_animated = VideoReader(r"assets\images\animated_background\moiseev_collider.mp4")
collider_top_1 = VideoReader(r"assets\images\animated_background\collider_top_2.mp4")
collider_top_2 = VideoReader(r"assets\images\animated_background\collider_top.mp4")
angar_animated = VideoReader(r"assets\images\animated_background\angar.mp4")
bulats_robot = VideoReader(r"assets\images\animated_background\center_robot.mp4")
africa_conveyer = VideoReader(r"assets\images\animated_background\africa_conveyer.mp4")
portal_final_battle = VideoReader(r"assets\images\animated_background\portal.mp4")
destroyed_daun_corp = VideoReader(r"assets\images\animated_background\iskhakov_corp_destroyed.mp4")

bgs = [ruins, shop, buildings, broken_robot, lab_mais, parlament, city_ruins, aboba,
       velicolepnoye, shelter, explosion, city_center, yellow, fight_tip]

# cut-scenes
briff_war = CutScene(r"assets\images\cut_scenes\se2_short_brief_2.mp4",
                     r"assets\images\cut_scenes\se2_short_brief_2.mp3")
end_cutscene_1 = CutScene(r"assets\images\cut_scenes\final_cutscene_1.mp4",
                          r"assets\images\cut_scenes\final_cutscene_1.mp3")
