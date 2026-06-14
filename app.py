from flask import Flask, render_template

app=Flask(__name__)

TEAM=[
    {
        "name": "Malu Azevedo",
        "role": "Campo Grande, MS • 2º ano • IFMS",
        "photo": "static/img/malu.jpg",
        "bio": (
            "Sou uma estudante de ensino médio técnico em eletrotécnica no IFMS! E sou apaixonada por STEM!! Eu adoro ensinar, pesquisar e também construir coisas! Sou apaixonada por matemática, física, ciência da computação e eletrônica. Sou uma pessoa muito curiosa, então sempre estou buscando aprender mais e também compartilhar meu conhecimento com outras pessoas. E também tenho uma quedinha por linguistica e arte !: )"
        ),
    },
    {
        "name": "Amanda Sarmento",
        "role": "Sapucaia do Sul, RS • 1º ano • IFSUL",
        "photo": "static/img/amanda.jpeg",
        "bio": (
            "Curso ensino médio técnico em desenvolvimento de sistemas no IFSUL. Amo a área de STEM, ensinar e aprender novas coisas. Computação e matemática são minhas paixões e amo participar de olimpíadas dessas áreas. Gosto muito de aprender e ensinar e acho que já passou da hora de termos mais mulheres dominando a área de STEM, e por isso tenho como objetivo contribuir para que isso aconteça. <3"
        ),
    },
    {
        "name": "Ana Laura Kogeyama",
        "role": "São Carlos, SP • 1º ano • IFSP",
        "photo": "static/img/ana.jpeg",
        "bio": (
            "Sou uma estudante de ensino médio de técnico em informática do IFSP. Adoro programação, matemática e robotica, e de participar de olimpíadas principalmente dessas áreas. Além disso, gosto muito de ensinar crianças e ajudar outras garotas que têm interesse nesses campos, além de divulgar para aquelas que não as conhecem.  "
        ),
    },
    {
        "name": "Marina Maia",
        "role": "Rio de Janeiro, RJ • 1º ano • The British School",
        "photo": "static/img/marina.jpeg",
        "bio": (
            "Estudo na British School. Sou apaixonada por aprender coisas novas e adoro curiosidades aleatorias. Em um geral, eu sou uma pessoa com interesses muito distintos, e eu tento muitas áreas diferentes, mas atualmente as minhas favoritas tem sido matemática, biologia e programação. Também gosto de ler, artes, gosto de ajudar, e acredito que aprender pode ser criativo"
        ),
    },
    {
        "name": "Aryane Bueno",
        "role": "Nova Andradina, MS • 2º ano • IFMS",
        "photo": "static/img/aryane.jpg",
        "bio": (
            "Curso Ensino Médio Técnico em Informática no IFMs e sou completamente apaixonada por tecnologia, lógica e matemática. Amo desafios que exigem raciocínio rápido, criatividade e estratégia, principalmente quando envolvem programação e resolução de problemas. Tenho uma curiosidade enorme e dificilmente consigo me contentar só com o básico , gosto de ir além, pesquisar, aprender coisas novas e me desafiar constantemente."
        ),
    },
    {
        "name": "Ágata Yoon",
        "role": "São Paulo, SP • 1º ano • ETEC",
        "photo": "static/img/agata.jpeg",
        "bio": (
            "Curso ensino médio técnico em desenvolvimento de sistemas na Etec Raposo Tavares! Sou uma pessoa muito curiosa, que ama aprender e experimentar coisas novas o tempo todo, e busco transmitir o que aprendo para outras pessoas! Adoro o mundo da tecnologia e computação, mas também sou fã de livros e fotos =3"
        ),
    },
]
PARTNERS = [
    {"name": "Instituto Alpha Lumen", "logo": "static/img/alpha_lumen.jpeg"},
    {"name": "Instituto Apontar",     "logo": "static/img/apontar.jpeg"},
    {"name": "MIT",                   "logo": "static/img/mit.jpeg"},
    {"name": "Instituto Blooma",      "logo": "static/img/blooma.jpeg"},
    {"name": "Fundação Behring",      "logo": "static/img/behring.jpeg"},
]

ODS = [
    {"num": "4",  "label": "Educação de Qualidade",       "color": "#C31F33"},
    {"num": "5",  "label": "Igualdade de Gênero",         "color": "#FF3A21"},
    {"num": "10", "label": "Redução das Desigualdades",   "color": "#DD1367"},
    {"num": "18", "label": "Igualdade Étnico-Racial",     "color": "#7B3F00"},
]

APOIADORES = [
    "Agata Yoon",
    "Mariana Botelho",
    "Aghata Vitória",
    "José Gabriel Alves",
    "Daysa de Campos",
    "Andressa Sabrina Santos",
    "Ana Yoon",
    "Rodrigo Berino",
    "Davi Hudson",
    "Carlos Eduardo Avellar",
    "Alessandra Teixeira",
    "Sthefany Souza",
    "Leonardo Barbosa",
    "Jessica Seabra",
    "Luis Eurico",
    "Beatriz Naitzki",
    "Marina Maia",
    "Tathiana de Oliveira",
    "Helder Nelson",
    "Eliana Vieira",
    "Marcia Aparecida",
    "Roger Sauandaj",
    "Karine Antunes",
    "Marcileia Silva",
    "Anannda Rios",
    "Ana Laura Kogeyama",
    "Richard Sousa",
    "Erik Seiji",
    "Patrizia Palmieri",
    "Flora Cardoso",
    "Ana Carolina Camargo",
    "Vanda Lucia da Costa",
    "Priscila da Silva",
    "Camila da Silva",
    "Enio da Rosa",
    "Elissa Yan",
    "Thiago Borges",
    "Fabio Henrique Andrade",
    "Lucas de Souza",
    "Arthur Wust",
    "Luana de Cunha",
    "Eduardo Seiiti",
    "Vitória Cruz",
    "Ravi Petry",
    "Pedro Henrique Peneira",
    "João Gabriel Kupske",
    "Rossana Gonçalves",
    "Paulo Henrique Kettner",
    "Ricardo Felipe de Souza",
    "Tamires Barbosa",
    "Mariana Rodrigues",
    "Aparecida Vines",
    "Fernanda da Silva",
    "Jessica Seabra",
    "Belissa Schonardie",
]
@app.route("/")
def index():
    return render_template(
        "index.html",
        team=TEAM,
        partners=PARTNERS,
        ods=ODS,
        youtube_url="https://www.youtube.com/embed/kM5vy7zZS6o",
        figma_url="https://www.figma.com/proto/Q42BqkIOGwgkxi42tdPbm6/AdaGraph?node-id=547-379&p=f&t=zvz2JQ0dejHW3wkq-1&scaling=scale-down&content-scaling=fixed&page-id=62%3A25",
        instagram_url="https://instagram.com/ctrldivas",
        app_download_url="#", 
    )
@app.route("/apoiadores")
def apoiadores():
    return render_template("apoiadores.html", apoiadores=APOIADORES)

if __name__ == "__main__":
    app.run(debug=True)