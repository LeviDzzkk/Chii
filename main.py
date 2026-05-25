import discord
from discord.ext import commands
import random
from dotenv import load_dotenv
import os

# ========== DICIONÁRIO DE KANJI N5 ==========
kanji_n5 = {
    "一": {"leituras": ["いち", "いつ", "ひと"], "significados": ["um"]},
    "二": {"leituras": ["に", "ふた"], "significados": ["dois"]},
    "三": {"leituras": ["さん", "みっ"], "significados": ["três"]},
    "四": {"leituras": ["し", "よん", "よ"], "significados": ["quatro"]},
    "五": {"leituras": ["ご", "いつ"], "significados": ["cinco"]},
    "六": {"leituras": ["ろく", "むっ"], "significados": ["seis"]},
    "七": {"leituras": ["しち", "なな"], "significados": ["sete"]},
    "八": {"leituras": ["はち", "や"], "significados": ["oito"]},
    "九": {"leituras": ["きゅう", "く"], "significados": ["nove"]},
    "十": {"leituras": ["じゅう", "とお"], "significados": ["dez"]},
    "百": {"leituras": ["ひゃく"], "significados": ["cem"]},
    "千": {"leituras": ["せん"], "significados": ["mil"]},
    "万": {"leituras": ["まん"], "significados": ["dez mil"]},
    "日": {"leituras": ["にち", "じつ", "ひ", "か"], "significados": ["dia", "sol"]},
    "月": {"leituras": ["げつ", "がつ", "つき"], "significados": ["mês", "lua"]},
    "火": {"leituras": ["か", "ひ"], "significados": ["fogo"]},
    "水": {"leituras": ["すい", "みず"], "significados": ["água"]},
    "木": {"leituras": ["もく", "ぼく", "き"], "significados": ["árvore", "madeira"]},
    "金": {"leituras": ["きん", "こん", "かね"], "significados": ["ouro", "dinheiro"]},
    "土": {"leituras": ["ど", "と", "つち"], "significados": ["terra"]},
    "曜": {"leituras": ["よう"], "significados": ["dia da semana"]},
    "年": {"leituras": ["ねん", "とし"], "significados": ["ano"]},
    "時": {"leituras": ["じ", "とき"], "significados": ["hora", "tempo"]},
    "分": {"leituras": ["ぶん", "ふん", "わ"], "significados": ["minuto", "parte"]},
    "半": {"leituras": ["はん"], "significados": ["metade"]},
    "今": {"leituras": ["こん", "いま"], "significados": ["agora"]},
    "毎": {"leituras": ["まい"], "significados": ["todo", "cada"]},
    "週": {"leituras": ["しゅう"], "significados": ["semana"]},
    "先": {"leituras": ["せん", "さき"], "significados": ["antes", "frente"]},
    "来": {"leituras": ["らい", "く"], "significados": ["vir"]},
    "人": {"leituras": ["じん", "にん", "ひと"], "significados": ["pessoa"]},
    "男": {"leituras": ["だん", "なん", "おとこ"], "significados": ["homem"]},
    "女": {"leituras": ["じょ", "にょ", "おんな"], "significados": ["mulher"]},
    "子": {"leituras": ["し", "す", "こ"], "significados": ["criança"]},
    "父": {"leituras": ["ふ", "ちち"], "significados": ["pai"]},
    "母": {"leituras": ["ぼ", "はは"], "significados": ["mãe"]},
    "友": {"leituras": ["ゆう", "とも"], "significados": ["amigo"]},
    "学": {"leituras": ["がく", "まな"], "significados": ["estudo", "estudar"]},
    "校": {"leituras": ["こう"], "significados": ["escola"]},
    "生": {"leituras": ["せい", "しょう", "い", "う"], "significados": ["vida", "nascer"]},
    "語": {"leituras": ["ご"], "significados": ["idioma"]},
    "文": {"leituras": ["ぶん", "もん"], "significados": ["frase", "texto"]},
    "字": {"leituras": ["じ"], "significados": ["letra", "caractere"]},
    "本": {"leituras": ["ほん", "もと"], "significados": ["livro", "origem"]},
    "読": {"leituras": ["どく", "よ"], "significados": ["ler"]},
    "書": {"leituras": ["しょ", "か"], "significados": ["escrever"]},
    "聞": {"leituras": ["ぶん", "き"], "significados": ["ouvir", "perguntar"]},
    "話": {"leituras": ["わ", "はな"], "significados": ["falar"]},
    "大": {"leituras": ["だい", "たい", "おお"], "significados": ["grande"]},
    "小": {"leituras": ["しょう", "ちい", "こ"], "significados": ["pequeno"]},
    "中": {"leituras": ["ちゅう", "なか"], "significados": ["meio", "dentro"]},
    "上": {"leituras": ["じょう", "うえ"], "significados": ["cima"]},
    "下": {"leituras": ["か", "した"], "significados": ["baixo"]},
    "左": {"leituras": ["さ", "ひだり"], "significados": ["esquerda"]},
    "右": {"leituras": ["う", "みぎ"], "significados": ["direita"]},
    "外": {"leituras": ["がい", "そと"], "significados": ["fora"]},
    "前": {"leituras": ["ぜん", "まえ"], "significados": ["frente", "antes"]},
    "後": {"leituras": ["ご", "あと", "うし"], "significados": ["depois", "atrás"]},
    "東": {"leituras": ["とう", "ひがし"], "significados": ["leste"]},
    "西": {"leituras": ["せい", "にし"], "significados": ["oeste"]},
    "南": {"leituras": ["なん", "みなみ"], "significados": ["sul"]},
    "北": {"leituras": ["ほく", "きた"], "significados": ["norte"]},
    "山": {"leituras": ["さん", "やま"], "significados": ["montanha"]},
    "川": {"leituras": ["せん", "かわ"], "significados": ["rio"]},
    "田": {"leituras": ["でん", "た"], "significados": ["campo"]},
    "天": {"leituras": ["てん"], "significados": ["céu"]},
    "気": {"leituras": ["き", "け"], "significados": ["energia", "ar"]},
    "雨": {"leituras": ["う", "あめ"], "significados": ["chuva"]},
    "空": {"leituras": ["くう", "そら"], "significados": ["céu", "vazio"]},
    "花": {"leituras": ["か", "はな"], "significados": ["flor"]},
    "草": {"leituras": ["そう", "くさ"], "significados": ["grama"]},
    "竹": {"leituras": ["ちく", "たけ"], "significados": ["bambu"]},
    "森": {"leituras": ["しん", "もり"], "significados": ["floresta"]},
    "目": {"leituras": ["もく", "め"], "significados": ["olho"]},
    "耳": {"leituras": ["じ", "みみ"], "significados": ["orelha"]},
    "口": {"leituras": ["こう", "くち"], "significados": ["boca"]},
    "手": {"leituras": ["しゅ", "て"], "significados": ["mão"]},
    "足": {"leituras": ["そく", "あし"], "significados": ["pé", "perna"]},
    "食": {"leituras": ["しょく", "た"], "significados": ["comer"]},
    "飲": {"leituras": ["いん", "の"], "significados": ["beber"]},
    "米": {"leituras": ["べい", "こめ"], "significados": ["arroz"]},
    "魚": {"leituras": ["ぎょ", "さかな"], "significados": ["peixe"]},
    "肉": {"leituras": ["にく"], "significados": ["carne"]},
    "茶": {"leituras": ["ちゃ"], "significados": ["chá"]},
    "行": {"leituras": ["こう", "い"], "significados": ["ir"]},
    "帰": {"leituras": ["き", "かえ"], "significados": ["voltar"]},
    "入": {"leituras": ["にゅう", "はい"], "significados": ["entrar"]},
    "出": {"leituras": ["しゅつ", "で"], "significados": ["sair"]},
    "休": {"leituras": ["きゅう", "やす"], "significados": ["descansar"]},
    "立": {"leituras": ["りつ", "た"], "significados": ["ficar em pé"]},
    "座": {"leituras": ["ざ", "すわ"], "significados": ["sentar"]},
    "見": {"leituras": ["けん", "み"], "significados": ["ver"]},
    "買": {"leituras": ["ばい", "か"], "significados": ["comprar"]},
    "会": {"leituras": ["かい", "あ"], "significados": ["encontrar"]},
    "名": {"leituras": ["めい", "な"], "significados": ["nome"]},
    "国": {"leituras": ["こく", "くに"], "significados": ["país"]},
    "円": {"leituras": ["えん"], "significados": ["iene", "círculo"]},
    "白": {"leituras": ["はく", "しろ"], "significados": ["branco"]},
    "黒": {"leituras": ["こく", "くろ"], "significados": ["preto"]},
    "赤": {"leituras": ["せき", "あか"], "significados": ["vermelho"]},
    "青": {"leituras": ["せい", "あお"], "significados": ["azul"]},
    "車": {"leituras": ["しゃ", "くるま"], "significados": ["carro"]},
    "電": {"leituras": ["でん"], "significados": ["eletricidade"]},
    "駅": {"leituras": ["えき"], "significados": ["estação"]},
    "店": {"leituras": ["てん", "みせ"], "significados": ["loja"]},
    "社": {"leituras": ["しゃ"], "significados": ["empresa", "santuário"]},
    "犬": {"leituras": ["けん", "いぬ"], "significados": ["cachorro"]},
    "猫": {"leituras": ["びょう", "ねこ"], "significados": ["gato"]},
    "何": {"leituras": ["か", "なに", "なん"], "significados": ["o quê"]},
}

# ========== PARTÍCULAS N5 ==========
particulas_n5 = {
    "は": {
        "romaji": "wa",
        "funcao": "Partícula de tópico",
        "descricao": "Marca o tópico da frase. Indica sobre o que a frase está falando.",
        "exemplos": [
            ("わたし**は** がくせいです。", "Eu sou estudante."),
            ("これ**は** ほんです。", "Isso é um livro."),
        ],
        "dica": "⚠️ Escrita como は (ha), mas lida como **wa** quando partícula."
    },
    "が": {
        "romaji": "ga",
        "funcao": "Partícula de sujeito",
        "descricao": "Marca o sujeito da oração. Enfatiza quem realiza a ação ou possui algo.",
        "exemplos": [
            ("ねこ**が** います。", "Tem um gato. (O gato está aqui.)"),
            ("だれ**が** きましたか？", "Quem veio?"),
        ],
        "dica": "💡 Use が para enfatizar o sujeito, especialmente em respostas."
    },
    "を": {
        "romaji": "wo",
        "funcao": "Partícula de objeto direto",
        "descricao": "Marca o objeto direto da ação (o que recebe a ação do verbo).",
        "exemplos": [
            ("パン**を** たべます。", "Como pão."),
            ("にほんご**を** べんきょうします。", "Estudo japonês."),
        ],
        "dica": "⚠️ Escrita como を (wo), mas geralmente lida como **o**."
    },
    "に": {
        "romaji": "ni",
        "funcao": "Partícula de direção / tempo / localização",
        "descricao": "Indica destino de movimento, ponto no tempo, ou onde algo/alguém existe.",
        "exemplos": [
            ("がっこう**に** いきます。", "Vou para a escola."),
            ("７じ**に** おきます。", "Acordo às 7 horas."),
            ("へや**に** います。", "Estou no quarto."),
        ],
        "dica": "💡 Pense em に como 'em direção a' ou 'em (ponto específico)'."
    },
    "へ": {
        "romaji": "e",
        "funcao": "Partícula de direção",
        "descricao": "Indica a direção de um movimento. Mais enfático na trajetória que no destino.",
        "exemplos": [
            ("にほん**へ** いきます。", "Vou ao Japão (direção)."),
            ("うえ**へ** あがります。", "Subo para cima."),
        ],
        "dica": "⚠️ Escrita como へ (he), mas lida como **e** quando partícula. Parecida com に, mas foca no caminho."
    },
    "で": {
        "romaji": "de",
        "funcao": "Partícula de local de ação / meio",
        "descricao": "Indica onde uma ação acontece, ou o meio/instrumento usado para algo.",
        "exemplos": [
            ("がっこう**で** べんきょうします。", "Estudo na escola."),
            ("バス**で** いきます。", "Vou de ônibus."),
        ],
        "dica": "💡 に = onde algo existe; で = onde algo acontece."
    },
    "の": {
        "romaji": "no",
        "funcao": "Partícula possessiva / de modificação",
        "descricao": "Liga dois substantivos indicando posse, pertencimento ou especificação.",
        "exemplos": [
            ("わたし**の** ほん。", "Meu livro."),
            ("にほんご**の** せんせい。", "Professor de japonês."),
        ],
        "dica": "💡 Funciona como 's ou 'de' em português."
    },
    "と": {
        "romaji": "to",
        "funcao": "Partícula de companhia / lista",
        "descricao": "Significa 'e' (para listar coisas) ou 'com' (para indicar companhia).",
        "exemplos": [
            ("ともだち**と** いきます。", "Vou com um amigo."),
            ("りんご**と** みかん。", "Maçã e tangerina."),
        ],
        "dica": "💡 と lista coisas de forma exaustiva (lista completa). Compare com や."
    },
    "や": {
        "romaji": "ya",
        "funcao": "Partícula de lista parcial",
        "descricao": "Significa 'e' para listar exemplos, sugerindo que há mais itens além dos citados.",
        "exemplos": [
            ("りんご**や** みかんなど。", "Maçã, tangerina, etc."),
            ("ほん**や** ざっし。", "Livros, revistas (entre outros)..."),
        ],
        "dica": "💡 Use や quando a lista não é completa. Frequentemente aparece com など (etc.)."
    },
    "も": {
        "romaji": "mo",
        "funcao": "Partícula de inclusão ('também')",
        "descricao": "Significa 'também' ou 'nem'. Substitui は ou が para adicionar algo.",
        "exemplos": [
            ("わたし**も** がくせいです。", "Eu também sou estudante."),
            ("これ**も** ください。", "Dê-me isso também."),
        ],
        "dica": "💡 も substitui は e が: わたしは → わたしも."
    },
    "か": {
        "romaji": "ka",
        "funcao": "Partícula interrogativa",
        "descricao": "Transforma uma frase em pergunta, como o ponto de interrogação em português.",
        "exemplos": [
            ("がくせいです**か**？", "Você é estudante?"),
            ("なんじです**か**？", "Que horas são?"),
        ],
        "dica": "💡 Coloque か no final da frase para fazer uma pergunta."
    },
    "ね": {
        "romaji": "ne",
        "funcao": "Partícula de confirmação / concordância",
        "descricao": "Pede confirmação ou concordância do interlocutor. Como 'né?' em português.",
        "exemplos": [
            ("いい てんきです**ね**。", "Que bom tempo, né?"),
            ("むずかしいです**ね**。", "É difícil, não é?"),
        ],
        "dica": "💡 Use ね para buscar aprovação ou concordância."
    },
    "よ": {
        "romaji": "yo",
        "funcao": "Partícula de ênfase / afirmação",
        "descricao": "Dá ênfase à informação, indicando que está dizendo algo que o outro não sabe.",
        "exemplos": [
            ("これは おいしいです**よ**。", "Isso é gostoso (te garanto)!"),
            ("もう おそいです**よ**。", "Já é tarde (saiba disso)!"),
        ],
        "dica": "💡 よ = 'te digo', 'saiba que'. Mais assertivo que ね."
    },
    "から": {
        "romaji": "kara",
        "funcao": "Partícula de origem / causa ('de', 'porque')",
        "descricao": "Indica ponto de origem no espaço/tempo, ou causa/motivo.",
        "exemplos": [
            ("とうきょう**から** きました。", "Vim de Tóquio."),
            ("９じ**から** じゅぎょうです。", "A aula começa às 9h."),
        ],
        "dica": "💡 De onde algo começa (lugar, tempo ou motivo)."
    },
    "まで": {
        "romaji": "made",
        "funcao": "Partícula de limite ('até')",
        "descricao": "Indica o ponto final de um deslocamento, tempo ou ação. Significa 'até'.",
        "exemplos": [
            ("えき**まで** あるきます。", "Caminho até a estação."),
            ("６じ**まで** はたらきます。", "Trabalho até as 6h."),
        ],
        "dica": "💡 から＋まで = de... até. Ex: ９じ**から**５じ**まで**。"
    },
}

# ========== GRAMÁTICAS N5 ==========
gramaticas_n5 = {
    "です": {
        "uso": "Cópula formal ('ser/estar')",
        "estrutura": "Substantivo/Adjetivo-な + です",
        "exemplos": ["わたしは がくせい**です**。 → Eu sou estudante.", "これは きれい**です**。 → Isso é bonito."],
        "nota": "Forma formal/educada. A forma negativa é ではありません ou じゃないです."
    },
    "ます": {
        "uso": "Forma verbal polida (presente/futuro)",
        "estrutura": "Radical do verbo + ます",
        "exemplos": ["まいにち べんきょうし**ます**。 → Estudo todo dia.", "あした いき**ます**。 → Irei amanhã."],
        "nota": "Negativa: ません. Passado: ました. Passado neg.: ませんでした."
    },
    "ない": {
        "uso": "Forma negativa informal de verbos",
        "estrutura": "Radical do verbo + ない",
        "exemplos": ["たべ**ない**。 → Não como. (informal)", "いか**ない**。 → Não vou. (informal)"],
        "nota": "Equivale a ません na forma polida."
    },
    "て形 (てけい)": {
        "uso": "Forma -te: conectar verbos, pedir permissão, ações contínuas",
        "estrutura": "Verbo conjugado na forma て",
        "exemplos": ["たべ**て** ください。 → Por favor, coma.", "みて います。 → Estou olhando."],
        "nota": "Base para muitas estruturas: ～てください, ～ている, ～てもいいですか."
    },
    "～てください": {
        "uso": "Pedido / instrução ('por favor, faça...')",
        "estrutura": "Verbo (forma て) + ください",
        "exemplos": ["ここに かい**てください**。 → Por favor, escreva aqui.", "みて**ください**。 → Por favor, olhe."],
        "nota": "Forma educada de pedir que alguém faça algo."
    },
    "～ている": {
        "uso": "Ação em progresso ou estado resultante",
        "estrutura": "Verbo (forma て) + いる",
        "exemplos": ["いま たべ**ています**。 → Estou comendo agora.", "けっこんし**ています**。 → Sou casado."],
        "nota": "Equivale ao gerúndio português ou estado atual."
    },
    "～たい": {
        "uso": "Expressar desejo ('quero fazer...')",
        "estrutura": "Radical do verbo + たい",
        "exemplos": ["にほんに いき**たい**です。 → Quero ir ao Japão.", "すしを たべ**たい**。 → Quero comer sushi."],
        "nota": "たい se conjuga como adjetivo-い. Negativo: たくない."
    },
    "～たことがある": {
        "uso": "Experiência passada ('já fiz...')",
        "estrutura": "Verbo (forma た) + ことがある",
        "exemplos": ["にほんに いっ**たことがあります**。 → Já fui ao Japão.", "すしを たべ**たことがある**。 → Já comi sushi."],
        "nota": "Negativo: ～たことがありません (nunca fiz)."
    },
    "～てもいいですか": {
        "uso": "Pedir permissão ('posso fazer...?')",
        "estrutura": "Verbo (forma て) + もいいですか",
        "exemplos": ["はいっ**てもいいですか**？ → Posso entrar?", "み**てもいいですか**？ → Posso ver?"],
        "nota": "Para dar permissão: ～てもいいです. Para negar: ～てはいけません."
    },
    "～てはいけない": {
        "uso": "Proibição ('não pode fazer...')",
        "estrutura": "Verbo (forma て) + はいけない",
        "exemplos": ["ここで たべ**てはいけません**。 → Não pode comer aqui.", "はし**ってはいけない**。 → Não pode correr."],
        "nota": "Forma mais educada: ～てはいけません."
    },
    "～なければならない": {
        "uso": "Obrigação ('tem que fazer...')",
        "estrutura": "Verbo (forma ない) + ければならない",
        "exemplos": ["べんきょうし**なければなりません**。 → Tenho que estudar.", "いか**なければならない**。 → Tenho que ir."],
        "nota": "Forma coloquial: ～なきゃ. Mais suave: ～たほうがいい."
    },
    "～から": {
        "uso": "Causa/motivo ('porque')",
        "estrutura": "Frase A + から + Frase B",
        "exemplos": ["あめです**から**、いえにいます。 → Porque está chovendo, fico em casa.", "たかい**から** かいません。 → Não compro porque é caro."],
        "nota": "Diferente da partícula から (de/desde). Aqui conecta duas frases."
    },
    "～が": {
        "uso": "Conjunção adversativa suave ('mas', 'porém')",
        "estrutura": "Frase A + が + Frase B",
        "exemplos": ["にほんごはすきです**が**、むずかしいです。 → Gosto de japonês, mas é difícil.", "いきたい**が**、じかんがない。 → Quero ir, mas não tenho tempo."],
        "nota": "Mais suave que でも. Também usado para introduzir um contexto."
    },
    "でも": {
        "uso": "Conjunção adversativa ('mas', 'porém')",
        "estrutura": "Frase A。でも、Frase B。",
        "exemplos": ["たかいです。**でも**、かいます。 → É caro. Mas vou comprar.", "つかれた。**でも**、がんばる。 → Estou cansado. Mas vou continuar."],
        "nota": "でも inicia uma nova frase. が fica dentro da frase."
    },
    "～と思う (とおもう)": {
        "uso": "Expressar opinião ('acho que...')",
        "estrutura": "Frase (forma simples) + と思う",
        "exemplos": ["かれはがくせいだ**と思います**。 → Acho que ele é estudante.", "むずかしい**と思う**。 → Acho que é difícil."],
        "nota": "Use forma simples (não ます/です) antes de と思う."
    },
    "～方 (かた)": {
        "uso": "Modo de fazer algo ('jeito de fazer')",
        "estrutura": "Radical do verbo + 方",
        "exemplos": ["たべ**かた** → jeito de comer", "かき**かた** → jeito de escrever"],
        "nota": "Muito útil para perguntar como se faz algo."
    },
    "～前に (まえに)": {
        "uso": "Antes de fazer algo",
        "estrutura": "Verbo (forma dict.) + 前に / Substantivo + の前に",
        "exemplos": ["ねる**まえに** はをみがきます。 → Escovo os dentes antes de dormir.", "しょくじの**まえに** てをあらう。 → Lavo as mãos antes de comer."],
        "nota": "O verbo antes de 前に fica sempre na forma dicionário."
    },
    "～後で (あとで)": {
        "uso": "Depois de fazer algo",
        "estrutura": "Verbo (forma た) + 後で / Substantivo + の後で",
        "exemplos": ["たべ**たあとで** はをみがきます。 → Escovo os dentes depois de comer.", "じゅぎょうの**あとで** あそびます。 → Brinco depois da aula."],
        "nota": "O verbo antes de 後で fica na forma passada (た形)."
    },
    "～ながら": {
        "uso": "Fazer duas coisas ao mesmo tempo",
        "estrutura": "Radical do verbo + ながら + verbo principal",
        "exemplos": ["おんがくをきき**ながら** べんきょうします。 → Estudo enquanto ouço música.", "あるき**ながら** はなします。 → Converso enquanto caminho."],
        "nota": "A ação principal é o segundo verbo. ながら = enquanto / ao mesmo tempo."
    },
    "どんな / どの / どれ": {
        "uso": "Palavras interrogativas de seleção",
        "estrutura": "どんな + substantivo / どの + substantivo / どれ (sozinho)",
        "exemplos": ["**どんな** おんがくがすきですか？ → Que tipo de música você gosta?", "**どの** かばんですか？ → Qual bolsa é?", "**どれ** ですか？ → Qual é?"],
        "nota": "どれ = qual (dentre opções visíveis). どの = qual + substantivo. どんな = que tipo de."
    },
}

# ========== QUIZ: FLASHCARDS ==========
quiz_sessions = {}  # Armazena sessões de quiz por usuário

# ========== CONFIGURAÇÃO DO BOT ==========
intents = discord.Intents.all()
bot = commands.Bot("/", intents=intents, help_command=None)

# ========== EVENTOS ==========
@bot.event
async def on_ready():
    print("Chii acordou ✨")

@bot.event
async def on_member_join(membro: discord.Member):
    canal = bot.get_channel(1507982331456131094)
    await canal.send(f"{membro.mention} Entrou no servidor! いらっしゃいませ～ 🎌")

# ===================================================
# COMANDO: /vk — Consultar kanji
# ===================================================
@bot.command()
async def vk(ctx: commands.Context, *, kanji):
    """Consulta um kanji N5. Uso: /vk 日"""
    if kanji in kanji_n5:
        dados = kanji_n5[kanji]
        leituras = ", ".join(dados["leituras"])
        significados = ", ".join(dados["significados"])

        embed = discord.Embed(
            title=f"漢字  {kanji}",
            color=discord.Color.blue()
        )
        embed.add_field(name="📖 Leituras", value=f"`{leituras}`", inline=False)
        embed.add_field(name="💬 Significados", value=significados, inline=False)
        embed.set_footer(text="JLPT N5 • Kanji")
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Kanji não encontrado no banco N5.")

# ===================================================
# COMANDO: /vp — Consultar partícula
# ===================================================
@bot.command()
async def vp(ctx: commands.Context, *, particula):
    """Consulta uma partícula N5. Uso: /vp は"""
    if particula in particulas_n5:
        dados = particulas_n5[particula]

        embed = discord.Embed(
            title=f"助詞  {particula}  ({dados['romaji']})",
            description=f"**{dados['funcao']}**",
            color=discord.Color.green()
        )
        embed.add_field(name="📝 Descrição", value=dados["descricao"], inline=False)

        exemplos_str = "\n".join([f"• {jp}\n  → {pt}" for jp, pt in dados["exemplos"]])
        embed.add_field(name="💬 Exemplos", value=exemplos_str, inline=False)

        if dados.get("dica"):
            embed.add_field(name="💡 Dica", value=dados["dica"], inline=False)

        embed.set_footer(text="JLPT N5 • Partícula")
        await ctx.send(embed=embed)
    else:
        lista = ", ".join(particulas_n5.keys())
        await ctx.send(f"❌ Partícula não encontrada.\n📋 Disponíveis: {lista}")

# ===================================================
# COMANDO: /gramaticas — Listar todas as gramáticas N5
# ===================================================
@bot.command()
async def gramaticas(ctx: commands.Context):
    """Lista todas as gramáticas N5 disponíveis."""
    embed = discord.Embed(
        title="📚 Gramáticas JLPT N5",
        description="Use `/vg <gramática>` para ver detalhes de cada uma.",
        color=discord.Color.gold()
    )

    lista = "\n".join([f"• `{g}` — {dados['uso']}" for g, dados in gramaticas_n5.items()])
    # Discord tem limite de 1024 por field, então dividimos se necessário
    itens = list(gramaticas_n5.items())
    metade = len(itens) // 2
    parte1 = "\n".join([f"• `{g}` — {d['uso']}" for g, d in itens[:metade]])
    parte2 = "\n".join([f"• `{g}` — {d['uso']}" for g, d in itens[metade:]])

    embed.add_field(name="Gramáticas (1)", value=parte1, inline=False)
    embed.add_field(name="Gramáticas (2)", value=parte2, inline=False)
    embed.set_footer(text=f"Total: {len(gramaticas_n5)} gramáticas • JLPT N5")
    await ctx.send(embed=embed)

# ===================================================
# COMANDO: /vg — Ver detalhes de uma gramática
# ===================================================
@bot.command()
async def vg(ctx: commands.Context, *, gramatica):
    """Detalha uma gramática N5. Uso: /vg です"""
    if gramatica in gramaticas_n5:
        dados = gramaticas_n5[gramatica]

        embed = discord.Embed(
            title=f"文法  {gramatica}",
            description=f"**{dados['uso']}**",
            color=discord.Color.orange()
        )
        embed.add_field(name="🔧 Estrutura", value=f"`{dados['estrutura']}`", inline=False)

        exemplos_str = "\n".join([f"• {ex}" for ex in dados["exemplos"]])
        embed.add_field(name="💬 Exemplos", value=exemplos_str, inline=False)

        if dados.get("nota"):
            embed.add_field(name="📌 Nota", value=dados["nota"], inline=False)

        embed.set_footer(text="JLPT N5 • Gramática")
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"❌ Gramática não encontrada. Use `/gramaticas` para ver a lista completa.")

# ===================================================
# COMANDO: /particulas — Listar todas as partículas N5
# ===================================================
@bot.command()
async def particulas(ctx: commands.Context):
    """Lista todas as partículas N5 disponíveis."""
    embed = discord.Embed(
        title="🔤 Partículas JLPT N5",
        description="Use `/vp <partícula>` para ver detalhes de cada uma.",
        color=discord.Color.teal()
    )

    for p, dados in particulas_n5.items():
        embed.add_field(
            name=f"{p} ({dados['romaji']})",
            value=dados["funcao"],
            inline=True
        )

    embed.set_footer(text=f"Total: {len(particulas_n5)} partículas • JLPT N5")
    await ctx.send(embed=embed)

# ===================================================
# COMANDO: /quiz — Flashcard aleatório de kanji
# ===================================================
@bot.command()
async def quiz(ctx: commands.Context):
    """Inicia um flashcard de kanji N5. Responda com /resposta <leitura>"""
    kanji = random.choice(list(kanji_n5.keys()))
    dados = kanji_n5[kanji]
    quiz_sessions[ctx.author.id] = {
        "kanji": kanji,
        "leituras": dados["leituras"],
        "significados": dados["significados"]
    }

    embed = discord.Embed(
        title="🎴 Flashcard — Qual a leitura deste kanji?",
        description=f"# {kanji}",
        color=discord.Color.purple()
    )
    embed.set_footer(text="Responda com /resposta <sua resposta>")
    await ctx.send(embed=embed)

# ===================================================
# COMANDO: /resposta — Responder ao quiz de kanji
# ===================================================
@bot.command()
async def resposta(ctx: commands.Context, *, resposta_usuario):
    """Responde ao flashcard de kanji. Uso: /resposta いち"""
    sessao = quiz_sessions.get(ctx.author.id)
    if not sessao:
        await ctx.send("❓ Nenhum quiz ativo. Use `/quiz` para iniciar um flashcard.")
        return

    kanji = sessao["kanji"]
    leituras_corretas = sessao["leituras"]
    significados = sessao["significados"]

    # Remove a sessão
    del quiz_sessions[ctx.author.id]

    if resposta_usuario.strip() in leituras_corretas:
        embed = discord.Embed(
            title="✅ Correto! おめでとう！",
            color=discord.Color.green()
        )
    else:
        embed = discord.Embed(
            title="❌ Errado! また頑張って！",
            color=discord.Color.red()
        )

    embed.add_field(name="Kanji", value=f"**{kanji}**", inline=True)
    embed.add_field(name="Leituras corretas", value=", ".join(leituras_corretas), inline=True)
    embed.add_field(name="Significados", value=", ".join(significados), inline=False)
    embed.add_field(name="Sua resposta", value=f"`{resposta_usuario}`", inline=False)
    await ctx.send(embed=embed)

# ===================================================
# COMANDO: /quizp — Flashcard de partículas
# ===================================================
quiz_p_sessions = {}

@bot.command()
async def quizp(ctx: commands.Context):
    """Flashcard de partícula N5: mostra o exemplo com lacuna e você escolhe a partícula."""
    particula = random.choice(list(particulas_n5.keys()))
    dados = particulas_n5[particula]
    exemplo_jp, exemplo_pt = random.choice(dados["exemplos"])

    quiz_p_sessions[ctx.author.id] = {
        "particula": particula,
        "exemplo_pt": exemplo_pt
    }

    # Remove a partícula do exemplo para criar a lacuna
    exemplo_lacuna = exemplo_jp.replace(f"**{particula}**", "___").replace(particula, "___")

    embed = discord.Embed(
        title="🎴 Flashcard — Qual partícula completa a frase?",
        description=f"**{exemplo_lacuna}**\n*{exemplo_pt}*",
        color=discord.Color.blurple()
    )
    embed.set_footer(text="Responda com /respostap <partícula>")
    await ctx.send(embed=embed)

# ===================================================
# COMANDO: /respostap — Responder ao quiz de partícula
# ===================================================
@bot.command()
async def respostap(ctx: commands.Context, *, resposta_usuario):
    """Responde ao flashcard de partícula. Uso: /respostap は"""
    sessao = quiz_p_sessions.get(ctx.author.id)
    if not sessao:
        await ctx.send("❓ Nenhum quiz ativo. Use `/quizp` para iniciar um flashcard de partícula.")
        return

    particula_correta = sessao["particula"]
    del quiz_p_sessions[ctx.author.id]

    dados = particulas_n5[particula_correta]

    if resposta_usuario.strip() == particula_correta:
        embed = discord.Embed(title="✅ Correto! すごい！", color=discord.Color.green())
    else:
        embed = discord.Embed(title="❌ Errado! もう一度！", color=discord.Color.red())

    embed.add_field(name="Partícula correta", value=f"**{particula_correta}** ({dados['romaji']})", inline=True)
    embed.add_field(name="Função", value=dados["funcao"], inline=True)
    embed.add_field(name="Sua resposta", value=f"`{resposta_usuario}`", inline=False)
    await ctx.send(embed=embed)

# ===================================================
# COMANDO: /kanjis — Listar todos os kanjis N5
# ===================================================
@bot.command()
async def kanjis(ctx: commands.Context):
    """Lista todos os kanjis N5 disponíveis."""
    lista = " ".join(kanji_n5.keys())
    embed = discord.Embed(
        title="🗂️ Kanjis JLPT N5",
        description=lista,
        color=discord.Color.blue()
    )
    embed.set_footer(text=f"Total: {len(kanji_n5)} kanjis • Use /vk <kanji> para ver detalhes")
    await ctx.send(embed=embed)

# ===================================================
# COMANDO: /aleatorio — Kanji ou partícula aleatório do dia
# ===================================================
@bot.command()
async def aleatorio(ctx: commands.Context):
    """Mostra um kanji N5 aleatório para estudar."""
    kanji = random.choice(list(kanji_n5.keys()))
    dados = kanji_n5[kanji]

    embed = discord.Embed(
        title="🎲 Kanji Aleatório do Momento!",
        description=f"# {kanji}",
        color=discord.Color.from_rgb(255, 165, 0)
    )
    embed.add_field(name="📖 Leituras", value=", ".join(dados["leituras"]), inline=False)
    embed.add_field(name="💬 Significados", value=", ".join(dados["significados"]), inline=False)
    embed.set_footer(text="Use /quiz para testar seus conhecimentos!")
    await ctx.send(embed=embed)

# ===================================================
# COMANDO: /help — Ajuda com todos os comandos
# ===================================================
@bot.command(name="help")
async def ajuda(ctx: commands.Context):
    """Mostra todos os comandos disponíveis do bot."""
    embed = discord.Embed(
        title="📖 Chii Bot — Comandos Disponíveis",
        description="Seu assistente de estudo para o JLPT N5! 🇯🇵",
        color=discord.Color.from_rgb(220, 80, 80)
    )

    embed.add_field(
        name="🔍 Consultas",
        value=(
            "`/vk <kanji>` — Ver leituras e significado de um kanji\n"
            "  ex: `/vk 日`\n"
            "`/vp <partícula>` — Ver uso e exemplos de uma partícula\n"
            "  ex: `/vp は`\n"
            "`/vg <gramática>` — Ver detalhes de uma gramática\n"
            "  ex: `/vg です`"
        ),
        inline=False
    )

    embed.add_field(
        name="📋 Listagens",
        value=(
            "`/kanjis` — Lista todos os kanjis N5\n"
            "`/particulas` — Lista todas as partículas N5\n"
            "`/gramaticas` — Lista todas as gramáticas N5"
        ),
        inline=False
    )

    embed.add_field(
        name="🎮 Treino / Quiz",
        value=(
            "`/quiz` — Flashcard de kanji (adivinhe a leitura)\n"
            "`/resposta <leitura>` — Responder ao quiz de kanji\n"
            "`/quizp` — Flashcard de partícula (complete a frase)\n"
            "`/respostap <partícula>` — Responder ao quiz de partícula"
        ),
        inline=False
    )

    embed.add_field(
        name="🎲 Extra",
        value=(
            "`/aleatorio` — Kanji aleatório para estudar\n"
            "`/help` — Mostra esta mensagem"
        ),
        inline=False
    )

    embed.set_footer(text="Chii Bot • JLPT N5 Study Assistant | がんばってね！")
    await ctx.send(embed=embed)

# ===================================================
# TOKEN DO BOT
# ===================================================
load_dotenv()
bot.run(os.getenv("DISCORD_TOKEN"))