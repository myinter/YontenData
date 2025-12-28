# ================================================================
# Copyright © 2014 Bighiung.
# All rights reserved.
#
# 版权所有 © 2014 Bighiung，保留所有权利。
#
# Created by Bighiung on 2014/10/18.
#
# ================================================================

import json
import sqlite3
from pathlib import Path

# ========= 数据库文件和生成结果输出路径 =========
BASE_DIR = Path(__file__).parent
DB_PATH = BASE_DIR / "kuangJyon.sqlite"
OUT_PATH = Path("/yondoData")
OUT_PATH.mkdir(parents=True, exist_ok=True)
OUT_FILE = OUT_PATH / "yondo.json"

# ========= 常量 =========
SJiengDeu = ["平声", "上声", "去声", "入声"]
LEVELS = ["一", "二", "三", "四"]
KHEEIGHEEP = ["開", "合"]

# ========= 涉及重钮的韵和声母 =========
DIUNG_NIU_YON = "支脂之微魚齊祭真仙宵侵鹽"
DIUNG_NIU_SJIANG_MO = "見溪群疑曉匣影以"

# ========= 读取 声母和韵类的JSON =========
with open(BASE_DIR / "Sjiengnjiu.json", encoding="utf-8") as f:
    SArray = json.load(f)

with open(BASE_DIR / "yonNjiu.json", encoding="utf-8") as f:
    YArray = json.load(f)

# ========= 数据库 =========
conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# ========= 主逻辑 =========
yondoDict = {}

# 遍历每一个韵类的数组，每个韵类的占用一张表
for yonTitle, yonDict in YArray.items():

    outputDict = {}
    outputDict["韻"] = yonTitle

    # ========= 当前韵表的项，是否涉及重钮 =========
    AB = bool(yonDict.get("AB", False))
    # ========= 当前韵表的项，涉及的调类 =========
    sjiangDeuDict = yonDict["四声"]

    yonTable = {}

    # ========= 各个调类分别查询 =========
    for deuLyi in SJiengDeu:
        deuLyiOut = {}

        # ========= 开合口分别查询 =========·
        for openClose in KHEEIGHEEP:
            openCloseOut = {}

            for teeng in LEVELS:
                SjiengCharDict = {}

                # ========= 获取当前韵，当前调类下包含的等 =========
                yon = (
                    sjiangDeuDict
                    .get(deuLyi, {})
                    .get(f"{teeng}等")
                )

                # ========= 韵部名称统一使用平声的韵名 =========
                yonpo = (
                    sjiangDeuDict
                    .get("平声", {})
                    .get(f"{teeng}等")
                )

                if yonpo is None:
                    if yon and deuLyi == "去声":
                        yonpo = yon
                    else:
                        continue

                SjiengCharDict["韻"] = yon


                for sjiengMo in SArray:
                    # ===== 兼容广韵全字表使用的异体字 =====
                    condiSjiengmo = "群" if sjiengMo == "羣" else sjiengMo
                    # ===== 重钮 A/B类分别检索 =====
                    if (
                        AB
                        and yonpo in DIUNG_NIU_YON
                        and sjiengMo in DIUNG_NIU_SJIANG_MO
                    ):
                    # ===== 根据等--韵部-声钮-开合-调类 查询填写到韵图上的字 =====
                        for suffix in ("A", "B"):
                            sql = """
                            SELECT CHAR FROM Jyonten
                            WHERE Teeng=?
                              AND JyonPo=?
                              AND SjengNjiu=?
                              AND KaiGhap=?
                              AND SjiengDeu=?
                            LIMIT 1
                            """
                            cursor.execute(
                                sql,
                                (
                                    teeng,
                                    yonpo + suffix, # ===== 重钮韵需要加上A/B后缀 ====
                                    condiSjiengmo,
                                    openClose,
                                    deuLyi[0],
                                ),
                            )
                            row = cursor.fetchone()
                            SjiengCharDict[sjiengMo + suffix] = (
                                row["CHAR"] if row else ""
                            )

                    else:
                        if yonpo in DIUNG_NIU_YON:
                            # ===== 为了兼容广韵全字表，对非重钮声母下的重钮韵也添加的A/B，所以也添加后缀予以兼容 ====
                            yonCondition = "(JyonPo=? OR JyonPo=?)"
                            params = [yonpo + "A", yonpo + "B"]
                        else:
                            yonCondition = "JyonPo=?"
                            params = [yonpo]

                        sql = f"""
                        SELECT CHAR FROM Jyonten
                        WHERE Teeng=?
                          AND {yonCondition}
                          AND SjengNjiu=?
                          AND KaiGhap=?
                          AND SjiengDeu=?
                        LIMIT 1
                        """

                        cursor.execute(
                            sql,
                            [teeng, *params, sjiengMo, openClose, deuLyi[0]],
                        )
                        row = cursor.fetchone()
                        SjiengCharDict[sjiengMo] = row["CHAR"] if row else ""

                openCloseOut[teeng] = SjiengCharDict

            deuLyiOut[openClose] = openCloseOut

        yonTable[deuLyi] = deuLyiOut

    outputDict["小韻表"] = yonTable
    yondoDict[yonTitle] = outputDict

# ========= 输出 =========
with open(OUT_FILE, "w", encoding="utf-8") as f:
    json.dump(yondoDict, f, ensure_ascii=False, indent=2)

conn.close()