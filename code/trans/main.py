import pprint
from collections import defaultdict

from tools import get_all_trans, zh_mapping, get_en_mapping


def trans(lang="zh-TW"):
    untrans_ts_path = f"/home/t/workspace/kiosk-web-src/src/language/{lang}/cer-shopflow/index.ts"
    with open(untrans_ts_path, "r") as f:
        untrans_content = f.read()

    tran_mapping = get_all_trans()
    en_mapping = get_en_mapping()
    lang_suffix = lang[:2]


    missing = defaultdict(dict)
    for k, v in zh_mapping.items():
        # print(k)
        for sub, zh_content in v.items():
            if sub not in untrans_content:
                en_content = en_mapping.get(sub)

                trans_detail = zh_content
                if orig_trans := tran_mapping.get(en_content):
                    trans_detail = orig_trans.get(lang_suffix)
                    missing[k][sub] = f"'{trans_detail}', // "
                else:
                    missing[k][sub] = f"'{trans_detail}', //cn "

    for kk, vv in missing.items():
        print("{}: {{".format(kk))
        for k, v in vv.items():
            print(f"\t{k}: {v}")
        print("}\n")

    print(len(missing))

    # pprint.pprint(missing)


trans()