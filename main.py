import dearpygui.dearpygui as dpg
import getpass
from jluksfiles import *
from Jlukscfg import *
import subprocess

username = getpass.getuser()
JJFile = Jfile("C:\\Users\\" + username + "\\AppData\\LocalLow\\Paragon launcher")
JJCFG = Jcfg(JJFile.path_to_dir)

def get_pdata():
    dpg.configure_item("modal", show=False)
    print(game_path)
    if game_path != '':

        dpg.set_value("messange","Download starts.")
        JJFile.download_from_git("https://github.com/SwimUp/ProjectParagonRelease/archive/refs/heads/1.4.zip",JJFile.path_to_dir)
        dpg.set_value("messange","Extracting zip...")
        JJFile.extract_zip(os.path.join(JJFile.path_to_dir,"ProjectParagonRelease-1.4.zip"),JJFile.path_to_dir)

        dpg.set_value("messange","Creating mods folder backup...")
        JJFile.create_archive(os.path.join(game_path,"Mods"),os.path.join(game_path,"Mods"))
        JJFile.delete_dir_content(os.path.join(game_path,"Mods"),True,False)

        dpg.set_value("messange","Creating Config backup...")
        path_to_game_cfg = "C:\\Users\\" + username + "\\AppData\\LocalLow\\Ludeon Studios\\RimWorld by Ludeon Studios"

        JJFile.create_archive(os.path.join(path_to_game_cfg,"Config"),os.path.join(path_to_game_cfg,"Config"))
        JJFile.delete_dir_content(os.path.join(path_to_game_cfg,"Config"),True,True)        
        
        dpg.set_value("messange","Installing mods...")
        JJFile.move_file(os.path.join(JJFile.path_to_dir,"ProjectParagonRelease-1.4","Mods"),game_path)
        dpg.set_value("messange","Installing config...")
        JJFile.move_file(os.path.join(JJFile.path_to_dir,"ProjectParagonRelease-1.4","ModsConfig.xml"),os.path.join(path_to_game_cfg,"Config"))

        dpg.set_value("messange","Deleting cache...")
        JJFile.delete_file(os.path.join(JJFile.path_to_dir,"ProjectParagonRelease-1.4.zip"))
        JJFile.delete_dir_content(os.path.join(JJFile.path_to_dir,"ProjectParagonRelease-1.4"),True,False)
        dpg.set_value("messange","All done!")
    else:
        dpg.set_value("messange","Please, enter game folder.")


def Initialization():
    global game_path
    game_path = JJCFG.get_value("options","game folder")


def update_game_path(sender,app_data):
    global game_path
    game_path = app_data.get("current_path")
    JJCFG.save_value(game_path,"options","game folder")


def run_game():
    dpg.set_value("messange","Starting exe...")
    try:
        subprocess.run(os.path.join(game_path,"RimWorldWin64.exe"))
        dpg.set_value("messange","Game started, enjoy!")
    except:
        dpg.set_value("messange","Something went wrong, please,\n enter right path to game.")
    


dpg.create_context()
with dpg.window(tag="paragon launcher V101A",no_resize=True):
    with dpg.tab_bar():
        with dpg.tab(label="main"):
            with dpg.group(horizontal=True):
                dpg.add_button(label="Play"         , pos=[670 / 2 - 310, 455 / 2 - 150], width=100,height=50, callback=run_game)
                dpg.add_button(label="install"      , pos=[670 / 2 - 310, 455 / 2 - 90] , width=100,height=50, callback=lambda: dpg.configure_item("modal", show=True))
                dpg.add_button(label="select folder", pos=[670 / 2 - 310, 455 / 2 - 30] , width=100,height=50, callback=lambda: dpg.configure_item("entergamepath", show=True))
                dpg.add_text("Paragon launcher \n V1.0.1-A", pos = [280,150])
                dpg.add_text("", pos = [280,179],tag="messange")

dpg.add_file_dialog(tag="entergamepath",directory_selector=True,show=False,width=600 ,height=350,callback=update_game_path)

with dpg.window(label="Reinstall packet?", modal=True, show=False, tag="modal",no_resize=True, no_title_bar=True,width=325,height=105,pos=[167,113.7]):
    dpg.add_text("Are you sure you want to install the build?\n This will take some time and require stable \ninternet traffic, your configs and mod folder\n will be backed up.")
    dpg.add_separator()
    with dpg.group(horizontal=True, pos=[82,76]):
        dpg.add_button(label="OK", width=75, callback=get_pdata)
        dpg.add_button(label="Cancel", width=75, callback=lambda: dpg.configure_item("modal", show=False))

dpg.create_viewport(title = "main", width=670, height=455)
dpg.set_primary_window("window",True)

Initialization()

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()







