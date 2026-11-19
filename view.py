from model import *

def main():
    escolha = int(input("""  
    ╔════════════════════════════════════════════════════════╗
    ║                          MENU                          ║
    ╠════════════════════════════════════════════════════════╣
    ║ ▸ PREPARAÇÃO                                           ║
    ║   [RJ] Registar Jogador      [IJ] Iniciar Jogo         ║
    ╠════════════════════════════════════════════════════════╣
    ║ ▸ TURNO                                                ║
    ║   [LD] Lançar Dados          [FT] Finalizar Turno      ║
    ╠════════════════════════════════════════════════════════╣
    ║ ▸ CONSTRUIR                                            ║
    ║   [CE] Construir Estrada     [CA] Construir Aldeia     ║
    ║   [CC] Construir Cidade      [TR] Trocar Recursos      ║
    ╠════════════════════════════════════════════════════════╣
    ║ ▸ JOGO                                                 ║
    ║   [G ] Gravar                [L ] Ler                  ║
    ║   [VT] Ver Tabuleiro         [EE] Estado do Jogo       ║
    ║   [AJ] Ajuda (regras)        [S ] Sair                 ║
    ╚════════════════════════════════════════════════════════╝
    
    """))
    