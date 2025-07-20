from django.core.management.base import BaseCommand
from product.models import Product
import random

MARCAS = [
    "Nike", "Adidas", "Zara", "H&M", "Levi's", "Calvin Klein", "Tommy Hilfiger", 
    "Gucci", "Louis Vuitton", "Balmain", "Dior", "Chanel", "Versace", "Armani",
    "Ralph Lauren", "Balenciaga", "Prada", "Fendi", "Burberry", "Valentino"
]

TIPOS_PRODUTO = [
    "Camiseta", "Calça", "Bermuda", "Vestido", "Tênis", "Jaqueta", "Blusa", 
    "Short", "Saia", "Sandália", "Blusão", "Camisetão", "Jaquetão", 
    "Vestido Longo", "Bermuda Cargo", "Sapato Social", "Óculos de Sol", "Bolsa", "Cinto"
]

ADJETIVOS = [
    "Esportiva", "Casual", "Premium", "Básica", "Estampada", "Listrada", "Floral",
    "Vintage", "Moderna", "Clássica", "Colorida", "Despojada", "Elegante", "Confortável",
    "Jovem", "Fashion", "Oversized", "Fitness", "Workwear", "Street"
]

MATERIAIS = [
    "Algodão Egípcio", "Linho", "Jeans Elastano", "Couro Legítimo", "Tecido Térmico", 
    "Resistente à Água", "Malha Premium", "Seda Natural", "Lã Merino", "Poliéster Reciclado"
]

DETALHES = [
    "Gola Alta", "Manga Longa", "Com Capuz", "Com Bolsos", "Sem Mangas", 
    "Com Recortes", "Com Aplicações", "Bordado", "Com Strass", "Com Zíper",
    "Botões de Madrepérola", "Estampa de Onça", "Listras Verticais", "Tie-Dye"
]

LOJAS = [
    "Moda Elegante", "Estilo Urbano", "Look Casual", "Fashion Premium", "Boutique Chic",
    "Style Street", "Trendy Wear", "Basic & Co", "Luxe Attire", "Urban Outfitters"
]

DESCRICOES_BASE = [
    "Produto de alta qualidade, confortável e estiloso. ",
    "Ideal para o dia a dia e ocasiões especiais. ",
    "Disponível em diversas cores e tamanhos. ",
    "Tecido leve e resistente que proporciona máximo conforto. ",
    "Design moderno e acabamento impecável para valorizar seu look. ",
    "Perfeito para compor looks versáteis em qualquer estação. ",
    "Excelente custo-benefício com durabilidade garantida. ",
    "Produto exclusivo da nova coleção outono/inverno. ",
    "Aproveite o conforto e a praticidade no seu dia a dia. ",
    "Peça indispensável para completar seu guarda-roupa. "
]

DETALHES_DESCRICAO = [
    "Confeccionado com atenção aos detalhes.",
    "Possui etiqueta de autenticidade da marca.",
    "Lavagem fácil e prática.",
    "Não desbota e mantém a forma após várias lavagens.",
    "Material ecologicamente sustentável.",
    "Produto vegano e cruelty free.",
    "Embalagem especial para presente.",
    "Garantia de satisfação do fabricante."
]

def gerar_nome_coerente():
    # Combinações mais lógicas
    combinacoes = [
        f"{random.choice(MARCAS)} {random.choice(TIPOS_PRODUTO)} {random.choice(ADJETIVOS)}",
        f"{random.choice(TIPOS_PRODUTO)} {random.choice(MATERIAIS)} {random.choice(DETALHES)}",
        f"{random.choice(MARCAS)} {random.choice(DETALHES)}",
        f"{random.choice(TIPOS_PRODUTO)} {random.choice(ADJETIVOS)} Coleção {random.choice(LOJAS)}",
        f"Edição Especial {random.choice(LOJAS)} - {random.choice(TIPOS_PRODUTO)} {random.choice(MARCAS)}",
        f"{random.choice(TIPOS_PRODUTO)} {random.choice(ADJETIVOS)} com {random.choice(DETALHES)}"
    ]
    
    nome = random.choice(combinacoes)
    
    # Aplicar variações de caixa
    caso = random.randint(0, 3)
    if caso == 0:
        nome = nome.upper()  # Tudo maiúsculo
    elif caso == 1:
        nome = nome.lower()  # Tudo minúsculo
    elif caso == 2:
        nome = nome.title()  # Primeiras Letras Maiúsculas
    
    return nome

def gerar_descricao_completa(tipo_produto):
    descricao = random.choice(DESCRICOES_BASE)
    
    # Adicionar detalhes específicos por tipo de produto
    if "Camiseta" in tipo_produto or "Blusa" in tipo_produto:
        descricao += f"Corte perfeito para o corpo. "
    elif "Calça" in tipo_produto or "Bermuda" in tipo_produto:
        descricao += f"Caimento impecável que valoriza a silhueta. "
    elif "Tênis" in tipo_produto or "Sapato" in tipo_produto:
        descricao += f"Sola antiderrapante e amortecimento de alta performance. "
    elif "Vestido" in tipo_produto or "Saia" in tipo_produto:
        descricao += f"Modelagem que proporciona movimento e elegância. "
    
    # Adicionar detalhes técnicos
    descricao += f"Material: {random.choice(MATERIAIS)}. "
    
    # Adicionar detalhes extras
    descricao += random.choice(DETALHES_DESCRICAO)
    
    # Menção à loja em 30% dos casos
    if random.random() < 0.3:
        descricao += f" Exclusivo {random.choice(LOJAS)}."
    
    return descricao

class Command(BaseCommand):
    help = 'Popula o banco com produtos realistas para testar eficiência da Trie'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        
        for i in range(1, 1001):
            name = gerar_nome_coerente()
            
            # Identificar o tipo de produto principal
            categoria = "Vestuário"
            for tipo in TIPOS_PRODUTO:
                if tipo.lower() in name.lower():
                    categoria = tipo
                    break
            
            price = round(random.uniform(29.90, 499.90), 2)
            
            # Gerar descrição completa
            descricao = gerar_descricao_completa(categoria)
            
            Product.objects.create(name=name, price=price, description=descricao)
            
            if i % 100 == 0:
                self.stdout.write(f'Criados {i} produtos...')
                self.stdout.write(f'Exemplo: {name}')
                self.stdout.write(f'Descrição: {descricao[:80]}...')
        
        self.stdout.write(self.style.SUCCESS('1000 produtos realistas criados com sucesso!'))