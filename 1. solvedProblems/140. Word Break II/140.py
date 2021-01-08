# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Tue, 12/08/2020, 04:18
# !! Description:

"""
import sys
from typing import List

sys.path.append('..')
from utils import binaryTree, nTree, singleLinkedList
from utils.utils import (
    printMatrix,
    printDict,
    printList,
    isMatrix,
)

ListNode = singleLinkedList.ListNode
TreeNode = binaryTree.TreeNode
Node = nTree.Node
null = None
testCaseCnt = 6
# maxFuncInputParaCnt = 8

# !! step1: replace these two lines with the given code
class Solution:
    """
    https://leetcode-cn.com/problems/word-break-ii/solution/python3ji-yi-hua-sou-suo-tian-jia-3xing-dai-ma-1ge/
    """

    def wordBreak1(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        memo = [1] * (len(s) + 1)
        failedPos = set()
        wordDict = set(wordDict)

        def dfs(wordDict, temp, pos):
            num = len(res)                  # 回溯前先记下答案中有多少个元素
            if pos == len(s):
                res.append(" ".join(temp))
                return
            for i in range(pos, len(s) + 1):
                if i not in failedPos and s[pos:i] in wordDict:  # 添加备忘录的判断条件
                # if memo[i] and s[pos:i] in wordDict:  # 添加备忘录的判断条件
                    temp.append(s[pos:i])
                    dfs(wordDict, temp, i)
                    temp.pop()
            # 答案中的元素没有增加，说明s[pos:]不能分割，修改备忘录
            # memo[pos] = 1 if len(res) > num else 0
            if len(res) > num:
                failedPos.add(pos)

        dfs(wordDict, [], 0)
        return res

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        rlt = []
        selected = set()
        memo = [1] * (len(s) + 1)

        def bt(s, selection, pos):
            if not s:
                rlt.append(' '.join(selection))
                return

            n = len(s)
            rltCnt = len(rlt)
            for i in range(n):
                left = s[:i + 1]
                right = s[i + 1:]
                if left in wordDict:
                    # if i in selected: continue
                    if not memo[i]: continue
                    bt(right, selection + [left], pos + i)
            memo[pos] = 1 if len(rlt) > rltCnt else 0
            # if len(rlt) == rltCnt:
                # selected.add(pos)

        bt(s, [], 0)
        return sorted(rlt)
    # endFunc
# endClass

def func():
    # !! step2: change function name
    s = Solution()
    myFuncLis = [
        s.wordBreak,
        # optional: add another function for comparison
    ]

    onlyDisplayError = True
    enableInput = [True] * testCaseCnt
    input = [None] * testCaseCnt
    expectedRlt = [None] * testCaseCnt
    enableInput[0] = False
    enableInput[1] = False
    enableInput[2] = False
    # enableInput[3] = False
    # enableInput[4] = False
    # enableInput[5] = False

    # !! step3: change input para, input para can be found in "run code" - "test case"
    # ! para1
    input[0] = (
        "catsanddog",
        ["cat", "cats", "and", "sand", "dog"],
        # binaryTree.buildTree(
        #     None
        # ),
        #
        # singleLinkedList.buildSingleList(
        #     None
        # ),
        #
        # nTree.buildTree(
        #     None
        # ),
    )
    expectedRlt[0] = None

    # ! para2
    input[1] = (
        "aaaaaaa",
        ["aaaa", "aa", "a"],
        #         # binaryTree.buildTree(
        #     None
        # ),
        #
        # singleLinkedList.buildSingleList(
        #     None
        # ),
        #
        # nTree.buildTree(
        #     None
        # ),,
        # singleLinkedList.buildSingleList(None),
        # nTree.buildTree(None),
    )
    expectedRlt[1] = sorted(["a a a a a a a", "aa a a a a a", "a aa a a a a", "a a aa a a a", "aa aa a a a", "aaaa a a a", "a a a aa a a", "aa a aa a a", "a aa aa a a", "a aaaa a a", "a a a a aa a", "aa a a aa a", "a aa a aa a", "a a aa aa a", "aa aa aa a", "aaaa aa a", "a a aaaa a", "aa aaaa a", "a a a a a aa", "aa a a a aa", "a aa a a aa", "a a aa a aa", "aa aa a aa", "aaaa a aa", "a a a aa aa", "aa a aa aa", "a aa aa aa", "a aaaa aa", "a a a aaaa", "aa a aaaa", "a aa aaaa"])

    # ! para3
    input[2] = (
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"],
        # singleLinkedList.buildSingleList(None),
        #         # binaryTree.buildTree(
        #     None
        # ),
        #
        # singleLinkedList.buildSingleList(
        #     None
        # ),
        #
        # nTree.buildTree(
        #     None
        # ),,
        # nTree.buildTree(None),
    )
    expectedRlt[2] = None

    # ! para4
    input[3] = (
        "fajbeokiakfmlacbinjdnjdmmfha",
        ["be", "ellaekgjhibcomc", "ahaklkan", "jcm", "lchidklmcone", "ljmdgagaen", "giioojldjkfnno", "el", "eibjaffacjll", "hn", "hbjakhjneml", "foi", "nbhf", "aigf", "cfdlnc", "fa", "amakgofedhkghgl", "ddhmhdhioh", "ijoddeabbiei", "giamcgco", "nholghlfbbendi", "emlc", "m", "elgibme", "behkignjenmh", "lodkkjgioe", "doe", "hgflgakna", "macghogdidmdm", "ec", "kncigolkog", "ljooio", "lch", "gkaclkbjn", "ofiaglfoffl", "alhfbb", "cfmdbgo", "cfcnajknk", "jfh", "almbgdjnbbbgmhb", "dmlnnohf", "olojeejfafc", "ndgcmgoe", "cmkdjilfeo", "bengdd", "enfg", "dbngiggni", "anmkljn", "njdnjdmmfha", "ndimmddfmhe", "hmkdjkhhiilnf", "ehd", "jfdl", "dlgki", "bhoflnomibkki", "lg", "fjojjnnkdfenhol", "lefhhl", "nimdl", "gejgomblmim", "ahbnlmlfmejjj", "glhacaojnf", "mfjdhnhdkm", "do", "fnh", "mnmjdk", "hfjgdlnnb", "hniolfhkhbie", "ldgodonogcab", "mabjnnohnijhn", "aceojlkmdg", "aedfljg", "cehk", "jag", "oniegflnhje", "jo", "maokc", "jkbndc", "djbn", "dajkdblojkf", "dmen", "kcdjdocinenc", "cgindbm", "h", "odaof", "cmogcbgj", "anjahlgbbmba", "haoe", "ggacnminj", "ilcfjoedhe", "klookammgofl", "onnmenn", "mbdneaioo", "jc", "dekgil", "bjdfibfd", "hfbnlgmlllcb", "afebehf", "obekljbnh", "eoaedhjk", "nobamccd", "mdieojoknf", "komcglmakkaa", "jcliimcc", "jmmgbmha", "gdogjnn", "ednembco", "dgno", "jiaheeabifahfmo", "djkcgnakkh", "kdkiglgf", "eb", "fmdnlhj", "eicohdciejc", "jgofmankkf", "o", "nnmomkmkmiaoga", "njchkccln", "ndamha", "eleanmojdi", "ebkl", "jcageehlelcg", "acfddofjihgmn", "iklaomfhjm", "io", "igmob", "lfnhnlnigbbignk", "anihfojmedf", "nj", "oilcabalhb", "adjfbkfjch", "lbfb", "mgfnngfccb", "jhmhggm", "dnllc", "c", "ljim", "jmikd", "mdfimdgac", "fhbclgo", "edclcdia", "nelmfjejff", "i", "cmcbbckdnjcoo", "cddocce", "hc", "keh", "keofhnhemd", "biln", "mjcnbjmkikon", "fekbdnkolahh", "hkfmjbj", "mjoj", "jn", "ilof", "ifhfk", "aofmg", "nofljgmmmf", "hcdifeiclbchlf", "imlijgdg", "ocdiiemcmbkglm", "nhoekmlkjfoa", "kibffkbleedda", "kdhdjekccbkc", "bcbflcag", "jekmkdimnnjjoo", "mmgfljchalbem", "kchk", "oi", "ncf", "jembgfa", "l", "kfkeianmmmdacl", "ecjkkfggj", "jdgcfnhfjonkhig", "jhagiokii", "nifm", "bbjjlj", "adajlokomibfg", "ojk", "lockdel", "bh", "hoojolglchck", "conko", "eadi", "kfigoijnfimolen", "g", "dbnj", "cojkbmo", "hh", "mcdbh", "ngdmgioen", "ehjagfohnolkho", "dgfgdlc", "aoglneoh", "gbc", "ijjckddeicld", "imekih", "liiaecniil", "hahejbhgiclb", "fnmojm", "ablihjhggiahhno", "colloaakco", "jhobddaanbhmlg", "cbfajfhkoh", "cim", "laghknigabn", "dcbnbkegkjam", "gem", "ljjim", "icclogji", "omidhe", "f", "giiaclfcjkagl", "ndcjldekjnkekm", "aiikdccohcj", "mkbmb", "oomhhafobic", "bkacdjfgbggn", "ahghdoahbi", "hedm", "eeoj", "bdgdlfollegej", "eg", "dfeb", "dkffkid", "hcne", "gjkohnaaabn", "jfeododjgdhlfbf", "clfkmconnkfb", "abnbkcni", "hk", "ghnmhjm", "oibjibmkaibdefa", "hjambim", "oe", "aao", "jil", "fmhomflfen", "hlidcklnmb", "hiaonkhd", "bibbmkandf", "hke", "bmfcionm", "inhcnlkbkkmjicn", "jckjedhgoghi", "chmik", "mnjldknhaec", "hocbccbg", "ljadj", "lciikgnlj", "ifjjhkbhifione", "foikblanoco", "ode", "mjc", "fhklofh", "mmoklkkog", "hocbojmhffeajo", "ccmmd", "bkkh", "nhhgcflniebkme", "lfohikenfbjacli", "cmehijnihijgng", "caa", "bmk", "emofof", "jjagiogohfab", "ibh", "eoacdlnodalkjbl", "cbbjbbnjom", "iljiomeloehen", "gignlngclmh", "b", "ll", "dokgngnocde", "cienegffibgieba", "agbachloidg", "mlelnafokd", "nmcmka", "akeogjbjcnf", "nebdic", "a", "efc", "ljdk", "jhcag", "bkbikbjgae", "mcjlgjeo", "lo", "dbiofobl", "cehebiljff", "eeagngm", "ondahcjiel", "coblanndhlhoggj", "jaobmjml", "jfejjinofek", "hhnna", "gdhcn", "acelcomgkgohm", "njkkjkkln", "jmc", "hkekoho", "boefec", "cioibfgjmhb", "ebggdbeimn", "emhg", "cfghkhii", "d", "k", "khoddedia", "nhje", "eebkfml", "bohhd", "kg", "n", "ilgemokdehcbaif", "cldicda", "einij", "akmabcgfn", "fmkmcn", "bnlfbagkke", "oakbgjejmcncj", "iehdfadgoik", "kkcfo", "jmjkmfcacjjnd", "ndokhh", "hjfeelhckkjjmj", "dnomohejbodkb", "jcmblncjadno", "oiofcodobiml", "ddmillkncjfdfj", "aihenmkdnhdhkhf", "bfdbakeilfdojnc", "jjhbkbne", "aigabk", "cae", "oednojjb", "gdoe", "jokjceohkmbm", "offkanbahigo", "kfomigbfddjli", "dkkjobgkcejei", "mdilld", "bofkika", "kkinig", "cljcflbghjmhmke", "kmbjlgdcbdjn", "bkgbmoahda", "kmnajjdemggnfg", "mgjndldil", "iemb", "kehaokgjg", "icign", "oijmaolehmoo", "amhgldifmgekhe", "diacnollhi", "lnjhdaafadl", "bdfiackhogoje", "ebjlfa", "deabkgfhnead", "gadcob", "haa", "dbhnbhjcmmab", "bbmjainilbbej", "dc", "bgjgafnjjflne", "ehholgnn", "fmhccbnc", "mdnfl", "feeejdgc", "mfhlobdadooh", "ojna", "gkgjnijdbgo", "ghngnhn", "nhnjaiaadiedgg", "nk", "hmd", "nmbmijaffogl", "onkcgbgmago", "gfli", "ofjlec", "nlfnbkkdc", "hakilani", "bofjdjkhllb", "ocjncleljnecfc", "gdonnkodmkejhf", "fiflchanfllgnf", "kaejakoibgln", "hmdlfioacgaci", "honmfbcog", "mlacbi", "gf", "ejbbemoeha", "acfjegee", "lllflaocnnkeadi", "mdgoebfgacecmbg", "faejgln", "kmlmhffgcmekm", "akcjmgdg", "kmhhh", "fdohjehacdln", "e", "ojba", "ohadmod", "eaenkdiaokl", "dii", "cgfjaklblafeifo", "imoeflkcgbbem", "nbjkmb", "jjgm", "hofgelg", "cnihecmdigdgflg", "fnmikkeldjgb", "onlhgonldjaedh", "fmkdn", "kfbcbleen", "oejioibnmab", "cg", "meadghbocjnj", "hmmdnkegfeieijn", "ijgenomhndlje", "maccdcgfjig", "iabemie", "mlfg", "mdblmdaechmeaml", "dhlafgjo", "eabbiila", "kf", "oehggehfmijlfmg", "klljaejidfhbon", "akmbgmignoag", "jgbkngmigdfm", "kjeelnbn", "ajaa", "mlcjoiaahoiga", "oalnielba", "ffmobgkc", "kmhoknfffdmo", "nagjiffnjhh", "dlehllomjok", "agaejefhdbk", "nnegoijfdj", "ndl", "dhfginocgi", "nflmglgh", "bcd", "gbgjijemmdio", "jk", "gidgjbmb", "hi", "lmgoah", "fdebefcech", "ach", "bahaoj", "ccmmblgibgjahi", "moid", "jhilgedidndm", "ldiakemnj", "bbnibccm", "jkbneoaheaajnm", "clkgmbjlgdnl", "lobbdldifnnijh", "dnmih", "jglia", "didicmghfe", "dlhbcfclf", "akbmioocoihkfh", "foofdldm", "imenimfcame", "ifekbmgnbdkc", "jjlkaabdollola", "gie", "hbaj", "noomfnfccmgaa", "dcjffeg", "nb", "obdb", "lolgjflimkib", "eaiigminlakkb", "cia", "hkf", "jknfklaio", "igklbiomo", "jfjgh", "ekgnkfnhjcch", "kmonfcclieehlik", "oggkmccklnmj", "bedhobcl", "egmnhajcnhcdgb", "imfdhekamfel", "bmmkhfdbm", "gnjfbcjlecfn", "llmkgclm", "gafinbnhfe", "mlbfedkoeeddfao", "kklcdmglleb", "ckekmeiea", "mi", "kfejn", "lm", "mk", "abkoajocfdili", "jidac", "jonhkanccl", "lllodjgnmm", "abfeaodlmjkngol", "cdncnh", "lkcb", "abhilnmmhijab", "hiljkfakojjld", "mbboobkaolkljo", "jhkblobaofgoh", "ncm", "mgbdhmcicomf", "oag", "akmjdd", "abkenodnhj", "mljf", "afb", "afejkobmiffeee", "oollnkilabmb", "gfaocokmcmjlmb", "cokmecdd", "bo", "endocdnmjiek", "bcf", "lhllbagiel", "bhihgofhj", "ffce", "neio", "ofbfiiab", "kjdo", "lgfggnamceeo", "kofledoinamcj", "femhndomndoakoa", "fmodaigcka", "omakggcalhn", "hhhogmcbjnhelkk", "mgah", "jghjjfmk", "ecolelfmcb", "eajjkdncafhhgab", "obno", "fifigfeok", "laafjimienff", "beckbbmhmofb", "nafhihmgnikd", "cbcfnhlkne", "kao", "nlkfhbm", "fmh", "ohfek", "oj", "hifgcgi", "adhkn", "lffgmodeafnn", "ngchmhdbmhmhh", "mcffimhnlffab", "blhmkdhbnhbb", "kkb", "lgkine", "hgfbdbfffanhik", "joebhbh", "img", "kglcddmloo", "hoflgfao", "bdhgdekb", "mggflahnoo", "cmnol", "imnmmgimmedf", "mcjmoofomiia", "mlakhbjfnbmgena", "ilhmcnkkeg", "domhbmkcd", "fco", "fdio", "cmkoagblnd", "kmihfigmceiiicm", "afgbadbgbaon", "menahlemehifooe", "jacokdiiokaic", "limj", "fkedaoomokjbkdi", "jkncd", "jblmcmfnegnk", "jjicjhjhbg", "gbfcead", "jf", "aifnkmnao", "effmhlhchngknl", "odhjeib", "ohcgmgb", "bgbd", "am", "kkjfbdlh", "hgbjakkokjgooel", "jbeokiakf", "flaoba", "cifcdnanmk", "mice", "ihhofdai", "ldnfmeiemhf", "kefbbohhgineacj", "bi", "njfie", "ociodahlomoekkf", "andhoindeca", "ajnndjocjeg", "bmijkmjbbkgbbh", "feanh", "bjemcefkfcaenal", "edfdenghinm", "moal", "ndbjdmijh", "enccnhmoifa", "dbckadjibam", "gd", "oglj", "aldjelhbemle", "cmbkofkcoe", "ihciacibeh", "lcojkclhmibgoif", "jfmjncnolfj", "gfcmcabhjki", "aggfmakaanjb", "mhbelld", "hon", "nkfoikcddehcah", "kggbigknacmohb", "jbkgndofcmaaohh", "gkjano", "afhhhh", "mjng", "jilckm", "dekkedjehmenbm", "clfm", "acmhbkdadgena", "oenokachg", "lhiea", "dceiag", "eebgj", "oolifidh", "dj", "cdfn", "eghdglgiok", "jdhegkefhbdhkm", "mhgngafea", "akabbcjkdnbc", "gcbn", "kimdgahf", "oc"],
        # singleLinkedList.buildSingleList(None),
        #         # binaryTree.buildTree(
        #     None
        # ),
        #
        # singleLinkedList.buildSingleList(
        #     None
        # ),
        #
        # nTree.buildTree(
        #     None
        # ),,
        # nTree.buildTree(None),
    )
    expectedRlt[3] = sorted(["f a jbeokiakf m l a c b i nj d nj d m m f h a", "fa jbeokiakf m l a c b i nj d nj d m m f h a", "f a jbeokiakf m l a c bi nj d nj d m m f h a", "fa jbeokiakf m l a c bi nj d nj d m m f h a", "f a jbeokiakf mlacbi nj d nj d m m f h a", "fa jbeokiakf mlacbi nj d nj d m m f h a", "f a jbeokiakf m l a c b i njdnjdmmfha", "fa jbeokiakf m l a c b i njdnjdmmfha", "f a jbeokiakf m l a c bi njdnjdmmfha", "fa jbeokiakf m l a c bi njdnjdmmfha", "f a jbeokiakf mlacbi njdnjdmmfha", "fa jbeokiakf mlacbi njdnjdmmfha"])

    # ! para5
    input[4] = (
        None
        # singleLinkedList.buildSingleList(None),
        #         # binaryTree.buildTree(
        #     None
        # ),
        #
        # singleLinkedList.buildSingleList(
        #     None
        # ),
        #
        # nTree.buildTree(
        #     None
        # ),,
        # nTree.buildTree(None),
    )
    expectedRlt[4] = None

    # ! para6
    input[5] = (
        None
        # singleLinkedList.buildSingleList(None),
        #         # binaryTree.buildTree(
        #     None
        # ),
        #
        # singleLinkedList.buildSingleList(
        #     None
        # ),
        #
        # nTree.buildTree(
        #     None
        # ),,
        # nTree.buildTree(None),
    )
    expectedRlt[5] = None
    # !! ====================================

    # function and parameters count
    allInput = [(input[i], enableInput[i], expectedRlt[i]) for i in range(testCaseCnt)]
    if not input[0]:
        print("ERROR: please assign at least one input for input[0]!")
        exit()
    funcParaCnt = 1 if not isinstance(input[0], tuple) else len(input[0])
    funcCnt = len(myFuncLis)

    # for each test case
    for inputPara, enableInput, expectedRlt in allInput:
        if not enableInput or not inputPara or (isinstance(inputPara, tuple) and not inputPara[0]): continue
        inputParaList = [None] * funcParaCnt

        if not isinstance(inputPara, tuple):
            inputPara = [inputPara]

        for j in range(funcParaCnt):
            inputParaList[j] = inputPara[j]

        # for each function
        for j in range(funcCnt):
            print('==' * 20)
            myFunc = myFuncLis[j]

            # ! manually call function, max para count: 8
            rlt = None
            if funcParaCnt == 1:
                rlt = myFunc(inputPara[0])
            if funcParaCnt == 2:
                rlt = myFunc(inputPara[0], inputPara[1])
            if funcParaCnt == 3:
                rlt = myFunc(inputPara[0], inputPara[1], inputPara[2])
            if funcParaCnt == 4:
                rlt = myFunc(inputPara[0], inputPara[1], inputPara[2], inputPara[3])
            if funcParaCnt == 5:
                rlt = myFunc(inputPara[0], inputPara[1], inputPara[2], inputPara[3], inputPara[4])
            if funcParaCnt == 6:
                rlt = myFunc(inputPara[0], inputPara[1], inputPara[2], inputPara[3], inputPara[4], inputPara[5])
            if funcParaCnt == 7:
                rlt = myFunc(inputPara[0], inputPara[1], inputPara[2], inputPara[3], inputPara[4], inputPara[5], inputPara[6])
            if funcParaCnt == 8:
                rlt = myFunc(inputPara[0], inputPara[1], inputPara[2], inputPara[3], inputPara[4], inputPara[5], inputPara[6], inputPara[7])

            # only output when the result is not expected
            if onlyDisplayError and expectedRlt is not None and expectedRlt == rlt: continue

            # output function name
            if funcCnt > 1:
                print('func: \t%s' % myFunc.__name__)

            # output para
            for k in range(funcParaCnt):
                para = inputParaList[k]
                if para:
                    formatPrint('input %s:' % (k + 1), para)
                else:
                    print(para)

            # output result
            print()
            if not rlt:
                print('rlt:\t', rlt)
            else:
                formatPrint('rlt:', rlt)
            if expectedRlt is not None:
                if not expectedRlt:
                    print('expRlt:\t', expectedRlt)
                else:
                    formatPrint('expRlt:', expectedRlt)
    print('==' * 20)
# endFunc

def isSpecialInstance(myInstance):
    for curType in [TreeNode, Node]:
        if isinstance(myInstance, curType):
            return True
    return False
# endFunc

def formatPrint(prefix, data):
    if isMatrix(data):
        print('%s' % prefix)
        printMatrix(data)
    else:
        splitter = '\n' if isSpecialInstance(data) else '\t'
        print('%s%s%s' % (prefix, splitter, data))
# endFunc

def main():
    func()
# endMain


if __name__ == "__main__":
    main()
# endIf
