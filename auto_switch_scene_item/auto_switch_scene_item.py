import obspython as obs

import getpixelcolor


def script_description():
    # Description du script qui sera affiché dans OBS
    return "Pour changer automatiquement de scènes"


# Méthode appelée au chargement du script
def script_load(settings):
    # Appelle la fonction "update_scenes" toutes les secondes (valeur définie en ms)
    obs.timer_add(update_scenes, 1000)


def update_scenes():
    print("-- update_scenes --")

    # Récupère la scène par son nom (ici stream_scene)
    stream_scene = obs.obs_get_scene_by_name("stream_scene")

    # Récupère la couleur moyenne dans la zone définie (x, y, width, height) et la compare. (Couleurs au format RVB)
    is_fight = (getpixelcolor.average(1131,561,578,55) == (43, 43, 43))

    # Récupère l'item dans la scène stream_scene portant le nom fighting_scene
    fighting_scene = obs.obs_scene_find_source(stream_scene, "fighting_scene")
    # Switch la visibilité de l'item fighting_scene (false <-> true)
    obs.obs_sceneitem_set_visible(fighting_scene, is_fight)

    # Récupère l'item dans la scène stream_scene portant le nom other_scene
    other_scene = obs.obs_scene_find_source(stream_scene, "other_scene")
    # Switch la visibilité de l'item other_scene (false <-> true)
    obs.obs_sceneitem_set_visible(other_scene, not is_fight)
