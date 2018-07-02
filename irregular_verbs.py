from collections import namedtuple

Tense = namedtuple('Tense',
                   ('PresenteIndicativo', 'PretéritoPerfeito', 'PretéritoImperfeito', 'PretéritoMaisQuePerfeito',
                    'FuturoSimples', 'Condicional', 'PresentedeSubjuntivo', 'PretéritoImperfeitodeSubjuntivo',
                    'FuturodeSubjuntivo', 'ImperativoAfirmativo', 'ImperativoNegativo'))

# complete conjugations of the most common used ones and used as a base for conjugations of others

caber = Tense(('caibo', 'cabes', 'cabe', 'cabemos', 'cabeis', 'cabem'),
              ('coube', 'coubeste', 'coube', 'coubemos', 'coubestes', 'couberam'),
              ('cabia', 'cabias', 'cabia', 'cabíamos', 'cabíeis', 'cabiame'),
              ('coubera', 'couberas', 'coubera', 'coubéramos', 'coubéreis', 'couberam'),
              ('caberei', 'caberás', 'caberá', 'caberemos', 'cabereis', 'caberão'),
              ('caiba', 'caibas', 'caiba', 'caibamos', 'caibais', 'caibam'),
              ('coubesse', 'coubesses', 'coubesse', 'coubéssemos', 'coubésseis', 'coubessem'),
              ('couber', 'couberes', 'couber', 'coubermos', 'couberdes', 'couberem'),
              ('caberia', 'caberias', 'caberia', 'caberíamos', 'caberíeis', 'caberiam'),
              ('-', '-', '-', '-',),
              ('-', '-', '-', '-',))

cobrir = Tense(('cubro', 'cobres', 'cobre', 'cobrimos', 'cobris', 'cobrem'),
               ('cobri', 'cobriste', 'cobriu', 'cobrimos', 'cobristes', 'cobriram'),
               ('cobria', 'cobrias', 'cobria', 'cobríamos', 'cobríeis', 'cobriam'),
               ('cobrira', 'cobriras', 'cobrira', 'cobríramos', 'cobríreis', 'cobriram'),
               ('cobrirei', 'cobrirás', 'cobrirá', 'cobriremos', 'cobrireis', 'cobrirão'),
               ('cubra', 'cubras', 'cubra', 'cubramos', 'cubrais', 'cubram'),
               ('cobrisse', 'cobrisses', 'cobrisse', 'cobríssemos', 'cobrísseis', 'cobrissem'),
               ('cobrir', 'cobrires', 'cobrir', 'cobrirmos', 'cobrirdes', 'cobrirem'),
               ('cobriria', 'cobririas', 'cobriria', 'cobriríamos', 'cobriríeis', 'cobririam'),
               ('-', 'cobre', 'cubra', 'cubramos', 'cobri', 'cubram'),
               ('-', 'não cubras', 'não cubra', 'não cubramos', 'não cubrais', 'não cubram'))

crer = Tense(('creio', 'crês', 'crê', 'cremos', 'credes', 'crêem'),
             ('cri', 'creste', 'creu', 'cremos', 'crestes', 'creram'),
             ('cria', 'crias', 'cria', 'críamos', 'críeis', 'criam'),
             ('crera', 'creras', 'crera', 'crêramos', 'crêreis', 'creram'),
             ('crerei', 'crerás', 'crerá', 'creremos', 'crereis', 'crerão'),
             ('creia', 'creias', 'creia', 'creiamos', 'creiais', 'creiam'),
             ('cresse', 'cresses', 'cresse', 'crêssemos', 'crêsseis', 'cressem'),
             ('crer', 'creres', 'crer', 'crermos', 'crerdes', 'crerem'),
             ('creria', 'creria', 'crerias', 'creríamos', 'creríeis', 'creriam'),
             ('-', 'crê', 'creia', 'creiamos', 'crede' 'creiam',),
             ('-', 'não creias', 'não creia', 'não creiamos', 'não creiais', 'não creiam'))

dar = Tense(('dou', 'dás', 'dá', 'damos', 'dais', 'dão'),
            ('dei', 'deste', 'deu', 'demos', 'destes', 'deram'),
            ('dava', 'davas', 'dava', 'dávamos', 'dáveis', 'davam'),
            ('dera', 'deras', 'dera', 'déramos', 'déreis', 'deram'),
            ('darei', 'darás', 'dará', 'daremos', 'dareis', 'darão'),
            ('dê', 'dês', 'dê', 'dêmos', 'deis', 'dêem'),
            ('desse', 'desses', 'desse', 'déssemos', 'désseis', 'dessem'),
            ('der', 'deres', 'der', 'dermos', 'derdes', 'derem'),
            ('daria', 'darias', 'daria', 'daríamos', 'dariam'),
            ('-', 'dá', 'dê', 'você', 'dêmos', 'daríeis', 'dêem'),
            ('-', 'não dês', 'não dê ', 'não dêmos', 'não dêem'))

dizer = Tense(('digo', 'dizes', 'diz', 'dizemos', 'dizeis', 'dizem'),
              ('disse', 'disseste', 'disse', 'dissemos', 'dissestes', 'disseram'),
              ('dizia', 'dizias', 'dizia', 'dizíamos', 'dizíeis', 'diziam'),
              ('dissera', 'disseras', 'dissera', 'disséramos', 'disséreis', 'disseram'),
              ('direi', 'dirás', 'dirá', 'diremos', 'direis', 'dirão'),
              ('diga', 'digas', 'diga', 'digamos', 'digais', 'digam'),
              ('dissesse', 'dissesses', 'dissesse', 'disséssemos', 'dissésseis', 'dissessem'),
              ('disser', 'disseres', 'disser', 'dissermos', 'disserdes', 'disserem'),
              ('diria', 'dirias', 'diria', 'diríamos', 'diríeis', 'diriam'),
              ('-', 'diz', 'diga', 'digamos', 'dizei', 'digas'),
              ('-', 'não digas', 'não diga', 'não digamos', 'não digais', 'não digam'))

fazer = Tense(('faço', 'fazes', 'faz', 'fazemos', 'fazeis', 'fazem'),
              ('fiz', 'fizeste', 'fez', 'fizemos', 'fizestes', 'fizeram'),
              ('fazia', 'fazias', 'fazia', 'fazíamos', 'fazíeis', 'faziam'),
              ('fizera', 'fizeras', 'fizera', 'fizéramos', 'fizéreis', 'fizeram'),
              ('farei', 'farás', 'fará', 'faremos', 'fareis', 'farão'),
              ('faça', 'faças', 'faça', 'façamos', 'façais', 'façam'),
              ('fizesse', 'fizesses', 'fizesse', 'fizéssemos', 'fizésseis', 'fizessem'),
              ('fizer', 'fizeres', 'fizer', 'fizermos', 'fizerdes', 'fizerem'),
              ('faria', 'farias', 'faria', 'faríamos', 'faríeis', 'fariam'),
              ('-', 'faz', 'faça', 'façamos', 'fazei', 'façam'),
              ('-', 'não faças', 'não faça', 'não façamos', 'não façais', 'não façam'))

haver = Tense(('hei', 'hás', 'há', 'havemos', 'haveis', 'hão'),
              ('houve', 'houveste', 'houve', 'houvemos', 'houvestes', 'houveram'),
              ('havia', 'havias', 'havia', 'havíamos,', 'havíeis', 'haviam'),
              ('houvera', 'houveras', 'houvera', 'houvéramos', 'houvéreis', 'houveram'),
              ('haverei', 'haverás', 'haverá', 'haveremos', 'havereis', 'haverão'),
              ('haja', 'hajas', 'haja', 'hajamos', 'hajais', 'hajam'),
              ('houvesse', 'houvesses', 'houvesse', 'houvéssemos', 'houvésseis', 'houvessem'),
              ('houver', 'houveres', 'houver', 'houvermos', 'houverdes', 'houverem'),
              ('haveria', 'haverias', 'haveria', 'haveríamos', 'haveríeis', 'haveriam'),
              ('-', 'há', 'haja', 'hajamos', 'havei', 'hajam'),
              ('-', 'não hajas', 'não haja', 'não hajamos', 'não hajais', 'não hajam'))

ler = Tense(('leio', 'lês', 'lê', 'lemos', 'ledes', 'lêem'),
            ('li', 'leste', 'leu', 'lemos', 'lestes', 'leram'),
            ('lia', 'lias', 'lia', 'líamos', 'líeis', 'liam'),
            ('lera', 'leras', 'lera', 'lêramos', 'lêreis', 'leram'),
            ('lerei', 'lerás', 'lerá', 'leremos', 'lereis', 'lerão'),
            ('leia', 'leias', 'leia', 'leiamos', 'leiais', 'leiam'),
            ('lesse', 'lesses', 'lesse', 'lêssemos', 'lêsseis', 'lessem'),
            ('ler', 'leres', 'ler', 'lermos', 'lerdes', 'lerem'),
            ('leria', 'lerias', 'leria', 'leríamos', 'leríeis', 'leriam'),
            ('-', 'lê', 'leia', 'leiamos', 'lede', 'leiam'),
            ('-', 'não leias', 'não leia', 'não leiamos', 'não leiais', 'não leiam'))

medir = Tense(('meço', 'medes', 'mede', 'medimos', 'medis', 'medem'),
              ('medi', 'mediste', 'mediu', 'medimos', 'medistes', 'mediram'),
              ('media', 'medias', 'media', 'medíamos', 'medíeis', 'mediam'),
              ('medira', 'mediras', 'medira', 'medíramos', 'medíreis', 'mediram'),
              ('medirei', 'medirás', 'medirá', 'mediremos', 'medireis', 'medirão'),
              ('meça', 'meças', 'meça', 'meçamos', 'meçais', 'meçam'),
              ('medisse', 'medisses', 'medisse', 'medíssemos', 'medísseis', 'medissem'),
              ('medir', 'medires', 'medir', 'medirmos', 'medirdes', 'medirem'),
              ('mediria', 'medirias', 'mediria', 'mediríamos', 'mediríeis', 'mediriam'),
              ('-', 'medetu', 'meçaele', 'meçamosnós', 'medivós', 'meçameles'),
              ('-', 'não meçastu', 'não meçaele', 'não meçamosnós', 'não meçaisvós', 'não meçameles'))

ouvir = Tense(('ouço', 'oiço', 'ouves', 'ouve', 'ouvimos', 'ouvis', 'ouvem'),
              ('ouvi', 'ouviste', 'ouviu', 'ouvimos', 'ouvistes', 'ouviram'),
              ('ouvia', 'ouvias', 'ouvia', 'ouvíamos', 'ouvíeis', 'ouviam'),
              ('ouvira', 'ouviras', 'ouvira', 'ouvíramos', 'ouvíreis', 'ouviram'),
              ('ouvirei', 'ouvirás', 'ouvirá', 'ouviremos', 'ouvireis', 'ouvirão'),
              ('ouça', 'ouças', 'ouça', 'ouçamos', 'ouçais', 'ouçam', 'oiçam'),
              ('ouvisse', 'ouvisses', 'ouvisse', 'ouvíssemos', 'ouvísseis', 'ocêsouvissem'),
              ('ouvir', 'ouvires', 'ouvir', 'ouvirmos', 'ouvirdes', 'ouvirem'),
              ('ouviria', 'ouvirias', 'ouviria', 'ouviríamos', 'ouviríeis', 'ouviriam'),
              ('-', 'ouve', 'ouça', 'oiçamos', 'ouvi', 'oiçam'),
              ('-', 'não ouças', 'não ouça', 'não ouçamos', 'não ouçais', 'não ouçam'))

pedir = Tense(('peço', 'pedes', 'pede', 'pedimos', 'pedis', 'pedem'),
              ('pedi', 'pediste', 'pediu', 'pedimos', 'pedistes', 'pediram'),
              ('pedia', 'pedias', 'pedia', 'pedíamos', 'pedíeis', 'pediam'),
              ('pedira', 'pediras', 'pedira', 'pedíramos', 'pedíreis', 'pediram'),
              ('pedirei', 'pedirás', 'pedirá', 'pediremos', 'pedireis', 'pedirão'),
              ('peça', 'peças', 'peça', 'peçamos', 'peçais', 'peçam'),
              ('pedisse', 'pedisses', 'pedisse', 'pedíssemos', 'pedísseis', 'pedissem'),
              ('pedir', 'pedires', 'pedir', 'pedirmos', 'pedirdes', 'pedirem'),
              ('pediria', 'pedirias', 'pediria', 'pediríamos', 'pediríeis', 'pediriam'),
              ('-', 'pede', 'peça', 'peçamos', 'pedi', 'peçam'),
              ('-', 'não peças', 'não peça', 'não peçamos', 'não peçais', 'não peçam'))

polir = Tense(('pulo', 'pules', 'pule', 'polimos', 'polis', 'pulem'),
              ('poli', 'poliste', 'poliu', 'polimos', 'polistes', 'poliram'),
              ('polia', 'polias', 'polia', 'políamos', 'políeis', 'poliam'),
              ('polira', 'poliras', 'polira', 'políramos', 'políreis', 'poliram'),
              ('polirei', 'polirás', 'polirá', 'poliremos', 'polireis', 'polirão'),
              ('pula', 'pulas', 'pula', 'pulamos', 'pulais', 'pulam'),
              ('polisse', 'polisses', 'polisse', 'políssemos', 'polísseis', 'polissem'),
              ('polir', 'polires', 'polir', 'polirmos', 'polirdes', 'polirem'),
              ('poliria', 'polirias', 'poliria', 'poliríamos', 'poliríeis', 'poliriam'),
              ('-', 'pule', 'pula', 'pulamos', 'poli', 'pulam'),
              ('-', 'não pulas', 'não pula', 'não pulamos', 'não pulais', 'não pulam'))

por = Tense(('ponho', 'pões', 'põe', 'pomos', 'pondes', 'põem'),
            ('pus', 'pseste', 'pôs', 'pusemos', 'pusestes', 'puseram'),
            ('punha', 'punhas', 'punha', 'púnhamos', 'púnheis', 'punham'),
            ('pusera', 'puseras', 'pusera', 'puséramos', 'puséreis', 'puseram'),
            ('porei', 'porás', 'porá', 'poremos', 'poreis', 'porão'),
            ('ponha', 'ponhas', 'ponha', 'ponhamos', 'ponhais', 'ponham'),
            ('pusesse', 'pusesses', 'pusesse', 'puséssemos', 'pusésseis', 'pusessem'),
            ('puser', 'puseres', 'puser', 'pusermos', 'puserdes', 'puserem'),
            ('poria', 'porias', 'poria', 'poríamos', 'poríeis', 'poriam'),
            ('-', 'põe', 'ponha', 'ponhamos', 'ponham'),
            ('-', 'não ponhas', 'não ponha', 'não ponhamos', 'não ponham'))

querer = Tense(('quero', 'queres', 'quer', 'queremos', 'quereis', 'querem'),
               ('quis', 'quiseste', 'quis', 'quisemos', 'quisestes', 'quiseram'),
               ('queria', 'querias', 'queria', 'queríamos', 'queríeis', 'queriam'),
               ('quisera', 'quiseras', 'quisera', 'quiséramos', 'quiséreis', 'quiseram'),
               ('quererei', 'quererás', 'quererá', 'quereremos', 'querereis', 'quererão'),
               ('queira', 'queiras', 'queira', 'queiramos', 'queirais', 'queiram'),
               ('quisesse', 'quisesses', 'quisesse', 'quiséssemos', 'quisésseis', 'quisessem'),
               ('quiser', 'quiseres', 'quiser', 'quisermos', 'quiserdes', 'quiserem'),
               ('quereria', 'quererias', 'quereria', 'quereríamos', 'quereríeis', 'quereriam'),
               ('-', 'queira', 'queiramos', 'querei', 'queiram'),
               ('-', '-', '-', '-', '-'))

saber = Tense(('sei', 'sabes', 'sabe', 'sabemos', 'sabeis', 'sabem'),
              ('soube', 'soubeste', 'soube', 'soubemos', 'soubestes', 'souberam'),
              ('sabia', 'sabias', 'sabia', 'sabíamos', 'sabíeis', 'sabiam'),
              ('soubera', 'souberas', 'soubera', 'soubéramos', 'soubéreis', 'souberam'),
              ('saberei', 'saberás', 'saberá', 'saberemos', 'sabereis', 'saberão'),
              ('saiba', 'saibas', 'saiba', 'saibamos', 'saibais', 'saibam'),
              ('soubesse', 'soubesses', 'soubesse', 'soubéssemos', 'soubésseis', 'soubessem'),
              ('souber', 'souberes', 'souber', 'soubermos', 'souberdes', 'souberem'),
              ('saberia', 'saberias', 'saberia', 'ssaberíamos', 'saberíeis', 'saberiam'),
              ('-', 'sabe', 'saiba', 'saibamos', 'sabei', 'saibam'),
              ('-', 'não saibas', 'não saiba', 'não saibamos', 'não saibais', 'não saibam'))

ter = Tense(('tenho', 'tens', 'tem', 'temos', 'tendes', 'têm'),
            ('tive', 'tiveste', 'tive', 'tivemos', 'tivestes', 'tiveram'),
            # index 1 has not to be included in conjugate_compound_tenses() method
            ('tinha', 'tinhas', 'tinha', 'tínhamos', 'tínheis', 'tinham'),
            ('tivera', 'tiveras', 'tivera', 'nóstivéramos', 'tivéreis', 'tiveram'),
            # index 3 has not to be included in conjugate_compound_tenses() method
            ('terei', 'terás', 'terá', 'teremos', 'tereis', 'terão'),
            ('tenha', 'tenhas', 'tenha', 'tenhamos', 'tenhais', 'tenham'),
            ('tivesse', 'tivesses', 'tivesse', 'tivéssemos', 'tivésseis', 'tivessem'),
            ('tiver', 'tiveres', 'tiver', 'tivermos', 'tiverdes', 'tiverem'),
            ('teria', 'terias', 'teria', 'teríamos', 'teríeis', 'teriam'),
            ('-', 'tem', 'tenha', 'tenhamos', 'tenham'),
            # index 9 has not to be included in conjugate_compound_tenses() method
            ('-', 'não tenhas', 'não tenha', 'não tenhamos',
             'não tenham'))  # index 10 has not to be included in conjugate_compound_tenses() method

valer = Tense(('valho', 'vales', 'vale', 'valemos', 'valeis', 'valem'),
              ('vali', 'valeste', 'valeu', 'valemos', 'valestes', 'valeram'),
              ('valia', 'valias', 'valia', 'valíamos', 'valíeis', 'valiam'),
              ('valera', 'valeras', 'valera', 'valêramos', 'valêreis', 'valeram'),
              ('valerei', 'valerás', 'valerá', 'valeremos', 'valereis', 'valerão'),
              ('valha', 'valhas', 'valha', 'valhamos', 'valhais', 'valham'),
              ('valesse', 'valesses', 'valesse', 'valêssemos', 'valêsseis', 'valessem'),
              ('valer', 'valeres', 'valer', 'valermos', 'valerdes', 'valerem'),
              ('valeria', 'valerias', 'valeria', 'valeríamos', 'valeríeis', 'valeriam'),
              ('-', 'vale', 'valha', 'valhamos', 'valei', 'valham'),
              ('-', 'não valhas', 'não valha', 'não valhamos', 'não valhais', 'não valham'))

ver = Tense(('vejo', 'vês', 'vê', 'vemos', 'vedes', 'vêem'),
            ('vi', 'viste', 'viu', 'vimos', 'vistes', 'viram'),
            ('via', 'vias', 'via', 'víamos', 'víeis', 'viam'),
            ('vira', 'viras', 'vira', 'víramos', 'víreis', 'viram'),
            ('verei', 'verás', 'verá', 'veremos', 'vereis', 'verão'),
            ('veja', 'vejas', 'veja', 'vejamos', 'vejais', 'vejam'),
            ('visse', 'visses', 'visse', 'víssemos', 'vísseis', 'vissem'),
            ('ver', 'veres', 'ver', 'vermos', 'verdes', 'verem'),
            ('veria', 'verias', 'veria', 'veríamos', 'veríeis', 'veriam'),
            ('-', 'vê', 'veja', 'vejamos', 'vede', 'vejam'),
            ('-', 'não vejas', 'não veja', 'não vejamos', 'não vejais', 'não vejam'))

vir = Tense(('venho', 'vens', 'vem', 'vimos', 'vindes', 'vêm'),
            ('vim', 'vieste', 'veio', 'viemos', 'viestes', 'vieram'),
            ('vinha', 'vinhas', 'vinha', 'vínhamos', 'vínheis', 'vinham'),
            ('viera', 'vieras', 'viera', 'viéramos', 'viéreis', 'vieram'),
            ('virei', 'virás', 'virá', 'viremos', 'vireis', 'virão'),
            ('venha', 'venhas', 'venha', 'venhamos', 'venhais', 'venham'),
            ('viesse', 'viesses', 'viesse', 'viéssemos', 'viésseis', 'viessem'),
            ('vier', 'vieres', 'vier', 'viermos', 'vierdes', 'vierem'),
            ('viria', 'virias', 'viria', 'viríamos', 'viríeis', 'viriam'),
            ('-', 'vem', 'venha', 'venhamos', 'vinde', 'venham'),
            ('-', 'não não venhas', 'não venha', 'não venhamos', 'não venhais', 'não venham'))

basic_irregular_verbs = {'caber': caber, 'medir': medir, 'pedir': pedir, 'por': por,
                         'valer': valer, 'polir': polir, 'saber': saber, 'dar': dar,
                         'dizer': dizer, 'ter': ter, 'cobrir': cobrir, 'ouvir': ouvir,
                         'fazer': fazer, 'ler': ler, 'querer': querer,
                         'crer': crer, 'vir': vir}

all_irregular_verbs_dict = {'consumir': None, 'esvair': None, 'readequar': None, 'predizer': None, 'retrair': None,
                            'disperder': None,
                            'indispor': None, 'advir': None, 'jazer': None, 'mediar': None, 'entrequerer': None,
                            'influir': None,
                            'prazer': None, 'desmentir': None, 'interpor': None, 'reaver': None, 'revir': None,
                            'desquerer': None,
                            'despolir': None, 'putrefazer': None, 'comprazer': None, 'avir': None, 'aspergir': None,
                            'remedir': None,
                            'aprazer': None, 'advertir': None, 'engolir': None, 'prevenir': None, 'propor': None,
                            'desprecaver': None,
                            'reavir': None, 'obter': None, 'atribuir': None, 'desmobiliar': None, 'descaber': None,
                            'atrair': None, 'sobrepor': None, 'descompor': None, 'intermediar': None, 'entrever': None,
                            'malparir': None,
                            'antever': None, 'expor': None, 'desaprazer': None, 'malfazer': None, 'desver': None,
                            'transgredir': None,
                            'desmedir': None, 'raer': None, 'puir': None, 'idear': None, 'progredir': None,
                            'contradizer': None,
                            'repelir': None, 'construir': None, 'desprover': None, 'fotocompor': None, 'concluir': None,
                            'acudir': None,
                            'trespor': None, 'sorrir': None, 'rarefazer': None, 'manter': None, 'sotopor': None,
                            'preterir': None,
                            'expelir': None, 'descomprazer': None, 'desdizer': None, 'repor': None, 'reimpor': None,
                            'conter': None,
                            'ser': None, 'prepor': None, 'interdizer': None, 'frigir': None, 'reindispor': None,
                            'recobrir': None,
                            'benquerer': None, 'prover': None, 'reexpor': None, 'denegrir': None, 'circunver': None,
                            'estar': None,
                            'decompor': None, 'minguar': None, 'tossir': None, 'desaguar': None, 'desconstruir': None,
                            'bem-fazer': None,
                            'devir': None, 'repedir': None, 'bem-querer': None, 'dessaber': None, 'ater': None,
                            'entrepor': None,
                            'ansiar': None, 'sentir': None, 'refazer': None, 'incluir': None, 'despedir': None,
                            'sacudir': None,
                            'prossupor': None, 'sobre-expor': None, 'supor': None, 'seguir': None, 'ir': None,
                            'adjazer': None,
                            'entrefazer': None, 'traspor': None, 'malinguar': None, 'afazer': None, 'contrair': None,
                            'desimpedir': None,
                            'mentir': None, 'distrair': None, 'satisfazer': None, 'agredir': None, 'digerir': None,
                            'redar': None,
                            'antedar': None, 'doer': None, 'expedir': None, 'submergir': None, 'conferir': None,
                            'desimpor': None,
                            'entupir': None, 'retranspor': None, 'suster': None, 'gelifazer': None, 'pleitear': None,
                            'desprazer': None,
                            'maldizer': None, 'enxaguar': None, 'deter': None, 'soer': None, 'recompor': None,
                            'compor': None,
                            'resfolegar': None, 'perseguir': None, 'descobrir': None, 'intervir': None,
                            'transpor': None,
                            'remediar': None, 'trazer': None, 'repropor': None, 'impedir': None, 'redispor': None,
                            'maisquerer': None,
                            'perfazer': None, 'treler': None, 'inserir': None, 'delinquir': None, 'condizer': None,
                            'reler': None,
                            'estrear': None, 'servir': None, 'opor': None, 'pressentir': None, 'destruir': None,
                            'contrapor': None,
                            'reconvir': None, 'rever': None, 'cuspir': None, 'pospor': None, 'sobrestar': None,
                            'reobter': None,
                            'consentir': None, 'confugir': None, 'entredizer': None, 'autodestruir': None,
                            'antepor': None,
                            'convir': None, 'desafazer': None, 'desapor': None, 'assentir': None, 'subir': None,
                            'obvir': None,
                            'liquefazer': None, 'precluir': None, 'impelir': None, 'superpor': None, 'pruir': None,
                            'subpor': None,
                            'santiguar': None, 'apor': None, 'adequar': None, 'desconvir': None, 'telever': None,
                            'extrapor': None,
                            'impor': None, 'desavir': None, 'esfazer': None, 'descrer': None, 'entrevir': None,
                            'odiar': None,
                            'condoer': None, 'malquerer': None, 'depor': None, 'trair': None, 'persentir': None,
                            'requerer': None,
                            'escapulir': None, 'circumpor': None, 'entreouvir': None, 'torrefazer': None,
                            'sobreexpor': None,
                            'buir': None, 'concernir': None, 'ressentir': None, 'contrapropor': None, 'parir': None,
                            'convergir': None,
                            'superexpor': None, 'desdar': None, 'prever': None, 'vestir': None, 'reexpedir': None,
                            'transfugir': None,
                            'apropinquar': None, 'predispor': None, 'imergir': None, 'sortear': None, 'benfazer': None,
                            'emergir': None,
                            'superimpor': None, 'sair': None, 'insatisfazer': None, 'contravir': None, 'sumir': None,
                            'embair': None,
                            'ruir': None, 'cerzir': None, 'incendiar': None, 'fugir': None, 'provir': None,
                            'abster': None,
                            'interver': None, 'cair': None, 'desvaler': None, 'equivaler': None, 'divertir': None,
                            'despor': None,
                            'pressupor': None, 'tresler': None, 'transfazer': None, 'fraguar': None, 'sobrevir': None,
                            'ver': None,
                            'redizer': None, 'bendizer': None, 'conseguir': None, 'perder': None, 'pôr': None,
                            'poder': None,
                            'aferir': None, 'sugerir': None, 'moer': None, 'sortir': None, 'rir': None,
                            'contrafazer': None,
                            'justapor': None, 'maldispor': None, 'sobpor': None, 'bulir': None, 'bem-dizer': None,
                            'mobiliar': None,
                            'tumefazer': None, 'reouvir': None, 'subtrair': None, 'encobrir': None, 'dormir': None,
                            'dispor': None,
                            'reter': None, 'regredir': None, 'deslinguar': None, 'haver': haver}

