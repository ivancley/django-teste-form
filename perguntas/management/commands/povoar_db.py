from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from salao.models import Salao
from funcionario.models import Funcionario
from ocupacao.models import Ocupacao
from cliente.models import Cliente
from procedimento.models import Procedimento
from pergunta.models import Pergunta

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def criarSaloes(self):
        print("Excluindo Saloes")
        Salao.objects.all().delete()
        print("Criando Ocupações")
        corte_certo = Salao()
        corte_certo.nome = "Corte Certo"
        corte_certo.nomeURL = "corte_certo"
        corte_certo.save()
        belo_corte = Salao()
        belo_corte.nome = "Belo Corte"
        belo_corte.nomeURL = "belo_corte"
        belo_corte.save()

    def criarOcupacoes(self):
        print("Excluindo Ocupações")
        Ocupacao.objects.all().delete()
        print("Criando Ocupações")
        cabelereiro = Ocupacao()
        cabelereiro.nome = "Cabelereiro(a)"
        cabelereiro.save()
        recepcionista = Ocupacao()
        recepcionista.nome = "Recepcionista"
        recepcionista.selecionavel = False
        recepcionista.save()
        pedicure = Ocupacao()
        pedicure.nome = "Pedicure/Manicure"
        pedicure.save()

    def criarProcedimentosCabelereiro(self):
        print("Excluindo Procedimentos")
        Procedimento.objects.all().delete()
        Pergunta.objects.all().delete()
        print("Criando Procedimentos de Cabelereiro salão Corte Certo")
        corte_certo = Salao.objects.get(nome = "Corte Certo")
        belo_corte = Salao.objects.get(nome = "Belo Corte")
        saloes = [ corte_certo, belo_corte]
        cabelereiro = Ocupacao.objects.get(nome="Cabelereiro(a)")
        for salao in saloes:
            proOrganizacaoAtendimento = Procedimento()
            proOrganizacaoAtendimento.nome = "Organização e Atendimento"
            proOrganizacaoAtendimento.ocupacao = cabelereiro
            proOrganizacaoAtendimento.salao = salao
            proOrganizacaoAtendimento.selecionavel = False
            proOrganizacaoAtendimento.selecionavel = False
            proOrganizacaoAtendimento.save()
            pergunta = Pergunta()
            pergunta.titulo = "O espaço estava limpo, organizado e com os materiais e equipamentos já separados para o atendimento"
            pergunta.tipo_pergunta = "sim/não"
            pergunta.procedimento = proOrganizacaoAtendimento
            pergunta.save()

            proLavagem = Procedimento()
            proLavagem.nome = "Lavagem de Cabelos"
            proLavagem.ocupacao = cabelereiro
            proLavagem.salao = salao
            proLavagem.save()
            pergunta = Pergunta()
            pergunta.titulo = "Durante processo de lavagem, foi aplicado técnicas de massagem capitar? "
            pergunta.tipo_pergunta = "sim/não"
            pergunta.procedimento = proLavagem
            pergunta.save()

            proEscovar = Procedimento()
            proEscovar.nome = "Escovar de Cabelos"
            proEscovar.ocupacao = cabelereiro
            proEscovar.salao = salao
            proEscovar.save()
            pergunta = Pergunta()
            pergunta.titulo = "O penteado sugerido está de acordo com as características da sua face e cabelo? "
            pergunta.tipo_pergunta = "sim/não"
            pergunta.procedimento = proEscovar
            pergunta.save()

            proCortar = Procedimento()
            proCortar.nome = "Cortar de Cabelos"
            proCortar.ocupacao = cabelereiro
            proCortar.salao = salao
            proCortar.save()
            pergunta = Pergunta()
            pergunta.titulo = "Quanto ao corte, qual seu nível de satisfação?"
            pergunta.tipo_pergunta = "estrelas"
            pergunta.procedimento = proCortar
            pergunta.save()

            proPintura = Procedimento()
            proPintura.nome = "Pintura capilar"
            proPintura.ocupacao = cabelereiro
            proPintura.salao = salao
            proPintura.save()
            pergunta = Pergunta()
            pergunta.titulo = "Foi realizado testes de mechas a fim de verificar compatibilidade do produto?"
            pergunta.tipo_pergunta = "sim/não"
            pergunta.procedimento = proCortar
            pergunta.save()
            pergunta = Pergunta()
            pergunta.titulo = "Quanto ao procedimento de Coloração e Descoloração, qual seu nível de satisfação"
            pergunta.tipo_pergunta = "estrelas"
            pergunta.procedimento = proCortar
            pergunta.save()

            proOndulacao = Procedimento()
            proOndulacao.nome = "Ondular/Desondular fios"
            proOndulacao.ocupacao = cabelereiro
            proOndulacao.salao = salao
            proOndulacao.save()
            pergunta = Pergunta()
            pergunta.titulo = "Quanto ao procedimento de Ondulação ou Desondulação, qual seu nível de satisfação?"
            pergunta.tipo_pergunta = "estrelas"
            pergunta.procedimento = proOndulacao

    def criarProcedimentosPedicure(self):
        print("Criando Procedimentos de Pedicure")
        corte_certo = Salao.objects.get(nome = "Corte Certo")
        belo_corte = Salao.objects.get(nome = "Belo Corte")
        saloes = [ corte_certo, belo_corte]
        pedicure = Ocupacao.objects.get(nome="Pedicure/Manicure")
        for salao in saloes:
            proOrganizacaoAtendimento = Procedimento()
            proOrganizacaoAtendimento.nome = "Organização e Atendimento - Pedicure"
            proOrganizacaoAtendimento.ocupacao = pedicure
            proOrganizacaoAtendimento.salao = salao
            proOrganizacaoAtendimento.selecionavel = False
            proOrganizacaoAtendimento.save()
            pergunta = Pergunta()
            pergunta.titulo = "O espaço estava limpo, organizado e com os materiais e equipamentos já separados para o atendimento"
            pergunta.tipo_pergunta = "sim/não"
            pergunta.procedimento = proOrganizacaoAtendimento
            pergunta.save()

            proCortarLixar = Procedimento()
            proCortarLixar.nome = "Cortar e Lixar Unhas"
            proCortarLixar.ocupacao = pedicure
            proCortarLixar.salao = salao
            proCortarLixar.save()
            pergunta = Pergunta()
            pergunta.titulo = "Qual a qualidade do procedimento de Higienização e hidratação de mão e pés"
            pergunta.tipo_pergunta = "estrelas"
            pergunta.procedimento = proCortarLixar
            pergunta.save()
            pergunta = Pergunta()
            pergunta.titulo = "Qual a sua satisfação quanto ao Corte, lixamento e polimento de suas unhas? "
            pergunta.tipo_pergunta = "estrelas"
            pergunta.procedimento = proCortarLixar
            pergunta.save()
            pergunta = Pergunta()
            pergunta.titulo = "Quanto a remoção de cutículas, qual o seu nível de satisfação? "
            pergunta.tipo_pergunta = "estrelas"
            pergunta.procedimento = proCortarLixar
            pergunta.save()
            proAlongamentoUnhas = Procedimento()
            proAlongamentoUnhas.nome = "Alongamento de unhas"
            proAlongamentoUnhas.ocupacao = pedicure
            proAlongamentoUnhas.salao = salao
            proAlongamentoUnhas.save()
            pergunta = Pergunta()
            pergunta.titulo = "Quanto o seu nível de satisfação quanto ao procedimento de Alogamento de unhas?"
            pergunta.tipo_pergunta = "estrelas"
            pergunta.procedimento = proAlongamentoUnhas
            pergunta.save()

    def criarProcedimentosRecepcionista(self):
        print("criando Procedimentos da recepcao")
        corte_certo = Salao.objects.get(nome = "Corte Certo")
        belo_corte = Salao.objects.get(nome = "Belo Corte")
        saloes = [ corte_certo, belo_corte]
        recepcionista = Ocupacao.objects.get(nome= "Recepcionista")
        for salao in saloes:
            proReceberClientes = Procedimento()
            proReceberClientes.nome = "Receber e orientar Clientes"
            proReceberClientes.ocupacao = recepcionista
            proReceberClientes.salao = salao
            proReceberClientes.save()
            pergunta = Pergunta()
            pergunta.titulo = "•	A recepção foi acolhedora? soube passar informações claras sobre os serviços prestados?"
            pergunta.tipo_pergunta = "estrelas"
            pergunta.procedimento = proReceberClientes
            pergunta.save()

    def criarFuncionarios1(self):
        print("Excluindo Funcionarios")
        Funcionario.objects.all().delete()
        User.objects.all().delete()
        print("Criando Funcionarios 1")
        cabelereiro = Ocupacao.objects.get(nome = "Cabelereiro(a)")
        recepcionista = Ocupacao.objects.get(nome = "Recepcionista")
        pedicure = Ocupacao.objects.get(nome = "Pedicure/Manicure")

        corte_certo = Salao.objects.get(nome = "Corte Certo")
        ivan = User.objects.create_superuser('ivan', 'ivan@uol.com', '123123')
        admbelocorte = User.objects.create_superuser('admbelocorte', 'admbelocorte@uol.com', '123123')
        admcortecerto = User.objects.create_superuser('admcortecerto', 'admcortecerto@uol.com', '123123')

        fabio = User.objects.create_user('fabio','fabio@uol.com', '123123')
        gerenteFabio = Funcionario()
        gerenteFabio.user = fabio
        gerenteFabio.gerente = True
        gerenteFabio.salao = corte_certo
        gerenteFabio.save()
        maria = User.objects.create_user('maria', 'maria@uol.com', '123123')
        cabelereiraMaria = Funcionario()
        cabelereiraMaria.user = maria
        cabelereiraMaria.salao = corte_certo
        cabelereiraMaria.save()
        cabelereiraMaria.ocupacao_set.add(cabelereiro)
        joana = User.objects.create_user('joana', 'joana@uol.com', '123123')
        pedicureJoana = Funcionario()
        pedicureJoana.user = joana
        pedicureJoana.salao = corte_certo
        pedicureJoana.save()
        cabelereiraMaria.ocupacao_set.add(pedicure)
        claudia = User.objects.create_user('claudia', 'claudia@uol.com', '123123')
        recepcionistaClaudia = Funcionario()
        recepcionistaClaudia.user = claudia
        recepcionistaClaudia.salao = corte_certo
        recepcionistaClaudia.save()
        cabelereiraMaria.ocupacao_set.add(recepcionista)

    def criarFuncionarios2(self):
        print("Criando Funcionarios 2")
        cabelereiro = Ocupacao.objects.get(nome = "Cabelereiro(a)")
        recepcionista = Ocupacao.objects.get(nome = "Recepcionista")
        pedicure = Ocupacao.objects.get(nome = "Pedicure/Manicure")
        belo_corte = Salao.objects.get(nome="Belo Corte")
        mario = User.objects.create_user('mario','mario@uol.com', '123123')
        gerenteMario = Funcionario()
        gerenteMario.user = mario
        gerenteMario.gerente = True
        gerenteMario.salao = belo_corte
        gerenteMario.save()
        fatima = User.objects.create_user('fatima', 'fatima@uol.com', '123123')
        cabelereiraFatima = Funcionario()
        cabelereiraFatima.user = fatima
        cabelereiraFatima.salao = belo_corte
        cabelereiraFatima.save()
        cabelereiraFatima.ocupacao_set.add(cabelereiro)
        ana = User.objects.create_user('ana', 'ana@uol.com', '123123')
        pedicureAna = Funcionario()
        pedicureAna.user = ana
        pedicureAna.salao = belo_corte
        pedicureAna.save()
        pedicureAna.ocupacao_set.add(pedicure)
        marcela = User.objects.create_user('marcela', 'marcela@uol.com', '123123')
        recepcionistaMarcela = Funcionario()
        recepcionistaMarcela.user = marcela
        recepcionistaMarcela.salao = belo_corte
        recepcionistaMarcela.save()
        recepcionistaMarcela.ocupacao_set.add(recepcionista)

    def defineOcupacoesDoSalao(self):
        corte_certo = Salao.objects.get(nome="Corte Certo")
        belo_corte = Salao.objects.get(nome="Belo Corte")
        cabelereiro = Ocupacao.objects.get(nome="Cabelereiro(a)")
        recepcionista = Ocupacao.objects.get(nome="Recepcionista")
        pedicure = Ocupacao.objects.get(nome="Pedicure/Manicure")
        corte_certo.ocupacao_set.add(cabelereiro)
        corte_certo.ocupacao_set.add(recepcionista)
        corte_certo.ocupacao_set.add(pedicure)
        belo_corte.ocupacao_set.add(cabelereiro)
        belo_corte.ocupacao_set.add(recepcionista)
        belo_corte.ocupacao_set.add(pedicure)

    def criarClientes(self):
        print("excluindo Clientes")
        Cliente.objects.all().delete()
        print("criando Clientes")
        antonia = Cliente()
        antonia.nome = "Antonia"
        antonia.cpf = "111.111.111-11"
        antonia.celular = "(11) 11111-1111"
        antonia.save()
        paula = Cliente()
        paula.nome = "Paula"
        paula.cpf = "222.222.222-22"
        paula.celular = "(22) 22222-2222"
        paula.save()
        carol = Cliente()
        carol.nome = "Carol"
        carol.cpf = "333.333.333-33"
        carol.celular = "(33) 33333-3333"
        carol.save()

    def handle(self, *args, **options):
        self.criarSaloes()
        self.criarOcupacoes()
        self.defineOcupacoesDoSalao()
        self.criarProcedimentosCabelereiro()
        self.criarProcedimentosPedicure()
        self.criarProcedimentosRecepcionista()
        self.criarFuncionarios1()
        self.criarFuncionarios2()
        self.criarClientes()
