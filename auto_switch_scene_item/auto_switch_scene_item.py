import obspython as obs
import getpixelcolor
import time

def script_description():
    # Description du script qui sera affiché dans OBS
    return "Pour changer automatiquement de scènes"

def script_load(settings):
    print("load 11")
    # Appelle la fonction "update_scenes", avec un paramètre en ms
    obs.timer_add(update_scenes, 500)

    obs.obs_frontend_add_event_callback(on_event)

def on_event(event):
    print(event)
    if event == obs.OBS_FRONTEND_EVENT_SCENE_COLLECTION_CHANGING:
        print("OBS_FRONTEND_EVENT_SCENE_COLLECTION_CHANGING")

        obs.obs_frontend_remove_event_callback(on_event)
        obs.timer_remove(update_scenes)
        time.sleep(3)
        stream_scene = obs.obs_get_scene_by_name("DQ9withScriptSwitch")
        fighting_scene = obs.obs_scene_find_source(stream_scene, "speedrun (haut)")
        other_scene = obs.obs_scene_find_source(stream_scene, "speedrun (bas)")
        obs.obs_scene_release(stream_scene)
        obs.obs_sceneitem_release(fighting_scene)
        obs.obs_sceneitem_release(other_scene)
        time.sleep(3)

        print("--->sOBS_FRONTEND_EVENT_SCENE_COLLECTION_CHANGING")

def update_scenes():
    print('coucou')
    # https://docs.obsproject.com/reference-core?highlight=obs_get_scene_by_name#c.obs_get_scene_by_name
    # OBS_FRONTEND_EVENT_SCENE_COLLECTION_CHANGING - https://docs.obsproject.com/reference-frontend-api?highlight=paused#functions
    # Récupère la scène par son nom (ici stream_scene)
    stream_scene = obs.obs_get_scene_by_name("DQ9withScriptSwitch")

    is_fight = (getpixelcolor.average(97, 303, 200, 5) == (182, 120, 59))

    # Récupère l'item dans la scène stream_scene portant le nom fighting_scene
    fighting_scene = obs.obs_scene_find_source(stream_scene, "speedrun (haut)")
    # Switch la visibilité de l'item fighting_scene (false <-> true)
    obs.obs_sceneitem_set_visible(fighting_scene, is_fight)

    # Récupère l'item dans la scène stream_scene portant le nom other_scene
    other_scene = obs.obs_scene_find_source(stream_scene, "speedrun (bas)")
    # Switch la visibilité de l'item other_scene (false <-> true)
    obs.obs_sceneitem_set_visible(other_scene, not is_fight)