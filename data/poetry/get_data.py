
import glob
import json

# datas = glob.glob("../../chinese-poetry/全唐诗/poet.*.json");
datas = glob.glob("../../chinese-poetry/曹操诗集/*.json");
for data in datas:
    with open(data, 'r', encoding='utf-8') as fp:
        poets = json.load(fp)
        for poet in poets:
            with open("poetry.txt", "a", encoding="utf-8") as f:
                f.write(''.join(poet['paragraphs']))
                f.write("\n")
