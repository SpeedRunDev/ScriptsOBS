import obspython as obs
import getpixelcolor
import time
from contextlib import contextmanager


def script_description():
    # Description du script qui sera affiché dans OBS
    return "Pour changer automatiquement de scènes"

def script_load(settings):
    print("LOAD")

    obs.obs_frontend_add_event_callback(on_event)
    obs.timer_add(update_scenes, 500)

def on_event(event):
    print(event)

    if event == obs.OBS_FRONTEND_EVENT_SCENE_COLLECTION_CHANGING:
        print("OBS_FRONTEND_EVENT_SCENE_COLLECTION_CHANGING")

        obs.obs_frontend_remove_event_callback(on_event)
        obs.timer_remove(update_scenes)
        print("--->sOBS_FRONTEND_EVENT_SCENE_COLLECTION_CHANGING")

@contextmanager
def get_scene_by_name_auto_release(source_name):
    scene = obs.obs_get_scene_by_name(source_name)
    try:
        yield scene
    finally:
      try:
        obs.obs_scene_release(scene)
      except Exception as e:
        logging.error(traceback.format_exc())
      except Error as e:
        logging.error(traceback.format_exc())

@contextmanager
def scene_find_source_auto_release(scene, source_name):
    source = obs.obs_scene_find_source(scene, source_name)
    try:
        yield source
    finally:
         obs.obs_sceneitem_release(source)

@contextmanager
def update_scenes():
    print('coucou')
    with get_scene_by_name_auto_release("DQ9withScriptSwitch") as stream_scene:

      is_fight = (getpixelcolor.average(97, 303, 200, 5) == (182, 120, 59))

      fighting_scene = obs.obs_scene_find_source(stream_scene, "speedrun (haut)")
      obs.obs_sceneitem_set_visible(fighting_scene, is_fight)

      #with scene_find_source_auto_release(stream_scene, "speedrun (haut)") as fighting_scene:
        #print(fighting_scene)
        # obs.obs_sceneitem_set_visible(fighting_scene, is_fight)
        #print('toto')

      other_scene = obs.obs_scene_find_source(stream_scene, "speedrun (bas)")
      obs.obs_sceneitem_set_visible(other_scene, not is_fight)
      #with scene_find_source_auto_release(stream_scene, "speedrun (bas)") as other_scene:
        # obs.obs_sceneitem_set_visible(other_scene, not is_fight)
        #print('toto')
      obs.obs_sceneitem_release(fighting_scene)
      obs.obs_sceneitem_release(other_scene)



