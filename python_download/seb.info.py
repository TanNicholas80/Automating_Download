from pywinauto.application import Application
import os

classroom_exe = "Classroom_Spy.exe"
classroom_dir = os.path.abspath(classroom_exe)
classroom_dir_escape = classroom_dir.replace("\\", "\\\\")

app = Application().start(classroom_dir_escape)
automation = Application(backend="uia").connect(path=classroom_dir_escape, title="classroom")

app.top_window().minimize()

jendela_utama = automation.window(title="Classroom Spy Pro Setup")

jendela_utama.Button.click()

judul_jendela = automation.window().wrapper_object().window_text()

jendela_berikutnya = automation.window(title=judul_jendela)

jendela_berikutnya.Button2.click()

judul_jendela2 = automation.window().wrapper_object().window_text()

jendela_berikutnya2 = automation.window(title=judul_jendela2)

jendela_berikutnya2.CheckBox.click()

jendela_berikutnya2.Button5.click()