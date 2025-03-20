class aluno:
    def __init__ (self, nome):
        self.nome = nome
        self.notas = []
        
    def numero(self):
            while True:
                try:
                    b1 = float(input("Qual as notas do aluno no 1° bimestre: "))
                    b2 = float(input("Qual as notas do aluno no 2° bimestre: "))
                    b3 = float(input("Qual as notas do aluno no 3° bimestre: "))
                    b4 = float(input("Qual as notas do aluno no 4° bimestre: "))
                    self.notas = b1, b2, b3, b4
                    print("Carregando...")
                    break
                except ValueError:
                    print("Por favor, insira um número válido para as notas.")
    def media(self):
            soma = sum(self.notas)
            self.media_es = 6
            media_aritmedica = soma / len(self.notas)
            print(f"O {self.nome} tirou as seguintes notas respectivamente em cada bimestre: {self.notas}, e sua media foi {media_aritmedica}")
            return media_aritmedica
    def verificar_aprovacao(self):
        media_aritmedica = self.media()
        if media_aritmedica >= 6:
            print("O Aluno(a) foi aprovado")
        else:
            print("O Aluno(a) foi reprovado")

nome_aluno = input("Qual o nome do aluno? ")
aluno = aluno(nome_aluno)
aluno.numero()
aluno.verificar_aprovacao()
