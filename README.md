# Gerador e Cofre de Tokens

Ferramenta de terminal em Python, feita como projeto pessoal de estudo de segurança. Ela tem contas de usuário, um gerador de tokens aleatórios e um "cofre" que só mostra os tokens da conta depois de pedir a senha outra vez.

> Este é um projeto de estudo. Ele **não** deve ser usado para guardar senhas ou tokens reais: as senhas ficam em texto puro no disco (veja [Limitações conhecidas](#limitações-conhecidas)).

## O que o programa faz

Ao rodar, aparece um menu:

```
===== GERADOR E COFRE =====
1 - Criar Conta
2 - Entrar na conta
3 - Gerar Token
4 - Abrir Cofre
0 - Sair
```

1. **Criar conta**: pede nome de usuário, e-mail e senha. Recusa nomes de usuário repetidos.
2. **Entrar na conta**: confere nome e senha e mantém a conta aberta enquanto o programa estiver rodando.
3. **Gerar token**: com a conta aberta, gera um token e o adiciona à lista da conta.
4. **Abrir cofre**: com a conta aberta, pede a senha de novo e só então abre o submenu do cofre, que lista os tokens gerados.

## Como funciona

- **Geração de tokens**: usa `secrets.token_urlsafe(8)`, do módulo [`secrets`](https://docs.python.org/3/library/secrets.html) da biblioteca padrão. Ele usa a fonte de aleatoriedade criptográfica do sistema operacional, ao contrário do módulo `random`, que é previsível. Cada token tem 8 bytes aleatórios, codificados em Base64 seguro para URL (cerca de 11 caracteres).
- **Proteção do cofre**: o cofre só abre se a senha digitada for igual à da conta logada. Ou seja, mesmo com o programa aberto e a conta logada, ver os tokens exige a senha outra vez.
- **Armazenamento**: as contas (nome, e-mail, senha e lista de tokens) ficam no arquivo `contas.json`, criado na pasta em que o programa é executado. Se o arquivo não existir ou estiver vazio/inválido, o programa começa com a lista de contas vazia.

## Requisitos

- Python 3.6 ou mais recente (o módulo `secrets` existe desde o 3.6). O projeto foi desenvolvido com Python 3.14.
- Nenhuma dependência externa: só a biblioteca padrão (`secrets`, `json`, `os`).

## Como rodar

```bash
git clone https://github.com/MatheusCortes02/3-Projeto-Gerador-e-Cofre-de-tokens.git
cd 3-Projeto-Gerador-e-Cofre-de-tokens
python main.py
```

O `contas.json` é criado na primeira conta cadastrada. Ele está no `.gitignore` porque guarda dados locais (inclusive senhas) e não deve ir para o repositório.

## Estrutura

```
.
├── main.py      # menu principal, contas (criar/entrar), geração de tokens e leitura/gravação do contas.json
├── cofre.py     # submenu do cofre: listar os tokens da conta logada
└── .gitignore   # ignora contas.json, __pycache__/, ambientes virtuais e pastas de IDE
```

## Limitações conhecidas

Estas limitações são reais e estão no código atual:

- **Senha em texto puro**: a senha é gravada sem hash em `contas.json`. Quem tiver acesso ao arquivo vê a senha de todas as contas.
- **Tokens sem cifra**: os tokens também ficam legíveis no arquivo. A senha pedida pelo cofre protege apenas a tela do programa, não os dados no disco.
- **Comparação de senha com `==`**: a conferência não é feita em tempo constante, o que, em tese, permite que o tempo de resposta dê pistas sobre a senha.
- **Sem testes automatizados**.
- O e-mail é pedido no cadastro, mas não é usado em nenhuma outra parte do programa.

## Próximos passos (v2)

- Guardar apenas o **hash da senha com sal**, usando **Argon2id** (ou bcrypt), nunca a senha em si.
- Fazer a **comparação em tempo constante** (por exemplo, a verificação da própria biblioteca de hash ou `hmac.compare_digest`).
- **Cifrar os tokens** no disco, com uma chave derivada da senha do usuário.
- Escrever **testes automatizados** para cadastro, login, geração de tokens e abertura do cofre.

## Autor

Matheus Cortes ([@MatheusCortes02](https://github.com/MatheusCortes02))
