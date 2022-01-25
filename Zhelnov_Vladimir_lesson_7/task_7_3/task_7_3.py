"""
Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).

python3 task_7_2.py my_config.indent

Написать скрипт, который собирает все шаблоны в одну папку templates, например:

|--my_project
   ...
   |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html

"""

import shutil
import os


project_folder = os.path.join(os.getcwd(), 'my_project')
templates_folder = os.path.join(project_folder, 'templates')

# Создать папку со всеми шаблонами
if not os.path.exists(templates_folder):
    os.makedirs(templates_folder)

for root, dirs, files in os.walk(project_folder):
    # Сужаем круг путей
    if 'templates' in root and len(files) > 0:
        basename = os.path.basename(root)
        # Исключаем неверно созданные папки таких как wrongapp
        if basename != 'templates' and root.count(basename) == 2:
            try:
                shutil.copytree(root, os.path.join(templates_folder, basename))
                print('copied namespace:', os.path.relpath(root, os.getcwd()))
            except FileExistsError:
                pass

# Просматриваем
for root, dirs, files in os.walk(templates_folder):
    for file in files:
        print(os.path.relpath(os.path.join(root, file), os.getcwd()))


# Работать конечно будет только с указанной нами структурой
# если структура файлов будет сложнее, надо переделать, не встречал django проектов
"""
copied namespace: my_project\authapp\templates\authapp
copied namespace: my_project\mainapp\templates\mainapp
copied namespace: my_project\testapp\templates\testapp
my_project\templates\authapp\base.html
my_project\templates\authapp\index.html
my_project\templates\mainapp\base.html
my_project\templates\mainapp\index.html
my_project\templates\testapp\index.html
"""